# @include-source start [import_bpy]
import bpy   # アドオン開発者に対して用意しているAPIを利用する
# @include-source end [import_bpy]


# @include-source start [bl_info]
# アドオンに関する情報を保持する、bl_info変数
bl_info = {
    "name": "サンプル 2-1: オブジェクトを生成するアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > 追加 > メッシュ",
    "description": "オブジェクトを生成するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object"
}
# @include-source end [bl_info]


# @include-source start [mem_var]
# オブジェクト（ICO球）を生成するオペレータ
class SAMPLE21_OT_CreateObject(bpy.types.Operator):

    bl_idname = "object.sample21_create_object"
    bl_label = "球"
    bl_description = "ICO球を追加します"
    bl_options = {'REGISTER', 'UNDO'}
# @include-source end [mem_var]

# @include-source start [execute]
    # メニューを実行したときに呼ばれる関数
    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("サンプル 2-1: ICO球を生成しました。")

        return {'FINISHED'}
# @include-source end [execute]


# @include-source start [build_menu]
# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SAMPLE21_OT_CreateObject.bl_idname)
# @include-source end [build_menu]

# Blenderに登録するクラス
classes = [
    SAMPLE21_OT_CreateObject,
]

# @include-source start [register]
# アドオン有効化時の処理
def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_fn)
    print("サンプル 2-1: アドオン『サンプル 2-1』が有効化されました。")
# @include-source end [register]


# @include-source start [unregister]
# アドオン無効化時の処理
def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 2-1: アドオン『サンプル 2-1』が無効化されました。")
# @include-source end [unregister]


# @include-source start [main]
# メイン処理
if __name__ == "__main__":
    register()
# @include-source end [main]
