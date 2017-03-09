import bpy
import unittest


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


class Test_Sample_1_5(unittest.TestCase):
    def test_addon_enabled(self):
        check_addon_enabled(self, 'sample_1-5')
        check_addon_disabled(self, 'sample_1-5')


class Test_Sample_2_1(unittest.TestCase):
    def test_addon_enabled(self):
        check_addon_enabled(self, 'sample_2-1')
        check_addon_disabled(self, 'sample_2-1')

    def test_addon_registered(self):
        check_addon_enabled(self, 'sample_2-1')
        self.assertTrue(operator_exists("object.create_object"))
        result = bpy.ops.object.create_object()
        self.assertSetEqual(result, {'FINISHED'})
        check_addon_disabled(self, 'sample_2-1')
        self.assertFalse(operator_exists("object.create_object"))


class Test_Sample_2_2(unittest.TestCase):
    def test_addon_enabled(self):
        check_addon_enabled(self, 'sample_2-2')
        check_addon_disabled(self, 'sample_2-2')

    def test_addon_registered(self):
        check_addon_enabled(self, 'sample_2-2')
        self.assertTrue(operator_exists("object.enlarge_object"))
        result = bpy.ops.object.enlarge_object()
        self.assertSetEqual(result, {'FINISHED'})
        self.assertTrue(operator_exists("object.reduce_object"))
        result = bpy.ops.object.reduce_object()
        self.assertSetEqual(result, {'FINISHED'})
        check_addon_disabled(self, 'sample_2-2')
        self.assertFalse(operator_exists("object.enlarge_object"))
        self.assertFalse(operator_exists("object.reduce_object"))


class Test_Sample_2_3(unittest.TestCase):
    def test_addon_enabled(self):
        check_addon_enabled(self, 'sample_2-3')
        check_addon_disabled(self, 'sample_2-3')

    def test_addon_registered(self):
        check_addon_enabled(self, 'sample_2-3')
        self.assertTrue(operator_exists("object.enlarge_object_2"))
        result = bpy.ops.object.enlarge_object_2(magnification=2.0)
        self.assertSetEqual(result, {'FINISHED'})
        self.assertTrue(operator_exists("object.reduce_object_2"))
        result = bpy.ops.object.reduce_object_2(reduction=0.2)
        self.assertSetEqual(result, {'FINISHED'})
        check_addon_disabled(self, 'sample_2-3')
        self.assertFalse(operator_exists("object.enlarge_object_2"))
        self.assertFalse(operator_exists("object.reduce_object_2"))


class Test_Sample_2_4(unittest.TestCase):
    def test_addon_enabled(self):
        check_addon_enabled(self, 'sample_2-4')
        check_addon_disabled(self, 'sample_2-4')

    def test_addon_registered(self):
        check_addon_enabled(self, 'sample_2-4')
        self.assertTrue(operator_exists("object.replicate_object"))
        bpy.data.objects['Cube'].select = True
        result = bpy.ops.object.replicate_object(
            location='ORIGIN',
            scale=(2.0, 1.5, 1.0),
            rotation=(0.1, -0.1, 0.5),
            offset=(10.0, -20.0, 15.0)
        )
        self.assertSetEqual(result, {'FINISHED'})
        self.assertIsNotNone(bpy.data.objects['Cube.001'])
        check_addon_disabled(self, 'sample_2-4')
        self.assertFalse(operator_exists("object.replicate_object"))


class Test_Sample_2_5(unittest.TestCase):
    def test_addon_enabled(self):
        check_addon_enabled(self, 'sample_2-5')
        check_addon_disabled(self, 'sample_2-5')

    def test_addon_registered(self):
        check_addon_enabled(self, 'sample_2-5')
        self.assertTrue(operator_exists("object.replicate_object"))
        result = bpy.ops.object.replicate_object(
            location='ORIGIN',
            scale=(2.0, 1.5, 1.0),
            rotation=(0.1, -0.1, 0.5),
            offset=(10.0, -20.0, 15.0),
            src_obj_name='Cube'
        )
        self.assertSetEqual(result, {'FINISHED'})
        self.assertIsNotNone(bpy.data.objects['Cube.001'])
        check_addon_disabled(self, 'sample_2-5')
        self.assertFalse(operator_exists("object.replicate_object"))


if __name__ == "__main__":
    test_cases = [
        Test_Sample_1_5,
        Test_Sample_2_1,
        Test_Sample_2_2,
        Test_Sample_2_3,
        Test_Sample_2_4,
        Test_Sample_2_5
    ]

    for case in test_cases:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(case)
        unittest.TextTestRunner().run(suite)
