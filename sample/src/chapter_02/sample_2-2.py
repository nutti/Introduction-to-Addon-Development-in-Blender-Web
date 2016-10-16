import bpy

bl_info = {
    "name": "サンプル2-2: オブジェクトを拡大・縮小するアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > オブジェクト",
    "description": "オブジェクトを拡大・縮小するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# オブジェクトを拡大するオペレーション
class EnlargeObject(bpy.types.Operator):

    bl_idname = "object.enlarge_object"
    bl_label = "選択オブジェクトの拡大"
    bl_description = "選択中のオブジェクトを拡大します"
    bl_options = {'REGISTER', 'UNDO'}

    # メニューを実行した時に呼ばれるメソッド
    def execute(self, context):
        active_obj = context.active_object
        active_obj.scale = active_obj.scale * 2.0
        self.report({'INFO'}, "サンプル2-2: 「" + active_obj.name + "」を2倍に拡大しました。")
        print("サンプル2-2: オペレーション「"+ self.bl_idname +"」が実行されました。")

        return {'FINISHED'}


# オブジェクトを縮小するオペレーション
class ReduceObject(bpy.types.Operator):

    bl_idname = "object.reduce_object"
    bl_label = "選択オブジェクトの縮小"
    bl_description = "選択中のオブジェクトを縮小します"
    bl_options = {'REGISTER', 'UNDO'}

    # メニューを実行した時に呼ばれる関数
    def execute(self, context):
        active_obj = context.active_object
        active_obj.scale = active_obj.scale * 0.5
        self.report({'INFO'}, "サンプル2-2: 「" + active_obj.name + "」を1/2倍に縮小しました。")
        print("サンプル2-2: オペレーション「"+self.bl_idname+"」が実行されました。")

        return {'FINISHED'}


# メニューを構築する関数
def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(EnlargeObject.bl_idname)
    self.layout.operator(ReduceObject.bl_idname)


# アドオン有効化時の処理
def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル2-2: アドオン「サンプル2-2」が有効化されました。")


# アドオン無効化時の処理
def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル2-2: アドオン「サンプル2-2」が無効化されました。")


# メイン処理
if __name__ == "__main__":
    register()
