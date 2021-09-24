import bpy
import blf
from bpy.props import IntProperty, IntVectorProperty
from bpy_extras import view3d_utils
from mathutils import Vector


bl_info = {
    "name": "サンプル 5-3: オブジェクト名の表示サポート",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > サンプル 5-3",
    "description": "オブジェクトの位置にオブジェクト名を表示し、マウスカーソルの位置に向けて発したレイと交差するオブジェクト名を表示するアドオン",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "3D View"
}


def get_region_space(context, area_type, region_type, space_type):
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


# オブジェクト名の表示サポートのオペレータ
class SAMPLE53_OT_ShowObjectName(bpy.types.Operator):

    bl_idname = "view3d.sample53_show_object_name"
    bl_label = "オブジェクト名の表示サポート"
    bl_description = "オブジェクトの位置にオブジェクト名を表示し、マウスカーソルの位置に向けて発したレイと交差するオブジェクト名を表示します"

    __handle = None           # 描画関数ハンドラ
    __running = False         # オブジェクト名表示中はTrue

    @classmethod
    def is_running(cls):
        return cls.__running

    def __init__(self):
        self.__intersected_objs = []      # マウスカーソルの位置に向けて発したレイと交差するオブジェクト一覧

    def __handle_add(self, context):
        op_cls = SAMPLE53_OT_ShowObjectName

        if op_cls.__handle is None:
            # 描画関数の登録
            op_cls.__handle = bpy.types.SpaceView3D.draw_handler_add(
                op_cls.__draw, (self, context),
                'WINDOW', 'POST_PIXEL'
            )
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)

    def __handle_remove(self, context):
        op_cls = SAMPLE53_OT_ShowObjectName

        if op_cls.__handle is not None:
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(op_cls.__handle, 'WINDOW')
            op_cls.__handle = None

    @staticmethod
    def __draw_text(size, x, y, msg):
        blf.color(0, 1.0, 1.0, 1.0, 1.0)
        blf.size(0, size, 72)
        blf.position(0, x, y, 0)
        blf.draw(0, msg)

    @staticmethod
    def __draw(self, context):
        op_cls = SAMPLE53_OT_ShowObjectName
        prefs = context.preferences.addons[__name__].preferences

        region, space = get_region_space(
            context, 'VIEW_3D', 'WINDOW', 'VIEW_3D')
        if (region is None) or (space is None):
            return

        # オブジェクトの位置にオブジェクト名を表示

        objs = [o for o in bpy.data.objects]
        # オブジェクトの位置座標（3D座標）をリージョン座標（2D座標）に変換
        locs_on_screen = [
            view3d_utils.location_3d_to_region_2d(
                region,
                space.region_3d,
                o.location
            ) for o in objs
        ]
        # 表示するテキストを装飾する
        blf.shadow(0, 3, 0.1, 0.1, 0.1, 1.0)
        blf.shadow_offset(0, 1, -1)
        blf.enable(0, blf.SHADOW)
        for obj, loc in zip(objs, locs_on_screen):
            # 表示範囲外なら表示しない
            if loc is not None:
                op_cls.__draw_text(prefs.font_size_2, loc.x, loc.y, obj.name)
        blf.disable(0, blf.SHADOW)

        # マウスカーソルの位置に向けて発したレイと交差するオブジェクト名を表示

        blf.shadow(0, 3, 0.0, 1.0, 0.0, 0.5)
        blf.shadow_offset(0, 2, -2)
        blf.enable(0, blf.SHADOW)
        op_cls.__draw_text(
            prefs.font_size_1,
            prefs.left_top[0],
            region.height - prefs.left_top[1],
            "Intersect"
        )
        blf.disable(0, blf.SHADOW)

        for i, o in enumerate(self.__intersected_objs):
            op_cls.__draw_text(
                int(prefs.font_size_1 * 0.8),
                prefs.left_top[0],
                (region.height - prefs.left_top[1]
                 - int(prefs.font_size_1 * 1.3)
                 - i * int(prefs.font_size_1 * 0.9)),
                o.name
            )

    def modal(self, context, event):
        op_cls = SAMPLE53_OT_ShowObjectName

        # エリアを再描画
        if context.area:
            context.area.tag_redraw()

        # オブジェクト名の表示サポートの停止
        if not op_cls.is_running():
            self.__handle_remove(context)
            return {'FINISHED'}

        if context.mode == 'OBJECT':
            # マウスカーソルのリージョン座標を取得
            mv = Vector((event.mouse_region_x, event.mouse_region_y))
            # [3Dビューポート] スペースを持つエリアの [ウィンドウ] リージョン
            # 情報と、[3Dビューポート] スペースのスペース情報を取得する
            region, space = get_region_space(context, 'VIEW_3D', 'WINDOW', 'VIEW_3D')
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
            # カメラやライトなど、メッシュ型ではないオブジェクトは除く
            objs = [o for o in bpy.data.objects if o.type == 'MESH']
            self.__intersected_objs = []
            for o in objs:
                try:
                    # レイとオブジェクトの交差判定
                    # 交差判定はオブジェクトのローカル座標で行われるため、
                    # レイの始点と終点をローカル座標に変換する
                    mwi = o.matrix_world.inverted()
                    # レイの始点
                    mwi_start = mwi @ start
                    # レイの終点
                    mwi_end = mwi @ end
                    # レイの向き
                    mwi_dir = mwi_end - mwi_start
                    # オブジェクトとレイの交差判定を行う
                    result = o.ray_cast(mwi_start, mwi_dir, distance=2000)
                    # オブジェクトとレイが交差した場合は交差した面のインデックス、
                    # 交差しない場合は-1が返ってくる
                    if result[0] == True:
                        self.__intersected_objs.append(o)
                # メッシュタイプのオブジェクトが作られているが、ray_cast対象の面が存在しない場合
                except RuntimeError:
                    print("サンプル 5-3: オブジェクト生成タイミングの問題により、例外エラー「レイキャスト可能なデータなし」が発生")

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        op_cls = SAMPLE53_OT_ShowObjectName

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not op_cls.is_running():
                op_cls.__running = True
                self.__handle_add(context)
                print("サンプル 5-3: オブジェクト名の表示を開始しました。")
                return {'RUNNING_MODAL'}
            # [終了] ボタンが押された時の処理
            else:
                op_cls.__running = False
                print("サンプル 5-3: オブジェクト名の表示を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE53_PT_ShowObjectName(bpy.types.Panel):

    bl_label = "オブジェクト名の表示サポート"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "サンプル 5-3"
    bl_context = "objectmode"

    def draw(self, context):
        op_cls = SAMPLE53_OT_ShowObjectName
        layout = self.layout

        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")


# プリファレンスのアドオン設定情報
class SAMPLE53_Preferences(bpy.types.AddonPreferences):

    bl_idname = __name__

    # 交差したオブジェクトの名前表示に使用する設定
    font_size_1: IntProperty(
        name="Font Size",
        description="フォントサイズ",
        default=20,
        max=50,
        min=10
    )
    left_top: IntVectorProperty(
        name="左上座標",
        description="情報を表示する左上の座標",
        size=2,
        subtype='XYZ',
        default=(20, 60),
        max=300,
        min=0
    )
    # オブジェクトの位置に表示する時に使用する設定
    font_size_2: IntProperty(
        name="Font Size",
        description="フォントサイズ",
        default=12,
        max=50,
        min=10
    )

    def draw(self, context):
        layout = self.layout

        layout.label(text="交差したオブジェクト名の表示:")
        sp = layout.split(factor=0.3)
        col = sp.column()
        col.prop(self, "left_top")
        sp = sp.split(factor=0.4)
        col = sp.column()
        col.label(text="フォントサイズ:")
        col.prop(self, "font_size_1")

        layout.label(text="オブジェクトの位置にオブジェクト名を表示:")
        sp = layout.split(factor=0.3)
        col = sp.column()
        col.prop(self, "font_size_2")


classes = [
    SAMPLE53_OT_ShowObjectName,
    SAMPLE53_PT_ShowObjectName,
    SAMPLE53_Preferences,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル 5-3: アドオン『サンプル 5-3』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 5-3: アドオン『サンプル 5-3』が無効化されました。")


if __name__ == "__main__":
    register()
