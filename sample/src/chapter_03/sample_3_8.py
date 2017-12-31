import bpy
from bpy.props import BoolProperty
from bpy_extras import view3d_utils
import bgl


bl_info = {
    "name": "サンプル3-8: オブジェクト移動の軌跡を描くアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > オブジェクトの軌跡表示",
    "description": "選択中のオブジェクトが移動した時の軌跡を描くアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


# オブジェクト名を表示
class DrawObjectTrajectory(bpy.types.Operator):

    bl_idname = "view3d.draw_object_trajectory"
    bl_label = "オブジェクトの軌跡表示"
    bl_description = "選択中のオブジェクトが移動した時に軌跡を表示します"

    __handle = None           # 描画関数ハンドラ
    __loc_history = []

    def __handle_add(self, context):
        if DrawObjectTrajectory.__handle is None:
            # 描画関数の登録
            space = bpy.types.SpaceView3D
            DrawObjectTrajectory.__handle = space.draw_handler_add(
                DrawObjectTrajectory.__render, (context, ),
                'WINDOW', 'POST_PIXEL'
            )

    def __handle_remove(self, context):
        if DrawObjectTrajectory.__handle is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(
                DrawObjectTrajectory.__handle, 'WINDOW'
            )
            DrawObjectTrajectory.__handle = None

    @staticmethod
    def __get_region_space(context, area_type, region_type, space_type):
        region = None
        area = None
        space = None

        # 指定されたエリアを取得する
        for a in context.screen.areas:
            if a.type == area_type:
                area = a
                break
        else:
            return (None, None)
        # 指定されたリージョンを取得する
        for r in area.regions:
            if r.type == region_type:
                region = r
                break
        # 指定されたスペースを取得する
        for s in area.spaces:
            if s.type == space_type:
                space = s
                break

        return (region, space)

    @staticmethod
    def __render(context):
        # 指定したリージョンとスペースを取得する
        region, space = DrawObjectTrajectory.__get_region_space(
            context, 'VIEW_3D', 'WINDOW', 'VIEW_3D'
        )
        if (region is None) or (space is None):
            return

        # 選択されたオブジェクトを取得
        objs = [o for o in bpy.data.objects if o.select]
        # オブジェクトの位置座標（3D座標）をリージョン座標（2D座標）に変換
        DrawObjectTrajectory.__loc_history.append([
            view3d_utils.location_3d_to_region_2d(
                region,
                space.region_3d,
                o.location
            ) for o in objs
        ])

        # 一定期間後、最も古い位置情報を削除する
        if len(DrawObjectTrajectory.__loc_history) >= 100:
            DrawObjectTrajectory.__loc_history.pop(0)

        # 軌跡を描画
        size = 6.0
        bgl.glEnable(bgl.GL_BLEND)
        # 保存されている過去の位置情報をすべて表示
        for hist in DrawObjectTrajectory.__loc_history:
            # 選択されたすべてのオブジェクトについて表示
            for loc in hist:
                bgl.glBegin(bgl.GL_QUADS)
                bgl.glColor4f(0.2, 0.6, 1.0, 0.7)
                bgl.glVertex2f(loc.x - size / 2.0, loc.y - size / 2.0)
                bgl.glVertex2f(loc.x - size / 2.0, loc.y + size / 2.0)
                bgl.glVertex2f(loc.x + size / 2.0, loc.y + size / 2.0)
                bgl.glVertex2f(loc.x + size / 2.0, loc.y - size / 2.0)
                bgl.glEnd()

    def invoke(self, context, event):
        sc = context.scene
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if sc.dot_running is False:
                sc.dot_running = True
                DrawObjectTrajectory.__loc_history = []
                self.__handle_add(context)
                print("サンプル3-8: オブジェクトの軌跡表示を開始しました。")
            # 終了ボタンが押された時の処理
            else:
                sc.dot_running = False
                self.__handle_remove(context)
                print("サンプル3-8: オブジェクトの軌跡表示を終了しました。")
            # 3Dビューの画面を更新
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_DOT(bpy.types.Panel):

    bl_label = "オブジェクトの軌跡表示"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        # 開始/停止ボタンを追加
        if sc.dot_running is False:
            layout.operator(
                DrawObjectTrajectory.bl_idname, text="開始", icon="PLAY"
            )
        else:
            layout.operator(
                DrawObjectTrajectory.bl_idname, text="終了", icon="PAUSE"
            )


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.dot_running = BoolProperty(
        name="動作中",
        description="オブジェクトの移動軌跡表示機能が動作中か？",
        default=False
    )


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.dot_running


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
