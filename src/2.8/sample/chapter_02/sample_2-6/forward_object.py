import bpy


# オブジェクトをX軸正方向に並進移動するオペレータ
class SAMPLE26_OT_ForwardXObject(bpy.types.Operator):

    bl_idname = "object.sample26_forward_x_object"
    bl_label = "X軸正方向へ並進移動"
    bl_description = "アクティブなオブジェクトをX軸正方向へ並進移動します"
    bl_options = {'REGISTER', 'UNDO'}

    # メニューを実行したときに呼ばれるメソッド
    def execute(self, context):
        active_obj = context.active_object
        active_obj.location[0] += 1.0
        self.report({'INFO'}, "サンプル2-6: 『{}』をX軸正方向へ並進移動しました。".format(active_obj.name))
        print("サンプル2-6: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}
