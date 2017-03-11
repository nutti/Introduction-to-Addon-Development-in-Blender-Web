import bpy
from bpy.props import StringProperty, FloatProperty
//! [import_aud]
import aud
//! [import_aud]


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
    "category": "3D View"
}


class AudioDevice():

    device = None       # サウンドデバイス
    factory = None      # サウンドファクトリ
    handle = None       # サウンドハンドラ


//! [set_volume]
# 音量を設定
def set_volume(self, value):
    self['paf_volume'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.volume = value
//! [set_volume]


//! [get_volume]
# 設定されている音量を取得
def get_volume(self):
    return self.get('paf_volume', 0.5)
//! [get_volume]


# オーディオファイルの選択
class SelectAudioFile(bpy.types.Operator):

    bl_idname = "view_3d.select_audio_file"
    bl_label = "オーディオファイルの選択"
    bl_description = "再生するオーディオファイルを選択します"

    filepath = StringProperty(subtype="FILE_PATH")      # ファイルパス
//! [filter_glob]
    # 検索フィルタ
    filter_glob = StringProperty(
        default="*.wav;*.mp3",
        options={'HIDDEN'}
    )
//! [filter_glob]

//! [select_audio_file_execute]
    def execute(self, context):
        sc = context.scene

        # 初回時のみサウンドデバイスを作成
        if AudioDevice.device is None:
            AudioDevice.device = aud.device()
        # サウンドファクトリを作成
        AudioDevice.factory = aud.Factory(self.filepath)
        # オーディオファイルを再生
        AudioDevice.handle = AudioDevice.device.play(AudioDevice.factory)
        AudioDevice.handle.volume = sc.paf_volume

        return {'FINISHED'}
//! [select_audio_file_execute]

    def invoke(self, context, event):
        wm = context.window_manager
        # ファイルブラウザ表示
        wm.fileselect_add(self)

        return {'RUNNING_MODAL'}


# 再生停止
class StopAudioFile(bpy.types.Operator):

    bl_idname = "view_3d.stop_audio_file"
    bl_label = "オーディオファイルの再生を停止"
    bl_description = "オーディオファイルの再生を停止します"

//! [stop_audio_file]
    def execute(self, context):
        if AudioDevice.handle is None:
            return {'CANCELLED'}
        # 再生停止
        AudioDevice.handle.stop()

        return {'FINISHED'}
//! [stop_audio_file]


# ツールシェルフに「オーディオ再生」タブを追加
class VIEW3D_PT_PlayAudioFileMenu(bpy.types.Panel):

    bl_label = "オーディオ再生"          # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "オーディオ再生"       # タブを開いたメニューのヘッダーに表示される文字列

    # メニューの描画処理
    def draw(self, context):
        layout = self.layout
        sc = context.scene

        if AudioDevice.handle is not None:
//! [check_play_status]
            # 再生中または一時停止中の状態
            if AudioDevice.handle.status:
                layout.operator(StopAudioFile.bl_idname, text="停止", icon='X')
            # 再生を停止した状態
            else:
                layout.operator(SelectAudioFile.bl_idname, text="オーディオファイルを選択", icon='PLAY')
//! [check_play_status]
        else:
            # ファイルブラウザを表示する
            layout.operator(SelectAudioFile.bl_idname, text="オーディオファイルを選択", icon='PLAY')
        layout.prop(sc, "paf_volume", text="音量")


# プロパティを初期化
def init_props():
    sc = bpy.types.Scene
//! [prop_volume]
    sc.paf_volume = FloatProperty(
        name="音量",
        description="音量を調整します",
        default=0.4,
        max=1.0,
        min=0.0,
        get=get_volume,
        set=set_volume
    )
//! [prop_volume]


# プロパティを削除
def clear_props():
    sc = bpy.types.Scene
    del sc.paf_volume


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
