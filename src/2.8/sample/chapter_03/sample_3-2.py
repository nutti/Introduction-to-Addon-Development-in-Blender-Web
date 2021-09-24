import bpy


bl_info = {
    "name": "サンプル 3-2: 入力したキーを表示するアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > サンプル 3-2",
    "description": "入力したキーのテキストオブジェクトを表示するアドオン",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object"
}


# @include-source start [make_alphabet_list]
# 大文字のアルファベットリスト
ALPHABET_LIST = [chr(i) for i in range(65, 65 + 26)]
# @include-source end [make_alphabet_list]


# 入力したキーのテキストオブジェクトを表示するオペレータ
class SAMPLE32_OT_ShowInputKey(bpy.types.Operator):

    bl_idname = "object.sample32_show_input_key"
    bl_label = "入力キーを表示"
    bl_description = "入力したキーをテキストオブジェクトとして表示します"

    # Trueの場合は、キーを入力したときに入力したキーに対する
    # テキストオブジェクトが表示される（Trueの場合は、モーダルモード中である）
    __running = False
    # テキストオブジェクトの名前
    __text_object_name = None

    # モーダルモード中はTrueを返す
    @classmethod
    def is_running(cls):
        return cls.__running

    def modal(self, context, event):
        op_cls = SAMPLE32_OT_ShowInputKey

        # エリアを再描画
        if context.area:
            context.area.tag_redraw()

# @include-source start [finish_modal_mode]
        # パネル [入力キーのテキストオブジェクト表示] のボタン [終了] を
        # 押したときに、モーダルモードを終了
        if not self.is_running():
            # テキストオブジェクトを削除
            if op_cls.__text_object_name in bpy.data.objects:
                bpy.data.objects.remove(bpy.data.objects[op_cls.__text_object_name])
            op_cls.__text_object_name = None
            return {'FINISHED'}
# @include-source end [finish_modal_mode]

# @include-source start [change_text_object_text]
        input_key = event.type
        # 大文字のアルファベット以外はすべてイベントを無視する
        if input_key not in ALPHABET_LIST:
            return {'PASS_THROUGH'}

        if op_cls.__text_object_name in bpy.data.objects:
            bpy.data.objects[op_cls.__text_object_name].data.body = input_key
# @include-source end [change_text_object_text]

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        op_cls = SAMPLE32_OT_ShowInputKey

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not op_cls.is_running():
                # テキストオブジェクト作成
                bpy.ops.object.text_add(location=(0.0, 0.0, 0.0), radius=2.0)
                op_cls.__text_object_name = context.active_object.name
                bpy.data.objects[op_cls.__text_object_name].data.body = ""
                # モーダルモードを開始
                context.window_manager.modal_handler_add(self)
                op_cls.__running = True
                print("サンプル 3-2: 入力キーの表示処理を開始しました。")
                return {'RUNNING_MODAL'}
            # [終了] ボタンが押された時の処理
            else:
                op_cls.__running = False
                print("サンプル 3-2: 入力キーの表示処理を終了しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE32_PT_ShowInputKey(bpy.types.Panel):

    bl_label = "入力キーを表示"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "サンプル 3-2"
    bl_context = "objectmode"

    def draw(self, context):
        op_cls = SAMPLE32_OT_ShowInputKey

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")


classes = [
    SAMPLE32_OT_ShowInputKey,
    SAMPLE32_PT_ShowInputKey,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル 3-2: アドオン『サンプル 3-2』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 3-2: アドオン『サンプル 3-2』が無効化されました。")


if __name__ == "__main__":
    register()
