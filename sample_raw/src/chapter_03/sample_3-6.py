import bpy
from bpy.props import BoolProperty
import aud

bl_info = {
    "name": "サンプル3-6: 指定したオーディオファイルを再生する",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > ツール・シェルフ > オーディオ再生",
    "description": "オーディオファイルを再生するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "UI"
}




# オーディオファイルの再生
class PlayAudioFile(bpy.types.Operator):
    bl_idname = "ui.play_audio_file"
    bl_label = "オーディオファイルの再生"
    bl_description = "オーディオファイルを再生します"

    device = None
    factory = None
    handle = None

    filepath = StringProperty(subtype="FILE_PATH")
    filename = StringProperty()
    directory = StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        if PlayAudioFile.device is None:
            PlayAudioFile.device = aud.device()

        PlayAudioFile.factory = aud.Factory('test.wav')

        # 再生中なら停止する
        if PlayAudioFile.handle is not None:
            PlayAudioFile.handle.stop()
        # 再生
        PlayAudioFile.handle = device.play()


    def invoke(self, context, event):
        wm = context.window_manager
        # ファイルブラウザ表示
        wm.fileselect_add(self)

        return {'RUNNING_MODAL'}


# ツールシェルフに「オーディオ再生」タブを追加
class VIEW3D_PT_CustomMenu(bpy.types.Panel):
    bl_label = "オーディオ再生"          # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "オーディオ再生"       # タブを開いたメニューのヘッダーに表示される文字列


    # メニューの描画処理
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # ファイルブラウザを表示する
        layout.operator(ShowFileBrowser.bl_idname, text="オーディオファイルを選択")


def init_props():
    sc = bpy.context.Scene


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル3-6: アドオン「サンプル3-6」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-6: アドオン「サンプル3-6」が無効化されました。")


if __name__ == "__main__":
    register()
