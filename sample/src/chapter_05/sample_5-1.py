import bpy
from bpy.props import BoolProperty, PointerProperty, EnumProperty
import enum
from mathutils import Vector

bl_info = {
    "name": "サンプル3-9: キーボードのキー入力に応じてオブジェクトを変形する（アドオン設定活用版）",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > プロパティパネル > 特殊オブジェクト編集モード",
    "description": "オブジェクトの並進移動、拡大・縮小、回転をキーボードから行うアドオン（アドオン設定活用版）",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

# Enumクラスを用いた列挙値の定義
EditType = enum.Enum('EditType', 'NONE TRANSLATE SCALE ROTATE')
EditAxis = enum.Enum('EditAxis', 'NONE X Y Z')
EditOption = enum.Enum('EditOption', 'NONE + -')


# プロパティ
class SOEM_Properties(bpy.types.PropertyGroup):
    is_special_mode = BoolProperty(
        name = "特殊オブジェクト編集モード中",
        description = "特殊オブジェクト編集モード中か？",
        default = False)


# 特殊オブジェクト編集モード時の処理
class SpecialObjectEditMode(bpy.types.Operator):
    bl_idname = "mesh.special_object_edit_mode"
    bl_label = "特殊オブジェクト編集モード"
    bl_description = "特殊オブジェクト編集モードへ移行します"

    # インスタンス変数の設定
    def __init__(self):
        self.edit_type = EditType['NONE']
        self.edit_axis = EditAxis['NONE']
        self.edit_opt = EditOption['NONE']

    # 発生したイベントをもとに、次の状態を返却するプライベートなメンバ関数
    # 本来であれば本処理を工夫し、本書のコラムに書いたバグを無くすべきだが、
    # 処理を単純化するためにバグをそのまま残している
    # 引数ev_value：イベントの値
    # 引数on：'PRESS'イベント発生時の状態遷移先
    # 引数off：'PRESS'以外のイベント発生時の状態遷移先
    def __change_state(self, ev_value, on, off):
        if ev_value == 'PRESS':
            return on
        elif ev_value == 'RELEASE':
            return off
        return off

    def modal(self, context, event):
        props = context.scene.soem_props
        prefs = context.user_preferences.addons[__name__].preferences

        # 3Dビューの画面を更新
        if context.area:
            context.area.tag_redraw()

        # キーボードのQキーが押された場合は、特殊オブジェクト編集モードを終了
        if event.type == 'Q' and event.value == 'PRESS':
            props.is_special_mode = False
            print("サンプル3-9: 通常モードへ移行しました。")
            return {'FINISHED'}

        # 処理するキーイベントのリスト
        # 要素1：キーの識別子
        # 要素2：オブジェクトの変形処理の状態を格納するためのインスタンス変数名
        # 要素3：'PRESS'イベント発生時の状態遷移先
        # 要素4：'PRESS'以外のイベント発生時の状態遷移先
        ev_key_list = (
            # 編集タイプ（並進移動、拡大・縮小、回転）
            (prefs.translate, "edit_type", EditType['TRANSLATE'], EditType['NONE']),
            (prefs.scale, "edit_type", EditType['SCALE'], EditType['NONE']),
            (prefs.rotate, "edit_type", EditType['ROTATE'], EditType['NONE']),
            # 軸（X軸、Y軸、Z軸）
            (prefs.x_axis, "edit_axis", EditAxis['X'], EditAxis['NONE']),
            (prefs.y_axis, "edit_axis", EditAxis['Y'], EditAxis['NONE']),
            (prefs.z_axis, "edit_axis", EditAxis['Z'], EditAxis['NONE']),
            # 方向（正方向、負方向）
            (prefs.increment, "edit_opt", EditOption['+'], EditOption['NONE']),
            (prefs.decrement, "edit_opt", EditOption['-'], EditOption['NONE'])
        )
        # キーボードのキーイベントが発生しているかを確認し、現在の状態を更新
        for ev_key in ev_key_list:
            if event.type == ev_key[0]:
                # self.__dict__には、クラスのインスタンス変数の一覧が、ディクショナリ型
                # （キー：値）＝（インスタンス変数名：インスタンス変数への参照）として
                # 保存されている
                self.__dict__[ev_key[1]] = self.__change_state(
                    event.value, ev_key[2], ev_key[3])

        # オブジェクト変換処理のための条件が揃っていない時は何もしない
        if self.edit_type == EditType['NONE']:
            return {'RUNNING_MODAL'}
        if self.edit_axis == EditAxis['NONE']:
            return {'RUNNING_MODAL'}
        if self.edit_opt == EditOption['NONE']:
            return {'RUNNING_MODAL'}

        # オブジェクトに変形処理を適用
        # 移動
        if self.edit_type == EditType['TRANSLATE']:
            value = Vector((0.0, 0.0, 0.0))
            for i, axis in enumerate(['X', 'Y', 'Z']):
                if self.edit_axis == EditAxis[axis]:
                    # オブジェクトを正方向に1.0だけ移動
                    if self.edit_opt == EditOption['+']:
                        value[i] = 1.0
                    # オブジェクトを負方向に-1.0だけ移動
                    elif self.edit_opt == EditOption['-']:
                        value[i] = -1.0
            # bpy.ops.transform.translate()：選択中のオブジェクトを並進移動する
            # 引数value：並進移動量
            bpy.ops.transform.translate(value=value)
        # 拡大・縮小
        if self.edit_type == EditType['SCALE']:
            value = Vector((1.0, 1.0, 1.0))
            for i, axis in enumerate(['X', 'Y', 'Z']):
                if self.edit_axis == EditAxis[axis]:
                    # オブジェクトのサイズを1.1倍に拡大
                    if self.edit_opt == EditOption['+']:
                        value[i] = 1.1
                    # オブジェクトのサイズを0.9倍に縮小
                    elif self.edit_opt == EditOption['-']:
                        value[i] = 0.9
            # bpy.ops.transform.resize()：選択中のオブジェクトを拡大・縮小する
            # 引数value：拡大・縮小量
            bpy.ops.transform.resize(value=value)
        # 回転
        elif self.edit_type == EditType['ROTATE']:
            # 回転軸を設定
            rot_axis = Vector((0.0, 0.0, 0.0))
            for i, axis in enumerate(['X', 'Y', 'Z']):
                if self.edit_axis == EditAxis[axis]:
                    rot_axis[i] = 1.0
            # 回転方向を設定
            # 正方向に0.1（ラジアン）回転
            if self.edit_opt == EditOption['+']:
                value = 0.1
            # 負方向に-0.1（ラジアン）回転
            elif self.edit_opt == EditOption['-']:
                value = -0.1
            # bpy.ops.transform.rotate()：選択中のオブジェクトを回転する
            # 引数value：回転量
            # 引数rot_axis：回転軸
            bpy.ops.transform.rotate(value=value, axis=rot_axis)

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        props = context.scene.soem_props
        if context.area.type == 'VIEW_3D':
            # 開始ボタンが押された時の処理
            if props.is_special_mode is False:
                props.is_special_mode = True
                # modal処理クラスを追加
                context.window_manager.modal_handler_add(self)
                print("サンプル3-9: 特殊オブジェクト編集モードへ移行しました。")
                return {'RUNNING_MODAL'}
            # 終了ボタンが押された時の処理
            else:
                props.is_special_mode = False
                print("サンプル3-9: 通常モードへ移行しました。")
                return {'FINISHED'}
        else:
            return {'CANCELLED'}


# UI
class OBJECT_PT_SOEM(bpy.types.Panel):
    bl_label = "特殊オブジェクト編集モード"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = context.scene.soem_props
        # 開始/停止ボタンを追加
        if props.is_special_mode is False:
            layout.operator(SpecialObjectEditMode.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(SpecialObjectEditMode.bl_idname, text="終了", icon="PAUSE")


def key_pref_list(self, context):
    # キーの識別子
    key_id = [
            'ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT',
            'NINE', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'LEFT_CTRL', 'LEFT_ALT', 'LEFT_SHIFT', 'RIGHT_ALT', 'RIGHT_CTRL',
            'RIGHT_SHIFT', 'TAB', 'SPACE', 'BACK_SPACE', 'DEL', 'SEMI_COLON',
            'PERIOD', 'COMMA', 'QUOTE', 'MINUS', 'SLASH', 'BACK_SLASH', 'EQUAL',
            'LEFT_ARROW', 'DOWN_ARROW', 'RIGHT_ARROW', 'UP_ARROW'
    ]
    # 表示文字列（説明文を兼ねる）
    key_name = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "[C]", "[D]",
            "E", "F", "G", "H", "I", "J", "K", "L", "M", "[N]", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z", "[Left Ctrl]", "[Left Alt]",
            "[Left Shift]", "[Right Alt]", "[Right Ctrl]", "[Right Shift]",
            "[Tab]", "[Space]", "[Back Space]", "[Delete]", "[;]", "[.]", "[,]",
            "[`]", "[-]", "[/]", "[¥]", "[=]", "←", "↓", "→", "↑"
    ]

    return [(id, name, name, i) for i, (name, id) in enumerate(zip(key_name, key_id))]


def get_pref_translate(self):
    key_list = key_pref_list(self, None)
    return self.get('translate', [key[3] for key in key_list if key[0] == 'T'][0])


def set_pref_translate(self, value):
    self['translate'] = value


def get_pref_scale(self):
    key_list = key_pref_list(self, None)
    return self.get('scale', [key[3] for key in key_list if key[0] == 'S'][0])


def set_pref_scale(self, value):
    self['scale'] = value


def get_pref_rotate(self):
    key_list = key_pref_list(self, None)
    return self.get('rotate', [key[3] for key in key_list if key[0] == 'R'][0])


def set_pref_rotate(self, value):
    self['rotate'] = value


def get_pref_x_axis(self):
    key_list = key_pref_list(self, None)
    return self.get('x_axis', [key[3] for key in key_list if key[0] == 'X'][0])


def set_pref_x_axis(self, value):
    self['x_axis'] = value


def get_pref_y_axis(self):
    key_list = key_pref_list(self, None)
    return self.get('y_axis', [key[3] for key in key_list if key[0] == 'Y'][0])


def set_pref_y_axis(self, value):
    self['y_axis'] = value


def get_pref_z_axis(self):
    key_list = key_pref_list(self, None)
    return self.get('z_axis', [key[3] for key in key_list if key[0] == 'Z'][0])


def set_pref_z_axis(self, value):
    self['z_axis'] = value


def get_pref_increment(self):
    key_list = key_pref_list(self, None)
    return self.get('increment', [key[3] for key in key_list if key[0] == 'RIGHT_ARROW'][0])


def set_pref_increment(self, value):
    self['increment'] = value


def get_pref_decrement(self):
    key_list = key_pref_list(self, None)
    return self.get('decrement', [key[3] for key in key_list if key[0] == 'LEFT_ARROW'][0])


def set_pref_decrement(self, value):
    self['decrement'] = value


# アドオン設定
class SOEM_Preferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    translate = EnumProperty(
        name="Translate",
        description="並進移動の処理を行うキー",
        items=key_pref_list,
        get=get_pref_translate,
        set=set_pref_translate)
    scale = EnumProperty(
        name="Scale",
        description="拡大・縮小の処理を行うキー",
        items=key_pref_list,
        get=get_pref_scale,
        set=set_pref_scale)
    rotate = EnumProperty(
        name="Rotate",
        description="回転の処理を行うキー",
        items=key_pref_list,
        get=get_pref_rotate,
        set=set_pref_rotate)
    x_axis = EnumProperty(
        name="X軸",
        description="X軸に関する処理を行うキー",
        items=key_pref_list,
        get=get_pref_x_axis,
        set=set_pref_x_axis)
    y_axis = EnumProperty(
        name="Y軸",
        description="Y軸に関する処理を行うキー",
        items=key_pref_list,
        get=get_pref_y_axis,
        set=set_pref_y_axis)
    z_axis = EnumProperty(
        name="Z軸",
        description="Z軸に関する処理を行うキー",
        items=key_pref_list,
        get=get_pref_z_axis,
        set=set_pref_z_axis)
    increment = EnumProperty(
        name="+",
        description="インクリメント方向の操作を行うキー",
        items=key_pref_list,
        get=get_pref_increment,
        set=set_pref_increment)
    decrement = EnumProperty(
        name="-",
        description="デクリメント方向の操作を行うキー",
        items=key_pref_list,
        get=get_pref_decrement,
        set=set_pref_decrement)


    def draw(self, context):
        layout = self.layout

        layout.label("キー割り当て: ")
        row = layout.row()
        col = row.column()
        col.prop(self, 'translate')
        col.prop(self, "scale")
        col.prop(self, "rotate")
        col = row.column()
        col.prop(self, "x_axis")
        col.prop(self, "y_axis")
        col.prop(self, "z_axis")
        col = row.column()
        col.prop(self, "increment")
        col.prop(self, "decrement")


def register():
    bpy.utils.register_module(__name__)
    sc = bpy.types.Scene
    sc.soem_props = PointerProperty(
        name="プロパティ",
        description="本アドオンで利用するプロパティ一覧",
        type=SOEM_Properties)
    print("サンプル3-9: アドオン「サンプル3-9」が有効化されました。")


def unregister():
    del bpy.types.Scene.soem_props
    bpy.utils.unregister_module(__name__)
    print("サンプル3-9: アドオン「サンプル3-9」が無効化されました。")


if __name__ == "__main__":
    register()
