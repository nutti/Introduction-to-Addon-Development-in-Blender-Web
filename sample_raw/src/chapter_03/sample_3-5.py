import bpy
from bpy.props import BoolProperty, PointerProperty, IntProperty, EnumProperty
//! [import_blf]
import blf
//! [import_blf]
import datetime
import math


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


# プロパティ
class RT_Properties(bpy.types.PropertyGroup):
    running = BoolProperty(
        name="テキスト描画中",
        description="テキスト描画中か？",
        default=False)


# テキスト描画
class RenderText(bpy.types.Operator):
    bl_idname = "view_3d.render_text"
    bl_label = "テキスト描画"
    bl_description = "テキストを描画します"

    handle = None           # 描画関数ハンドラ


    def __handle_add(self, context):
        if RenderText.handle is None:
//! [add_render_func]
            # 描画関数の登録
            RenderText.handle = bpy.types.SpaceView3D.draw_handler_add(
                RenderText.render, (self, context), 'WINDOW', 'POST_PIXEL')
//! [add_render_func]
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)


    def __handle_remove(self, context):
//! [remove_render_func]
        if RenderText.handle is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(RenderText.handle, 'WINDOW')
            RenderText.handle = None
//! [remove_render_func]


//! [render_text]
    @staticmethod
    def render_text(size, x, y, s):
        # フォントサイズを指定
        blf.size(0, size, 72)
        # 描画位置を指定
        blf.position(0, x, y, 0)
        # テキストを描画
        blf.draw(0, s)
//! [render_text]


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
    def render(self, context):
        # リージョン幅を取得するため、描画先のリージョンを得る
        region = RenderText.get_region(context, 'VIEW_3D', 'WINDOW')

//! [call_render_region]
        # 描画先のリージョンへテキストを描画
        if region is not None:
            # 影の効果を設定
            blf.shadow(0, 3, 0.0, 1.0, 0.0, 0.5)
            # 影の位置を設定
            blf.shadow_offset(0, 2, -2)
            # 影の効果を有効化
            blf.enable(0, blf.SHADOW)
            RenderText.render_text(40, 40, region.height - 120, "Hello Blender world!!")
            # 影の効果を無効化
            blf.disable(0, blf.SHADOW)
            RenderText.render_text(30, 40, region.height - 180, "Suzanne on your lap")
//! [call_render_region]


    def modal(self, context, event):
        props = context.scene.rt_props
        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if props.running is False:
            self.__handle_remove(context)
            return {'FINISHED'}

        return {'PASS_THROUGH'}


    def invoke(self, context, event):
        props = context.scene.rt_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.running is False:
                props.running = True
                self.__handle_add(context)
                print("サンプル3-5: テキストの描画を開始しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.running = False
                print("サンプル3-5: テキストの描画を終了しました。")
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
        props = sc.rt_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(RenderText.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(RenderText.bl_idname, text="終了", icon="PAUSE")


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.rt_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=RT_Properties)


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.rt_props


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
