import bpy
import bmesh
from bpy.props import IntProperty, BoolProperty, PointerProperty

bl_info = {
    "name": "サンプル7: マウスの右クリックで面を削除する",
    "author": "Nutti",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > マウスの右クリックで面を削除",
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

    def modal(self, context, event):
        props = context.scene.dfrc_props

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 起動していない場合は終了
        if props.running is False:
            return {'PASS_THROUGH'}

        # クリック状態を更新
        if event.type == 'RIGHTMOUSE':
            if event.value == 'PRESS':
                props.right_mouse_down = True
            elif event.value == 'RELEASE':
                props.right_mouse_down = False

        # 右クリックされた面を削除
        if props.right_mouse_down is True and props.deleted is False:
            # bmeshの構築
            obj = context.edit_object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            # クリックされた面を選択
            loc = event.mouse_region_x, event.mouse_region_y
            ret = bpy.ops.view3d.select(location=loc)
            if ret == {'PASS_THROUGH'}:
                print("サンプル7: 選択範囲外です。")
                return {'PASS_THROUGH'}
            # 選択面を取得
            e = bm.select_history[-1]
            if not isinstance(e, bmesh.types.BMFace):
                bm.select_history.remove(e)
                print("サンプル7: 面以外を選択しました。")
                return {'PASS_THROUGH'}
            # 選択面を削除
            bm.select_history.remove(e)
            bmesh.ops.delete(bm, geom=[e], context=5)
            # bmeshの更新
            bmesh.update_edit_mesh(me, True)
            # 削除面数をカウントアップ
            props.deleted_count = props.deleted_count + 1
            # マウスクリック中に連続して面が削除されることを防ぐ
            props.deleted = True
            print("サンプル7: 面を削除しました。")

        # マウスがクリック状態から解除された時に、削除禁止状態を解除
        if props.right_mouse_down is False:
            props.deleted = False

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        props = context.scene.dfrc_props
        if context.area.type == 'VIEW_3D':
            # 処理開始
            if props.running is False:
                props.running = True
                props.deleted = False
                props.right_mouse_down = False
                props.deleted_count = 0
                # modal処理クラスを追加
                context.window_manager.modal_handler_add(self)
                print("サンプル7: 削除処理を開始しました。")
                return {'RUNNING_MODAL'}
            # 処理停止
            else:
                props.running = False
                self.report({'INFO'}, "サンプル7: %d個の面を削除しました。" % (props.deleted_count))
                print("サンプル7: %d個の面を削除しました。" % (props.deleted_count))
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
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(DeleteFaceByRClick.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(DeleteFaceByRClick.bl_idname, text="終了", icon="PAUSE")


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.dfrc_props = PointerProperty(
        name = "プロパティ",
        description = "本アドオンで利用するプロパティ一覧",
        type = DFRC_Properties)
    print("サンプル7: アドオン「サンプル7」が有効化されました。")


def unregister():
    del bpy.types.Scene.dfrc_props
    bpy.utils.unregister_module(__name__)
    print("サンプル7: アドオン「サンプル7」が無効化されました。")


if __name__ == "__main__":
    register()
