import bpy
from bpy.props import IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, StringProperty


bl_info = {
    "name": "サンプル2-9: BlenderのUIを制御するアドオン2",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > ツールシェルフ",
    "description": "BlenderのUIを制御するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Interface"
}


class NullOperation(bpy.types.Operator):

    bl_idname = "object.null_operation"
    bl_label = "NOP"
    bl_description = "何もしない"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


class NullOperationMenu(bpy.types.Menu):

    bl_idname = "object.null_operation_menu"
    bl_label = "NOP メニュー"
    bl_description = "何もしない処理を複数持つメニュー"

    def draw(self, context):
        layout = self.layout
        # メニュー項目の追加
        for i in range(3):
            layout.operator(NullOperation.bl_idname, text=("項目 %d" % (i)))


class ShowAllIcons(bpy.types.Operator):

    bl_idname = "object.show_all_icons"
    bl_label = "利用可能なアイコンをすべて表示"
    bl_description = "利用可能なアイコンをすべて表示"
    bl_options = {'REGISTER', 'UNDO'}

    num_column = IntProperty(
        name="一行に表示するアイコン数",
        description="一行に表示するアイコン数",
        default=2,
        min=1,
        max=5
    )

    # オプションのUI
    def draw(self, context):
        layout = self.layout

        layout.prop(self, "num_column")

        layout.separator()

        # 利用可能なアイコンをすべて表示
        layout.label(text="利用可能なアイコン一覧:")
        for i, key in enumerate(bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items.keys()):
            if i % self.num_column == 0:
                row = layout.row()
            row.label(text=key, icon=key)

    def execute(self, context):
        return {'FINISHED'}


