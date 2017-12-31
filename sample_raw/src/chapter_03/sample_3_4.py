import bpy
//! [import_bgl]
import bgl
//! [import_bgl]
from bpy.props import FloatVectorProperty, BoolProperty, EnumProperty


bl_info = {
    "name": "サンプル3-4: OpenGL向けのAPIを利用して図形を表示する",
    "author": "Nutti",
    "version": (2, 0),
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

//! [handle_add]
    # 画像描画関数を登録
    def __handle_add(self, context):
        if RenderFigure.__handle is None:
            RenderFigure.__handle = bpy.types.SpaceView3D.draw_handler_add(
                RenderFigure.__render,
                (context, ), 'WINDOW', 'POST_PIXEL'
            )
//! [handle_add]

//! [handle_remove]
    # 画像描画関数を登録解除
    def __handle_remove(self, context):
        if RenderFigure.__handle is not None:
            bpy.types.SpaceView3D.draw_handler_remove(
                RenderFigure.__handle, 'WINDOW'
            )
            RenderFigure.__handle = None
//! [handle_remove]

//! [render]
    @staticmethod
    def __render(context):
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
        # 有効化したOpenGLの設定は無効化する
        bgl.glDisable(bgl.GL_BLEND)
//! [render]

    def invoke(self, context, event):
        sc = context.scene
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if sc.rf_running is False:
                sc.rf_running = True
                self.__handle_add(context)
                print("サンプル3-4: 図形の描画を開始しました。")
            # 終了ボタンが押された時の処理
            else:
                sc.rf_running = False
                self.__handle_remove(context)
                print("サンプル3-4: 図形の描画を終了しました。")
            # 3Dビューの画面を更新
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


//! [panel_class]
class OBJECT_PT_RF(bpy.types.Panel):

    bl_label = "図形を表示"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        if sc.rf_running is True:
            layout.operator(RenderFigure.bl_idname, text="終了", icon="PAUSE")
            layout.prop(sc, "rf_figure", "図形")
            layout.prop(sc, "rf_vert_1", "頂点1")
            layout.prop(sc, "rf_vert_2", "頂点2")
            layout.prop(sc, "rf_vert_3", "頂点3")
            if sc.rf_figure == 'RECTANGLE':
                layout.prop(sc, "rf_vert_4", "頂点4")
        else:
            layout.operator(RenderFigure.bl_idname, text="開始", icon="PLAY")
//! [panel_class]


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.rf_running = BoolProperty(
        name="実行中",
        description="実行中か？",
        default=False
    )
    sc.rf_figure = EnumProperty(
        name="図形",
        description="表示する図形",
        items=[
            ('TRIANGLE', "三角形", "三角形を表示します"),
            ('RECTANGLE', "四角形", "四角形を表示します")
        ]
    )
    sc.rf_vert_1 = FloatVectorProperty(
        name="頂点1",
        description="図形の頂点",
        size=2,
        default=(50.0, 50.0)
    )
    sc.rf_vert_2 = FloatVectorProperty(
        name="頂点2",
        description="図形の頂点",
        size=2,
        default=(50.0, 100.0)
    )
    sc.rf_vert_3 = FloatVectorProperty(
        name="頂点3",
        description="図形の頂点",
        size=2,
        default=(100.0, 100.0)
    )
    sc.rf_vert_4 = FloatVectorProperty(
        name="頂点4",
        description="図形の頂点",
        size=2,
        default=(100.0, 50.0)
    )


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.rf_running
    del sc.rf_figure
    del sc.rf_vert_1
    del sc.rf_vert_2
    del sc.rf_vert_3
    del sc.rf_vert_4


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル3-4: アドオン「サンプル3-4」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-4: アドオン「サンプル3-4」が無効化されました。")


if __name__ == "__main__":
    register()
