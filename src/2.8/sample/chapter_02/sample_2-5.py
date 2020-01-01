import bpy
from bpy.props import FloatProperty, EnumProperty


bl_info = {
    "name": "サンプル 2-5: オブジェクトを並進移動するアドオン④",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > オブジェクト, Ctrl + Alt + R",
    "description": "アクティブなオブジェクトを並進移動するサンプルアドオン（ショートカットあり）",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

addon_keymaps = []          # 登録したショートカットキー一覧


# オブジェクトを並進移動するオペレータ
class SAMPLE25_OT_TranslateObject(bpy.types.Operator):

    bl_idname = "object.sample25_translate_object"
    bl_label = "並進移動"
    bl_description = "アクティブなオブジェクトを並進移動します"
    bl_options = {'REGISTER', 'UNDO'}

    axis: EnumProperty(
        name="移動軸",
        description="移動軸を設定します",
        default='X',
        items=[
            ('X', "X軸", "X軸に沿って並進移動します"),
            ('Y', "Y軸", "Y軸に沿って並進移動します"),
            ('Z', "Z軸", "Z軸に沿って並進移動します"),
        ]
    )
    amount: FloatProperty(
        name="移動量",
        description="移動量を設定します",
        default=1.0,
    )

    def execute(self, context):
        active_obj = context.active_object
        if self.axis == 'X':
            active_obj.location[0] += self.amount
        elif self.axis == 'Y':
            active_obj.location[1] += self.amount
        elif self.axis == 'Z':
            active_obj.location[2] += self.amount
        self.report({'INFO'}, "サンプル 2-5: 『{}』を{}軸方向へ {} 並進移動しました。"
                              .format(active_obj.name, self.axis, self.amount))
        print("サンプル 2-5: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SAMPLE25_OT_TranslateObject.bl_idname)


classes = [
    SAMPLE25_OT_TranslateObject,
]


# @include-source start [register_shortcut]
def register_shortcut():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # [3Dビューポート] スペースのショートカットキーとして登録
        km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')
        # ショートカットキーの登録
        kmi = km.keymap_items.new(
            idname=SAMPLE25_OT_TranslateObject.bl_idname,
            type='T',
            value='PRESS',
            shift=False,
            ctrl=True,
            alt=True
        )
        # ショートカットキー一覧に登録
        addon_keymaps.append((km, kmi))
# @include-source end [register_shortcut]


# @include-source start [unregister_shortcut]
def unregister_shortcut():
    for km, kmi in addon_keymaps:
        # ショートカットキーの登録解除
        km.keymap_items.remove(kmi)
    # ショートカットキー一覧をクリア
    addon_keymaps.clear()
# @include-source end [unregister_shortcut]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    register_shortcut()
    print("サンプル 2-5: アドオン『サンプル 2-5』が有効化されました。")


def unregister():
    unregister_shortcut()
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 2-5: アドオン『サンプル 2-5』が無効化されました。")


if __name__ == "__main__":
    register()
