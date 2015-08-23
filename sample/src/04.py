import bpy

bl_info = {
	"name": "サンプル 0: 何もしないアドオン",
	"author": "Nutti",
	"version": (1, 0),
	"blender": (2, 75, 0),
	"location": "Object > サンプル 0: 何もしないアドオン",
	"description": "アドオンのインストールとアンインストールを試すためのサンプル",
	"warning": "",
	"support": "TESTING",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Object"
}


def register():
	print("アドオンがインストールされました。")


def unregister():
	print("アドオンがアンインストールされました。")


if __name__ == "__main__":
	register()

