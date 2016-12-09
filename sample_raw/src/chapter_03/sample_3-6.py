import bpy
from bpy.props import StringProperty, FloatProperty, FloatVectorProperty
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

    @staticmethod
    def set_volume(self, value):
        self['paf_volume'] = value
        if PlayAudioFile.handle is not None:
            PlayAudioFile.handle.volume = value

    @staticmethod
    def get_volume(self):
        return self.get('paf_volume', 0.5)

    @staticmethod
    def set_pitch(self, value):
        self['paf_pitch'] = value
        if PlayAudioFile.handle is not None:
            PlayAudioFile.handle.pitch = value

    @staticmethod
    def get_pitch(self):
        return self.get('paf_pitch', 0.5)


    def execute(self, context):
        sc = context.scene

        if PlayAudioFile.device is None:
            PlayAudioFile.device = aud.device()

        PlayAudioFile.factory = aud.Factory(self.filepath)
        PlayAudioFile.factory.volume(sc.paf_volume)

        # 再生中なら停止する
        if PlayAudioFile.handle is not None:
            PlayAudioFile.handle.stop()
        # 再生
        PlayAudioFile.handle = PlayAudioFile.device.play(PlayAudioFile.factory)

        return {'FINISHED'}


    def invoke(self, context, event):
        wm = context.window_manager
        # ファイルブラウザ表示
        wm.fileselect_add(self)

        return {'RUNNING_MODAL'}


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

        # ファイルブラウザを表示する
        layout.operator(PlayAudioFile.bl_idname, text="オーディオファイルを選択")
        layout.prop(sc, "paf_volume", text="音量")
        layout.prop(sc, "paf_pitch", text="ピッチ")
        layout.prop(sc, "paf_location", text="位置")
        layout.prop(sc, "paf_orientation", text="向き")

        if PlayAudioFile.handle is not None:
            if PlayAudioFile.handle.status == aud.AUD_STATUS_PLAYING:
            elif PlayAudioFile.handle.status == aud.AUD_STATUS_STOPPED:
            elif PlayAudioFile.handle.status == aud.AUD_STATUS_PAUSED:


def init_props():
    sc = bpy.types.Scene
    sc.paf_volume = FloatProperty(
        name="音量",
        description="音量を調整します",
        default=0.5,
        max=1.0,
        min=0.0,
        get=PlayAudioFile.get_volume,
        set=PlayAudioFile.set_volume
    )
    sc.paf_pitch = FloatProperty(
        name="ピッチ",
        description="ピッチを調整します",
        default=0.5,
        max=1.0,
        min=0.0,
        get=PlayAudioFile.get_pitch,
        set=PlayAudioFile.set_pitch
    )
    sc.paf_location = FloatVectorProperty(
        name="位置",
        description="音源の位置を設定します",
        size = 3,
        default = (0.0, 0.0, 0.0)
    )
    sc.paf_orientation = FloatVectorProperty(
        name="向き",
        description="音源の向きを設定します",
        size = 4,
        default = (0.0, 0.0, 0.0, 0.0)
    )


def clear_props():
    pass


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
