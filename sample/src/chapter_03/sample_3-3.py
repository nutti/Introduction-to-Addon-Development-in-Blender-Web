import bpy
from bpy.props import BoolProperty, PointerProperty, IntProperty, EnumProperty
import datetime
import math


bl_info = {
    "name": "サンプル3-3: オブジェクトモードとエディットモードでの作業時間を計測する",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > 作業時間計測",
    "description": "各オブジェクトについて、オブジェクトモードとエディットモードでの作業時間を計測するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "System"
}


# プロパティ
class CWH_Properties(bpy.types.PropertyGroup):
    is_calc_mode = BoolProperty(
        name="作業時間計測中",
        description="作業時間計測中か？",
        default=False)
    working_hour_db = {}    # 作業時間を保存するためのデータベース


# 作業時間計測時の処理
class CalculateWorkingHours(bpy.types.Operator):
    bl_idname = "ui.calculate_working_hours"
    bl_label = "作業時間計測"
    bl_description = "作業時間を計測します"


    def __init__(self):
        self.timer = None           # タイマのハンドラ
        self.prev_time = 0.0        # __calc_delta()メソッドを呼び出した時の時間
        self.prev_obj = None        # __calc_delta()メソッドを呼び出した時に選択していたオブジェクト
        self.prev_mode = None   # __calc_delta()メソッドを呼び出した時のモード


    def __handle_add(self, context):
        if self.timer is None:
            # タイマを登録
            CalculateWorkingHours.timer = context.window_manager.event_timer_add(
                0.10, context.window)
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)


    def __handle_remove(self, context):
        if self.timer is not None:
            # タイマの登録を解除
            context.window_manager.event_timer_remove(self.timer)
            self.timer = None


    # 前回の呼び出しからの時間差分を計算
    def __calc_delta(self, obj):
        # 現在時刻を取得
        cur_time = datetime.datetime.now()

        # オブジェクトやモードが異なっていた場合は無効とし、時間差分を0とする
        if (self.prev_obj != obj) or (self.prev_mode != obj.mode):
            delta = 0.0
        else:
            delta = (cur_time - self.prev_time).total_seconds()

        # 情報をアップデート
        self.prev_time = cur_time
        self.prev_obj = obj
        self.prev_mode = obj.mode

        return delta


    # データベースを更新
    def __update_db(self, context):
        props = context.scene.cwh_props

        # 全てのメッシュ型オブジェクトの取得
        obj_list = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']
        # データベースに存在しないオブジェクトをデータベースに追加
        for o in obj_list:
            if not o in props.working_hour_db.keys():
                props.working_hour_db[o] = {}
                props.working_hour_db[o]['OBJECT'] = 0
                props.working_hour_db[o]['EDIT'] = 0

        # 作業時間更新
        active_obj = context.active_object
        delta = self.__calc_delta(active_obj)
        if active_obj.mode in ['OBJECT', 'EDIT']:
            props.working_hour_db[active_obj.name][active_obj.mode] += delta


    def modal(self, context, event):
        props = context.scene.cwh_props

        # タイマイベント以外の場合は無視
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if props.is_calc_mode is False:
            self.__handle_remove(context)
            return {'FINISHED'}

        # データベース更新
        self.__update_db(context)

        return {'PASS_THROUGH'}


    def invoke(self, context, event):
        props = context.scene.cwh_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.is_calc_mode is False:
                props.is_calc_mode = True
                self.__handle_add(context)
                print("サンプル3-3: 作業時間の計測を開始しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.is_calc_mode = False
                print("サンプル3-3: 作業時間の計測を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_CWH(bpy.types.Panel):
    bl_label = "作業時間計測"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


    # 作業時間を表示用にフォーマット化
    def __make_time_fmt(self, time):
        msec = math.floor(time * 1000) % 1000   # ミリ秒
        sec = math.floor(time) % 60                     # 秒
        minute = math.floor(time / 60) % 60         # 分
        hour = math.floor(time / (60 * 60))           # 時

        return "%d:%02d:%02d.%d" % (hour, minute, sec, math.floor(msec / 100))


    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = sc.cwh_props
        # 開始/停止ボタンを追加
        if props.is_calc_mode is False:
            layout.operator(CalculateWorkingHours.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(CalculateWorkingHours.bl_idname, text="終了", icon="PAUSE")

        layout.separator()

        # 作業時間の描画
        layout.prop(sc, "cwh_prop_object", text="オブジェクト")
        if sc.cwh_prop_object != "":
            column = layout.column()
            row = column.row()
            row.label(text="オブジェクトモード")
            row.label(text=self.__make_time_fmt(props.working_hour_db[sc.cwh_prop_object]['OBJECT']))
            row = column.row()
            row.label(text="エディットモード")
            row.label(text=self.__make_time_fmt(props.working_hour_db[sc.cwh_prop_object]['EDIT']))


# 作業時間を表示するオブジェクトを選択するための項目リストを作成
def object_list_fn(scene, context):
    props = context.scene.cwh_props
    items = [("", "", "")]
    items.extend([(o, o, "") for o in props.working_hour_db.keys()])

    return items


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.cwh_prop_object = EnumProperty(
        name="オブジェクト",
        description="作業時間を表示する対象のオブジェクト",
        items=object_list_fn)
    sc.cwh_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=CWH_Properties)


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.cwh_prop_object
    del sc.cwh_props


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル3-3: アドオン「サンプル3-3」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-3: アドオン「サンプル3-3」が無効化されました。")


if __name__ == "__main__":
    register()
