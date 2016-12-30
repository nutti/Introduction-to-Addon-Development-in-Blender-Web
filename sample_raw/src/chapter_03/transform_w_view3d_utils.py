import bpy
import bmesh
from bpy_extras import view3d_utils
from mathutils import Vector


# 指定したエリア、リージョン、スペースを取得する関数
def get_region_and_space(area_type, region_type, space_type):
    for area in bpy.context.screen.areas:
        if area.type == area_type:
            break
    else:
        return (None, None, None)

    for region in area.regions:
        if region.type == region_type:
            break
    else:
        return (area, None, None)

    for space in area.spaces:
        if space.type == space_type:
            break
    else:
        return (area, region, None)

    return (area, region, space)


if __name__ == "__main__":
    # 3Dビューエリアのウィンドウリージョンのリージョンとスペースを取得
    (area, region, space) = get_region_and_space('VIEW_3D', 'WINDOW', 'VIEW_3D')
    if space is not None:
        # 選択中の頂点のローカル座標を取得する
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)
        vert_local = [v.co for v in bm.verts if v.select]
        # ローカル座標からリージョン座標への変換
        vert_region = [view3d_utils.location_3d_to_region_2d(
                region,
                space.region_3d,
                obj.matrix_world * v) for v in vert_local]
        # 座標を出力
        for l, r in zip(vert_local, vert_region):
            print("==========")
            print("local: " + repr(l))
            print("region: " + repr(r))
