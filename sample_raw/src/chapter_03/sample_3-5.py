import bpy
from bpy.props import BoolProperty, PointerProperty, IntProperty, EnumProperty
//! [import_blf]
import blf
//! [import_blf]
import datetime
import math


bl_info = {
    "name": "サンプル3-5: オブジェクトモードとエディットモードでの作業時間を計測する（UI改善版）",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > 作業時間計測",
    "description": "各オブジェクトについて、オブジェクトモードとエディットモードでの作業時間を計測するアドオン（UI改善版）",
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

    handle = None           # 描画関数ハンドラ

    def __init__(self):
        self.timer = None           # タイマハンドラ
        self.prev_time = 0.0        # __calc_delta()メソッドを呼び出した時の時間
        self.prev_obj = None        # __calc_delta()メソッドを呼び出した時に選択していたオブジェクト
        self.prev_mode = None   # __calc_delta()メソッドを呼び出した時のモード


    def __handle_add(self, context):
        if (self.timer is None) and (CalculateWorkingHours.handle is None):
            # タイマを登録
            self.timer = context.window_manager.event_timer_add(
                0.10, context.window)
//! [add_render_func]
            # 描画関数の登録
            CalculateWorkingHours.handler = bpy.types.SpaceView3D.draw_handler_add(
                CalculateWorkingHours.render_working_hours, (self, context), 'WINDOW', 'POST_PIXEL')
//! [add_render_func]
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)


    def __handle_remove(self, context):
//! [remove_render_func]
        if CalculateWorkingHours.handler is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(CalculateWorkingHours.handler, 'WINDOW')
            CalculateWorkingHours.handler = None
//! [remove_render_func]
        if self.timer is not None:
            # タイマの登録を解除
            context.window_manager.event_timer_remove(self.timer)
            self.timer = None


    # 作業時間を表示用にフォーマット化
    @staticmethod
    def make_time_fmt(time):
        msec = math.floor(time * 1000) % 1000   # ミリ秒
        sec = math.floor(time) % 60                     # 秒
        minute = math.floor(time / 60) % 60         # 分
        hour = math.floor(time / (60 * 60))           # 時

        return "%d:%02d:%02d.%d" % (hour, minute, sec, math.floor(msec / 100))


//! [render_message]
    @staticmethod
    def render_message(size, x, y, msg):
        # フォントサイズを指定
        blf.size(0, size, 72)
        # 描画位置を指定
        blf.position(0, x, y, 0)
        # 文字列を描画
        blf.draw(0, msg)
//! [render_message]


//! [get_region]
    @staticmethod
    def get_region(context, area_type, region_type):
        region = None

        # 指定されたエリアを取得する
        for area in context.screen.areas:
            if area.type == area_type:
                break
        # 指定されたリージョンを取得する
        for region in area.regions:
            if region.type == region_type:
                break

        return region
//! [get_region]


    @staticmethod
    def render_working_hours(self, context):
        sc = context.scene
        props = sc.cwh_props

        # 表示するオブジェクトが選択されていない場合は、描画しない
        if sc.cwh_prop_object == '':
            return

        # リージョン幅を取得するため、描画先のリージョンを得る
        region = CalculateWorkingHours.get_region(context, 'VIEW_3D', 'WINDOW')

//! [call_render_region]
        # 描画先のリージョンへ文字列を描画
        if region is not None:
            # 影の効果を設定
            blf.shadow(0, 3, 0.0, 1.0, 0.0, 0.5)
            # 影の位置を設定
            blf.shadow_offset(0, 2, -2)
            # 影の効果を有効化
            blf.enable(0, blf.SHADOW)
            CalculateWorkingHours.render_message(20, 20, region.height - 60, "Working Hour")
            # 影の効果を無効化
            blf.disable(0, blf.SHADOW)
            CalculateWorkingHours.render_message(15, 20, region.height - 90, "Object: " + sc.cwh_prop_object)
            CalculateWorkingHours.render_message(15, 20, region.height - 115,
                "Object Mode: " + CalculateWorkingHours.make_time_fmt(props.working_hour_db[sc.cwh_prop_object]['OBJECT']))
            CalculateWorkingHours.render_message(15, 20, region.height - 135, "Edit Mode: " + CalculateWorkingHours.make_time_fmt(props.working_hour_db[sc.cwh_prop_object]['EDIT']))
//! [call_render_region]


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
                print("サンプル3-5: 作業時間の計測を開始しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.is_calc_mode = False
                print("サンプル3-5: 作業時間の計測を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_CWH(bpy.types.Panel):
    bl_label = "作業時間計測"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


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
    print("サンプル3-5: アドオン「サンプル3-5」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-5: アドオン「サンプル3-5」が無効化されました。")


if __name__ == "__main__":
    register()
