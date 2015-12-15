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

    __handle = None

    # 画像描画関数を登録
    @staticmethod
    def handle_add():
        RenderLoadedTexture.__handle = bpy.types.SpaceView3D.draw_handler_add(
            RenderLoadedTexture.render,
            (), 'WINDOW', 'POST_PIXEL')

    # 画像描画関数を登録解除
    @staticmethod
    def handle_remove():
        if RenderLoadedTexture.__handle is not None:
            bpy.types.SpaceView3D.draw_handler_remove(
                RenderLoadedTexture.__handle, 'WINDOW')
            RenderLoadedTexture.__handle = None

    @staticmethod
    def render(self, context):
        wm = context.window_manager
        sc = context.scene

        # no texture is selected
        if sc.tex_image == "None":
            return

        # 描画領域の作成
        positions = [
            [10.0, 10.0],     # 左下
            [10.0, 600.0],    # 左上
            [600.0, 600.0],   # 右上
            [600.0, 10.0]     # 右下
            ]
        tex_coords = [
            [0.0, 0.0],
            [0.0, 1.0],
            [1.0, 1.0],
            [1.0, 0.0]
            ]

        # get texture to be renderred
        img = bpy.data.images[sc.tex_image]

        # OpenGL configuration
        bgl.glEnable(bgl.GL_BLEND)
        bgl.glEnable(bgl.GL_TEXTURE_2D)
        if img.bindcode:
            bind = img.bindcode
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, bind)
            bgl.glTexParameteri(
                bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_LINEAR)
            bgl.glTexParameteri(
                bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_LINEAR)
            bgl.glTexEnvi(
                bgl.GL_TEXTURE_ENV, bgl.GL_TEXTURE_ENV_MODE, bgl.GL_MODULATE)

        # render texture
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor4f(1.0, 1.0, 1.0, 0.7)
        for (x, y), (u, v) in zip(positions, tex_coords):
            bgl.glTexCoord2f(u, v)
            bgl.glVertex2f(x, y)
        bgl.glEnd()

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
