import bpy
import bmesh
from mathutils import Vector


# 射影座標からリージョン座標へ変換する関数
def viewport_transform(region, v):
    wh = region.width / 2.0
    hh = region.height/ 2.0
    return Vector((wh + wh * v.x / v.w, hh + hh * v.y / v.w))


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
        vert_local = [Vector((v.co[0], v.co[1], v.co[2], 1.0)) for v in bm.verts if v.select]
        # ローカル座標からグローバル座標への変換
        vert_global = [obj.matrix_world * v for v in vert_local]
        # グローバル座標から射影座標への変換
        vert_perspective = [space.region_3d.perspective_matrix * v for v in vert_global]
        # 射影座標からリージョン座標への変換
        vert_region = [viewport_transform(region, v) for v in vert_perspective]
        # 座標を出力
        for l, g, p, r in zip(vert_local, vert_global, vert_perspective, vert_region):
            print("==========")
            print("local: " + repr(l))
            print("global: " + repr(g))
            print("perspective: " + repr(p))
            print("region: " + repr(r))
