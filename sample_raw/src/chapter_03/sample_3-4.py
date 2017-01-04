import bpy
import bgl
from bpy.props import FloatVectorProperty, BoolProperty, EnumProperty

bl_info = {
    "name": "サンプル8: OpenGL向けのAPIを利用して図形を表示する",
    "author": "Nutti",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > 図形を表示",
    "description": "OpenGL向けのAPIを利用して3Dビューに図形を表示する",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


# 図形を表示
class RenderFigure(bpy.types.Operator):
    bl_idname = "view_3d.render_figure"
    bl_label = "図形を表示"
    bl_description = "図形を表示します"

    __handle = None

    # 画像描画関数を登録
    @staticmethod
    def handle_add(self, context):
        if RenderFigure.__handle is None:
            RenderFigure.__handle = bpy.types.SpaceView3D.draw_handler_add(
                RenderFigure.render,
                (self, context), 'WINDOW', 'POST_PIXEL')

    # 画像描画関数を登録解除
    @staticmethod
    def handle_remove(self, context):
        if RenderFigure.__handle is not None:
            bpy.types.SpaceView3D.draw_handler_remove(
                RenderFigure.__handle, 'WINDOW')
            RenderFigure.__handle = None

    @staticmethod
    def render(self, context):
        sc = context.scene

        # OpenGLの設定
        bgl.glEnable(bgl.GL_BLEND)

        # 図形を表示
        if sc.rf_figure == 'TRIANGLE':
            bgl.glBegin(bgl.GL_TRIANGLES)
            bgl.glColor4f(1.0, 1.0, 1.0, 0.7)
            bgl.glVertex2f(sc.rf_vert_1[0], sc.rf_vert_1[1])
            bgl.glVertex2f(sc.rf_vert_2[0], sc.rf_vert_2[1])
            bgl.glVertex2f(sc.rf_vert_3[0], sc.rf_vert_3[1])
            bgl.glEnd()
        elif sc.rf_figure == 'RECTANGLE':
            bgl.glBegin(bgl.GL_QUADS)
            bgl.glColor4f(1.0, 1.0, 1.0, 0.7)
            bgl.glVertex2f(sc.rf_vert_1[0], sc.rf_vert_1[1])
            bgl.glVertex2f(sc.rf_vert_2[0], sc.rf_vert_2[1])
            bgl.glVertex2f(sc.rf_vert_3[0], sc.rf_vert_3[1])
            bgl.glVertex2f(sc.rf_vert_4[0], sc.rf_vert_4[1])
            bgl.glEnd()


class RenderingButton(bpy.types.Operator):
    bl_idname = "view3d.rendering_button"
    bl_label = "図形表示/非表示切り替えボタン"
    bl_description = "図形の表示/非表示を切り替えるボタン"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        sc = context.scene
        if sc.rf_running is True:
            RenderFigure.handle_remove(self, context)
            sc.rf_running = False
        elif sc.rf_running is False:
            RenderFigure.handle_add(self, context)
            sc.rf_running = True

        return {'FINISHED'}


class OBJECT_PT_RF(bpy.types.Panel):
    bl_label = "図形を表示"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        if context.area:
            context.area.tag_redraw()
        if sc.rf_running is True:
            layout.operator(RenderingButton.bl_idname, text="Stop", icon="PAUSE")
            layout.prop(sc, "rf_figure", "図形")
            layout.prop(sc, "rf_vert_1", "頂点1")
            layout.prop(sc, "rf_vert_2", "頂点2")
            layout.prop(sc, "rf_vert_3", "頂点3")
            if sc.rf_figure == 'RECTANGLE':
                layout.prop(sc, "rf_vert_4", "頂点4")
        elif sc.rf_running is False:
            layout.operator(RenderingButton.bl_idname, text="Start", icon="PLAY")


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.rf_running = BoolProperty(
        name = "実行中",
        description = "実行中か？",
        default = False
    )
    sc.rf_figure = EnumProperty(
        name = "図形",
        description = "表示する図形",
        items = [
            ('TRIANGLE', "三角形", "三角形を表示します"),
            ('RECTANGLE', "四角形", "四角形を表示します")]
    )
    sc.rf_vert_1 = FloatVectorProperty(
        name = "頂点1",
        description = "図形の頂点",
        size = 2,
        default = (50.0, 50.0)
    )
    sc.rf_vert_2 = FloatVectorProperty(
        name = "頂点2",
        description = "図形の頂点",
        size = 2,
        default = (50.0, 100.0)
    )
    sc.rf_vert_3 = FloatVectorProperty(
        name = "頂点3",
        description = "図形の頂点",
        size = 2,
        default = (100.0, 100.0)
    )
    sc.rf_vert_4 = FloatVectorProperty(
        name = "頂点4",
        description = "図形の頂点",
        size = 2,
        default = (100.0, 50.0)
    )
    print("サンプル8: アドオン「サンプル8」が有効化されました。")


def unregister():
    sc = bpy.types.Scene
    del sc.rf_running
    del sc.rf_figure
    del sc.rf_vert_1
    del sc.rf_vert_2
    del sc.rf_vert_3
    del sc.rf_vert_4
    bpy.utils.unregister_module(__name__)
    print("サンプル8: アドオン「サンプル8」が無効化されました。")


if __name__ == "__main__":
    register()
