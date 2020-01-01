import bpy
from bpy.props import StringProperty, FloatProperty, EnumProperty


bl_info = {
    "name": "サンプル 2-4: オブジェクトを並進移動するアドオン③",
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
class SAMPLE24_OT_TranslateObject(bpy.types.Operator):

    bl_idname = "object.sample24_translate_object"
    bl_label = "並進移動"
    bl_description = "オブジェクトを並進移動します"
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
# @include-source start [string_prop]
    obj_name: StringProperty(options={'HIDDEN'})
# @include-source end [string_prop]

    def execute(self, context):
        # 並進移動するオブジェクトを取得
        obj = bpy.data.objects[self.obj_name]
        if self.axis == 'X':
            obj.location[0] += self.amount
        elif self.axis == 'Y':
            obj.location[1] += self.amount
        elif self.axis == 'Z':
            obj.location[2] += self.amount
        self.report({'INFO'}, "サンプル 2-4: 『{}』を{}軸方向へ {} 並進移動しました。"
                              .format(obj.name, self.axis, self.amount))
        print("サンプル 2-4: オペレータ『{}』が実行されました。".format(self.bl_idname))

        return {'FINISHED'}


# @include-source start [menu_cls]
# メインメニュー
class SAMPLE24_MT_TranslateObject(bpy.types.Menu):

    bl_idname = "SAMPLE24_MT_TranslateObject"
    bl_label = "オブジェクトの並進移動"
    bl_description = "オブジェクトを並進移動します"

    def draw(self, context):
        layout = self.layout
        # サブメニューの登録
        # bpy.data.objects：オブジェクト一覧
        for o in bpy.data.objects:
            if o.type == 'MESH':
                ops = layout.operator(
                    SAMPLE24_OT_TranslateObject.bl_idname, text=o.name
                )
                ops.obj_name = o.name
# @include-source end [menu_cls]


# @include-source start [build_menu]
def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(SAMPLE24_MT_TranslateObject.bl_idname)
# @include-source end [build_menu]


classes = [
    SAMPLE24_OT_TranslateObject,
    SAMPLE24_MT_TranslateObject,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)
    print("サンプル 2-4: アドオン『サンプル 2-4』が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
    print("サンプル 2-4: アドオン『サンプル 2-4』が無効化されました。")


if __name__ == "__main__":
    register()
