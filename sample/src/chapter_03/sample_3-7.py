import bpy
import bmesh
from bpy.props import IntProperty, BoolProperty, PointerProperty


bl_info = {
    "name": "サンプル3-7: マウスの右クリックで面を削除する（多言語対応版）",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > マウスの右クリックで面を削除",
    "description": "マウスの右クリックで面を削除するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Mesh"
}


# 翻訳辞書
translation_dict = {
    "en_US" : {
        ("*", "Delete Face By Right Click") :
            "Delete Face By Right Click",
        ("*", "Sample3-7: Out of range") :
            "Sample3-7: Out of range",
        ("*", "Sample3-7: No face is selected") :
            "Sample3-7: No face is selected",
        ("*", "Sample3-7: Deleted Face") :
            "Sample3-7: Deleted Face",
        ("*", "Sample3-7: Start deleting faces") :
            "Sample3-7: Start deleting faces",
        ("*", "Sample3-7: %d face(s) are deleted") :
            "Sample3-7: %d face(s) are deleted",
        ("*", "Start") :
            "Start",
        ("*", "End") :
            "End",
        ("*", "Sample3-7: Enabled add-on 'Sample3-7'") :
            "Sample3-7: Enabled add-on 'Sample3-7'",
        ("*", "Sample3-7: Disabled add-on 'Sample3-7'") :
            "Sample3-7: Disabled add-on 'Sample3-7'"
    },
    "ja_JP" : {
        ("*", "Delete Face By Right Click") :
            "マウスの右クリックで面を削除",
        ("*", "Sample3-7: Out of range") :
            "サンプル3-7: 選択範囲外です。",
        ("*", "Sample3-7: No face is selected") :
            "サンプル3-7: 面以外を選択しました。",
        ("*", "Sample3-7: Deleted Face") :
            "サンプル3-7: 面を削除しました。",
        ("*", "Sample3-7: Start deleting faces") :
            "サンプル3-7: 削除処理を開始しました。",
        ("*", "Sample3-7: %d face(s) are deleted") :
            "サンプル3-7: %d個の面を削除しました。",
        ("*", "Start") :
            "開始",
        ("*", "End") :
            "終了",
        ("*", "Sample3-7: Enabled add-on 'Sample3-7'") :
            "サンプル3-7: アドオン「サンプル3-7」が有効化されました。",
        ("*", "Sample3-7: Disabled add-on 'Sample3-7'") :
            "サンプル3-7: アドオン「サンプル3-7」が無効化されました。"
    }
}


# プロパティ
class DFRC_Properties(bpy.types.PropertyGroup):

    running = BoolProperty(
        name="動作中",
        description="削除処理が動作中か？",
        default=False
    )
    right_mouse_down = BoolProperty(
        name="右クリックされた状態",
        description="右クリックされた状態か？",
        default=False
    )
    deleted = BoolProperty(
        name="面が削除された状態",
        description="面が削除された状態か？",
        default=False
    )
    deleted_count = IntProperty(
        name="削除した面数",
        description="削除した面の数",
        default=0
    )


# マウスの右クリックで面を削除
class DeleteFaceByRClick(bpy.types.Operator):

    bl_idname = "mesh.delete_face_by_rclick"
    bl_label = bpy.app.translations.pgettext("Delete Face By Right Click")
    bl_description = bpy.app.translations.pgettext("Delete Face By Right Click")

    def modal(self, context, event):
        props = context.scene.dfrc_props

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # 起動していない場合は終了
        if props.running is False:
            return {'FINISHED'}

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
                print(bpy.app.translations.pgettext("Sample3-7: Out of range"))
                return {'PASS_THROUGH'}
            # 選択面を取得
            e = bm.select_history[-1]
            if not isinstance(e, bmesh.types.BMFace):
                bm.select_history.remove(e)
                print(bpy.app.translations.pgettext("Sample3-7: No face is selected"))
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
            print(bpy.app.translations.pgettext("Sample3-7: Deleted Face"))

        # マウスがクリック状態から解除された時に、削除禁止状態を解除
        if props.right_mouse_down is False:
            props.deleted = False

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        props = context.scene.dfrc_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.running is False:
                props.running = True
                props.deleted = False
                props.right_mouse_down = False
                props.deleted_count = 0
                # modal処理クラスを追加
                context.window_manager.modal_handler_add(self)
                print(bpy.app.translations.pgettext("Sample3-7: Start deleting faces"))
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.running = False
                self.report({'INFO'}, bpy.app.translations.pgettext_iface("Sample3-7: %d face(s) are deleted") % (props.deleted_count))
                print(bpy.app.translations.pgettext_iface("Sample3-7: %d face(s) are deleted") % (props.deleted_count))
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_DFRC(bpy.types.Panel):

    bl_label = bpy.app.translations.pgettext("Delete Face By Right Click")
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        props = context.scene.dfrc_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(DeleteFaceByRClick.bl_idname, text=bpy.app.translations.pgettext("Start"), icon="PLAY")
        else:
            layout.operator(DeleteFaceByRClick.bl_idname, text=bpy.app.translations.pgettext("End"), icon="PAUSE")


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.dfrc_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=DFRC_Properties
    )
    # 翻訳辞書の登録
    bpy.app.translations.register(__name__, translation_dict)
    print(bpy.app.translations.pgettext("Sample3-7: Enabled add-on 'Sample3-7'"))


def unregister():
    # 翻訳辞書の登録解除
    bpy.app.translations.unregister(__name__)
    del bpy.types.Scene.dfrc_props
    bpy.utils.unregister_module(__name__)
    print(bpy.app.translations.pgettext("Sample3-7: Disabled add-on 'Sample3-7'"))


if __name__ == "__main__":
    register()
