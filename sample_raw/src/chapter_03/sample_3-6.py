import bpy
from bpy.props import StringProperty, FloatProperty, BoolProperty
//! [import_aud]
import aud
//! [import_aud]
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
    "category": "3D View"
}


class AudioDevice():
    device = None       # サウンドデバイス
    factory = None      # サウンドファクトリ
    handle = None       # サウンドハンドラ
    filename = None     # 開いているオーディオファイル名
    paused = False      # 再生を一時停止している場合はTrue
    running = False     # 再生処理が行われた場合はTrue（再生時間超過時にもTrueとなり、明に停止した時にFalseとなる）


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


# ピッチを設定
def set_pitch(self, value):
    self['paf_pitch'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.pitch = value


# 設定されているピッチを取得
def get_pitch(self):
    return self.get('paf_pitch', 1.0)


# ループ再生するか否かを設定
def set_loop(self, value):
    self['paf_loop'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.loop_count = -1 if value is False else 0


# ループ再生か否かを取得
def get_loop(self):
    return self.get('paf_loop', False)


# 再生時間更新
class AudioPlayTimeUpdater(bpy.types.Operator):
    bl_idname = "ui.audio_play_time_updater"
    bl_label = "オーディオ再生時間更新処理"

    timer = None        # タイマ


    def __init__(self):
        self.timer = None


    def modal(self, context, event):
        if event.type == 'TIMER':
//! [redraw_toolself]
            # ツール・シェルフ部のみ更新
            for region in context.area.regions:
                if region.type == 'TOOLS':
                    region.tag_redraw()
//! [redraw_toolself]

        # 再生停止時には更新処理を中断
        if AudioDevice.handle is None or (AudioDevice.running and AudioDevice.handle.status == aud.AUD_STATUS_INVALID):
            if self.timer is not None:
                # タイマの登録を解除
                context.window_manager.event_timer_remove(self.timer)
                self.timer = None
                return {'FINISHED'}

        return {'PASS_THROUGH'}


    def execute(self, context):
        # 再生時間更新処理開始
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

    filepath = StringProperty(subtype="FILE_PATH")      # ファイルパス
    filename = StringProperty()     # ファイル名
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
        AudioDevice.filename = self.filename
        AudioDevice.pause = False

        # 再生中なら停止し、サウンドハンドラを破棄
        if AudioDevice.handle is not None:
            AudioDevice.handle.stop()
            AudioDevice.handle = None

        return {'FINISHED'}
//! [select_audio_file_execute]


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

//! [play_audio_file]
    def execute(self, context):
        sc = context.scene

        if AudioDevice.handle is not None:
            return {'CANCELLED'}

        # 再生
        AudioDevice.handle = AudioDevice.device.play(AudioDevice.factory)
        AudioDevice.handle.volume = sc.paf_volume
        AudioDevice.handle.pitch = sc.paf_pitch
        AudioDevice.handle.loop_count = sc.paf_loop
        AudioDevice.paused = False
        AudioDevice.running = True

        # 再生時間更新処理開始
        bpy.ops.ui.audio_play_time_updater()

        return {'FINISHED'}
//! [play_audio_file]


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
        AudioDevice.running = False

        return {'FINISHED'}


# ツールシェルフに「オーディオ再生」タブを追加
class VIEW3D_PT_PlayAudioFileMenu(bpy.types.Panel):
    bl_label = "オーディオ再生"          # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "オーディオ再生"       # タブを開いたメニューのヘッダーに表示される文字列


    # 作業時間を表示用にフォーマット化
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

        # 選択中のオーディオファイルを表示
        if AudioDevice.filename is not None:
            layout.label(AudioDevice.filename)

//! [destroy_sound_handle]
        # 1度再生されたが、再生を終わっている状態
        if AudioDevice.handle is not None and AudioDevice.handle.status == aud.AUD_STATUS_INVALID:
            AudioDevice.handle = None
//! [destroy_sound_handle]

        if AudioDevice.handle is not None:
//! [display_play_time]
            layout.label("再生時間： " + self.__make_time_fmt(AudioDevice.handle.position))
//! [display_play_time]
            layout.prop(sc, "paf_loop", text="ループ再生")

            # 再生中または一時停止中の状態
            if AudioDevice.handle.status == aud.AUD_STATUS_PLAYING:
                # 一時停止の時
                if AudioDevice.paused:
                    row = layout.row()
                    row.operator(ResumeAudioFile.bl_idname, text="再生再開", icon='PLAY')
                    row.operator(StopAudioFile.bl_idname, text="停止", icon='X')
                # 再生中の時
                else:
                    row = layout.row()
                    row.operator(PauseAudioFile.bl_idname, text="一時停止", icon='PAUSE')
                    row.operator(StopAudioFile.bl_idname, text="停止", icon='X')
            # 再生を停止した状態
            elif AudioDevice.handle.status == aud.AUD_STATUS_STOPPED:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')
            # 再生時間を超過して再生が停止された状態
            elif AudioDevice.running:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')

            row = layout.row()
            row.prop(sc, "paf_volume", text="音量")
            row.prop(sc, "paf_pitch", text="ピッチ")
        else:
            # 選択中のオーディオファイルがない
            if AudioDevice.filename is not None:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')


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
    sc.paf_pitch = FloatProperty(
        name="ピッチ",
        description="ピッチを調整します",
        default=1.0,
        max=3.0,
        min=0.0,
        get=get_pitch,
        set=set_pitch
    )
    sc.paf_loop = BoolProperty(
        name="ループ再生",
        description="ループ再生します",
        default=False,
        get=get_loop,
        set=set_loop
    )


# プロパティを削除
def clear_props():
    sc = bpy.types.Scene
    del sc.paf_volume
    del sc.paf_pitch
    del sc.paf_loop


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
