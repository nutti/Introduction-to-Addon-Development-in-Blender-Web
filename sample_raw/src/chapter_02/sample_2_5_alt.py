import bpy
from bpy.props import StringProperty, FloatVectorProperty, EnumProperty
from mathutils import Vector


bl_info = {
    "name": "サンプル2-5: オブジェクトを複製するアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > オブジェクト",
    "description": "オブジェクトを複製するアドオン",
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
        ('ORIGIN', "原点", "原点に配置します")]
    items.extend([
        ('OBJ_' + o.name, o.name, "オブジェクトに配置します")
        for o in bpy.data.objects
    ])

    return items


# 選択したオブジェクトを複製するアドオン
class ReplicateObject(bpy.types.Operator):

    bl_idname = "object.replicate_object"
    bl_label = "オブジェクトの複製"
    bl_description = "オブジェクトを複製します"
    bl_options = {'REGISTER', 'UNDO'}

    location = EnumProperty(
        name="配置位置",
        description="複製したオブジェクトの配置位置",
        items=location_list_fn
    )
    scale = FloatVectorProperty(
        name="拡大率",
        description="複製したオブジェクトの拡大率を設定します",
        default=(1.0, 1.0, 1.0),
        subtype='XYZ',
        unit='LENGTH'
    )
    rotation = FloatVectorProperty(
        name="回転角度",
        description="複製したオブジェクトの回転角度を設定します",
        default=(0.0, 0.0, 0.0),
        subtype='AXISANGLE',
        unit='ROTATION'
    )
    offset = FloatVectorProperty(
        name="オフセット",
        description="複製したオブジェクトの配置位置からのオフセットを設定します",
        default=(0.0, 0.0, 0.0),
        subtype='TRANSLATION',
        unit='LENGTH'
    )
    src_obj_name = StringProperty()

    def execute(self, context):
        # bpy.ops.object.duplicate()は選択中のオブジェクトをコピーするため、
        # メニューで選択されたオブジェクトを選択された状態にする
        # context.scene.objects：オブジェクト一覧
        # context.scene.objects.active：現在アクティブなオブジェクト
        for o in context.scene.objects:
            if self.src_obj_name == o.name:
                context.scene.objects.active = o
                o.select = True
                break
            else:
                o.select = False
        # オブジェクトの複製
        bpy.ops.object.duplicate()
        active_obj = context.active_object

        # 複製したオブジェクトを配置位置に移動
        if self.location == '3D_CURSOR':
            active_obj.location = context.scene.cursor_location.copy()
        elif self.location == 'ORIGIN':
            active_obj.location = Vector((0.0, 0.0, 0.0))
        elif self.location[0:4] == 'OBJ_':
            objs = bpy.data.objects
            active_obj.location = objs[self.location[4:]].location.copy()

        # 複製したオブジェクトの拡大率を設定
        active_obj.scale.x = active_obj.scale.x * self.scale[0]
        active_obj.scale.y = active_obj.scale.y * self.scale[1]
        active_obj.scale.z = active_obj.scale.z * self.scale[2]

        # 複製したオブジェクトの回転角度を設定
        rot_euler = active_obj.rotation_euler
        active_obj.rotation_euler.x = rot_euler.x + self.rotation[0]
        active_obj.rotation_euler.y = rot_euler.y + self.rotation[1]
        active_obj.rotation_euler.z = rot_euler.z + self.rotation[2]

        # 複製したオブジェクトの最終位置を設定
        active_obj.location = active_obj.location + Vector(self.offset)

        self.report({'INFO'}, "サンプル2-5: 「%s」を複製しました。" % (self.src_obj_name))
        print("サンプル2-5: オペレーション「%s」が実行されました。" % (self.bl_idname))

        return {'FINISHED'}


//! [sub_menu_cls]
# サブメニュー
class ReplicateObjectSubMenu(bpy.types.Menu):

    bl_idname = "object.replicate_object_sub_menu"
    bl_label = "オブジェクトの複製（サブメニュー）"
    bl_description = "オブジェクトを複製します（サブメニュー）"

    def draw(self, context):
        layout = self.layout
        # サブサブメニューの登録
        for o in bpy.data.objects:
            layout.operator(
                ReplicateObject.bl_idname, text=o.name
            ).src_obj_name = o.name
//! [sub_menu_cls]


//! [main_menu_cls]
# メインメニュー
class ReplicateObjectMenu(bpy.types.Menu):

    bl_idname = "object.replicate_object_menu"
    bl_label = "オブジェクトの複製"
    bl_description = "オブジェクトを複製します"

    def draw(self, context):
        layout = self.layout
        # サブメニューの登録
        layout.menu(ReplicateObjectSubMenu.bl_idname)
//! [main_menu_cls]


def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(ReplicateObjectMenu.bl_idname)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル2-5: アドオン「サンプル2-5」が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル2-5: アドオン「サンプル2-5」が無効化されました。")


if __name__ == "__main__":
    register()
