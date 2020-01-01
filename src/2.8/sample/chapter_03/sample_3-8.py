import bpy
import mathutils
import bmesh
from bpy_extras import view3d_utils


bl_info = {
    "name": "サンプル 3-8: メッシュの面を選択するアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > サンプル 3-8",
    "description": "マウスカーソルの位置にあるメッシュの面を選択するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"
}


def get_region_and_space(context, area_type, region_type, space_type):
    region = None
    area = None
    space = None

    # 指定されたエリアの情報を取得する
    for a in context.screen.areas:
        if a.type == area_type:
            area = a
            break
    else:
        return (None, None)
    # 指定されたリージョンの情報を取得する
    for r in area.regions:
        if r.type == region_type:
            region = r
            break
    # 指定されたスペースの情報を取得する
    for s in area.spaces:
        if s.type == space_type:
            space = s
            break

    return (region, space)


# マウスカーソルの位置にあるメッシュの面を選択するオペレータ
class SAMPLE38_OT_SelectMouseOveredMesh(bpy.types.Operator):

    bl_idname = "object.sample38_selelct_mouseovered_face"
    bl_label = "メッシュの面選択"
    bl_description = "マウスカーソルの位置にあるメッシュの面を選択します"

    # Trueの場合は、マウスカーソルの位置にあるメッシュの面を選択する
    # （Trueの場合は、モーダルモード中である）
    __running = False

    # モーダルモード中はTrueを返す
    @classmethod
    def is_running(cls):
        return cls.__running

    def modal(self, context, event):
        op_cls = SAMPLE38_OT_SelectMouseOveredMesh
        active_obj = context.active_object

        # エリアを再描画
        if context.area:
            context.area.tag_redraw()

        # パネル [マウスドラッグでオブジェクトを回転] のボタン [終了] を
        # 押したときに、モーダルモードを終了
        if not self.is_running():
            return {'FINISHED'}

        # マウスドラッグ中は、マウスカーソルの位置にあるメッシュの面を選択
        if event.type == 'MOUSEMOVE':
            # マウスカーソルのリージョン座標を取得
            mv = mathutils.Vector((event.mouse_region_x, event.mouse_region_y))
            # [3Dビューポート] スペースを表示するエリアの [Window] リージョンの
            # 情報と、[3Dビューポート] スペースのスペース情報を取得する
            region, space = get_region_and_space(
                context, 'VIEW_3D', 'WINDOW', 'VIEW_3D'
            )
            # マウスカーソルの位置に向けて発したレイの方向を求める
            ray_dir = view3d_utils.region_2d_to_vector_3d(
                region,
                space.region_3d,
                mv
            )
            # マウスカーソルの位置に向けて発したレイの発生源を求める
            ray_orig = view3d_utils.region_2d_to_origin_3d(
                region,
                space.region_3d,
                mv
            )
            # レイの始点
            start = ray_orig
            # レイの終点
            end = ray_orig + ray_dir

            # レイとオブジェクトの交差判定
            # 交差判定はオブジェクトのローカル座標で行われるため、
            # レイの始点と終点をローカル座標に変換する
            mwi = active_obj.matrix_world.inverted()
            # レイの始点
            mwi_start = mwi @ start
            # レイの終点
            mwi_end = mwi @ end
            # レイの向き
            mwi_dir = mwi_end - mwi_start

            # オブジェクトの面選択解除
            bpy.ops.mesh.select_all(action='DESELECT')

            # bmeshオブジェクトの構築
            bm = bmesh.from_edit_mesh(active_obj.data)
            # BVHツリーの構築
            tree = mathutils.bvhtree.BVHTree.FromBMesh(bm)
            # オブジェクトとレイの交差判定を行う
            _, _, fidx, _ = tree.ray_cast(mwi_start, mwi_dir, 2000.0)
            
            # メッシュとレイが衝突した場合
            if fidx is not None:
                bm.faces[fidx].select = True

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        op_cls = SAMPLE38_OT_SelectMouseOveredMesh

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not self.is_running():
                # モーダルモードを開始
                context.window_manager.modal_handler_add(self)
                op_cls.__running = True
                print("サンプル 3-8: メッシュの面選択処理を開始しました。")
                return {'RUNNING_MODAL'}
            # [終了] ボタンが押された時の処理
            else:
                op_cls.__running = False
                print("サンプル 3-8: メッシュの面選択処理を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE38_PT_SelectMouseOveredMesh(bpy.types.Panel):

    bl_label = "メッシュの面選択"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "サンプル 3-8"
    bl_context = "mesh_edit"

    def draw(self, context):
        op_cls = SAMPLE38_OT_SelectMouseOveredMesh

        layout = self.layout
        # [開始] / [終了] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname,text="開始", icon='PLAY')
        else:
            layout.operator(op_cls.bl_idname,text="終了", icon='PAUSE')


classes = [
    SAMPLE38_OT_SelectMouseOveredMesh,
    SAMPLE38_PT_SelectMouseOveredMesh,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル 3-8: アドオン『サンプル 3-8』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 3-8: アドオン『サンプル 3-8』が無効化されました。")


if __name__ == "__main__":
    register()