# ツールシェルフに「カスタムメニュー」タブを追加
class VIEW3D_PT_CustomMenu(bpy.types.Panel):

    bl_label = "カスタムメニュー"          # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "カスタムメニュー"       # タブを開いたメニューのヘッダーに表示される文字列
    bl_context = "objectmode"           # パネルを表示するコンテキスト

    # 本クラスの処理が実行可能かを判定する
    @classmethod
    def poll(cls, context):
        # オブジェクトが選択されている時のみメニューを表示させる
        for o in bpy.data.objects:
            if o.select:
                return True
        return False

    # ヘッダーのカスタマイズ
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='PLUGIN')

    # メニューの描画処理
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # ボタンを追加
        layout.label(text="ボタンを追加する:")
        layout.operator(NullOperation.bl_idname, text="ボタン1")
        layout.operator(NullOperation.bl_idname, text="ボタン2", emboss=False)

        # 上下の間隔を空ける
        layout.separator()

        # メニューを追加
        layout.label(text="メニューを追加する:")
        layout.menu(NullOperationMenu.bl_idname, text="メニュー")

        layout.separator()

        # プロパティを追加
        layout.label(text="プロパティを追加する:")
        layout.prop(scene, "cm_prop_int", text="プロパティ 1")
        layout.prop(scene, "cm_prop_float", text="プロパティ 2")
        layout.prop(scene, "cm_prop_enum", text="プロパティ 3")
        layout.prop(scene, "cm_prop_floatv", text="プロパティ 4")

        layout.separator()

        # 一行に並べる（アライメント無）
        layout.label(text="一行に並べる（アライメント無）:")
        row = layout.row(align=False)
        for i in range(3):
            row.operator(NullOperation.bl_idname, text=("列 %d" % (i)))

        layout.separator()

        # 一行に並べる（アライメント有）
        layout.label(text="一行に並べる（アライメント有）:")
        row = layout.row(align=True)
        for i in range(3):
            row.operator(NullOperation.bl_idname, text=("列 %d" % (i)))

        layout.separator()

        # 一列に並べる（アライメント無）
        layout.label(text="一列に並べる（アライメント無）:")
        column = layout.column(align=False)
        for i in range(3):
            column.operator(NullOperation.bl_idname, text=("行 %d" % (i)))

        layout.separator()

        # 一列に並べる（アライメント有）
        layout.label(text="一列に並べる（アライメント有）:")
        column = layout.column(align=True)
        for i in range(3):
            column.operator(NullOperation.bl_idname, text=("行 %d" % (i)))

        layout.separator()

        # 複数列に配置する
        layout.label(text="複数列に配置する:")
        column = layout.column(align=True)
        row = column.row(align=True)
        row.operator(NullOperation.bl_idname, text="列 1, 行 1")
        row.operator(NullOperation.bl_idname, text="列 2, 行 1")
        row = column.row(align=True)
        row.operator(NullOperation.bl_idname, text="列 1, 行 2")
        row.operator(NullOperation.bl_idname, text="列 2, 行 2")

        layout.separator()

        # 領域を分割する
        layout.label(text="領域を分割する:")
        split = layout.split(percentage=0.3)
        column = split.column(align=True)
        column.label(text="領域1:")
        column.operator(NullOperation.bl_idname, text="行 1")
        column.operator(NullOperation.bl_idname, text="行 2")
        split = split.split(percentage=0.7)
        column = split.column()
        column.label(text="領域2:")
        column.operator(NullOperation.bl_idname, text="行 1")
        column.operator(NullOperation.bl_idname, text="行 2")
        split = split.split(percentage=1.0)
        column = split.column(align=False)
        column.label(text="領域3:")
        column.operator(NullOperation.bl_idname, text="行 1")
        column.operator(NullOperation.bl_idname, text="行 2")

        layout.separator()

        # 横幅を自動的に拡大する
        layout.label(text="横幅を自動的に拡大する:")
        row = layout.row()
        row.alignment = 'EXPAND'
        row.operator(NullOperation.bl_idname, text="列 1")
        row.operator(NullOperation.bl_idname, text="列 2")

        layout.separator()

        # 左寄せする
        layout.label(text="左寄せする:")
        row = layout.row()
        row.alignment = 'LEFT'
        row.operator(NullOperation.bl_idname, text="列 1")
        row.operator(NullOperation.bl_idname, text="列 2")

        layout.separator()

        # 右寄せする
        layout.label(text="右寄せする:")
        row = layout.row()
        row.alignment = 'RIGHT'
        row.operator(NullOperation.bl_idname, text="列 1")
        row.operator(NullOperation.bl_idname, text="列 2")

        layout.separator()

        # グループ化する
        layout.label(text="グループ化する:")
        row = layout.row()
        box = row.box()
        box_row = box.row()
        box_column = box_row.column()
        box_column.operator(NullOperation.bl_idname, text="行 1, 列 1")
        box_column.separator()
        box_column.operator(NullOperation.bl_idname, text="行 2, 列 1")
        box_row.separator()
        box_column = box_row.column()
        box_column.operator(NullOperation.bl_idname, text="行 1, 列 2")
        box_column.separator()
        box_column.operator(NullOperation.bl_idname, text="行 2, 列 2")

        layout.separator()

        # プロパティのUIをカスタマイズする＋アイコン一覧を表示する
        layout.label(text="プロパティのUIをカスタマイズする")
        layout.operator(ShowAllIcons.bl_idname)


# プロパティの初期化
def init_props():
    scene = bpy.types.Scene
    scene.cm_prop_int = IntProperty(
        name="Prop 1",
        description="Integer Property",
        default=100,
        min=0,
        max=255
    )
    scene.cm_prop_float = FloatProperty(
        name="Prop 2",
        description="Float Property",
        default=0.75,
        min=0.0,
        max=1.0
    )
    scene.cm_prop_enum = EnumProperty(
        name="Prop 3",
        description="Enum Property",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")
        ],
        default='ITEM_1'
    )
    scene.cm_prop_floatv = FloatVectorProperty(
        name="Prop 4",
        description="Float Vector Property",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0
    )


# プロパティを削除
def clear_props():
    scene = bpy.types.Scene
    del scene.cm_prop_int
    del scene.cm_prop_float
    del scene.cm_prop_enum
    del scene.cm_prop_floatv


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル2-9: アドオン「サンプル2-9」が有効化されました。")


def unregister():
    bpy.utils.unregister_module(__name__)
    clear_props()
    print("サンプル2-9: アドオン「サンプル2-9」が無効化されました。")


if __name__ == "__main__":
    register()
