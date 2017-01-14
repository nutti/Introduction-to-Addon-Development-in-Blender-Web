import bpy
from bpy.props import BoolProperty, PointerProperty
from mathutils import Vector
import math


bl_info = {
    "name": "サンプル3-3: メッシュ型のオブジェクトを一定間隔で動かす",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > 一定間隔でオブジェクトを移動",
    "description": "選択中のメッシュ型オブジェクトが一定間隔ごとに円を描くように移動するアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# プロパティ
class MOI_Properties(bpy.types.PropertyGroup):
    running = BoolProperty(
        name="一定間隔でオブジェクト移動中",
        description="一定間隔でオブジェクト移動中か？",
        default=False)


# オブジェクト移動の処理
class MoveObjectInterval(bpy.types.Operator):
    bl_idname = "object.move_object_interval"
    bl_label = "一定間隔でオブジェクトを移動"
    bl_description = "一定間隔でオブジェクトを移動します"


    def __init__(self):
        self.timer = None           # タイマのハンドラ
        self.count = 0.0             # タイマイベントが発生した回数
        self.orig_obj_loc = {}      # 初期のオブジェクトの位置


//! [add_timer]
    def __handle_add(self, context):
        if self.timer is None:
            # タイマを登録
            self.timer = context.window_manager.event_timer_add(
                0.1, context.window)
            # モーダルモードへの移行
            context.window_manager.modal_handler_add(self)
//! [add_timer]


//! [remove_timer]
    def __handle_remove(self, context):
        if self.timer is not None:
            # タイマの登録を解除
            context.window_manager.event_timer_remove(self.timer)
            self.timer = None
//! [remove_timer]


//! [update_object_location]
    # オブジェクトの位置を更新
    def __update_object_location(self, context):
        self.count = self.count + 1
        radius = 5.0                 # 回転半径
        angular_velocity = 3.0  # 角速度
        angle = angular_velocity * self.count * math.pi / 180
        for obj, loc in self.orig_obj_loc.items():
            obj.location = loc + Vector((radius * math.sin(angle), radius * math.cos(angle), 0.0))
//! [update_object_location]


    def modal(self, context, event):
        props = context.scene.moi_props

//! [handle_non_timer_event]
        # タイマイベント以外の場合は無視
        if event.type != 'TIMER':
            return {'PASS_THROUGH'}
//! [handle_non_timer_event]

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

//! [stop_moving_object]
        # オブジェクトの移動を停止
        if props.running is False:
            self.__handle_remove(context)
            # オブジェクトを初期の位置に移動する
            for obj, loc in self.orig_obj_loc.items():
                obj.location = loc
            return {'FINISHED'}
//! [stop_moving_object]

        # オブジェクトの位置を更新
        self.__update_object_location(context)

        return {'PASS_THROUGH'}


    def invoke(self, context, event):
        props = context.scene.moi_props
        if context.area.type == 'VIEW_3D':
//! [store_obj_loc]
            # 開始ボタンが押された時の処理
            if props.running is False:
                self.orig_obj_loc = {obj: obj.location.copy() for obj in bpy.data.objects if obj.type == 'MESH' and obj.select}
//! [store_obj_loc]
                props.running = True
                self.__handle_add(context)
                print("サンプル3-3: 一定間隔でオブジェクトが移動するようになります。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.running = False
                print("サンプル3-3: 一定間隔でオブジェクトが移動しなくなります。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_MOI(bpy.types.Panel):
    bl_label = "一定間隔でオブジェクトを移動"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


//! [poll]
    @classmethod
    def poll(cls, context):
        objs = [obj for obj in bpy.data.objects if obj.type == 'MESH' and obj.select and obj.mode == 'OBJECT']
        if len(objs) == 0:
            return False
        return True
//! [poll]


    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = sc.moi_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(MoveObjectInterval.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(MoveObjectInterval.bl_idname, text="終了", icon="PAUSE")


# プロパティの作成
def init_props():
    sc = bpy.types.Scene
    sc.moi_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=MOI_Properties)


# プロパティの削除
def clear_props():
    sc = bpy.types.Scene
    del sc.moi_props


def register():
    bpy.utils.register_module(__name__)
    init_props()
    print("サンプル3-3: アドオン「サンプル3-3」が有効化されました。")


def unregister():
    clear_props()
    bpy.utils.unregister_module(__name__)
    print("サンプル3-3: アドオン「サンプル3-3」が無効化されました。")


if __name__ == "__main__":
    register()
