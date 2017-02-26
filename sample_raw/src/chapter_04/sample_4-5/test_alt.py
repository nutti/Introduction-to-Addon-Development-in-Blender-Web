import bpy
import sys


if __name__ == "__main__":
    try:
        # bl_name = object.test_ops_1 のテスト
        assert bpy.ops.object.test_ops_1 != None, "test_ops_1が有効化されていません"
        result = bpy.ops.object.test_ops_1()
        assert result == {'FINISHED'}, "test_ops_1にエラーが存在します"
        # bl_name = object.test_ops_2 のテスト
        assert bpy.ops.object.test_ops_2 != None, "test_ops_2が有効化されていません"
        bpy.ops.object.select_all(action='DESELECT')    # $オブジェクトの選択を解除
        bpy.data.objects['Cube'].select = True          # $オブジェクト名が「Cube」のオブジェクトを削除
        bpy.ops.object.delete()                         # $選択中のオブジェクトを削除
        result = bpy.ops.object.test_ops_2()
        assert result == {'FINISHED'}, "test_ops_2にエラーが存在します"       # オブジェクト「Cube」は削除済みのためエラーとなる
    # テスト失敗時の処理
    except AssertionError as e:
        print(e)        # テストが失敗した原因（assert文の第2引数）を表示
        sys.exit(1)     # Blenderを復帰値1で終了する
    # スクリプトの実行が正常に終了すると、Blenderは復帰値0で終了する
