```py:sample_4.py
import bpy
from bpy.props import FloatProperty

bl_info = {
	"name": "サンプル4: オブジェクトを複製するアドオン",
	"author": "Nutti",
	"version": (1, 0),
	"blender": (2, 75, 0),
	"location": "Object > サンプル4: オブジェクトを複製するアドオン",
	"description": "選択したオブジェクトを複製するアドオン",
	"warning": "",
	"support": "TESTING",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Object"
}


# 選択したオブジェクトを複製するアドオン
class ReplicateObject(bpy.types.Operator):

	bl_idname = "object.replicate_object"
	bl_label = "選択オブジェクトの複製"
	bl_description = "選択中のオブジェクトを複製します"
	bl_options = {'REGISTER', 'UNDO'}

	magnification = FloatProperty(
		name = "拡大率",
		description = "拡大率を設定します",
		default = 2.0,
		min = 1.0,
		max = 10.0
	)

	def execute(self, context):
		active_obj = context.active_object
		active_obj.scale = active_obj.scale * self.magnification
		self.report({'INFO'}, "サンプル 3: 「%s」を%f倍に拡大しました。" % (active_obj.name, self.magnification))
		print("サンプル 3: オペレーション「%s」が実行されました。" % self.bl_idname)

		return {'FINISHED'}


def menu_fn(self, context):
	self.layout.separator()
	self.layout.operator(ReplicateObject.bl_idname)


def register():
	bpy.utils.register_module(__name__)
	bpy.types.VIEW3D_MT_object.append(menu_fn)
	print("サンプル 4: アドオン「サンプル4」が有効化されました。")


def unregister():
	bpy.types.VIEW3D_MT_object.remove(menu_fn)
	bpy.utils.unregister_module(__name__)
	print("サンプル 4: アドオン「サンプル 4」が無効化されました。")


if __name__ == "__main__":
	register()

```
