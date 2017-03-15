import bpy
import bmesh
from bpy_extras import view3d_utils
from mathutils import Vector


# 指定したエリア、リージョン、スペースを取得する関数
def get_region_and_space(area_type, region_type, space_type):
    region = None
    area = None
    space = None

    # 指定されたエリアを取得する
    for a in bpy.context.screen.areas:
        if a.type == area_type:
            area = a
            break
    else:
        return (None, None, None)
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

    return (area, region, space)


def main():
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
                obj.matrix_world * v
            ) for v in vert_local
        ]
        # 座標を出力
        for l, r in zip(vert_local, vert_region):
            print("==========")
            print("local: " + repr(l))
            print("region: " + repr(r))


if __name__ == "__main__":
    main()
