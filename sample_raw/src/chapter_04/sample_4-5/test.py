import bpy

if __name__ == "__main__":
    # bl_name = object.test_ops_1 のテスト
    assert bpy.ops.object.test_ops_1 != None, "test_ops_1が有効化されていません"
    result = bpy.ops.object.test_ops_1()
    assert result == {'FINISHED'}, "test_ops_1にエラーが存在します"
    # bl_name = object.test_ops_2 のテスト
    assert bpy.ops.object.test_ops_2 != None, "test_ops_2が有効化されていません"
    result = bpy.ops.object.test_ops_2()
    assert result == {'FINISHED'}, "test_ops_2にエラーが存在します"
