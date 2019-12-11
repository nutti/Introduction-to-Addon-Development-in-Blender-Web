import bpy


bl_info = {
    "name": "サンプル2-2: オブジェクトを並進移動するアドオン①",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > オブジェクト",
    "description": "アクティブなオブジェクトを並進移動するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# @include-source start [op_forward_object]
# オブジェクトをX軸正方向に並進移動するオペレータ
class SAMPLE22_OT_ForwardXObject(bpy.types.Operator):

    bl_idname = "object.sample22_forward_x_object"
    bl_label = "X軸正方向へ並進移動"
    bl_description = "アクティブなオブジェクトをX軸正方向へ並進移動します"
    bl_options = {'REGISTER', 'UNDO'}
# @include-source end [op_forward_object]

# @include-source start [execute_forward_object]
    # メニューを実行したときに呼ばれるメソッド
    def execute(self, context):
        active_obj = context.active_object
        active_obj.location[0] += 1.0
        self.report({'INFO'}, "サンプル2-2: 『{}』をX軸正方向へ並進移動しました。".format(active_obj.name))
        print("サンプル2-2: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}
# @include-source end [execute_forward_object]


# @include-source start [op_backward_object]
# オブジェクトをX軸負方向に並進移動するオペレータ
class SAMPLE22_OT_BackwardXObject(bpy.types.Operator):

    bl_idname = "object.sample22_backward_x_object"
    bl_label = "X軸負方向へ並進移動"
    bl_description = "アクティブなオブジェクトをX軸負方向へ並進移動します"
    bl_options = {'REGISTER', 'UNDO'}
# @include-source end [op_backward_object]

# @include-source start [execute_backward_object]
    # メニューを実行したときに呼ばれる関数
    def execute(self, context):
        active_obj = context.active_object
        active_obj.location[0] -= 1.0
        self.report({'INFO'}, "サンプル2-2: 『{}』をX軸負方向へ並進移動しました。".format(active_obj.name))
        print("サンプル2-2: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}
# @include-source end [execute_backward_object]


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SAMPLE22_OT_ForwardXObject.bl_idname)
    self.layout.operator(SAMPLE22_OT_BackwardXObject.bl_idname)


classes = [
    SAMPLE22_OT_ForwardXObject,
    SAMPLE22_OT_BackwardXObject,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル2-2: アドオン『サンプル2-2』が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル2-2: アドオン『サンプル2-2』が無効化されました。")


if __name__ == "__main__":
    register()
