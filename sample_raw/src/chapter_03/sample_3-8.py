import bpy
from bpy.props import BoolProperty, PointerProperty, IntProperty, EnumProperty
import blf
import datetime
import math


bl_info = {
    "name": "サンプル3-8: オブジェクト名の表示を補助するアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > オブジェクト名の表示補助",
    "description": "オブジェクトの位置にオブジェクト名を表示し、マウスカーソルから発するレイと交差するオブジェクト名を表示するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}



# オブジェクト名を表示
class ShowObjectName(bpy.types.Operator):
    bl_idname = "view3d.show_object_name"
    bl_label = "オブジェクト名の表示補助"
    bl_description = "オブジェクトの位置にオブジェクト名を表示し、マウスカーソルから発するレイと交差するオブジェクト名を表示します"

    handle = None           # 描画関数ハンドラ


    def __handle_add(self, context):
        if ShowObjectName.handle is None:
            # 描画関数の登録
            ShowObjectName.handler = bpy.types.SpaceView3D.draw_handler_add(
                ShowObjectName.render_object_name, (self, context), 'WINDOW', 'POST_PIXEL')
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)


    def __handle_remove(self, context):
        if ShowObjectName.handler is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(ShowObjectName.handler, 'WINDOW')
            ShowObjectName.handler = None


    @staticmethod
    def render_message(size, x, y, msg):
        blf.size(0, size, 72)
        blf.position(0, x, y, 0)
        blf.draw(0, msg)


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


    @staticmethod
    def render_working_hours(self, context):
        sc = context.scene
        props = sc.cwh_props

        # 表示するオブジェクトが選択されていない場合は、描画しない
        if sc.cwh_prop_object == '':
            return

        # リージョン幅を取得するため、描画先のリージョンを得る
        region = ShowObjectName.get_region(context, 'VIEW_3D', 'WINDOW')

        # 描画先のリージョンへ文字列を描画
        if region is not None:
            blf.shadow(0, 3, 0.0, 1.0, 0.0, 0.5)
            blf.shadow_offset(0, 2, -2)
            blf.enable(0, blf.SHADOW)
            ShowObjectName.render_message(20, 20, region.height - 60, "Intersect")
            blf.disable(0, blf.SHADOW)
            #ShowObjectName.render_message(15, 20, region.height - 90,  sc.cwh_prop_object)


    def modal(self, context, event):
        props = context.scene.cwh_props

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if props.is_calc_mode is False:
            self.__handle_remove(context)
            return {'FINISHED'}

        return {'PASS_THROUGH'}


    def invoke(self, context, event):
        props = context.scene.cwh_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.is_calc_mode is False:
                props.is_calc_mode = True
                self.__handle_add(context)
                print("サンプル3-8: オブジェクト名の表示を開始しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.is_calc_mode = False
                print("サンプル3-8: オブジェクト名の表示を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_CWH(bpy.types.Panel):
    bl_label = "オブジェクト名の表示補助"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = sc.cwh_props
        # 開始/停止ボタンを追加
        if props.is_calc_mode is False:
            layout.operator(ShowObjectName.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(ShowObjectName.bl_idname, text="終了", icon="PAUSE")


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル3-8: アドオン「サンプル3-8」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-8: アドオン「サンプル3-8」が無効化されました。")


if __name__ == "__main__":
    register()
