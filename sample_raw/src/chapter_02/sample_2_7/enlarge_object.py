import bpy


# オブジェクトを拡大するオペレーション
class EnlargeObject(bpy.types.Operator):

    bl_idname = "object.enlarge_object"
    bl_label = "選択オブジェクトの拡大"
    bl_description = "選択中のオブジェクトを拡大します"
    bl_options = {'REGISTER', 'UNDO'}

    # メニューを実行した時に呼ばれる関数
    def execute(self, context):
        active_obj = context.active_object
        active_obj.scale = active_obj.scale * 2.0
        self.report({'INFO'}, "サンプル 2-7: 「%s」を2倍に拡大しました。" % (active_obj.name))
        print("サンプル 2-7: オペレーション「%s」が実行されました。" % (self.bl_idname))

        return {'FINISHED'}
