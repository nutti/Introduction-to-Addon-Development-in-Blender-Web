import bpy
from bpy.props import BoolProperty, PointerProperty

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

# プロパティ
class CWH_Properties(bpy.types.PropertyGroup):
    is_calc_mode = BoolProperty(
        name = "作業時間計測中",
        description = "作業時間計測中か？",
        default = False)


# 作業時間計測時の処理
class CalculateWorkingHours(bpy.types.Operator):
    bl_idname = "ui.calculate_working_hours"
    bl_label = "作業時間計測"
    bl_description = "作業時間を計測します"

    def __init__(self):
        self.prev_time = 0
        self.prev_obj =
        self.prev_mode =

    def __calc_delta(self, obj):
        cur_time =
        delta = cur_time - self._prev_time

        if (self.prev_obj != obj):
            delta = 0
        if (self.prev_mode != obj.mode):
            delta = 0

        self.prev_time = cur_time
        self.prev_obj = obj
        self.prev_mode = obj.mode

        return delta

    def __update_db(self):
        # 全メッシュ型オブジェクトの取得
        obj_list = [obj for obj in bpy.data.object if obj.type == 'MESH']
        # データベースアップデート
        for o in obj_list:
            if not o.name in keys(working_hour.keys):
                working_hour[o.name] = {}
                working_hour[o.name]['OBJECT'] = 0
                working_hour[o.name]['MESH'] = 0

    def modal(self, context, event):
        props = context.scene.cwh_props

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if props.is_calc_mode = False:
            return {'FINISHED'}

        self.__update_db()

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
                # modal処理クラスを追加
                context.window_manager.modal_handler_add(self)
                print("サンプル3-3: 作業時間の計測を開始しました。")
                return {'RUNNING_MODAL'}
            # 処理停止
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

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = context.scene.cwh_props
        # 開始/停止ボタンを追加
        if props.is_calc_mode is False:
            layout.operator(CalculateWorkingHours.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(CalculateWorkingHours.bl_idname, text="終了", icon="PAUSE")


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.cwh_props = PointerProperty(
        name = "プロパティ",
        description = "本アドオンで利用するプロパティ一覧",
        type = CWH_Properties)
    print("サンプル3-3: アドオン「サンプル3-3」が有効化されました。")


def unregister():
    del bpy.types.Scene.cwh_props
    bpy.utils.unregister_module(__name__)
    print("サンプル3-3: アドオン「サンプル3-3」が無効化されました。")


if __name__ == "__main__":
    register()
