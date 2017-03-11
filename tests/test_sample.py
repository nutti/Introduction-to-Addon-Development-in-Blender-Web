# coding:utf-8

import bpy
import unittest
from io import StringIO
import sys


def check_addon_enabled(self, mod):
    result = bpy.ops.wm.addon_enable(module=mod)
    self.assertSetEqual(result, {'FINISHED'})
    self.assertTrue(mod in bpy.context.user_preferences.addons.keys())


def check_addon_disabled(self, mod):
    result = bpy.ops.wm.addon_disable(module=mod)
    self.assertSetEqual(result, {'FINISHED'})
    self.assertFalse(mod in bpy.context.user_preferences.addons.keys())


def operator_exists(idname):
    try:
        from bpy.ops import op_as_string
        op_as_string(idname)
        return True
    except:
        return False


def menu_exists(idname):
    return idname in dir(bpy.types)


class StdoutCapture():
    def setUp(self):
        self.capture = StringIO()
        sys.stdout = self.capture

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def get_captured_value(self):
        return self.capture.getValue()


class TestBase(unittest.TestCase):

    def setUp(self):
        bpy.ops.wm.read_factory_settings()
        check_addon_enabled(self, self.mod_name())
        for op in self.idname_lists():
            if op[0] == 'OPERATOR':
                self.assertTrue(operator_exists(op[1]))
            elif op[0] == 'MENU':
                self.assertTrue(menu_exists(op[1]))

    def tearDown(self):
        check_addon_disabled(self, self.mod_name())
        for op in self.idname_lists():
            if op[0] == 'OPERATOR':
                self.assertFalse(operator_exists(op[1]))
            elif op[0] == 'MENU':
                self.assertFalse(menu_exists(op[1]))

    def mod_name(self):
        return None

    def idname_lists(self):
        return []


class Test_Sample_1_5(TestBase):

    def mod_name(self):
        return 'sample_1-5'

    def test_addon(self):
        pass


class Test_Sample_2_1(TestBase):

    def mod_name(self):
        return 'sample_2-1'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.create_object')
        ]

    def test_addon(self):
        result = bpy.ops.object.create_object()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_2(TestBase):

    def mod_name(self):
        return 'sample_2-2'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.enlarge_object'),
            ('OPERATOR', 'object.reduce_object')
        ]

    def test_addon(self):
        result = bpy.ops.object.enlarge_object()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.reduce_object()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_3(TestBase):

    def mod_name(self):
        return 'sample_2-3'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.enlarge_object_2'),
            ('OPERATOR', 'object.reduce_object_2')
        ]

    def test_addon(self):
        result = bpy.ops.object.enlarge_object_2(magnification=2.0)
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.reduce_object_2(reduction=0.2)
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_4(TestBase):

    def mod_name(self):
        return 'sample_2-4'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_2-5'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_2-5_alt'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_2-6'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_2-7'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.enlarge_object'),
            ('OPERATOR', 'object.reduce_object')
        ]

    def test_addon(self):
        result = bpy.ops.object.enlarge_object()
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.object.reduce_object()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_8(TestBase):

    def mod_name(self):
        return 'sample_2-8'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.null_operation')
        ]

    def test_addon(self):
        result = bpy.ops.object.null_operation()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_8(TestBase):

    def mod_name(self):
        return 'sample_2-8'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.null_operation')
        ]

    def test_addon(self):
        result = bpy.ops.object.null_operation()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_2_9(TestBase):

    def mod_name(self):
        return 'sample_2-9'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_2-10'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_3-1'

    def idname_lists(self):
        return [
            ('OPERATOR', 'mesh.delete_face_by_rclick')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_2(TestBase):

    def mod_name(self):
        return 'sample_3-2'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.translate_object_mode')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_3(TestBase):

    def mod_name(self):
        return 'sample_3-3'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.move_object_interval')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_4(TestBase):

    def mod_name(self):
        return 'sample_3-4'

    def idname_lists(self):
        return [
            ('OPERATOR', 'view_3d.render_figure')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_5(TestBase):

    def mod_name(self):
        return 'sample_3-5'

    def idname_lists(self):
        return [
            ('OPERATOR', 'view_3d.render_text')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_6(TestBase):

    def mod_name(self):
        return 'sample_3-6'

    def idname_lists(self):
        return [
            ('OPERATOR', 'view_3d.select_audio_file'),
            ('OPERATOR', 'view_3d.stop_audio_file')
        ]

    def test_addon(self):
        result = bpy.ops.view_3d.select_audio_file(filepath='test.wav')
        self.assertSetEqual(result, {'FINISHED'})
        result = bpy.ops.view_3d.stop_audio_file()
        self.assertSetEqual(result, {'FINISHED'})


class Test_Sample_3_7(TestBase):

    def mod_name(self):
        return 'sample_3-7'

    def idname_lists(self):
        return [
            ('OPERATOR', 'mesh.delete_face_by_rclick')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_8(TestBase):

    def mod_name(self):
        return 'sample_3-8'

    def idname_lists(self):
        return [
            ('OPERATOR', 'view3d.draw_object_trajectory')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_9(TestBase):

    def mod_name(self):
        return 'sample_3-9'

    def idname_lists(self):
        return [
            ('OPERATOR', 'view3d.select_object_on_mouseover')
        ]

    def test_addon(self):
        pass


class Test_Sample_3_10(TestBase):

    def mod_name(self):
        return 'sample_3-10'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.translate_object_mode')
        ]

    def test_addon(self):
        pass


class Test_Sample_4_5(TestBase):

    def mod_name(self):
        return 'sample_4-5.testee'

    def idname_lists(self):
        return [
            ('OPERATOR', 'object.test_ops_1'),
            ('OPERATOR', 'object.test_ops_2')
        ]

    def test_addon(self):
        pass


class Test_Sample_5_1(TestBase):

    def mod_name(self):
        return 'sample_5-1'

    def idname_lists(self):
        return [
            ('OPERATOR', 'mesh.special_object_edit_mode')
        ]

    def test_addon(self):
        pass


class Test_Sample_5_2(TestBase):

    def mod_name(self):
        return 'sample_5-2'

    def idname_lists(self):
        return [
            ('OPERATOR', 'ui.calculate_working_hours')
        ]

    def test_addon(self):
        pass


class Test_Sample_5_3(TestBase):

    def mod_name(self):
        return 'sample_5-3'

    def idname_lists(self):
        return [
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

    def mod_name(self):
        return 'sample_5-4'

    def idname_lists(self):
        return [
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
