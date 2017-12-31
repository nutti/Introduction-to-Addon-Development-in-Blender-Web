import bpy
import debug     # デバッグ実行するクリプトをimport


bl_info = {
    "name": "デバッグテスト用のアドオン",
    "author": "Nutti",
    "version": (2, 0),
    "blender": (2, 75, 0),
    "location": "3Dビュー > 追加 > メッシュ",
    "description": "アドオンのデバッグテスト用アドオン",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}


class DebugTestOps(bpy.types.Operator):

    bl_idname = "object.debug_test"
    bl_label = "デバッグのテスト"
    bl_description = "デバッグのテストを実行する"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        debug_var = 10.0
        debug_var = debug_var + 30.0
        debug_var = debug_var + 9.5
        print("debug_var=%f" % (debug_var))

        return {'FINISHED'}


def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(DebugTestOps.bl_idname)


def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_mesh_add.append(menu_fn)
    # デバッグ開始
    debug.start_debug()


def unregister():
    bpy.types.INFO_MT_mesh_add.remove(menu_fn)
    bpy.utils.unregister_module(__name__)


if __name__ == "__main__":
    register()
