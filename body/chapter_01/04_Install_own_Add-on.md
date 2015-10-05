# 1-4. 自作のアドオンをインストールしてみよう

アドオンの作り方の解説に移る前に、簡単なアドオンを作ってインストールしてみましょう。

## アドオンを作成する

コンソールからBlenderを起動し、 **テキストエディター** の下のメニューバーにある **新規** をクリックし、空のテキストを作成します。

![アドオン作成 手順1](https://dl.dropboxusercontent.com/s/6x7jkbaadtehb2e/blender_make_add-on_1.png "アドオン作成 手順1")

次に以下に示すソースコード全文を入力してください。空白は全て半角スペースにします。

```py3:04.py
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

```

![アドオン作成 手順2](https://dl.dropboxusercontent.com/s/t6agj2bu859vk1c/blender_make_add-on_2.png "アドオン作成 手順2")

入力が完了したら、メニューバーの **テキスト** > **名前つけて保存** を実行します。

![アドオン作成 手順3](https://dl.dropboxusercontent.com/s/cbwyg0yebb8loww/blender_make_add-on_3.png "アドオン作成 手順3")

保存先に **04.py** という名前で保存します。
[2節](02_Use_Blender_Add-on.md)のアドオンインストールの解説でも書きましたが、保存先はOSごとに異なりますので注意してください。

|OS|保存先|
|--|--|
|Windows|```C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons```|
|Mac|```/Users/<ログインユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons```|
|Linux|```/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons```|

![アドオン作成 手順4](https://dl.dropboxusercontent.com/s/z9ibf7qz2t1jlj7/blender_make_add-on_4.png "アドオン作成 手順4")

## アドオンを有効化する

作成したアドオンを有効化してみましょう。
**情報** ウィンドウの **ファイル** > **ユーザ設定** を選択してください。
**アドオン** タブを選択し、サポートレベルを **テスト中** に変更します。
今回作成したアドオンが表示されていると思います。

![アドオン有効化 手順1](https://dl.dropboxusercontent.com/s/7p3apgnyvjj8dl0/blender_enable_add-on_1.png "アドオン有効化 手順1")

**チェックボックス** をクリックし、アドオンを有効化してみましょう。

![アドオン有効化 手順2](https://dl.dropboxusercontent.com/s/ghc3rhh2wf3v9zc/blender_enable_add-on_2.png "アドオン有効化 手順2")

アドオンの有効化が正常に終了した場合は、Windowsであれば **コマンドプロンプト** 、 Mac/Linuxであれば **コンソール** （以降長くなるのでまとめて **コンソール** と呼ぶことにします）に以下の文字列が出力されているはずです。

```sh
アドオンが有効化されました。
```

今回作成したアドオンはこれで有効化され、使用する準備が整ったことになります。

## アドオンを無効化する

アドオンを無効化しましょう。
無効化は、アドオンを有効化した時にクリックした **チェックボックス** を再度クリックすることで行えます。

![アドオン無効化](https://dl.dropboxusercontent.com/s/73xlppzkxu21u5w/blender_disable_add-on.png "アドオン無効化")

アドオンの無効化が正常に終了した場合は、Windowsであれば **コマンドプロンプト** 、 Mac/Linuxであれば **コンソール** に以下の文字列が出力されているはずです。

```sh
アドオンが無効化されました。
```

## まとめ

本章ではアドオンを自作し、自作したアドオンを有効化/無効化してみました。
実際にアドオンのソースコードを入力してもらったと思いますが、解説が無いので何をしているかよくわからなかったと思います。
次章からは新たなサンプルともう少し踏み込んだ解説を用いて、アドオンの作り方を紹介していきます。

### ポイント

* アドオンのソースコードは、Blender本体に備わっている **テキストエディタ** から作成・編集できる
* アドオンの有効化/無効化は、 **情報** ウィンドウの **ファイル** > **ユーザ設定** で表示される **Blenderユーザ設定** の **アドオン** タブから行う
