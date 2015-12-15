```py:sample_8.py
import bpy
import bmesh
from bpy.props import IntProperty, BoolProperty, PointerProperty

bl_info = {
    "name": "サンプル8: Blenderに読み込まれている画像を表示する",
    "author": "Nutti",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > サンプル8: Blenderに読み込まれている画像を表示する",
    "description": "Blenderに読み込まれている画像を3Dビューに表示する",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "View3D"
}


# 読み込まれている画像の名前一覧を返す関数
def image_list_fn(scene, context):
    items = [(key, key, "") for key in bpy.data.images.keys()]
    return items


# 読み込んだ画像を表示
class RenderLoadedTexture(bpy.types.Operator):
    bl_idname = "view_3d.delete_face_by_rclick"
    bl_label = "読み込んだ画像を表示"
    bl_description = "読み込んだ画像を表示します"

    def execute(self, context):
        return {'FINISHED'}


# UI
class OBJECT_PT_RLT(bpy.types.Panel):
    bl_label = "読み込んだ画像を表示"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        layout.prop(sc, "rtl_image", text="")
        layout.prop(sc, "rtl_running", "表示")


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.rtl_image = EnumProperty(
        name = "画像",
        description = "表示する画像",
        type = image_list_fn)
    sc.rtl_running = BoolProperty(
        name = "表示",
        description = "表示する",
        default = False)
    print("サンプル 8: アドオン「サンプル 8」が有効化されました。")


def unregister():
    del bpy.types.Scene.dfrc_props
    bpy.utils.unregister_module(__name__)
    print("サンプル 8: アドオン「サンプル 8」が無効化されました。")


if __name__ == "__main__":
    register()

```
