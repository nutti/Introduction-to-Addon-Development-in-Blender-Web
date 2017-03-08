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


if __name__ == "__main__":
    suite_1_5 = unittest.defaultTestLoader.loadTestsFromTestCase(Test_Sample_1_5)
    unittest.TextTestRunner().run(suite_1_5)

    suite_2_1 = unittest.defaultTestLoader.loadTestsFromTestCase(Test_Sample_2_1)
    unittest.TextTestRunner().run(suite_2_1)
