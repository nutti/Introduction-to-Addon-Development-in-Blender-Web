# coding:utf-8

import bpy
import unittest
from io import StringIO
import sys


def check_addon_enabled(mod):
    result = bpy.ops.wm.addon_enable(module=mod)
    assert (result == {'FINISHED'}), "Failed to enable add-on %s" % (mod)
    assert (mod in bpy.context.user_preferences.addons.keys()), "Failed to enable add-on %s" % (mod)


def check_addon_disabled(mod):
    result = bpy.ops.wm.addon_disable(module=mod)
    assert (result == {'FINISHED'}), "Failed to disable add-on %s" % (mod)
    assert (not mod in bpy.context.user_preferences.addons.keys()), "Failed to disable add-on %s" % (mod)


def operator_exists(idname):
    try:
        from bpy.ops import op_as_string
        op_as_string(idname)
        return True
    except:
        return False


def menu_exists(idname):
    return idname in dir(bpy.types)


def get_invoke_context(area_type, region_type):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == area_type:
                break
        else:
            continue
        for region in area.regions:
            if region.type == region_type:
                break
        else:
            continue
        return {'window': window, 'screen': screen, 'area': area, 'region': region}


class StdoutCapture():
    def setUp(self):
        self.capture = StringIO()
        sys.stdout = self.capture

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def get_captured_value(self):
        return self.capture.getValue()


class TestBase(unittest.TestCase):

    modname = None
    idname = []

    @classmethod
    def setUpClass(cls):
        try:
            bpy.ops.wm.read_factory_settings()
            check_addon_enabled(cls.modname)
            for op in cls.idname:
                if op[0] == 'OPERATOR':
                    assert operator_exists(op[1]), "Operator %s does not exist" % (op[1])
                elif op[0] == 'MENU':
                    assert menu_exists(op[1]), "Menu %s does not exist" % (op[1])
        except AssertionError as e:
            print(e)
            sys.exit(1)

    @classmethod
    def tearDownClass(cls):
        try:
            check_addon_disabled(cls.modname)
            for op in cls.idname:
                if op[0] == 'OPERATOR':
                    assert not operator_exists(op[1]), "Operator %s exists" % (op[1])
                elif op[0] == 'MENU':
                    assert not menu_exists(op[1]), "Menu %s exists" % (op[1])
        except AssertionError as e:
            print(e)
            sys.exit(1)


class Test_Sample_1_5(TestBase):

    modname = 'sample_1-5'
    idname = []

    def test_addon(self):
        pass


class Test_Sample_2_1(TestBase):

    modname = 'sample_2-1'
    idname = [
        ('OPERATOR', 'object.create_object')
    ]

    def test_addon(self):
        result = bpy.ops.object.create_object()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_2(TestBase):

    modname = 'sample_2-2'
    idname = [
        ('OPERATOR', 'object.enlarge_object'),
        ('OPERATOR', 'object.reduce_object')
    ]

    def test_addon(self):
        result = bpy.ops.object.enlarge_object()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.reduce_object()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_3(TestBase):

    modname = 'sample_2-3'
    idname = [
        ('OPERATOR', 'object.enlarge_object_2'),
        ('OPERATOR', 'object.reduce_object_2')
    ]

    def test_addon(self):
        result = bpy.ops.object.enlarge_object_2(magnification=2.0)
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.reduce_object_2(reduction=0.2)
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_4(TestBase):

    modname = 'sample_2-4'
    idname = [
        ('OPERATOR', 'object.replicate_object')
    ]

    def test_addon(self):
        bpy.data.objects['Cube'].select = True
        result = bpy.ops.object.replicate_object(
            location='ORIGIN',
            scale=(2.0, 1.5, 1.0),
            rotation=(0.1, -0.1, 0.5),
            offset=(10.0, -20.0, 15.0)
        )
        self.assertSetEqual(result, {'FINISHED'})
        self.assertIsNotNone(bpy.data.objects['Cube.001'])



class Test_Sample_2_5(TestBase):

    modname = 'sample_2-5'
    idname = [
        ('MENU', 'object.replicate_object_menu'),
        ('OPERATOR', 'object.replicate_object')
    ]

    def test_addon_registered(self):
        result = bpy.ops.object.replicate_object(
            location='ORIGIN',
            scale=(2.0, 1.5, 1.0),
            rotation=(0.1, -0.1, 0.5),
            offset=(10.0, -20.0, 15.0),
            src_obj_name='Cube'
        )
        self.assertSetEqual(result, {'FINISHED'})
        self.assertIsNotNone(bpy.data.objects['Cube.001'])


