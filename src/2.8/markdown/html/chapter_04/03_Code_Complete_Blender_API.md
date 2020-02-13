---
pagetitle: 4-3. BlenderのAPIをコード補完する
subtitle: 4-3. BlenderのAPIをコード補完する
---

プログラムを作るとき、テキストエディタを使ってソースコードを編集することが多いと思います。
ほとんどのテキストエディタにはコード補完機能が備わっていて、この機能を利用することで開発効率を上げることができます。
そこで本節では、Visual Studio Code上でBlenderのAPIをコード補完する方法を説明します。


# 「fake-bpy-module」の紹介

Blenderが提供するPython APIの一部は、Pythonのソースコードではなくバイナリデータとして提供されるため、そのままではコードを補完できません。
筆者はこの問題を解決するため、Blenderが提供するPython APIのインタフェース部分のみを記述した、疑似モジュール「[fake-bpy-module](https://github.com/nutti/fake-bpy-module)」を開発しました。
「fake-bpy-module」を利用することで、基本的にコード補完機能を持つすべてのエディタで、BlenderのPython APIに関してコード補完できます。

「fake-bpy-module」がサポートするバージョンは、GitHubの [README](https://github.com/nutti/fake-bpy-module#supported-blender-version) を参考にしてください。
「fake-bpy-module」は、Windows/Mac/Linuxのいずれの環境でも動作しますが、Type Hint機能が導入されたPython 3.6以上のPythonでなければ、補完機能が利用できないことに注意してください。

「fake-bpy-module」は、次の3つの方式で提供しています。

1. PyPIパッケージ
2. GitHubで公開中のモジュール
3. モジュールの自作

本記事ではそれぞれについて、Visual Studio Code上での具体的なコード補完の手順を説明します。


# 方法1: PyPIパッケージ

## 1. pipコマンドを用いてパッケージをインストール

pipコマンドを利用することで、PyPIに登録されている「fake-bpy-module」をインストールできます。
次に示すコマンドを実行して、「fake-bpy-module」をインストールしてください。

```sh
 $ pip install fake-bpy-module-[version]
```

ここで `[version]` には、Blenderのバージョンを指定します。
Blender 2.80に対応する「fake-bpy-module」をインストール場合は、次のコマンドを実行します。

```sh
 $ pip install fake-bpy-module-2.80
```

pipを利用できる環境であれば、pipを利用して「fake-bpy-module」をインストールするのが簡単で確実ですが、pipを利用できない環境の場合は、後述する他の方法を試みてください。


## 2. Visual Studio Codeでコード補完する

pipコマンドを用いてパッケージをインストールした場合、コード補完するためのVisual Studio Code上での設定は不要です。
Visual Studio Code上で、コード補完する例を示します。

![](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/38888/d5c3c58e-8473-a38b-08d7-cfff624122af.png)

![](../../images/chapter_04/03_Code_Complete_Blender_API/complete_blender_api.png "Visual Studio Code上でのコード補完")


# 方法2: GitHubで公開中のモジュール


## 1. GitHubからモジュールをダウンロードする

「fake-bpy-module」は、[GitHubでも公開](https://github.com/nutti/fake-bpy-module/releases) しています。
モジュール一式をまとめたファイルは、`fake_bpy_modules_[Blenderのバージョン]-[モジュールを作成した年月日].zip` として公開しているため、環境にあわせて必要なモジュールをダウンロードします。
ここでは、[2020/1/11に作成したBlender 2.80向けのモジュール](https://github.com/nutti/fake-bpy-module/releases/tag/20200111) である `fake_bpy_modules_2.80-20200111.zip` をダウンロードします。
ダウンロードが完了したら、ファイルを解凍します。


## 2. Visual Studio Codeにモジュールのパスを伝える

次の手順に従って、Visual Studio Codeにダウンロードしたモジュールのパスを伝え、コード補完できるようにします。

1. Pythonの [Visual Studio Code Extention](https://marketplace.visualstudio.com/items?itemName=ms-python.python) をダウンロードします
2. *[File]* > *[Preferences]* > *[Settings]* をクリックしたあとに、*[Python › Auto Complete: Extra Paths]* から *[Edit in settings.json]* をクリックすると `settings.json` が開きます
3. `settings.json` が開いたら、`python.autoComplete.extraPaths` にモジュールのパスを設定します

```json
{
    "python.autoComplete.extraPaths": [
        "[path-to-modules]"
    ]
}
```

`[path-to-modules]` には、1で解凍されたあとのモジュールの絶対パスを指定してください。


## 3. Visual Studio Codeでコード補完を確認する

方法1の方式でモジュールをインストールした場合と同様、Visual Studio Codeでコード補完できるようになります。


# 方法3: モジュールの自作


## 1. Blenderのバイナリをダウンロードする

[公式のBlenderのダウンロードサイト](https://download.blender.org/release/) から、対象となるBlenderのバイナリをダウンロードします。
Blender 2.80のバイナリは、https://download.blender.org/release/Blender2.80/ で公開されています。


## 2. Blenderのソースコードをcloneする

次に示すコマンドを実行し、Blenderのソースコードをダウンロードします。

```sh
$ git clone git://git.blender.org/blender.git
```


## 3. GitHubの「fake-bpy-module」プロジェクトをcloneする

次に示すコマンドを実行し、GitHubに公開されている「fake-bpy-module」プロジェクトをcloneします。

```sh
$ git clone https://github.com/nutti/fake-bpy-module.git
```


## 4. 「fake-bpy-module」を生成する

次に示すコマンドを実行し、「fake-bpy-module」を生成します。

```sh
$ cd fake-bpy-module/src
$ sh gen_module.sh [source-dir] [blender-dir] [branch/tag/commit] [output-dir] [mod-version]
```

* `[source-dir]` ：Blenderのソースコードのルートディレクトリ
* `[blender-dir]` ：Blenderのバイナリが配置されたディレクトリ
* `[branch/tag/commit]` ：生成するモジュールに対応する、Blenderのソースコードのブランチ/タグ/コミット
* `[output-dir]` ：モジュールの生成先ディレクトリ
* `[mod_version]` ：指定したバージョンについて、`mods` ディレクトリに配置したパッチを使ってAPIを修正する

仮に2から連続してコマンドを実行してきた場合は、次のようにコマンドを実行します。

```sh
$ cd fake-bpy-module/src
$ sh gen_module.sh ../../blender [1でダウンロードしたBlenderのバイナリが配置されたディレクトリ] v2.80 out 2.80
```

## 5. Visual Studio Codeにモジュールのパスを伝える

方法2の方式に従い、モジュールのパスをVisual Studio Codeに伝えます。


## 6. Visual Studio Codeでコード補完を確認する

方法1や方法2の方式と同様、Visual Studio Codeでコード補完できるようになります。


# まとめ

「fake-bpy-module」を使って、BlenderのPython APIを、Visual Studio Code上でコード補完する方法を紹介しました。
コード補完を利用することで、Blenderのスクリプトやアドオン開発の効率が向上するため、ぜひ活用してみてください。
本節では紹介していませんが、Visual Studio Code以外のエディタでコード補完するための方法を、GitHubのプロジェクトページにて [ドキュメント](https://github.com/nutti/fake-bpy-module/blob/master/docs/setup_all_text_editor.md) として公開しています。
こちらもぜひ参考にしてみてください。

なお、「fake-bpy-module」はOSSとして公開していますので、[バグ報告](https://github.com/nutti/fake-bpy-module/issues) や [Pull Request](https://github.com/nutti/fake-bpy-module/pulls) などのContributionは大歓迎です！


## ポイント

* 「fake-bpy-module」を利用することにより、Visual Studio Codeなどのエディタで、BlenderのPython APIに関してコード補完できる
