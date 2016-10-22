bl_info = {
    "name": "サンプル2-7: オブジェクトを拡大・縮小するアドオン（ファイル分割版）",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > オブジェクト",
    "description": "オブジェクトを拡大・縮小するサンプルアドオン（ファイル分割版）",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

//! [import_moudle]
if "bpy" in locals():
    import imp
    imp.reload(enlarge_object)
    imp.reload(reduce_object)
else:
    from . import enlarge_object
    from . import reduce_object

import bpy
//! [import_moudle]

# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(enlarge_object.EnlargeObject.bl_idname)
    self.layout.operator(reduce_object.ReduceObject.bl_idname)


# アドオン有効化時の処理
def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル 2-7: アドオン「サンプル 2-7」が有効化されました。")


# アドオン無効化時の処理
def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル 2-7: アドオン「サンプル 2-7」が無効化されました。")


# メイン処理
if __name__ == "__main__":
    register()
