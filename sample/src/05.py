```py:05.py
import bpy   # Blenderがアドオン開発者に対して用意しているAPIを利用するために必要

# アドオンに関する情報
bl_info = {
	"name": "サンプル 1: オブジェクトを生成するアドオン",               # アドオン名
	"author": "Nutti",                                             # 作者
	"version": (1, 0),                                             # アドオンのバージョン
	"blender": (2, 75, 0),                                         # アドオンが動作するBlender本体の"最古"のバージョン
	"location": "Object > サンプル 1: オブジェクトを生成するアドオン",  # アドオンの場所
	"description": "オブジェクトを生成するサンプルアドオン",            # アドオンのコメント
	"warning": "",                                                 # バグや問題発生時に表示させる文字列
	"support": "TESTING",                                          # アドオンのサポートレベル
	"wiki_url": "",                                                # アドオンに関連する情報が得られるURL
	"tracker_url": "",                                             # アドオンのサポートサイトのURL
	"category": "Object"                                           # アドオンのカテゴリ
}


# オブジェクト（ICO球）を生成するオペレーション
class CreateObject(bpy.types.Operator):

	bl_idname = "object.create_object"       # Blender内部で使用するID
	bl_label = "球"                          # オペレーションのラベル（メニュー画面に表示される文字）
	bl_description = "ICO球を追加します"       # オペレーションの説明（メニュー画面に表示される説明文）
	bl_options = {'REGISTER', 'UNDO'}        # オペレーションへ追加するオプション

    # メニューを実行した時に呼ばれる関数
	def execute(self, context):
        # ICO球を追加
		bpy.ops.mesh.primitive_ico_sphere_add()
		# ICO球が生成されたことをコンソール・ウィンドウへ表示
		print("サンプル1: 3DビューにICO球を生成しました。")
		# 処理が正常に終了したことを通知する
		return {'FINISHED'}


# メニューを構築する関数
def menu_fn(self, context):
	# セパレータを追加
	self.layout.separator()
	# オペレーションをメニューに追加
	self.layout.operator(CreateObject.bl_idname)


# アドオン有効化時の処理
def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_mesh_add.append(menu_fn)
	# コンソールへ指定した文字列を表示
	print("サンプル 1: アドオン「サンプル1」が有効化されました。")


# アドオン無効化時の処理
def unregister():
	bpy.types.INFO_MT_mesh_add.remove(menu_fn)
	bpy.utils.unregister_module(__name__)
	# コンソールへ指定した文字列を表示
	print("サンプル 1: アドオン「サンプル 1」が無効化されました。")


# メイン関数
if __name__ == "__main__":
	register()

```
