import bpy
from bpy.props import FloatVectorProperty, EnumProperty
from mathutils import Vector


bl_info = {
    "name": "サンプル2-6: オブジェクトを複製するアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > オブジェクト, Ctrl + Alt + R",
    "description": "選択したオブジェクトを複製するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

addon_keymaps = []          # 登録したショートカットキー一覧


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
    bl_label = "選択オブジェクトの複製"
    bl_description = "選択中のオブジェクトを複製します"
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

    def execute(self, context):
        # bpy.ops.object.duplicate()実行後に複製オブジェクトが選択されるため、選択中のオブジェクトを保存
        src_obj_name = context.active_object.name
        bpy.ops.object.duplicate()
        active_obj = context.active_object

        # 複製したオブジェクトを配置位置に移動
        if self.location == '3D_CURSOR':
            # Shallow copyを避けるため、copy()によるDeep copyを実行
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

        self.report({'INFO'}, "サンプル2-6: 「%s」を複製しました。" % (src_obj_name))
        print("サンプル2-6: オペレーション「%s」が実行されました。" % (self.bl_idname))

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(ReplicateObject.bl_idname)


def register_shortcut():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # 3Dビューのショートカットキーとして登録
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        # ショートカットキーの登録
        kmi = km.keymap_items.new(
            idname=ReplicateObject.bl_idname,
            type="R",
            value="PRESS",
            shift=False,
            ctrl=True,
            alt=True
        )
        # ショートカットキー一覧に登録
        addon_keymaps.append((km, kmi))


def unregister_shortcut():
    for km, kmi in addon_keymaps:
        # ショートカットキーの登録解除
        km.keymap_items.remove(kmi)
    # ショートカットキー一覧をクリア
    addon_keymaps.clear()


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    register_shortcut()
    print("サンプル2-6: アドオン「サンプル2-6」が有効化されました。")


def unregister():
    unregister_shortcut()
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル2-6: アドオン「サンプル2-6」が無効化されました。")


if __name__ == "__main__":
    register()
