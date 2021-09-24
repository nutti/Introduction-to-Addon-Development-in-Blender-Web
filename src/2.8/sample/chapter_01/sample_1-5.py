bl_info = {
    "name": "サンプル 1-5: 何もしないアドオン",
    "author": "ぬっち（Nutti）",
    "version": (3, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "アドオンの有効化と無効化を試すためのサンプル",
    "warning": "",
    "support": "TESTING",
    "doc_url": "",
    "tracker_url": "",
    "category": "Object"
}


def register():
    print("サンプル 1-5: アドオン『サンプル 1-5』が有効化されました。")


def unregister():
    print("サンプル 1-5: アドオン『サンプル 1-5』が無効化されました。")


if __name__ == "__main__":
    register()
