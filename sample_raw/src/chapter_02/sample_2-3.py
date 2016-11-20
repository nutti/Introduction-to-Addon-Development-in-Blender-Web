import bpy
from bpy.props import FloatProperty

bl_info = {
    "name": "サンプル2-3: オブジェクトを拡大・縮小するアドオン（拡大率/縮小率 任意指定版）",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > オブジェクト",
    "description": "オブジェクトを拡大・縮小するサンプルアドオン（拡大率/縮小率を任意に指定可能）",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# オブジェクトを拡大するオペレーション
class EnlargeObject2(bpy.types.Operator):

    bl_idname = "object.enlarge_object_2"
    bl_label = "選択オブジェクトの拡大（拡大率任意指定）"
    bl_description = "選択中のオブジェクトを拡大します（拡大率任意指定可能）"
    bl_options = {'REGISTER', 'UNDO'}

//! [prop_enlarge_object_2]
    magnification = FloatProperty(
        name = "拡大率",
        description = "拡大率を設定します",
        default = 2.0,
        min = 1.0,
        max = 10.0
    )
//! [prop_enlarge_object_2]

    def execute(self, context):
        active_obj = context.active_object
        active_obj.scale = active_obj.scale * self.magnification
        self.report({'INFO'}, "サンプル2-3: 「%s」を%f倍に拡大しました。" % (active_obj.name, self.magnification))
        print("サンプル2-3: オペレーション「%s」が実行されました。" % self.bl_idname)

        return {'FINISHED'}


# オブジェクトを縮小するオペレーション
class ReduceObject2(bpy.types.Operator):

    bl_idname = "object.reduce_object_2"
    bl_label = "選択オブジェクトの縮小（縮小率任意指定）"
    bl_description = "選択中のオブジェクトを縮小します（縮小率任意指定可能）"
    bl_options = {'REGISTER', 'UNDO'}

//! [prop_reduce_object_2]
    reduction = FloatProperty(
        name = "縮小率",
        description = "縮小率を設定します",
        default = 0.5,
        min = 0.001,
        max = 1.0
    )
//! [prop_reduce_object_2]

    def execute(self, context):
        active_obj = context.active_object
//! [access_to_prop]
        active_obj.scale = active_obj.scale * self.reduction
//! [access_to_prop]
        self.report({'INFO'}, "サンプル2-3: 「%s」を%f倍に縮小しました。" % (active_obj.name, self.reduction))
        print("サンプル2-3: オペレーション「%s」が実行されました。" % self.bl_idname)

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(EnlargeObject2.bl_idname)
    self.layout.operator(ReduceObject2.bl_idname)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル2-3: アドオン「サンプル2-3」が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル2-3: アドオン「サンプル2-3」が無効化されました。")


if __name__ == "__main__":
    register()
