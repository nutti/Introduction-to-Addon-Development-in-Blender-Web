import bpy
from bpy.props import FloatProperty, EnumProperty


bl_info = {
    "name": "サンプル 3-6: オブジェクトを並進移動するアドオン⑥",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > オブジェクト, Ctrl + Alt + R",
    "description": "アクティブなオブジェクトを並進移動するサンプルアドオン（多言語対応）",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

addon_keymaps = []
# 翻訳辞書
translation_dict = {
    "en_US": {
        ("*", "Translate object"): "Translate",
        ("*", "Translate active object"): "Translate active object",
        ("*", "Translation axis"): "Translation axis",
        ("*", "Set translation axis"): "Set translation axis",
        ("*", "X-axis"): "X-axis",
        ("*", "Translate along X-axis"): "Translate along X-axis",
        ("*", "Y-axis"): "Y-axis",
        ("*", "Translate along Y-axis"): "Translate along Y-axis",
        ("*", "Z-axis"): "Z-axis",
        ("*", "Translate along Z-axis"): "Translate along Z-axis",
        ("*", "Translation amount"): "Translation amount",
        ("*", "Set translation amount"): "Set translation amount",
        ("*", "Sample 3-6: Translated object '%s' (Axis: %s, Amount: %f)"): "Sample 3-6: Translated object '%s' (Axis: %s, Amount: %f)",
        ("*", "Sample 3-6: Executed operator '%s'"): "Sample 3-6: Executed operator '%s'",
        ("*", "Sample 3-6: Add-on 'Sample 3-6' is enabled"): "Sample 3-6: Add-on 'Sample 3-6' is enabled",
        ("*", "Sample 3-6: Add-on 'Sample 3-6' is disabled"): "Sample 3-6: Add-on 'Sample 3-6' is disabled",
    },
    "ja_JP": {
        ("*", "Translate object"): "並進移動",
        ("*", "Translate active object"): "アクティブなオブジェクトを並進移動します",
        ("*", "Translation axis"): "移動軸",
        ("*", "Set translation axis"): "移動軸を設定します",
        ("*", "X-axis"): "X軸",
        ("*", "Translate along X-axis"): "X軸に沿って並進移動します",
        ("*", "Y-axis"): "Y軸",
        ("*", "Translate along Y-axis"): "Y軸に沿って並進移動します",
        ("*", "Z-axis"): "Z軸",
        ("*", "Translate along Z-axis"): "Z軸に沿って並進移動します",
        ("*", "Translation amount"): "移動量",
        ("*", "Set translation amount"): "移動量を設定します",
        ("*", "Sample 3-6: Translated object '%s' (Axis: %s, Amount: %f)"): "サンプル 3-6: 『%s』を%s軸方向へ %f 並進移動しました。",
        ("*", "Sample 3-6: Executed operator '%s'"): "サンプル 3-6: オペレータ『%s』が実行されました。",
        ("*", "Sample 3-6: Add-on 'Sample 3-6' is enabled"): "サンプル 3-6: アドオン『サンプル 3-6』が有効化されました。",
        ("*", "Sample 3-6: Add-on 'Sample 3-6' is disabled"): "サンプル 3-6: アドオン『サンプル 3-6』が無効化されました。",
    }
}

# オブジェクトを並進移動するオペレータ
class SAMPLE36_OT_TranslateObject(bpy.types.Operator):

    bl_idname = "object.sample36_translate_object"
    bl_label = "Translate"
    bl_description = bpy.app.translations.pgettext("Translate active object")
    bl_options = {'REGISTER', 'UNDO'}

    axis: EnumProperty(
        name=bpy.app.translations.pgettext("Translation axis"),
        description=bpy.app.translations.pgettext("Set translation axis"),
        default='X',
        items=[
            ('X', bpy.app.translations.pgettext("X-axis"),
             bpy.app.translations.pgettext("Translate along X-axis")),
            ('Y', bpy.app.translations.pgettext("Y-axis"),
             bpy.app.translations.pgettext("Translate along Y-axis")),
            ('Z', bpy.app.translations.pgettext("Z-axis"),
             bpy.app.translations.pgettext("Translate along Z-axis")),
        ]
    )
    amount: FloatProperty(
        name=bpy.app.translations.pgettext("Translation amount"),
        description=bpy.app.translations.pgettext("Set translation amount"),
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
        self.report(
            {'INFO'},
            bpy.app.translations.pgettext_iface(
                "Sample 3-6: Translated object '%s' (Axis: %s, Amount: %f)"
            )
            % (active_obj.name, self.axis, self.amount)
        )
# @include-source start [translation_func_with_format]
        print(
            bpy.app.translations.pgettext_iface(
                "Sample 3-6: Executed operator '%s'"
            )
            % (self.bl_idname)
        )
# @include-source end [translation_func_with_format]

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SAMPLE36_OT_TranslateObject.bl_idname,
                         text=bpy.app.translations.pgettext("Translate object"))


classes = [
    SAMPLE36_OT_TranslateObject,
]


def register_shortcut():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')
        kmi = km.keymap_items.new(
            idname=SAMPLE36_OT_TranslateObject.bl_idname,
            type='T',
            value='PRESS',
            shift=False,
            ctrl=True,
            alt=True
        )
        addon_keymaps.append((km, kmi))


def unregister_shortcut():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    register_shortcut()
# @include-source start [register_dict]
    # 翻訳辞書の登録
    bpy.app.translations.register(__name__, translation_dict)
# @include-source end [register_dict]
# @include-source start [translation_func]
    print(bpy.app.translations.pgettext(
        "Sample 3-6: Add-on 'Sample 3-6' is enabled"
    ))
# @include-source end [translation_func]


def unregister():
# @include-source start [unregister_dict]
    # 翻訳辞書の登録解除
    bpy.app.translations.unregister(__name__)
# @include-source end [unregister_dict]
    unregister_shortcut()
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print(bpy.app.translations.pgettext(
        "Sample 3-6: Add-on 'Sample 3-6' is disabled"
    ))


if __name__ == "__main__":
    register()
