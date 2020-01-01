import bpy
from bpy.props import (
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    EnumProperty,
    BoolProperty,
)


bl_info = {
    "name": "サンプル 2-7: BlenderのUIを制御するアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar",
    "description": "BlenderのUIを制御するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "User Interface"
}


class SAMPLE27_OT_Nop(bpy.types.Operator):

    bl_idname = "object.sample27_nop"
    bl_label = "NOP"
    bl_description = "何もしない"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


class SAMPLE27_MT_NopMenu(bpy.types.Menu):

    bl_idname = "SAMPLE27_MT_NopMenu"
    bl_label = "NOP メニュー"
    bl_description = "何もしないオペレータを複数持つメニュー"

    def draw(self, context):
        layout = self.layout
        # メニュー項目の追加
        for i in range(3):
            layout.operator(SAMPLE27_OT_Nop.bl_idname, text=("項目 %d" % (i)))


# @include-source start [panel_cls]
# Sidebarのタブ [カスタムタブ] に、パネル [カスタムパネル] を追加
class SAMPLE27_PT_CustomPanel(bpy.types.Panel):

    bl_label = "カスタムパネル"         # パネルのヘッダに表示される文字列
    bl_space_type = 'VIEW_3D'           # パネルを登録するスペース
    bl_region_type = 'UI'               # パネルを登録するリージョン
    bl_category = "カスタムタブ"        # パネルを登録するタブ名
    bl_context = "objectmode"           # パネルを表示するコンテキスト
# @include-source end [panel_cls]

# @include-source start [poll]
    # 本クラスの処理が実行可能かを判定する
    @classmethod
    def poll(cls, context):
        # オブジェクトが選択されているときのみメニューを表示させる
        for o in bpy.data.objects:
            if o.select_get():
                return True
        return False
# @include-source end [poll]

# @include-source start [draw_header]
    # ヘッダーのカスタマイズ
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='PLUGIN')
# @include-source end [draw_header]

    # メニューの描画処理
    def draw(self, context):
        layout = self.layout
        scene = context.scene

# @include-source start [add_button]
        # ボタンを追加
        layout.label(text="ボタン:")
        layout.operator(SAMPLE27_OT_Nop.bl_idname, text="ボタン1")
        layout.operator(SAMPLE27_OT_Nop.bl_idname, text="ボタン2", emboss=False)
# @include-source end [add_button]

# @include-source start [add_separator]
        # セパレータを追加
        layout.separator()
# @include-source end [add_separator]

# @include-source start [add_dropdown_menu]
        # ドロップダウンメニューを追加
        layout.label(text="ドロップダウンメニュー:")
        layout.menu(SAMPLE27_MT_NopMenu.bl_idname,
                    text="ドロップダウンメニュー")
# @include-source end [add_dropdown_menu]

        layout.separator()

# @include-source start [add_textbox]
        # テキストボックスを追加
        layout.label(text="テキストボックス:")
        layout.prop(scene, "sample27_prop_int", text="プロパティ 1")
        layout.prop(scene, "sample27_prop_float", text="プロパティ 2")
        layout.prop(scene, "sample27_prop_floatv", text="プロパティ 3")
# @include-source end [add_textbox]

# @include-source start [add_dropdown_property]
        # ドロップダウンプロパティを追加
        layout.label(text="ドロップダウンプロパティ:")
        layout.prop(scene, "sample27_prop_enum", text="プロパティ 4")
# @include-source end [add_dropdown_property]

# @include-source start [add_checkbox]
        # チェックボックスを追加
        layout.label(text="チェックボックス:")
        layout.prop(scene, "sample27_prop_bool", text="プロパティ 5")
# @include-source end [add_checkbox]

        layout.separator()

# @include-source start [arrange_column]
        # 一行配置（アライメントなし）
        layout.label(text="一行配置（アライメントなし）:")
        row = layout.row(align=False)
        for i in range(3):
            row.operator(SAMPLE27_OT_Nop.bl_idname, text=("列 %d" % (i)))
# @include-source end [arrange_column]

        layout.separator()

# @include-source start [arrange_column_align]
        # 一行配置（アライメントあり）
        layout.label(text="一行配置（アライメントあり）:")
        row = layout.row(align=True)
        for i in range(3):
            row.operator(SAMPLE27_OT_Nop.bl_idname, text=("列 %d" % (i)))
# @include-source end [arrange_column_align]

        layout.separator()

