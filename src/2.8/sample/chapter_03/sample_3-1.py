import bpy


bl_info = {
    "name": "サンプル 3-1: オブジェクトを回転するアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > サンプル 3-1",
    "description": "マウスの右ドラッグでオブジェクトを回転するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# マウスドラッグでオブジェクトを回転するオペレータ
class SAMPLE31_OT_RotateObjectByMouseDragging(bpy.types.Operator):

    bl_idname = "object.sample31_rotate_object_by_mouse_dragging"
    bl_label = "オブジェクトを回転"
    bl_description = "マウスドラッグでオブジェクトを回転します"

# @include-source start [class_variable]
    # Trueの場合は、マウスをドラッグさせたときに、アクティブなオブジェクトが
    # 回転する（Trueの場合は、モーダルモード中である）
    __running = False
    # マウスが右クリックされている間に、Trueとなる
    __right_mouse_down = False
    # 初期のX軸回転角度
    __initial_rotation_x = None
    # 初期のマウスポインタのX座標
    __initial_mouse_x = None
# @include-source end [class_variable]

    # モーダルモード中はTrueを返す
    @classmethod
    def is_running(cls):
        return cls.__running

    def modal(self, context, event):
        op_cls = SAMPLE31_OT_RotateObjectByMouseDragging
        active_obj = context.active_object

# @include-source start [redraw_view3d]
        # エリアを再描画
        if context.area:
            context.area.tag_redraw()
# @include-source end [redraw_view3d]

# @include-source start [exit_modal_mode]
        # パネル [マウスドラッグでオブジェクトを回転] のボタン [終了] を
        # 押したときに、モーダルモードを終了
        if not self.is_running():
            return {'FINISHED'}
# @include-source end [exit_modal_mode]

# @include-source start [update_click_status]
        # マウスのクリック状態を更新
        if event.type == 'RIGHTMOUSE':
            # 右ボタンを押されたとき
            if event.value == 'PRESS':
                op_cls.__right_mouse_down = True
                op_cls.__initial_rotation_x = active_obj.rotation_euler[0]
                op_cls.__initial_mouse_x = event.mouse_region_x
            # 右ボタンが離されたとき
            elif event.value == 'RELEASE':
                op_cls.__right_mouse_down = False
                op_cls.__initial_rotation_x = None
                op_cls.__initial_mouse_x = None
            return {'RUNNING_MODAL'}
# @include-source end [update_click_status]
# @include-source start [update_object_rotation]
        # マウスドラッグによるオブジェクト回転
        elif event.type == 'MOUSEMOVE':
            if op_cls.__right_mouse_down:
                rotate_angle_x = (event.mouse_region_x - op_cls.__initial_mouse_x) * 0.01
                active_obj.rotation_euler[0] = op_cls.__initial_rotation_x + rotate_angle_x
                return {'RUNNING_MODAL'}
# @include-source end [update_object_rotation]

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        op_cls = SAMPLE31_OT_RotateObjectByMouseDragging

        if context.area.type == 'VIEW_3D':
# @include-source start [press_start_button]
            # [開始] ボタンが押された時の処理
            if not self.is_running():
                op_cls.__right_mouse_down = False
                op_cls.__initial_rotation = None
                op_cls.__initial_mouse_x = None
                # モーダルモードを開始
                context.window_manager.modal_handler_add(self)
                op_cls.__running = True
                print("サンプル 3-1: オブジェクトの回転処理を開始しました。")
                return {'RUNNING_MODAL'}
# @include-source end [press_start_button]
# @include-source start [press_stop_button]
            # [終了] ボタンが押された時の処理
            else:
                op_cls.__running = False
                print("サンプル 3-1: オブジェクトの回転処理を終了しました。")
                return {'FINISHED'}
# @include-source end [press_stop_button]
        else:
            return {'CANCELLED'}


# @include-source start [define_panel_class]
# UI
class SAMPLE31_PT_RotateObjectByMouseDragging(bpy.types.Panel):

    bl_label = "オブジェクトを回転"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "サンプル 3-1"
    bl_context = "objectmode"
# @include-source end [define_panel_class]

# @include-source start [define_draw_method]
    def draw(self, context):
        op_cls = SAMPLE31_OT_RotateObjectByMouseDragging

        layout = self.layout
        # [開始] / [終了] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname,text="開始", icon='PLAY')
        else:
            layout.operator(op_cls.bl_idname,text="終了", icon='PAUSE')
# @include-source end [define_draw_method]


classes = [
    SAMPLE31_OT_RotateObjectByMouseDragging,
    SAMPLE31_PT_RotateObjectByMouseDragging,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル 3-1: アドオン『サンプル 3-1』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 3-1: アドオン『サンプル 3-1』が無効化されました。")


if __name__ == "__main__":
    register()
