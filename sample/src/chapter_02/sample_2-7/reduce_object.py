import bpy

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
        self.report({'INFO'}, "サンプル 2-7: 「" + active_obj.name + "」を1/2倍に縮小しました。")
        print("サンプル 2-7: オペレーション「" + self.bl_idname + "」が実行されました。")

        return {'FINISHED'}