class Test_Sample_2_5_alt(TestBase):

    modname = 'sample_2-5_alt'
    idname = [
        ('MENU', 'object.replicate_object_menu'),
        ('MENU', 'object.replicate_object_sub_menu'),
        ('OPERATOR', 'object.replicate_object')
    ]

    def test_addon(self):
        result = bpy.ops.object.replicate_object(
            location='ORIGIN',
            scale=(2.0, 1.5, 1.0),
            rotation=(0.1, -0.1, 0.5),
            offset=(10.0, -20.0, 15.0),
            src_obj_name='Cube'
        )
        self.assertSetEqual(result, {'FINISHED'})
        self.assertIsNotNone(bpy.data.objects['Cube.001'])


class Test_Sample_2_6(TestBase):

    modname = 'sample_2-6'
    idname = [
        ('OPERATOR', 'object.replicate_object')
    ]

    def test_addon(self):
        bpy.data.objects['Cube'].select = True
        result = bpy.ops.object.replicate_object(
            location='ORIGIN',
            scale=(2.0, 1.5, 1.0),
            rotation=(0.1, -0.1, 0.5),
            offset=(10.0, -20.0, 15.0)
        )
        self.assertSetEqual(result, {'FINISHED'})
        self.assertIsNotNone(bpy.data.objects['Cube.001'])


