import bpy
from bpy.props import BoolProperty, PointerProperty, EnumProperty
from mathutils import Vector

bl_info = {
    "name": "サンプル3-10: キーボードのキー入力に応じてオブジェクトを並進移動させる（アドオン設定活用版）",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > オブジェクト並進移動",
    "description": "キーボードからの入力に応じてオブジェクトを並進移動させるアドオン（アドオン設定活用版）",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# プロパティ
class TOM_Properties(bpy.types.PropertyGroup):
    running = BoolProperty(
        name="オブジェクト並進移動モード中",
        description="オブジェクト並進移動モード中か？",
        default=False)


# オブジェクト並進移動モード時の処理
class TranslateObjectMode(bpy.types.Operator):
    bl_idname = "object.translate_object_mode"
    bl_label = "オブジェクト並進移動モード"
    bl_description = "オブジェクト並進移動モードへ移行します"

    def modal(self, context, event):
        props = context.scene.tom_props
//! [get_prefs]
        prefs = context.user_preferences.addons[__name__].preferences
//! [get_prefs]

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # キーボードのQキーが押された場合は、オブジェクト並進移動モードを終了
        if event.type == 'Q' and event.value == 'PRESS':
            props.running = False
            print("サンプル3-10: 通常モードへ移行しました。")
            return {'FINISHED'}

//! [refer_prefs]
        if event.value == 'PRESS':
            value = Vector((0.0, 0.0, 0.0))
            if event.type == prefs.x_axis:
                value.x = 1.0 if not event.shift else -1.0
            if event.type == prefs.y_axis:
                value.y = 1.0 if not event.shift else -1.0
            if event.type == prefs.z_axis:
                value.z = 1.0 if not event.shift else -1.0
            # 選択中のオブジェクトを並進移動する
            bpy.ops.transform.translate(value=value)
//! [refer_prefs]

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        props = context.scene.tom_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.running is False:
                props.running = True
                # modal処理クラスを追加
                context.window_manager.modal_handler_add(self)
                print("サンプル3-2: オブジェクト並進移動モードへ移行しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.running = False
                print("サンプル3-2: 通常モードへ移行しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_SOEM(bpy.types.Panel):
    bl_label = "オブジェクト並進移動モード"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = context.scene.tom_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(TranslateObjectMode.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(TranslateObjectMode.bl_idname, text="終了", icon="PAUSE")


key_list = [
    ('X', "X", 'X'),
    ('Y', "Y", 'Y'),
    ('Z', "Z", 'Z')
]

//! [addon_prefs]
# アドオン設定
class SOEM_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    x_axis = EnumProperty(
        name="X軸",
        description="X軸に関する処理を行うキー",
        items=key_list,
        default='X')
    y_axis = EnumProperty(
        name="Y軸",
        description="Y軸に関する処理を行うキー",
        items=key_list,
        default='Y')
    z_axis = EnumProperty(
        name="Z軸",
        description="Z軸に関する処理を行うキー",
        items=key_list,
        default='Z')

    def draw(self, context):
        layout = self.layout

        layout.label("キー割り当て: ")
        row = layout.row()
        row.prop(self, "x_axis")
        row.prop(self, "y_axis")
        row.prop(self, "z_axis")
//! [addon_prefs]


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.tom_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=TOM_Properties)
    print("サンプル3-10: アドオン「サンプル3-10」が有効化されました。")


def unregister():
    del bpy.types.Scene.tom_props
    bpy.utils.unregister_module(__name__)
    print("サンプル3-10: アドオン「サンプル3-10」が無効化されました。")


if __name__ == "__main__":
    register()
