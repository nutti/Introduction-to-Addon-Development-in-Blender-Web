import datetime

import bpy
import blf
from bpy.props import IntProperty, IntVectorProperty


bl_info = {
    "name": "サンプル 3-7: 日時を表示するアドオン③",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > Sidebar > サンプル 3-7",
    "description": "現在の日時を表示するアドオン（プリファレンス利用版）",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "3D View"
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
class SAMPLE37_OT_ShowDatetime(bpy.types.Operator):

    bl_idname = "object.sample37_show_datetime"
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
# @include-source start [get_prefs]
        prefs = context.preferences.addons[__name__].preferences
# @include-source end [get_prefs]

        # リージョンの幅を取得するため、描画先のリージョンを得る
        region = get_region(context, 'VIEW_3D', 'WINDOW')

        # 描画先のリージョンへテキストを描画
        if region is not None:
# @include-source start [refer_prefs]
            blf.color(0, 1.0, 1.0, 1.0, 1.0)
            blf.size(0, prefs.font_size, 72)
            blf.position(0, prefs.position[0],
                         region.height - prefs.position[1], 0)
            date_str = datetime.datetime.now().strftime("%Y.%m.%d")
            blf.draw(0, date_str)
# @include-source end [refer_prefs]

    def invoke(self, context, event):
        op_cls = SAMPLE37_OT_ShowDatetime

        if context.area.type == 'VIEW_3D':
            # [開始] ボタンが押された時の処理
            if not op_cls.is_running():
                self.__handle_add(context)
                print("サンプル 3-7: 日時の表示処理を開始しました。")
            # [終了] ボタンが押された時の処理
            else:
                self.__handle_remove(context)
                print("サンプル 3-7: 日時の表示処理を終了しました。")
            # エリアを再描画
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class SAMPLE37_PT_ShowDatetime(bpy.types.Panel):

    bl_label = "日時を表示"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "サンプル 3-7"
    bl_context = "objectmode"

    def draw(self, context):
        op_cls = SAMPLE37_OT_ShowDatetime

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")


# @include-source start [addon_prefs]
# プリファレンスのアドオン設定情報
class SAMPLE37_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    position: IntVectorProperty(
        name="位置",
        description="描画位置",
        size=2,
        min=0,
        default=(100, 120),
        subtype='TRANSLATION'
    )
    font_size: IntProperty(
        name="フォントサイズ",
        description="描画フォントサイズ",
        min=10,
        max=100,
        default=30,
    )

    def draw(self, context):
        layout = self.layout

        sp = layout.split(factor=0.3)
        col = sp.column()
        col.prop(self, "position")

        sp = sp.split(factor=0.4)
        col = sp.column()
        col.label(text="フォントサイズ:")
        col.prop(self, "font_size", text="")
# @include-source end [addon_prefs]


classes = [
    SAMPLE37_OT_ShowDatetime,
    SAMPLE37_PT_ShowDatetime,
    SAMPLE37_Preferences,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print("サンプル 3-7: アドオン『サンプル 3-7』が有効化されました。")


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 3-7: アドオン『サンプル 3-7』が無効化されました。")


if __name__ == "__main__":
    register()
