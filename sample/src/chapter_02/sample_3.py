```py:sample_2.py
import bpy

bl_info = {
	"name": "サンプル3: オブジェクトを拡大・縮小するアドオン（拡大率/縮小率 任意指定版）",
	"author": "Nutti",
	"version": (1, 0),
	"blender": (2, 75, 0),
	"location": "Object > サンプル3: オブジェクトを拡大・縮小するアドオン（拡大率/縮小率 任意指定版）",
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

	magnification =

    # メニューを実行した時に呼ばれる関数
	def execute(self, context):
		active_obj = context.active_object
		active_obj.scale = active_obj.scale * self.magnification
		self.report({'INFO'}, "サンプル 2: 「" + active_obj.name + "」を" + self.magnification + "倍に拡大しました。")
		print("サンプル 3: オペレーション「" + self.bl_idname + "」が実行されました。")

		return {'FINISHED'}


# オブジェクトを縮小するオペレーション
class ReduceObject2(bpy.types.Operator):

	bl_idname = "object.reduce_object_2"
	bl_label = "選択オブジェクトの縮小（縮小率任意指定）"
	bl_description = "選択中のオブジェクトを縮小します（縮小率任意指定可能）"
	bl_options = {'REGISTER', 'UNDO'}

	reduction =

    # メニューを実行した時に呼ばれる関数
	def execute(self, context):
		active_obj = context.active_object
		active_obj.scale = active_obj.scale * 0.5
		self.report({'INFO'}, "サンプル 2: 「" + active_obj.name + "」を" + self.reduction + "倍に縮小しました。")
		print("サンプル 3: オペレーション「" + self.bl_idname + "」が実行されました。")

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
	print("サンプル 3: アドオン「サンプル3」が有効化されました。")


# アドオン無効化時の処理
def unregister():
	bpy.types.VIEW3D_MT_object.remove(menu_fn)
	bpy.utils.unregister_module(__name__)
	print("サンプル 3: アドオン「サンプル 3」が無効化されました。")


# メイン処理
if __name__ == "__main__":
	register()

```
