import bpy
from bpy.props import IntProperty, FloatProperty, EnumProperty, FloatVectorProperty, StringProperty

bl_info = {
    "name": "サンプル2-8: BlenderのUIを制御するアドオン1",
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


# ツールシェルフに「カスタムメニュー」タブを追加
class VIEW3D_PT_CustomMenu(bpy.types.Panel):
    bl_label = "カスタムメニュー"           # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "カスタムメニュー"        # タブを開いたメニューのヘッダーに表示される文字列
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


def menu_fn_1(self, context):
    self.layout.separator()
    self.layout.operator(NullOperation.bl_idname, text="項目 1", icon='PLUGIN')


def menu_fn_2(self, context):
    self.layout.operator(NullOperation.bl_idname, text="項目 2", icon='PLUGIN')
    self.layout.separator()


def register():
    bpy.utils.register_module(__name__)
    # 項目をメニューの先頭に追加
    bpy.types.VIEW3D_MT_object.append(menu_fn_1)
    # 項目をメニューの末尾に追加
    bpy.types.VIEW3D_MT_object.prepend(menu_fn_2)
    print("サンプル2-8: アドオン「サンプル2-8」が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn_2)
    bpy.types.VIEW3D_MT_object.remove(menu_fn_1)
    bpy.utils.unregister_module(__name__)
    print("サンプル2-8: アドオン「サンプル2-8」が無効化されました。")


if __name__ == "__main__":
    register()