# @include-source start [arrange_row]
        # 一列配置（アライメントなし）
        layout.label(text="一列配置（アライメントなし）:")
        column = layout.column(align=False)
        for i in range(3):
            column.operator(SAMPLE27_OT_Nop.bl_idname, text=("行 %d" % (i)))
# @include-source end [arrange_row]

        layout.separator()

# @include-source start [arrange_row_align]
        # 一列配置（アライメントあり）
        layout.label(text="一列配置（アライメントあり）:")
        column = layout.column(align=True)
        for i in range(3):
            column.operator(SAMPLE27_OT_Nop.bl_idname, text=("行 %d" % (i)))
# @include-source end [arrange_row_align]

        layout.separator()

# @include-source start [arrange_row_multi]
        # 複数列配置
        layout.label(text="複数列配置:")
        column = layout.column(align=True)
        row = column.row(align=True)
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 1, 行 1")
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 2, 行 1")
        row = column.row(align=True)
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 1, 行 2")
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 2, 行 2")
# @include-source end [arrange_row_multi]

        layout.separator()

# @include-source start [divide_region]
        # 領域分割
        layout.label(text="領域分割:")
        split = layout.split(factor=0.3)
        column = split.column(align=True)
        column.label(text="領域1:")
        column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 1")
        column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 2")
        split = split.split(factor=0.7)
        column = split.column()
        column.label(text="領域2:")
        column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 1")
        column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 2")
        split = split.split(factor=1.0)
        column = split.column(align=False)
        column.label(text="領域3:")
        column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 1")
        column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 2")
# @include-source end [divide_region]

        layout.separator()

# @include-source start [align_expand]
        # 横幅の自動拡大
        layout.label(text="横幅の自動拡大:")
        row = layout.row()
        row.alignment = 'EXPAND'
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 1")
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 2")
# @include-source end [align_expand]

        layout.separator()

# @include-source start [align_left]
        # 左寄せ
        layout.label(text="左寄せ:")
        row = layout.row()
        row.alignment = 'LEFT'
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 1")
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 2")
# @include-source end [align_left]

        layout.separator()

# @include-source start [align_right]
        # 右寄せ
        layout.label(text="右寄せ:")
        row = layout.row()
        row.alignment = 'RIGHT'
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 1")
        row.operator(SAMPLE27_OT_Nop.bl_idname, text="列 2")
# @include-source end [align_right]

        layout.separator()

# @include-source start [grouping]
        # グループ化
        layout.label(text="グループ化:")
        row = layout.row()
        box = row.box()
        box_row = box.row()
        box_column = box_row.column()
        box_column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 1, 列 1")
        box_column.separator()
        box_column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 2, 列 1")
        box_row.separator()
        box_column = box_row.column()
        box_column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 1, 列 2")
        box_column.separator()
        box_column.operator(SAMPLE27_OT_Nop.bl_idname, text="行 2, 列 2")
# @include-source end [grouping]


# @include-source start [init_props]
# プロパティの初期化
def init_props():
    scene = bpy.types.Scene
    scene.sample27_prop_int = IntProperty(
        name="プロパティ 1",
        description="プロパティ（int）",
        default=100,
        min=0,
        max=255
    )
    scene.sample27_prop_float = FloatProperty(
        name="プロパティ 2",
        description="プロパティ（float）",
        default=0.75,
        min=0.0,
        max=1.0
    )
    scene.sample27_prop_floatv = FloatVectorProperty(
        name="プロパティ 3",
        description="プロパティ（float vector）",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0
    )
    scene.sample27_prop_enum = EnumProperty(
        name="プロパティ 4",
        description="プロパティ（enum）",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")
        ],
        default='ITEM_1'
    )
    scene.sample27_prop_bool = BoolProperty(
        name="プロパティ 5",
        description="プロパティ（bool）",
        default=False
    )
# @include-source end [init_props]


# @include-source start [clear_props]
# プロパティを削除
def clear_props():
    scene = bpy.types.Scene
    del scene.sample27_prop_int
    del scene.sample27_prop_float
    del scene.sample27_prop_floatv
    del scene.sample27_prop_enum
    del scene.sample27_prop_bool
# @include-source end [clear_props]


classes = [
    SAMPLE27_OT_Nop,
    SAMPLE27_MT_NopMenu,
    SAMPLE27_PT_CustomPanel,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    init_props()
    print("サンプル 2-7: アドオン『サンプル 2-7』が有効化されました。")


def unregister():
    clear_props()
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 2-7: アドオン『サンプル 2-7』が無効化されました。")


if __name__ == "__main__":
    register()
