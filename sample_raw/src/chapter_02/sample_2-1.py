//! [_dummy] 一行目の指示は無視されるため、ダミー指示を配置
//! [import_bpy]
import bpy   # アドオン開発者に対して用意しているAPIを利用する
//! [import_bpy]

//! [bl_info]
# アドオンに関する情報を保持する、bl_info変数
bl_info = {
    "name": "サンプル2-1: オブジェクトを生成するアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > 追加 > メッシュ",
    "description": "オブジェクトを生成するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}
//! [bl_info]


//! [mem_var]
# オブジェクト（ICO球）を生成するオペレーション
class CreateObject(bpy.types.Operator):

    bl_idname = "object.create_object"
    bl_label = "球"
    bl_description = "ICO球を追加します"
    bl_options = {'REGISTER', 'UNDO'}
//! [mem_var]

//! [execute]
    # メニューを実行した時に呼ばれる関数
    def execute(self, context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("サンプル2-1: 3DビューにICO球を生成しました。")

        return {'FINISHED'}
//! [execute]


//! [build_menu]
# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(CreateObject.bl_idname)
//! [build_menu]


//! [register]
# アドオン有効化時の処理
def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(menu_fn)
    print("サンプル2-1: アドオン「サンプル2-1」が有効化されました。")
//! [register]


//! [unregister]
# アドオン無効化時の処理
def unregister():
    bpy.types.INFO_MT_mesh_add.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル2-1: アドオン「サンプル2-1」が無効化されました。")
//! [unregister]


//! [main]
# メイン処理
if __name__ == "__main__":
    register()
//! [main]
//! [_dummy]
