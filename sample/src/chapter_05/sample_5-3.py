import bpy
from bpy.props import StringProperty, FloatProperty, BoolProperty
import aud
import math

bl_info = {
    "name": "サンプル5-3: オーディオプレイヤー",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > ツール・シェルフ > オーディオプレイヤー",
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


# 音量を設定
def set_volume(self, value):
    self['ap_volume'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.volume = value


# 設定されている音量を取得
def get_volume(self):
    return self.get('ap_volume', 0.5)


# ピッチを設定
def set_pitch(self, value):
    self['ap_pitch'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.pitch = value


# 設定されているピッチを取得
def get_pitch(self):
    return self.get('ap_pitch', 1.0)


# ループ再生するか否かを設定
def set_loop(self, value):
    self['ap_loop'] = value
    if AudioDevice.handle is not None:
        AudioDevice.handle.loop_count = -1 if value is True else 0


# ループ再生か否かを取得
def get_loop(self):
    return self.get('ap_loop', False)


# 再生時間更新
class AudioPlayTimeUpdater(bpy.types.Operator):
    bl_idname = "ui.audio_play_time_updater"
    bl_label = "オーディオ再生時間更新処理"

    def __init__(self):
        self.__timer = None

    def modal(self, context, event):
        if event.type == 'TIMER':
            # ツール・シェルフ部のみ更新
            for region in context.area.regions:
                if region.type == 'TOOLS':
                    region.tag_redraw()

        # 再生停止時には更新処理を中断
        if AudioDevice.handle is None or not AudioDevice.handle.status:
            if self.__timer is not None:
                # タイマの登録を解除
                context.window_manager.event_timer_remove(self.__timer)
                self.__timer = None
                return {'FINISHED'}

        return {'PASS_THROUGH'}

    def execute(self, context):
        # 再生時間更新処理開始
        if self.__timer is None:
            self.__timer = context.window_manager.event_timer_add(
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
    # 検索フィルタ
    filter_glob = StringProperty(
        default="*.wav;*.mp3",
        options={'HIDDEN'})

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
        AudioDevice.handle.volume = sc.ap_volume
        AudioDevice.handle.pitch = sc.ap_pitch
        AudioDevice.handle.loop_count = sc.ap_loop
        AudioDevice.paused = False

        # 再生時間更新処理開始
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


# ツール・シェルフに「オーディオプレイヤー」タブを追加
class VIEW3D_PT_PlayAudioFileMenu(bpy.types.Panel):
    bl_label = "オーディオプレイヤー"          # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "オーディオプレイヤー"       # タブを開いたメニューのヘッダーに表示される文字列

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

        # 1度再生されたが、再生を終わっている状態
        if AudioDevice.handle is not None and not AudioDevice.handle.status:
            AudioDevice.handle = None

        if AudioDevice.handle is not None:
            layout.label("再生時間： " + self.__make_time_fmt(AudioDevice.handle.position))
            layout.prop(sc, "ap_loop", text="ループ再生")

            # 再生中または一時停止中の状態
            if AudioDevice.handle.status:
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
            # 再生を停止した状態または、再生時間を超過して再生が停止された状態
            else:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')

            row = layout.row()
            row.prop(sc, "ap_volume", text="音量")
            row.prop(sc, "ap_pitch", text="ピッチ")
        else:
            # 選択中のオーディオファイルがない
            if AudioDevice.filename is not None:
                layout.operator(PlayAudioFile.bl_idname, text="再生", icon='PLAY')


# プロパティを初期化
def init_props():
    sc = bpy.types.Scene
    sc.ap_volume = FloatProperty(
        name="音量",
        description="音量を調整します",
        default=0.4,
        max=1.0,
        min=0.0,
        get=get_volume,
        set=set_volume)
    sc.ap_pitch = FloatProperty(
        name="ピッチ",
        description="ピッチを調整します",
        default=1.0,
        max=3.0,
        min=0.0,
        get=get_pitch,
        set=set_pitch)
    sc.ap_loop = BoolProperty(
        name="ループ再生",
        description="ループ再生します",
        default=False,
        get=get_loop,
        set=set_loop)


# プロパティを削除
def clear_props():
    sc = bpy.types.Scene
    del sc.ap_volume
    del sc.ap_pitch
    del sc.ap_loop


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル5-3: アドオン「サンプル5-3」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル5-3: アドオン「サンプル5-3」が無効化されました。")


if __name__ == "__main__":
    register()
