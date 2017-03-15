import sys


DEBUGGING = True     # デバッグ有効化
PYDEV_SRC_DIR = "(eclipseディレクトリへのパス)/plugins/org.python.pydev_XXXXX/pysrc"    # PyDevのパス（環境に応じて書き換えが必要）


def start_debug():
    if DEBUGGING is True:
        if PYDEV_SRC_DIR not in sys.path:
            sys.path.append(PYDEV_SRC_DIR)
            import pydevd
            pydevd.settrace()
            print("started blender add-on debugging...")
