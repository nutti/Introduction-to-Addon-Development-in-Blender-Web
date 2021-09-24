bl_info = {
    "name": "サンプル 2-6: オブジェクトを並進移動するアドオン⑤",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > オブジェクト",
    "description": "アクティブなオブジェクトを並進移動するサンプルアドオン（ファイル分割版）",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object"
}


# @include-source start [import_moudle]
if "bpy" in locals():
    import imp
    imp.reload(forward_object)
    imp.reload(backward_object)
else:
    from . import forward_object
    from . import backward_object


import bpy
# @include-source end [import_moudle]


# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(forward_object.SAMPLE26_OT_ForwardXObject.bl_idname)
    self.layout.operator(backward_object.SAMPLE26_OT_BackwardXObject.bl_idname)


# Blenderに登録するクラス
classes = [
    forward_object.SAMPLE26_OT_ForwardXObject,
    backward_object.SAMPLE26_OT_BackwardXObject,
]


# アドオン有効化時の処理
def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル 2-6: アドオン『サンプル 2-6』が有効化されました。")


# アドオン無効化時の処理
def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 2-6: アドオン『サンプル 2-6』が無効化されました。")


# メイン処理
if __name__ == "__main__":
    register()
