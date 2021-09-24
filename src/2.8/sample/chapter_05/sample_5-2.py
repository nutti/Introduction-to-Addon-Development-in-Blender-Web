import datetime
import math

import bpy
import blf
from bpy.props import IntProperty, IntVectorProperty, EnumProperty


bl_info = {
    "name": "サンプル 5-2: 作業時間計測",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > サンプル 5-2",
    "description": "各オブジェクトについて、オブジェクトモードとエディットモードでの作業時間を計測するアドオン",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "User Interface"
}


def time_to_str(time):
    msec = math.floor(time * 1000) % 1000   # ミリ秒
    sec = math.floor(time) % 60             # 秒
    minute = math.floor(time / 60) % 60     # 分
    hour = math.floor(time / (60 * 60))     # 時

    return "%d:%02d:%02d.%d" % (hour, minute, sec, math.floor(msec / 100))


def get_region(context, area_type, region_type):
    region = None
    area = None

    # 指定されたエリアを取得する
    for a in context.screen.areas:
        if a.type == area_type:
            area = a
            break
    else:
        return None
    # 指定されたリージョンを取得する
    for r in area.regions:
        if r.type == region_type:
            region = r
            break

    return region


# 作業時間計測のオペレータ
class SAMPLE52_OT_CalculateWorkingHours(bpy.types.Operator):

    bl_idname = "ui.sample52_calculate_working_hours"
    bl_label = "作業時間計測"
    bl_description = "作業時間を計測します"

    __handle = None           # 描画関数ハンドラ
    __timer = None            # タイマハンドラ
    __running = False         # Trueの場合は、作業時間計測中
    working_hour_db = {}      # 作業時間を保存するためのデータベース

    def __init__(self):
        self.__prev_time = 0.0        # __calc_delta()メソッドを呼び出した時の時間
        self.__prev_obj = None        # __calc_delta()メソッドを呼び出した時に選択していたオブジェクト
        self.__prev_mode = None       # __calc_delta()メソッドを呼び出した時のモード

    # モーダルモード中はTrueを返す
    @classmethod
    def is_running(cls):
        return cls.__running

    def __handle_add(self, context):
        op_cls = SAMPLE52_OT_CalculateWorkingHours

        if op_cls.__timer is None:
            # タイマを登録
            op_cls.__timer = context.window_manager.event_timer_add(
                0.10, window=context.window)
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)
        if op_cls.__handle is None:
            # 描画関数の登録
            op_cls.__handle = bpy.types.SpaceView3D.draw_handler_add(
                op_cls.__draw,
                (self, context), 'WINDOW', 'POST_PIXEL'
            )

    def __handle_remove(self, context):
        op_cls = SAMPLE52_OT_CalculateWorkingHours

        if op_cls.__handle is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(op_cls.__handle, 'WINDOW')
            op_cls.__handle = None
        if op_cls.__timer is not None:
            # タイマの登録を解除
            context.window_manager.event_timer_remove(op_cls.__timer)
            op_cls.__timer = None

    @staticmethod
    def __draw_text(size, x, y, msg):
        # フォントの色を指定
        blf.color(0, 1.0, 1.0, 1.0, 1.0)
        # フォントサイズを指定
        blf.size(0, size, 72)
        # 描画位置を指定
        blf.position(0, x, y, 0)
        # 文字列を描画
        blf.draw(0, msg)

    @staticmethod
    def __draw(self, context):
        op_cls = SAMPLE52_OT_CalculateWorkingHours
        sc = context.scene
        prefs = context.preferences.addons[__name__].preferences

        # 表示するオブジェクトが選択されていない場合は、描画しない
        if sc.sample52_prop_object == '':
            return

        # リージョン幅を取得するため、描画先のリージョンを得る
        region = get_region(context, 'VIEW_3D', 'WINDOW')

        # 描画先のリージョンへ文字列を描画
        if region is not None:
            # 影の効果を設定
            blf.shadow(0, 3, 0.0, 1.0, 0.0, 0.5)
            # 影の位置を設定
            blf.shadow_offset(0, 2, -2)
            # 影の効果を有効化
            blf.enable(0, blf.SHADOW)
            op_cls.__draw_text(
                int(prefs.font_size * 1.3),
                prefs.left_top[0],
                region.height - prefs.left_top[1],
                "Working Hour"
            )
            # 影の効果を無効化
            blf.disable(0, blf.SHADOW)
            op_cls.__draw_text(
                prefs.font_size,
                prefs.left_top[0],
                region.height - int(prefs.left_top[1] + prefs.font_size * 1.5),
                "Object: " + sc.sample52_prop_object
            )
            op_cls.__draw_text(
                prefs.font_size,
                prefs.left_top[0],
                region.height - int(
                    prefs.left_top[1] + prefs.font_size * (1.5 + 2.5)
                ),
                "Object Mode: " + time_to_str(
                    op_cls.working_hour_db[sc.sample52_prop_object]['OBJECT']
                )
            )
            op_cls.__draw_text(
                prefs.font_size,
                prefs.left_top[0],
                region.height - int(
                    prefs.left_top[1] + prefs.font_size * (1.5 + 4.0)
                ),
                "Edit Mode: " + time_to_str(
                    op_cls.working_hour_db[sc.sample52_prop_object]['EDIT']
                )
            )

    # 前回の呼び出しからの時間差分を計算
    def __calc_delta(self, obj):
        # 現在時刻を取得
        cur_time = datetime.datetime.now()

        # オブジェクトやモードが異なっていた場合は無効とし、時間差分を0とする
        if (self.__prev_obj != obj) or (self.__prev_mode != obj.mode):
            delta = 0.0
        else:
            delta = (cur_time - self.__prev_time).total_seconds()

        # 情報をアップデート
        self.__prev_time = cur_time
        self.__prev_obj = obj
        self.__prev_mode = obj.mode

        return delta

    # データベースを更新
    def __update_db(self, context):
        op_cls = SAMPLE52_OT_CalculateWorkingHours

        # 全てのメッシュ型オブジェクトの取得
        obj_list = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']

        # データベースに存在しないオブジェクトをデータベースに追加
        for o in obj_list:
            if o not in op_cls.working_hour_db.keys():
                op_cls.working_hour_db[o] = {}
                op_cls.working_hour_db[o]['OBJECT'] = 0
                op_cls.working_hour_db[o]['EDIT'] = 0

        # 作業時間更新
        active_obj = context.active_object
        if not active_obj.name in obj_list:
            return      # メッシュ型オブジェクト以外は、作業時間を更新しない
        delta = self.__calc_delta(active_obj)
        if active_obj.mode in ['OBJECT', 'EDIT']:
            op_cls.working_hour_db[active_obj.name][active_obj.mode] += delta

    def modal(self, context, event):
        op_cls = SAMPLE52_OT_CalculateWorkingHours

        # タイマイベント以外の場合は無視
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}

        # 再描画
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if not op_cls.is_running():
            self.__handle_remove(context)
            return {'FINISHED'}

        # データベース更新
        self.__update_db(context)

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        op_cls = SAMPLE52_OT_CalculateWorkingHours

        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if not op_cls.is_running():
                op_cls.__running = True
                self.__handle_add(context)
                print("サンプル 5-2: 作業時間の計測を開始しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                op_cls.__running = False
                print("サンプル 5-2: 作業時間の計測を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE52_PT_CalculateWorkingHours(bpy.types.Panel):

    bl_label = "作業時間計測"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "サンプル 5-2"

    def draw(self, context):
        op_cls = SAMPLE52_OT_CalculateWorkingHours
        sc = context.scene
        layout = self.layout

        # 開始/停止ボタンを追加
        if not op_cls.is_running():
            layout.operator(
                SAMPLE52_OT_CalculateWorkingHours.bl_idname,
                text="開始", icon='PLAY'
            )
        else:
            layout.operator(
                SAMPLE52_OT_CalculateWorkingHours.bl_idname,
                text="終了", icon='PAUSE'
            )

        layout.separator()

        # 作業時間の描画
        layout.prop(sc, "sample52_prop_object", text="オブジェクト")


# プリファレンスのアドオン設定情報
class SAMPLE52_Preferences(bpy.types.AddonPreferences):

    bl_idname = __name__

    font_size: IntProperty(
        name="フォントサイズ",
        description="表示テキストのフォントサイズ",
        default=15,
        max=50,
        min=10
    )
    left_top: IntVectorProperty(
        name="左上座標",
        description="情報を表示する左上の座標",
        size=2,
        subtype='XYZ',
        default=(20, 60),
        max=300,
        min=0
    )

    def draw(self, context):
        layout = self.layout

        sp = layout.split(factor=0.3)
        col = sp.column()
        col.prop(self, "left_top")

        sp = sp.split(factor=0.4)
        col = sp.column()
        col.label(text="フォントサイズ")
        col.prop(self, "font_size", text="")


# 作業時間を表示するオブジェクトを選択するための項目リストを作成
def object_list_fn(scene, context):
    op_cls = SAMPLE52_OT_CalculateWorkingHours

    items = [("", "", "")]
    items.extend([(o, o, "") for o in op_cls.working_hour_db.keys()])

    return items


# プロパティの作成
def init_props():
    sc = bpy.types.Scene

    sc.sample52_prop_object = EnumProperty(
        name="オブジェクト",
        description="作業時間を表示する対象のオブジェクト",
        items=object_list_fn
    )


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene

    del sc.sample52_prop_object


classes = [
    SAMPLE52_OT_CalculateWorkingHours,
    SAMPLE52_PT_CalculateWorkingHours,
    SAMPLE52_Preferences,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    init_props()
    print("サンプル 5-2: アドオン『サンプル 5-2』が有効化されました。")


def unregister():
    clear_props()
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 5-2: アドオン『サンプル 5-2』が無効化されました。")


if __name__ == "__main__":
    register()
