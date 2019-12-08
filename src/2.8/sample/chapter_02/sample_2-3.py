import bpy
from bpy.props import FloatProperty, EnumProperty


bl_info = {
    "name": "サンプル2-3: オブジェクトを並進移動するアドオン（移動量、移動軸 任意指定版）",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "3Dビューポート > オブジェクト",
    "description": "オブジェクトを並進移動するサンプルアドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


# オブジェクトを並進移動するオペレータ
class SAMPLE23_OT_TranslateObject(bpy.types.Operator):

    bl_idname = "object.sample23_translate_object"
    bl_label = "並進移動"
    bl_description = "アクティブなオブジェクトを並進移動します"
    bl_options = {'REGISTER', 'UNDO'}

# @include-source start [prop_translate_object]
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
# @include-source end [prop_translate_object]

    # メニューを実行したときに呼ばれるメソッド
    def execute(self, context):
        active_obj = context.active_object
# @include-source start [access_to_prop]
        if self.axis == 'X':
            active_obj.location[0] += self.amount
        elif self.axis == 'Y':
            active_obj.location[1] += self.amount
        elif self.axis == 'Z':
            active_obj.location[2] += self.amount
# @include-source end [access_to_prop]
        self.report({'INFO'}, "サンプル2-3: 『{}』を{}軸方向へ {} 並進移動しました。"
                              .format(active_obj.name, self.axis, self.amount))
        print("サンプル2-3: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(SAMPLE23_OT_TranslateObject.bl_idname)


classes = [
    SAMPLE23_OT_TranslateObject,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル2-3: アドオン『サンプル2-3』が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル2-3: アドオン『サンプル2-3』が無効化されました。")


if __name__ == "__main__":
    register()
