import bpy


bl_info = {
    "name": "デバッグテスト用のアドオン2",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > 追加 > メッシュ",
    "description": "アドオン『BreakPoint』を用いたデバッグテスト用アドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

//! [short_call]
# ブレークポイント関数
breakpoint = bpy.types.bp.bp
//! [short_call]


class DebugTestOps2(bpy.types.Operator):

    bl_idname = "object.debug_test_2"
    bl_label = "デバッグのテスト2"
    bl_description = "デバッグのテストを実行する"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        debug_var = 10.0
        debug_var = debug_var + 30.0
        debug_var = debug_var + 9.5
//! [set_breakpoint]
        # ブレークポイント
        breakpoint(locals(), debug_var)
//! [set_breakpoint]

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(DebugTestOps2.bl_idname)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(menu_fn)


def unregister():
    bpy.types.INFO_MT_mesh_add.remove(menu_fn)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
