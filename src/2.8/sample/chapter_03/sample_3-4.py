import math

import bpy
import gpu
from bpy.props import FloatProperty, FloatVectorProperty
from gpu_extras.batch import batch_for_shader


bl_info = {
    "name": "サンプル3-4: 星型の図形を描画するアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > Sample 3-4",
    "description": "星型の図形を描画するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


# 星型の図形を描画するオペレータ
class SAMPLE34_OT_DrawStar(bpy.types.Operator):

    bl_idname = "object.sample34_draw_star"
    bl_label = "星型の図形を描画"
    bl_description = "星型の図形を描画します"

    # 描画ハンドラ
    __handle = None

    @classmethod
    def is_running(cls):
        # 描画中はTrue
        return True if cls.__handle else False

    @classmethod
    def __handle_add(cls, context):
        if not cls.is_running():
            # 描画関数の登録
            cls.__handle = bpy.types.SpaceView3D.draw_handler_add(
                cls.__draw, (context, ), 'WINDOW', 'POST_PIXEL'
            )

    @classmethod
    def __handle_remove(cls, context):
        if cls.is_running():
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(
                cls.__handle, 'WINDOW'
            )
            cls.__handle = None

    @classmethod
    def __draw(cls, context):
        sc = context.scene

        # ビルトインのシェーダを取得
        shader = gpu.shader.from_builtin('2D_UNIFORM_COLOR')

        # 頂点データを作成
        center = sc.sample34_center
        radius = sc.sample34_size / 2.0
        angle = 72 * math.pi / 180
        data = {"pos": [
            [center[0], center[1] + radius],
            [center[0] + radius * math.sin(angle), center[1] + radius * math.cos(angle)],
            [center[0] + radius * math.sin(2 * angle), center[1] + radius * math.cos(2 * angle)],
            [center[0] - radius * math.sin(2 * angle), center[1] + radius * math.cos(2 * angle)],
            [center[0] - radius * math.sin(angle), center[1] + radius * math.cos(angle)]
        ]}
        
        # インデックスデータを作成
        indices = [
            [0, 2], [2, 4], [4, 1], [1, 3], [3, 0]
        ]      

        # バッチを作成
        batch = batch_for_shader(shader, 'LINES', data, indices=indices)

        # シェーダのパラメータ設定
        color = [0.5, 1.0, 1.0, 1.0]
        shader.bind()
        shader.uniform_float("color", color)

        # 描画
        batch.draw(shader)

    def invoke(self, context, event):
        op_cls = SAMPLE34_OT_DrawStar

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not op_cls.is_running():
                self.__handle_add(context)
                print("サンプル3-4: 星型の図形の描画処理を開始しました。")
            # [終了] ボタンが押された時の処理
            else:
                self.__handle_remove(context)
                print("サンプル3-4: 星型の図形の描画処理を終了しました。")
            # エリアを再描画
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE34_PT_DrawStar(bpy.types.Panel):

    bl_label = "星型の図形を表示"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sample 3-4"
    bl_context = "objectmode"

    def draw(self, context):
        sc = context.scene
        op_cls = SAMPLE34_OT_DrawStar

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")

            layout.separator()

            layout.prop(sc, "sample34_center")
            layout.prop(sc, "sample34_size")


def init_props():
    sc = bpy.types.Scene
    sc.sample34_center = FloatVectorProperty(
        name="中心",
        description="星の中心座標",
        size=2,
        min=0.0,
        default=(200.0, 200.0)
    )
    sc.sample34_size = FloatProperty(
        name="サイズ",
        description="星の大きさ",
        min=10.0,
        default=200.0
    )


def clear_props():
    sc = bpy.types.Scene
    del sc.ngons
    for i in range(10):
        del sc["vert_{}".format(i + 1)]

classes = [
    SAMPLE34_OT_DrawStar,
    SAMPLE34_PT_DrawStar,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    init_props()
    print("サンプル3-4: アドオン『サンプル3-4』が有効化されました。")


def unregister():
    clear_props()
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル3-4: アドオン『サンプル3-4』が無効化されました。")


if __name__ == "__main__":
    register()
