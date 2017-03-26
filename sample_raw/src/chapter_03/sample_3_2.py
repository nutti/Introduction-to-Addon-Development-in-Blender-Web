import bpy
from bpy.props import BoolProperty, PointerProperty
from mathutils import Vector


bl_info = {
    "name": "サンプル3-2: キーボードのキー入力に応じてオブジェクトを並進移動させる",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > オブジェクト並進移動",
    "description": "キーボードからの入力に応じてオブジェクトを並進移動させるアドオン",
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
        default=False
    )


# オブジェクト並進移動モード時の処理
class TranslateObjectMode(bpy.types.Operator):

    bl_idname = "object.translate_object_mode"
    bl_label = "オブジェクト並進移動モード"
    bl_description = "オブジェクト並進移動モードへ移行します"

    def modal(self, context, event):
        props = context.scene.tom_props

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

//! [exit_modal_mode]
        # キーボードのQキーが押された場合は、オブジェクト並進移動モードを終了
        if event.type == 'Q' and event.value == 'PRESS':
            props.running = False
            print("サンプル3-2: 通常モードへ移行しました。")
            return {'FINISHED'}
//! [exit_modal_mode]

//! [check_key_state]
        if event.value == 'PRESS':
            value = Vector((0.0, 0.0, 0.0))
            if event.type == 'X':
                value.x = 1.0 if not event.shift else -1.0
            if event.type == 'Y':
                value.y = 1.0 if not event.shift else -1.0
            if event.type == 'Z':
                value.z = 1.0 if not event.shift else -1.0
//! [check_key_state]
//! [translate_object]
            # 選択中のオブジェクトを並進移動する
            bpy.ops.transform.translate(value=value)
//! [translate_object]

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
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_SOEM(bpy.types.Panel):

    bl_label = "オブジェクト並進移動モード"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        props = context.scene.tom_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(
                TranslateObjectMode.bl_idname, text="開始", icon="PLAY"
            )
        else:
            layout.operator(
                TranslateObjectMode.bl_idname, text="終了", icon="PAUSE"
            )


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.tom_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=TOM_Properties
    )
    print("サンプル3-2: アドオン「サンプル3-2」が有効化されました。")


def unregister():
    del bpy.types.Scene.tom_props
    bpy.utils.unregister_module(__name__)
    print("サンプル3-2: アドオン「サンプル3-2」が無効化されました。")


if __name__ == "__main__":
    register()
