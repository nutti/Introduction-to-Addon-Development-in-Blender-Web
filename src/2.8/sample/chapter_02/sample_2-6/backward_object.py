import bpy


# オブジェクトをX軸負方向に並進移動するオペレータ
class SAMPLE26_OT_BackwardXObject(bpy.types.Operator):

    bl_idname = "object.sample26_backward_x_object"
    bl_label = "X軸負方向へ並進移動"
    bl_description = "アクティブなオブジェクトをX軸負方向へ並進移動します"
    bl_options = {'REGISTER', 'UNDO'}

    # メニューを実行したときに呼ばれる関数
    def execute(self, context):
        active_obj = context.active_object
        active_obj.location[0] -= 1.0
        self.report({'INFO'}, "サンプル 2-6: 『{}』をX軸負方向へ並進移動しました。".format(active_obj.name))
        print("サンプル 2-6: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}
