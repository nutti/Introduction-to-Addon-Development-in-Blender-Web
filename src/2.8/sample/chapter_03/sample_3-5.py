import datetime

import bpy
import blf


bl_info = {
    "name": "サンプル3-5: 日時を表示するアドオン②",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > Sample 3-5",
    "description": "現在の日時を表示するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# リージョン情報の取得
def get_region(context, area_type, region_type):
    region = None
    area = None

    # 指定されたエリアの情報を取得する
    for a in context.screen.areas:
        if a.type == area_type:
            area = a
            break
    else:
        return None
    # 指定されたリージョンの情報を取得する
    for r in area.regions:
        if r.type == region_type:
            region = r
            break

    return region


# 日時を表示するオペレータ
class SAMPLE35_OT_ShowDatetime(bpy.types.Operator):

    bl_idname = "object.sample35_show_datetime"
    bl_label = "日時を表示"
    bl_description = "日時を表示します"

    # 描画ハンドラ
    __handle = None

    @classmethod
    def is_running(cls):
        # 描画中はTrue
        return True if cls.__handle else False

    @classmethod
    def __handle_add(cls, context):
        if not cls.is_running():
            # 描画関数の登録
            cls.__handle = bpy.types.SpaceView3D.draw_handler_add(
                cls.__draw, (context, ), 'WINDOW', 'POST_PIXEL'
            )

    @classmethod
    def __handle_remove(cls, context):
        if cls.is_running():
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(
                cls.__handle, 'WINDOW'
            )
            cls.__handle = None

    @classmethod
    def __draw(cls, context):
        sc = context.scene

        # リージョンの幅を取得するため、描画先のリージョンを得る
        region = get_region(context, 'VIEW_3D', 'WINDOW')

        # 描画先のリージョンへテキストを描画
        #   注意：本来ならタイマを併用して再描画しないと日時が更新されないが、
        #         説明簡略化のためにタイマを利用していない。
        #         このため表示の不自然さを避けるため、時間以下の情報を表示していない。
        if region is not None:
            blf.size(0, 30, 72)
            blf.position(0, 100.0, region.height - 120.0, 0)
            date_str = datetime.datetime.now().strftime("%Y.%m.%d")
            blf.draw(0, date_str)

    def invoke(self, context, event):
        op_cls = SAMPLE35_OT_ShowDatetime

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not op_cls.is_running():
                self.__handle_add(context)
                print("サンプル3-5: 日時の表示処理を開始しました。")
            # [終了] ボタンが押された時の処理
            else:
                self.__handle_remove(context)
                print("サンプル3-5: 日時の表示処理を終了しました。")
            # エリアを再描画
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE35_PT_ShowDatetime(bpy.types.Panel):

    bl_label = "日時を表示"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Sample 3-5"
    bl_context = "objectmode"

    def draw(self, context):
        op_cls = SAMPLE35_OT_ShowDatetime

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")


classes = [
    SAMPLE35_OT_ShowDatetime,
    SAMPLE35_PT_ShowDatetime,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル3-5: アドオン『サンプル3-5』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル3-5: アドオン『サンプル3-5』が無効化されました。")


if __name__ == "__main__":
    register()
