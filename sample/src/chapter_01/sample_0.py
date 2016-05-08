import bpy

bl_info = {
	"name": "サンプル0: 何もしないアドオン",
	"author": "Nutti",
	"version": (1, 0),
	"blender": (2, 75, 0),
	"location": "",
	"description": "アドオンの有効化と無効化を試すためのサンプル",
	"warning": "",
	"support": "TESTING",
	"wiki_url": "",
	"tracker_url": "",
	"category": "Object"
}


def register():
	print("アドオンが有効化されました。")


def unregister():
	print("アドオンが無効化されました。")


if __name__ == "__main__":
	register()
