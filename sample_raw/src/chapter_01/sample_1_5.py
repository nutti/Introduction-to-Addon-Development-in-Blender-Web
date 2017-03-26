bl_info = {
    "name": "サンプル1-5: 何もしないアドオン",
    "author": "Nutti",
    "version": (2, 0),
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
    print("サンプル1-5: アドオン「サンプル1-5」が有効化されました。")


def unregister():
    print("サンプル1-5: アドオン「サンプル1-5」が無効化されました。")


if __name__ == "__main__":
    register()
