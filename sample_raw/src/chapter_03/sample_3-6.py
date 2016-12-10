import bpy
from bpy.props import StringProperty, FloatProperty, FloatVectorProperty
import aud
import math

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


class AudioDevice():
    device = None
    factory = None
    handle = None
    filename = None
    paused = False
    timer = None


def set_volume(self, value):
    self['paf_volume'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.volume = value


def get_volume(self):
    return self.get('paf_volume', 0.5)


def set_pitch(self, value):
    self['paf_pitch'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.pitch = value


def get_pitch(self):
    return self.get('paf_pitch', 1.0)


def set_location(self, value):
    self['paf_location'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.location = value


def get_location(self):
    return self.get('paf_location', (0.0, 0.0, 0.0))


def set_orientation(self, value):
    self['paf_orientation'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.orientation = value


def get_orientation(self):
    return self.get('paf_orientation', (0.0, 0.0, 0.0, 0.0))


class AudioPlayTimeUpdater(bpy.types.Operator):
    bl_idname = "ui.audio_play_time_updater"
    bl_label = "オーディオ再生時間更新処理"

    timer = None


    def __init__(self):
        self.timer = None


    def modal(self, context, event):
        if event.type == 'TIMER':
            for region in context.area.regions:
                if region.type == 'TOOLS':
                    region.tag_redraw()

        if AudioDevice.handle is None:
            if self.timer is not None:
                # タイマの登録を解除
                context.window_manager.event_timer_remove(self.timer)
                self.timer = None
                return {'FINISHED'}

        return {'PASS_THROUGH'}


    def execute(self, context):
        if self.timer is None:
            self.timer = context.window_manager.event_timer_add(
                0.10, context.window)
            context.window_manager.modal_handler_add(self)

        return {'RUNNING_MODAL'}


# オーディオファイルの選択
class SelectAudioFile(bpy.types.Operator):
    bl_idname = "ui.select_audio_file"
    bl_label = "オーディオファイルの選択"
    bl_description = "再生するオーディオファイルを選択します"

    filepath = StringProperty(subtype="FILE_PATH")
    filename = StringProperty()

    def execute(self, context):
        sc = context.scene

        if AudioDevice.device is None:
            AudioDevice.device = aud.device()
            AudioDevice.device.distance_model = aud.AUD_DISTANCE_MODEL_LINEAR
            AudioDevice.device.listener_location = (0.0, 0.0, 0.0)
            AudioDevice.device.listener_orientation = (0.0, 0.0, 0.0, 0.0)

        AudioDevice.factory = aud.Factory(self.filepath)
        AudioDevice.filename = self.filename
        AudioDevice.pause = False

        # 再生中なら停止する
        if AudioDevice.handle is not None:
            AudioDevice.handle.stop()
            AudioDevice.handle = None

        return {'FINISHED'}


    def invoke(self, context, event):
        wm = context.window_manager
        # ファイルブラウザ表示
        wm.fileselect_add(self)

        return {'RUNNING_MODAL'}


# オーディオファイルの再生
class PlayAudioFile(bpy.types.Operator):
    bl_idname = "ui.play_audio_file"
    bl_label = "オーディオファイルの再生"
    bl_description = "オーディオファイルを再生します"

    def execute(self, context):
        sc = context.scene

        if AudioDevice.handle is not None:
            return {'CANCELLED'}

        # 再生
        AudioDevice.handle = AudioDevice.device.play(AudioDevice.factory)
        AudioDevice.handle.volume = sc.paf_volume
        AudioDevice.handle.pitch = sc.paf_pitch
        AudioDevice.handle.location = sc.paf_location
        AudioDevice.handle.orientation = sc.paf_orientation
        AudioDevice.handle.relative = False
        AudioDevice.handle.distance_maximum = 100
        AudioDevice.handle.distance_reference = 1
        AudioDevice.handle.attenuation = 12

        AudioDevice.paused = False
        bpy.ops.ui.audio_play_time_updater()

        return {'FINISHED'}


# オーディオファイルの再生再開
class ResumeAudioFile(bpy.types.Operator):
    bl_idname = "ui.resume_audio_file"
    bl_label = "オーディオファイルの再生再開"
    bl_description = "オーディオファイルの再生を再開します"

    def execute(self, context):
        sc = context.scene

        if AudioDevice.handle is None:
            return {'CANCELLED'}

        # 再生再開
        ret = AudioDevice.handle.resume()
        if ret:
            AudioDevice.paused = False

        return {'FINISHED'}


# 再生一時停止
class PauseAudioFile(bpy.types.Operator):
    bl_idname = "ui.pause_audio_file"
    bl_label = "オーディオファイルの再生を一時停止"
    bl_description = "オーディオファイルの再生を一時停止します"

    def execute(self, context):
        sc = context.scene

        if AudioDevice.handle is None:
            return {'CANCELLED'}

        # 一時停止
        ret = AudioDevice.handle.pause()
        if ret:
            AudioDevice.paused = True

        return {'FINISHED'}


# 再生停止
class StopAudioFile(bpy.types.Operator):
    bl_idname = "ui.stop_audio_file"
    bl_label = "オーディオファイルの再生を停止"
    bl_description = "オーディオファイルの再生を停止します"

    def execute(self, context):
        sc = context.scene

        if AudioDevice.handle is None:
            return {'CANCELLED'}

        # 再生停止
        AudioDevice.handle.stop()
        AudioDevice.handle = None
        AudioDevice.paused = False

        return {'FINISHED'}


# ツールシェルフに「オーディオ再生」タブを追加
class VIEW3D_PT_PlayAudioFileMenu(bpy.types.Panel):
    bl_label = "オーディオ再生"          # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "オーディオ再生"       # タブを開いたメニューのヘッダーに表示される文字列


    def __make_time_fmt(self, time):
        sec = math.floor(time) % 60                     # 秒
        minute = math.floor(time / 60) % 60         # 分
        hour = math.floor(time / (60 * 60))           # 時

        return "%d:%02d:%02d" % (hour, minute, sec)


    # メニューの描画処理
    def draw(self, context):
        layout = self.layout
        sc = context.scene

        # ファイルブラウザを表示する
        layout.operator(SelectAudioFile.bl_idname, text="オーディオファイルを選択")

        if AudioDevice.filename is not None:
            # 選択中のオーディオファイル
            layout.label(AudioDevice.filename)

        if AudioDevice.handle is not None:
            layout.label("再生時間： " + self.__make_time_fmt(AudioDevice.handle.position))

            layout.prop(sc, "paf_volume", text="音量")
            layout.prop(sc, "paf_pitch", text="ピッチ")
            layout.prop(sc, "paf_location", text="位置")
            layout.prop(sc, "paf_orientation", text="向き")
            if AudioDevice.handle.status == aud.AUD_STATUS_PLAYING:
                if AudioDevice.paused:
                        layout.operator(ResumeAudioFile.bl_idname, text="再生再開", icon='PLAY')
                else:
                    layout.operator(PauseAudioFile.bl_idname, text="一時停止", icon='PAUSE')
                layout.operator(StopAudioFile.bl_idname, text="停止", icon='X')
            elif AudioDevice.handle.status == aud.AUD_STATUS_STOPPED:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')
        else:
            if AudioDevice.filename is not None:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')


def init_props():
    sc = bpy.types.Scene
    sc.paf_volume = FloatProperty(
        name="音量",
        description="音量を調整します",
        default=0.4,
        max=1.0,
        min=0.0,
        get=get_volume,
        set=set_volume
    )
    sc.paf_pitch = FloatProperty(
        name="ピッチ",
        description="ピッチを調整します",
        default=1.0,
        max=3.0,
        min=0.0,
        get=get_pitch,
        set=set_pitch
    )
    sc.paf_location = FloatVectorProperty(
        name="位置",
        description="音源の位置を設定します",
        size=3,
        default=(0.0, 0.0, 0.0),
        set=set_location,
        get=get_location
    )
    sc.paf_orientation = FloatVectorProperty(
        name="向き",
        description="音源の向きを設定します",
        size=4,
        default=(0.0, 0.0, 0.0, 0.0),
        set=set_orientation,
        get=get_orientation
    )


def clear_props():
    sc = bpy.types.Scene
    del sc.paf_volume
    del sc.paf_pitch
    del sc.paf_location
    del sc.paf_orientation


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
