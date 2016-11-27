import bpy
from bpy.props import BoolProperty, PointerProperty, IntProperty, EnumProperty
import datetime

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
    "category": "UI"
}


working_hour = {}

def update_db():
    # 全メッシュ型オブジェクトの取得
    obj_list = [obj.name for obj in bpy.data.objects if obj.type == 'MESH']
    # データベースアップデート
    for o in obj_list:
        if not o in working_hour.keys():
            working_hour[o] = {}
            working_hour[o]['OBJECT'] = 0
            working_hour[o]['EDIT'] = 0

# プロパティ
class CWH_Properties(bpy.types.PropertyGroup):
    is_calc_mode = BoolProperty(
        name="作業時間計測中",
        description="作業時間計測中か？",
        default=False)


# 作業時間計測時の処理
class CalculateWorkingHours(bpy.types.Operator):
    bl_idname = "ui.calculate_working_hours"
    bl_label = "作業時間計測"
    bl_description = "作業時間を計測します"

    timer = None

    def __init__(self):
        self.prev_time = 0.0
        self.prev_obj = None
        self.prev_mode = None

    @staticmethod
    def handle_add(self, context):
        if CalculateWorkingHours.timer is None:
            CalculateWorkingHours.timer = context.window_manager.event_timer_add(
                0.10, context.window)
            context.window_manager.modal_handler_add(self)

    @staticmethod
    def handle_remove(self, context):
        if CalculateWorkingHours.timer is not None:
            context.window_manager.event_timer_remove(CalculateWorkingHours.timer)
            CalculateWorkingHours.timer = None

    def __calc_delta(self, obj):
        cur_time = datetime.datetime.now()

        if (self.prev_obj != obj) or (self.prev_mode != obj.mode):
            delta = 0.0
        else:
            delta = (cur_time - self.prev_time).total_seconds()

        self.prev_time = cur_time
        self.prev_obj = obj
        self.prev_mode = obj.mode

        return delta

    def modal(self, context, event):
        global working_hour
        props = context.scene.cwh_props

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if props.is_calc_mode is False:
            return {'FINISHED'}

        update_db()

        active_obj = context.active_object
        delta = self.__calc_delta(active_obj)
        if active_obj.mode in ['OBJECT', 'EDIT']:
            working_hour[active_obj.name][active_obj.mode] += delta

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        props = context.scene.cwh_props
        if context.area.type == 'VIEW_3D':
            # 処理開始
            if props.is_calc_mode is False:
                props.is_calc_mode = True
                CalculateWorkingHours.handle_add(self, context)
                print("サンプル3-3: 作業時間の計測を開始しました。")
                return {'RUNNING_MODAL'}
            # 処理停止
            else:
                CalculateWorkingHours.handle_remove(self, context)
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

    def draw(self, context):
        global working_hour
        sc = context.scene
        layout = self.layout
        props = sc.cwh_props
        # 開始/停止ボタンを追加
        if props.is_calc_mode is False:
            layout.operator(CalculateWorkingHours.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(CalculateWorkingHours.bl_idname, text="終了", icon="PAUSE")

        layout.separator()

        layout.prop(sc, "cwh_prop_object", text="オブジェクト")
        if sc.cwh_prop_object != "":
            layout.label(text="オブジェクトモード：%.1f" % working_hour[sc.cwh_prop_object]['OBJECT'])
            layout.label(text="エディットモード：%.1f" % working_hour[sc.cwh_prop_object]['EDIT'])


def object_list_fn(scene, context):
    global working_hour
    items = [("", "", "")]
    items.extend([(o, o, "") for o in working_hour.keys()])

    return items


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
