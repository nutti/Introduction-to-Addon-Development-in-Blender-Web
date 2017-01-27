import bpy
from bpy.props import BoolProperty, PointerProperty
from bpy_extras import view3d_utils
from mathutils import Vector


bl_info = {
    "name": "サンプル3-9: マウスカーソルが重なったオブジェクトを選択するアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > マウスオーバでオブジェクト選択",
    "description": "マウスカーソルが重なったオブジェクトを選択状態に、重なっていないオブジェクトを非選択状態にするアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


# プロパティ
class SOOM_Properties(bpy.types.PropertyGroup):
    running = BoolProperty(
        name="動作中",
        description="マウスオーバでオブジェクト選択機能が動作中か？",
        default=False)


# オブジェクト名を表示
class SelectObjectOnMouseover(bpy.types.Operator):
    bl_idname = "view3d.select_object_on_mouseover"
    bl_label = "マウスオーバでオブジェクト選択"
    bl_description = "マウスカーソルが重なったオブジェクトを選択状態に、重なっていないオブジェクトを非選択状態にします"

    def __init__(self):
        self.intersected_objs = []      # マウスカーソルの位置に向けて発したレイと交差するオブジェクト一覧

    @staticmethod
    def get_region_space(context, area_type, region_type, space_type):
        region = None
        # 指定されたエリアを取得する
        for area in context.screen.areas:
            if area.type == area_type:
                break
        # 指定されたリージョンを取得する
        for region in area.regions:
            if region.type == region_type:
                break
        # 指定されたスペースを取得する
        for space in area.spaces:
            if space.type == space_type:
                break

        return (region, space)


    def modal(self, context, event):
        props = context.scene.soom_props

        if context.mode == 'OBJECT':
            # マウスカーソルのリージョン座標を取得
            mv = Vector((event.mouse_region_x, event.mouse_region_y))
            # 3Dビューエリアのウィンドウリージョンと、スペースを取得する
            region, space = SelectObjectOnMouseover.get_region_space(context, 'VIEW_3D', 'WINDOW', 'VIEW_3D')
            # マウスカーソルの位置に向けて発したレイの方向を求める
            ray_dir = view3d_utils.region_2d_to_vector_3d(
                region,
                space.region_3d,
                mv)
            # マウスカーソルの位置に向けて発したレイの発生源を求める
            ray_orig = view3d_utils.region_2d_to_origin_3d(
                region,
                space.region_3d,
                mv)
            # レイの始点
            start = ray_orig
            # レイの終点（線分の長さは2000とした）
            end = ray_orig + ray_dir * 2000
            # カメラやライトなど、メッシュ型ではないオブジェクトは除く
            objs = [o for o in bpy.data.objects if o.type == 'MESH']
            self.intersected_objs = []
            for o in objs:
                try:
                    # レイとオブジェクトの交差判定
                    mwi = o.matrix_world.inverted()
                    result = o.ray_cast(mwi * start, mwi * end)
                    # オブジェクトとレイが交差した場合は交差した面のインデックス、交差しない場合は-1が返ってくる
                    if result[2] != -1:
                        self.intersected_objs.append(o)
                # メッシュタイプのオブジェクトが作られているが、ray_cast対象の面が存在しない場合
                except RuntimeError as e:
                    print("サンプル3-9: オブジェクト生成タイミングの問題により、例外エラー「レイキャスト可能なデータなし」が発生")

        # レイと交差したオブジェクトを選択
        for o in bpy.data.objects:
            o.select = True if o in self.intersected_objs else False

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 作業時間計測を停止
        if props.running is False:
            return {'FINISHED'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        props = context.scene.soom_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.running is False:
                props.running = True
                context.window_manager.modal_handler_add(self)
                print("サンプル3-9: オブジェクト名の表示を開始しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.running = False
                print("サンプル3-9: オブジェクト名の表示を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_SOOM(bpy.types.Panel):
    bl_label = "マウスオーバでオブジェクト選択"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = sc.soom_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(SelectObjectOnMouseover.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(SelectObjectOnMouseover.bl_idname, text="終了", icon="PAUSE")


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.soom_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=SOOM_Properties)


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.soom_props


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル3-9: アドオン「サンプル3-9」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-9: アドオン「サンプル3-9」が無効化されました。")


if __name__ == "__main__":
    register()