class Test_Sample_2_7(TestBase):

    modname = 'sample_2-7'
    idname = [
        ('OPERATOR', 'object.enlarge_object'),
        ('OPERATOR', 'object.reduce_object')
    ]

    def test_addon(self):
        result = bpy.ops.object.enlarge_object()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.reduce_object()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_8(TestBase):

    modname = 'sample_2-8'
    idname = [
        ('OPERATOR', 'object.null_operation')
    ]

    def test_addon(self):
        result = bpy.ops.object.null_operation()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_9(TestBase):

    modname = 'sample_2-9'
    idname = [
        ('OPERATOR', 'object.null_operation'),
        ('MENU', 'object.null_operation_menu'),
        ('OPERATOR', 'object.show_all_icons')
    ]

    def test_addon(self):
        result = bpy.ops.object.null_operation()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.show_all_icons(num_column=3)
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_10(TestBase):

    modname = 'sample_2-10'
    idname = [
        ('OPERATOR', 'object.show_popup_message'),
        ('OPERATOR', 'object.show_dialog_menu'),
        ('OPERATOR', 'object.show_file_browser'),
        ('OPERATOR', 'object.show_confirm_popup'),
        ('OPERATOR', 'object.show_property_popup'),
        ('OPERATOR', 'object.show_search_popup')
    ]

    def test_addon(self):
        result = bpy.ops.object.show_popup_message()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.show_dialog_menu(
            prop_int=10,
            prop_float=0.5,
            prop_enum='ITEM_2',
            prop_floatv=(0.1, 0.3, 0.0)
        )
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.show_file_browser(
            filepath="/hoge/test.dat",
            filename="test.dat",
            directory="/hoge"
        )
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.show_confirm_popup()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.show_property_popup(
            prop_int=10,
            prop_float=0.5,
            prop_enum='ITEM_2',
            prop_floatv=(0.1, 0.3, 0.0)
        )
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.show_search_popup(item='ITEM_2')
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_3_1(TestBase):

    modname = 'sample_3-1'
    idname = [
        ('OPERATOR', 'mesh.delete_face_by_rclick')
    ]

    def test_addon(self):
        context = get_invoke_context('VIEW_3D', 'WINDOW')
        result = bpy.ops.mesh.delete_face_by_rclick(context, 'INVOKE_DEFAULT')
        self.assertSetEqual(result, {'PASS_THROUGH'})
        result = bpy.ops.mesh.delete_face_by_rclick(context, 'INVOKE_DEFAULT')
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_3_2(TestBase):

    modname = 'sample_3-2'
    idname = [
        ('OPERATOR', 'object.translate_object_mode')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_3(TestBase):

    modname = 'sample_3-3'
    idname = [
        ('OPERATOR', 'object.move_object_interval')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_4(TestBase):

    modname = 'sample_3-4'
    idname = [
        ('OPERATOR', 'view_3d.render_figure')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_5(TestBase):

    modname = 'sample_3-5'
    idname = [
        ('OPERATOR', 'view_3d.render_text')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_6(TestBase):

    modname = 'sample_3-6'
    idname = [
        ('OPERATOR', 'view_3d.select_audio_file'),
        ('OPERATOR', 'view_3d.stop_audio_file')
    ]

    def test_addon(self):
        result = bpy.ops.view_3d.select_audio_file(filepath='test.wav')
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.view_3d.stop_audio_file()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_3_7(TestBase):

    modname = 'sample_3-7'
    idname = [
        ('OPERATOR', 'mesh.delete_face_by_rclick')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_8(TestBase):

    modname = 'sample_3-8'
    idname = [
        ('OPERATOR', 'view3d.draw_object_trajectory')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_9(TestBase):

    modname = 'sample_3-9'
    idname = [
        ('OPERATOR', 'view3d.select_object_on_mouseover')
    ]

    def test_addon(self):
        pass


class Test_Sample_3_10(TestBase):

    modname = 'sample_3-10'
    idname = [
        ('OPERATOR', 'object.translate_object_mode')
    ]

    def test_addon(self):
        pass


class Test_Sample_4_5(TestBase):

    modname = 'sample_4-5.testee'
    idname = [
        ('OPERATOR', 'object.test_ops_1'),
        ('OPERATOR', 'object.test_ops_2')
    ]

    def test_addon(self):
        pass


class Test_Sample_5_1(TestBase):

    modname = 'sample_5-1'
    idname = [
        ('OPERATOR', 'mesh.special_object_edit_mode')
    ]

    def test_addon(self):
        pass


class Test_Sample_5_2(TestBase):

    modname = 'sample_5-2'
    idname = [
        ('OPERATOR', 'ui.calculate_working_hours')
    ]

    def test_addon(self):
        pass


class Test_Sample_5_3(TestBase):

    modname = 'sample_5-3'
    idname = [
        ('OPERATOR', 'ui.audio_play_time_updater'),
        ('OPERATOR', 'ui.select_audio_file'),
        ('OPERATOR', 'ui.play_audio_file'),
        ('OPERATOR', 'ui.resume_audio_file'),
        ('OPERATOR', 'ui.pause_audio_file'),
        ('OPERATOR', 'ui.stop_audio_file')
    ]

    def test_addon(self):
        result = bpy.ops.ui.select_audio_file(filepath='test.wav')
        self.assertSetEqual(result, {'FINISHED'})
        # result = bpy.ops.ui.play_audio_file()
        # self.assertSetEqual(result, {'FINISHED'})
        # result = bpy.ops.ui.pause_audio_file()
        # self.assertSetEqual(result, {'FINISHED'})
        # result = bpy.ops.ui.resume_audio_file()
        # self.assertSetEqual(result, {'FINISHED'})
        # result = bpy.ops.ui.stop_audio_file()
        # self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_5_4(TestBase):

    modname = 'sample_5-4'
    idname = [
        ('OPERATOR', 'view3d.show_object_name')
    ]

    def test_addon(self):
        pass


if __name__ == "__main__":
    test_cases = [
        Test_Sample_1_5,
        Test_Sample_2_1,
        Test_Sample_2_2,
        Test_Sample_2_3,
        Test_Sample_2_4,
        Test_Sample_2_5,
        Test_Sample_2_5_alt,
        Test_Sample_2_6,
        Test_Sample_2_7,
        Test_Sample_2_8,
        Test_Sample_2_9,
        Test_Sample_2_10,
        Test_Sample_3_1,
        Test_Sample_3_2,
        Test_Sample_3_3,
        Test_Sample_3_4,
        Test_Sample_3_5,
        Test_Sample_3_6,
        Test_Sample_3_7,
        Test_Sample_3_8,
        Test_Sample_3_9,
        Test_Sample_3_10,
        Test_Sample_5_1,
        Test_Sample_5_2,
        Test_Sample_5_3,
        Test_Sample_5_4,

    ]

    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTest(unittest.makeSuite(case))
    ret = unittest.TextTestRunner().run(suite).wasSuccessful()
    sys.exit(not ret)
