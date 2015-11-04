```py:sample_4.py
import bpy
from bpy.props import FloatVectorProperty, EnumProperty
from mathutils import Vector

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


# EnumPropertyで表示したい項目リストを作成する関数
def location_list_fn(scene, context):
    items = [
		('3D_CURSOR', "3Dカーソル", "3Dカーソル上に配置します"),
		('ORIGIN', "原点", "原点に配置します")
	]
	items.extend([('OBJ_' + o.name, o.name, o.name + "に配置します") for o in bpy.data.objects])
	return items


# 選択したオブジェクトを複製するアドオン
class ReplicateObject(bpy.types.Operator):

	bl_idname = "object.replicate_object"
	bl_label = "選択オブジェクトの複製"
	bl_description = "選択中のオブジェクトを複製します"
	bl_options = {'REGISTER', 'UNDO'}

	location = EnumProperty(
		name = "配置位置",
		description = "複製したオブジェクトの配置位置",
		items = location_list_fn
	)

	scale = FloatVectorProperty(
		name = "拡大率",
		description = "複製したオブジェクトの拡大率を設定します",
		default = (1.0, 1.0, 1.0),
		subtype = 'XYZ',
		unit = 'LENGTH'
	)

	rotation = FloatVectorProperty(
		name = "回転角度",
		description = "複製したオブジェクトの回転角度を設定します",
		default = (0.0, 0.0, 0.0),
		subtype = 'AXISANGLE',
		unit = 'ROTATION'
	)

	offset = FloatVectorProperty(
		name = "オフセット",
		description = "複製したオブジェクトの配置位置からのオフセットを設定します",
		default = (0.0, 0.0, 0.0),
		subtype = 'TRANSLATION',
		unit = 'LENGTH'
	)

	def execute(self, context):
		bpy.ops.object.duplicate()
		active_obj = context.active_object
		if self.location == '3D_CURSOR':
			active_obj.location = context.scene.cursor_location.copy()
		elif self.location == 'ORIGIN':
			active_obj.location = Vector((0.0, 0.0, 0.0))
		else:
			active_obj.location = bpy.data.objects[self.location[4:]].location.copy()
		active_obj.scale.x = active_obj.scale.x * self.scale[0]
		active_obj.scale.y = active_obj.scale.y * self.scale[1]
		active_obj.scale.z = active_obj.scale.z * self.scale[2]
		active_obj.rotation_euler.x = active_obj.rotation_euler.x + self.rotation[0]
		active_obj.rotation_euler.y = active_obj.rotation_euler.y + self.rotation[1]
		active_obj.rotation_euler.z = active_obj.rotation_euler.z + self.rotation[2]
		active_obj.location = active_obj.location + Vector(self.offset)
		self.report({'INFO'}, "サンプル 4: 「%s」を複製しました。" % active_obj.name)
		print("サンプル 4: オペレーション「%s」が実行されました。" % self.bl_idname)

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
