import bpy
from bpy.props import BoolProperty, PointerProperty
//! [import_blf]
import blf
//! [import_blf]


bl_info = {
    "name": "サンプル3-5: 3Dビューエリアにテキストを描画する",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > テキスト描画",
    "description": "3Dビューエリアにテキストを描画するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


# テキスト描画
class RenderText(bpy.types.Operator):

    bl_idname = "view_3d.render_text"
    bl_label = "テキスト描画"
    bl_description = "テキストを描画します"

    __handle = None           # 描画関数ハンドラ

    def __handle_add(self, context):
        if RenderText.__handle is None:
//! [add_render_func]
            # 描画関数の登録
            RenderText.__handle = bpy.types.SpaceView3D.draw_handler_add(
                RenderText.__render, (self, context), 'WINDOW', 'POST_PIXEL')
//! [add_render_func]

    def __handle_remove(self, context):
//! [remove_render_func]
        if RenderText.__handle is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(
                RenderText.__handle, 'WINDOW'
            )
            RenderText.__handle = None
//! [remove_render_func]

//! [render_text]
    @staticmethod
    def __render_text(size, x, y, s):
        # フォントサイズを指定
        blf.size(0, size, 72)
        # 描画位置を指定
        blf.position(0, x, y, 0)
        # テキストを描画
        blf.draw(0, s)
//! [render_text]

//! [get_region]
    @staticmethod
    def __get_region(context, area_type, region_type):
        region = None
        area = None

        # 指定されたエリアを取得する
        for a in context.screen.areas:
            if a.type == area_type:
                area = a
                break
        else:
            return None
        # 指定されたリージョンを取得する
        for r in area.regions:
            if r.type == region_type:
                region = r
                break

        return region
//! [get_region]

    @staticmethod
    def __render(self, context):
        # リージョン幅を取得するため、描画先のリージョンを得る
        region = RenderText.__get_region(context, 'VIEW_3D', 'WINDOW')

//! [call_render_region]
        # 描画先のリージョンへテキストを描画
        if region is not None:
            # 影の効果を設定
            blf.shadow(0, 3, 0.0, 1.0, 0.0, 0.5)
            # 影の位置を設定
            blf.shadow_offset(0, 2, -2)
            # 影の効果を有効化
            blf.enable(0, blf.SHADOW)
            RenderText.__render_text(
                40, 40, region.height - 120, "Hello Blender world!!"
            )
            # 影の効果を無効化
            blf.disable(0, blf.SHADOW)
            RenderText.__render_text(
                30, 40, region.height - 180, "Suzanne on your lap"
            )
//! [call_render_region]

    def invoke(self, context, event):
        sc = context.scene
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if sc.rt_running is False:
                sc.rt_running = True
                self.__handle_add(context)
                print("サンプル3-5: テキストの描画を開始しました。")
            # 終了ボタンが押された時の処理
            else:
                sc.rt_running = False
                self.__handle_remove(context)
                print("サンプル3-5: テキストの描画を終了しました。")
            # 3Dビューの画面を更新
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_RT(bpy.types.Panel):

    bl_label = "テキスト描画"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        # 開始/停止ボタンを追加
        if sc.rt_running is False:
            layout.operator(RenderText.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(RenderText.bl_idname, text="終了", icon="PAUSE")


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.rt_running = BoolProperty(
        name="実行中",
        description="実行中か？",
        default=False
    )


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.rt_running


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
