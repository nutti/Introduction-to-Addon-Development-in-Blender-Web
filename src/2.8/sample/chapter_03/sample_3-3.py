import datetime

import bpy


bl_info = {
    "name": "サンプル3-3: 日時を表示するアドオン①",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > Sample 3-3",
    "description": "現在の日時をテキストオブジェクトとして表示するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# 日時をテキストオブジェクトとして表示するオペレータ
class SAMPLE33_OT_ShowDatetime(bpy.types.Operator):

    bl_idname = "object.sample33_show_datetime"
    bl_label = "日時を表示"
    bl_description = "日時をテキストオブジェクトとして表示します"

    # タイマのハンドラ
    __timer = None
    # テキストオブジェクトの名前
    __text_object_name = None

    @classmethod
    def is_running(cls):
        # モーダルモード中はTrue
        return True if cls.__timer else False

# @include-source start [add_timer]
    def __handle_add(self, context):
        if not self.is_running():
            # タイマを登録
            SAMPLE33_OT_ShowDatetime.__timer = \
                context.window_manager.event_timer_add(
                    0.5, window=context.window
                )
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)
# @include-source end [add_timer]

# @include-source start [remove_timer]
    def __handle_remove(self, context):
        if self.is_running():
            # タイマの登録を解除
            context.window_manager.event_timer_remove(
                SAMPLE33_OT_ShowDatetime.__timer)
            SAMPLE33_OT_ShowDatetime.__timer = None
# @include-source end [remove_timer]

    def modal(self, context, event):
        op_cls = SAMPLE33_OT_ShowDatetime

        # エリアを再描画
        if context.area:
            context.area.tag_redraw()

        # パネル [日時を表示] のボタン [終了] を押したときに、モーダルモードを終了
        if not self.is_running():
            # テキストオブジェクトを削除
            if op_cls.__text_object_name in bpy.data.objects:
                bpy.data.objects.remove(bpy.data.objects[op_cls.__text_object_name])
            op_cls.__text_object_name = None
            return {'FINISHED'}

# @include-source begin [handle_timer_event]
        if event.type == 'TIMER':
            bpy.data.objects[op_cls.__text_object_name].data.body = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
# @include-source end [handle_timer_event]

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        op_cls = SAMPLE33_OT_ShowDatetime

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not op_cls.is_running():
# @include-source begin [make_text_object]
                # テキストオブジェクト作成
                bpy.ops.object.text_add(location=(0.0, 0.0, 0.0), radius=2.0)
                op_cls.__text_object_name = context.active_object.name
                bpy.data.objects[op_cls.__text_object_name].data.body = ""
# @include-source end [make_text_object]
                # モーダルモードを開始
                self.__handle_add(context)
                print("サンプル3-3: 日時の表示処理を開始しました。")
                return {'RUNNING_MODAL'}
            # [終了] ボタンが押された時の処理
            else:
                # モーダルモードを終了
                self.__handle_remove(context)
                print("サンプル3-3: 日時の表示処理を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE33_PT_ShowDatetime(bpy.types.Panel):

    bl_label = "日時を表示"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sample 3-3"
    bl_context = "objectmode"

    def draw(self, context):
        op_cls = SAMPLE33_OT_ShowDatetime

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")


classes = [
    SAMPLE33_OT_ShowDatetime,
    SAMPLE33_PT_ShowDatetime,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル3-3: アドオン『サンプル3-3』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル3-3: アドオン『サンプル3-3』が無効化されました。")


if __name__ == "__main__":
    register()
