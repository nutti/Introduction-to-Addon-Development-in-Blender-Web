```py:sample_7.py
import bpy

bl_info = {
    "name": "サンプル7: マウスの右クリックで面を削除する",
    "author": "Nutti",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "Mesh > サンプル7: マウスの右クリックで面を削除する",
    "description": "マウスの右クリックで面を削除するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"
}


# プロパティ
class DFRC_Properties(bpy.types.PropertyGroup):
    running = BoolProperty(
        name = "動作中",
        description = "削除処理が動作中か？",
        default = False)
    right_mouse_down = BoolProperty(
        name = "右クリックされた状態",
        description = "右クリックされた状態か？",
        default = False)
    deleted = BoolProperty(
        name = "面が削除された状態",
        description = "面が削除された状態か？",
        default = False)
    deleted_count = IntProperty(
        name = "削除した面数",
        description = "削除した面の数",
        default = 0)

# マウスの右クリックで面を削除
class DeleteFaceByRClick(bpy.types.Operator):

    bl_idname = "mesh.delete_face_by_rclick"
    bl_label = "マウスの右クリックで面を削除"
    bl_description = "マウスの右クリックで面を削除します"
    bl_options = {'REGISTER', 'UNDO'}

    def modal(self, context, event):
        props = context.scene.dfrc_props

        if context.area:
            context.area.tag_redraw()

        if dfrc_props.running is False:
            return {'PASS_THROUGH'}

        # クリック状態を更新
        if event.type == 'RIGHTMOUSE':
            if event.value == 'PRESS':
                props.right_mouse_down = True
            elif event.value == 'RELEASE':
                props.right_mouse_down = False

        # クリックされた面を削除
        if props.right_mouse_down is True and props.deleted is False:
            # get adjacent vertex
            obj = context.edit_object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)


            props.deleted_count = props.deleted_count + 1
            # マウスクリック中に連続して面が削除されることを防ぐ
            props.merged = True

        # マウスがクリック状態から解除された時に、削除禁止状態を解除
        if props.right_mouse_down is False:
            props.merged = False

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        sc = context.scene
        props = context.scene.dfrc_props
        if context.area.type == 'VIEW_3D':
            # 起動時の処理
            if props.running is False:
                props.running = True
                props.deleted = False
                props.right_mouse_down = False
                props.deleted_count = 0
                context.window_manager.modal_handler_add(self)
                return {'RUNNING_MODAL'}
            # 停止時の処理
            else:
                props.running = False
                self.report({'INFO'}, "サンプル 7: %d個の面を削除しました。" % (props.merged_count))
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_DFRC(bpy.types.Panel):
    bl_label = "マウスの右クリックで面を削除"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = context.scene.dfrc_props
        if props.running is False:
            layout.operator(DeleteFaceByRClick.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(DeleteFaceByRClick.bl_idname, text="終了", icon="PAUSE")


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(ReplicateObject.bl_idname)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル 7: アドオン「サンプル 7」が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    bpy.utils.unregister_module(__name__)
    print("サンプル 7: アドオン「サンプル 7」が無効化されました。")


if __name__ == "__main__":
    register()

```
