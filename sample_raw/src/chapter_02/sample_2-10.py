import bpy
from bpy.props import IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, StringProperty

bl_info = {
    "name": "サンプル2-10: BlenderのUIを制御するアドオン3",
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


//! [ops_show_popup_message]
class ShowPopupMessage(bpy.types.Operator):
    bl_idname = "object.show_popup_message"
    bl_label = "ポップアップメッセージ"
    bl_description = "ポップアップメッセージ"
    bl_options = {'REGISTER', 'UNDO'}

    # execute() メソッドがないと、やり直し未対応の文字が出力される
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # ポップアップメッセージ表示
        return wm.invoke_popup(self, width=200, height=100)

    # ポップアップメッセージに表示する内容
    def draw(self, context):
        layout = self.layout
        layout.label("メッセージ")
//! [ops_show_popup_message]


//! [ops_show_dialog_menu]
class ShowDialogMenu(bpy.types.Operator):
    bl_idname = "object.show_dialog_menu"
    bl_label = "ダイアログメニュー"
    bl_description = "ダイアログメニュー"
    bl_options = {'REGISTER', 'UNDO'}

    prop_int = IntProperty(
        name="ダイアログプロパティ 1",
        description="ダイアログプロパティ 1",
        default=100,
        min=0,
        max=255)
    prop_float = FloatProperty(
        name="ダイアログプロパティ 2",
        description="ダイアログプロパティ 2",
        default=0.75,
        min=0.0,
        max=1.0)
    prop_enum = EnumProperty(
        name="ダイアログプロパティ 3",
        description="ダイアログプロパティ 3",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")],
        default='ITEM_1')
    prop_floatv = FloatVectorProperty(
        name="ダイアログプロパティ 4",
        description="ダイアログプロパティ 4",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0)

    def execute(self, context):
        self.report({'INFO'}, "サンプル2-10: [1] %d, [2] %f, [3] %s, [4] (%f, %f, %f)"
            % (self.prop_int, self.prop_float, self.prop_enum, self.prop_floatv[0], self.prop_floatv[1], self.prop_floatv[2]))

        return {'FINISHED'}

    def invoke(self, context, event):
        scene = context.scene

        self.prop_int = scene.cm_prop_int
        self.prop_float = scene.cm_prop_float
        self.prop_enum = scene.cm_prop_enum
        self.prop_floatv = scene.cm_prop_floatv

        # ダイアログメニュー呼び出し
        return context.window_manager.invoke_props_dialog(self)
//! [ops_show_dialog_menu]


//! [ops_show_file_browser]
class ShowFileBrowser(bpy.types.Operator):
    bl_idname = "object.show_file_browser"
    bl_label = "ファイルブラウザ"
    bl_description = "ファイルブラウザ"
    bl_options = {'REGISTER', 'UNDO'}

    filepath = StringProperty(subtype="FILE_PATH")
    filename = StringProperty()
    directory = StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        self.report({'INFO'}, "サンプル2-10: [FilePath] %s, [FileName] %s, [Directory] %s" % (self.filepath, self.filename, self.directory))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # ファイルブラウザ表示
        wm.fileselect_add(self)

        return {'RUNNING_MODAL'}
//! [ops_show_file_browser]


//! [ops_show_confirm_popup]
class ShowConfirmPopup(bpy.types.Operator):
    bl_idname = "object.show_confirm_popup"
    bl_label = "確認ポップアップ"
    bl_description = "確認ポップアップ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "サンプル2-10: 確認ポップアップボタンをクリックしました")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # 確認メッセージ表示
        return wm.invoke_confirm(self, event)
//! [ops_show_confirm_popup]


//! [ops_show_property_popup]
class ShowPropertyPopup(bpy.types.Operator):
    bl_idname = "object.show_property_popup"
    bl_label = "プロパティ付きポップアップ"
    bl_description = "プロパティ付きポップアップ"
    bl_options = {'REGISTER', 'UNDO'}

    prop_int = IntProperty(
        name="プロパティ 1",
        description="プロパティ 1",
        default=100,
        min=0,
        max=255)
    prop_float = FloatProperty(
        name="プロパティ 2",
        description="プロパティ 2",
        default=0.75,
        min=0.0,
        max=1.0)
    prop_enum = EnumProperty(
        name="プロパティ 3",
        description="プロパティ 3",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")],
        default='ITEM_1')
    prop_floatv = FloatVectorProperty(
        name="プロパティ 4",
        description="プロパティ 4",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0)

    def execute(self, context):
        self.report({'INFO'}, "サンプル2-10: [1] %d, [2] %f, [3] %s, [4] (%f, %f, %f)"
            % (self.prop_int, self.prop_float, self.prop_enum, self.prop_floatv[0], self.prop_floatv[1], self.prop_floatv[2]))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # プロパティ付きポップアップ表示
        return wm.invoke_props_popup(self, event)
//! [ops_show_property_popup]


//! [ops_show_search_popup]
class ShowSearchPopup(bpy.types.Operator):
    bl_idname = "object.show_search_popup"
    bl_label = "検索ウィンドウ付きポップアップ"
    bl_description = "検索ウィンドウ付きポップアップ"
    bl_options = {'REGISTER', 'UNDO'}
    bl_property = "item"

    item = EnumProperty(
        name="配置位置",
        description="複製したオブジェクトの配置位置",
        items=[
            ('ITEM_1', '項目1', '項目1'),
            ('ITEM_2', '項目2', '項目2'),
            ('ITEM_3', '項目3', '項目3')
        ],
        default='ITEM_1'
    )

    def execute(self, context):
        self.report({'INFO'}, "サンプル2-10: %s を選択しました" % self.item)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # 検索ウィンドウ付きポップアップ表示
        wm.invoke_search_popup(self)

        # {'FINISHED'} を返す必要がある
        return {'FINISHED'}
//! [ops_show_search_popup]


# ツールシェルフに「カスタムメニュー」タブを追加
class VIEW3D_PT_CustomMenu(bpy.types.Panel):
    bl_label = "カスタムメニュー"       # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "カスタムメニュー"    # タブを開いたメニューのヘッダーに表示される文字列
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

//! [show_popup_message]
        # ポップアップメッセージを表示する
        layout.label(text="ポップアップメッセージを表示する:")
        layout.operator(ShowPopupMessage.bl_idname)
//! [show_popup_message]

        layout.separator()

//! [show_dialog_menu]
        # ダイアログメニューを表示する
        layout.label(text="ダイアログメニューを表示する:")
        layout.operator(ShowDialogMenu.bl_idname)
//! [show_dialog_menu]

        layout.separator()

//! [show_file_browser]
        # ファイルブラウザを表示する
        layout.label(text="ファイルブラウザを表示する:")
        layout.operator(ShowFileBrowser.bl_idname)
//! [show_file_browser]

        layout.separator()

//! [show_confirm_popup]
        # 確認ポップアップを表示する
        layout.label(text="確認ポップアップを表示する:")
        layout.operator(ShowConfirmPopup.bl_idname)
//! [show_confirm_popup]

        layout.separator()

//! [show_property_popup]
        # プロパティ付きポップアップを表示する
        layout.label(text="プロパティ付きポップアップを表示する:")
        layout.operator(ShowPropertyPopup.bl_idname)
//! [show_property_popup]

        layout.separator()

//! [show_search_popup]
        # 検索ポップアップを表示する
        layout.label(text="検索ポップアップを表示する:")
        layout.operator(ShowSearchPopup.bl_idname)
//! [show_search_popup]


# プロパティの初期化
def init_props():
    scene = bpy.types.Scene
    scene.cm_prop_int = IntProperty(
        name="Prop 1",
        description="Integer Property",
        default=100,
        min=0,
        max=255)
    scene.cm_prop_float = FloatProperty(
        name="Prop 2",
        description="Float Property",
        default=0.75,
        min=0.0,
        max=1.0)
    scene.cm_prop_enum = EnumProperty(
        name="Prop 3",
        description="Enum Property",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")],
        default='ITEM_1')
    scene.cm_prop_floatv = FloatVectorProperty(
        name="Prop 4",
        description="Float Vector Property",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0)


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
    print("サンプル2-10: アドオン「サンプル2-10」が有効化されました。")


def unregister():
    bpy.utils.unregister_module(__name__)
    clear_props()
    print("サンプル2-10: アドオン「サンプル2-10」が無効化されました。")


if __name__ == "__main__":
    register()
