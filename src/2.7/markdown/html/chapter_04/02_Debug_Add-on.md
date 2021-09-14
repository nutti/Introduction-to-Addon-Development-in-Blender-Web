---
pagetitle: 4-2. アドオンをデバッグする
subtitle: 4-2. アドオンをデバッグする
---

プログラムを作ったことがある方は知っていると思いますが、ソフトウェアにバグはつきものです。
そしてそれは、Blenderアドオンでも同じことが言えます。
発生したバグの原因を調べて修正するためにかかる時間は、アドオン開発の大半の時間を占めることが多いため、できることならバグを修正する時間を短くし、本来の開発に注力したいと考えるのが普通です。
そこで本節では、バグの原因を効率的に調べる（デバッグ）方法について説明します。


# アドオンのデバッグ手段

プログラムで発生したバグを取り除く作業は、一般的にデバッグと呼ばれます。
Blenderのアドオン開発もプログラムを作ることと同じですので、ここでもバグを取り除く作業をデバッグと呼ぶことにします。
Blenderのアドオン開発においてデバッグする手段はいくつかありますが、通常のプログラム開発と異なり、デバッグ手段が確立していません。
このため本節では、筆者が行っている次のデバッグ方法について説明します。

* self.reportデバッグ
* printデバッグ
* 外部デバッガを利用したデバッグ
* アドオン『BreakPoint』を利用したデバッグ


# self.reportデバッグ

タイトルの通り、スクリプト実行ログに文字列を出力する `self.report` メソッドを使ったデバッグ手法です。
`self.report` メソッドの第2引数に出力する文字列を渡しますが、ここに確認したい変数の値を指定することで変数の値をスクリプト実行ログに表示させます。
そして、表示された変数の値を見て、期待した値が保存されていることを確認します。

self.reportデバッグの例を次に示します。
次の例では、`execute` メソッド内で定義された変数 `a` と `b` の値をスクリプト実行ログに表示することで、それぞれの変数に正しい値が代入されていることを確認します。

```python
def execute(self, context):
    a = 50
    b = 4.0
    self.report({'INFO'}, "a=%d, b=%f" % (a, b))
```

この例で `execute` メソッドが実行されると、次のように変数 `a` と `b` の値がスクリプト実行ログに出力されます。

```python
a=50, b=4.0
```

self.reportデバッグは、変数を表示したい箇所に `self.report` メソッドを記述するだけで良いため、他のデバッグ方法に比べて手軽にデバッグを行える点がメリットです。
ただし、`modal` メソッド内などの `self.report` メソッドを利用できない処理の中では、デバッグできないことに注意する必要があります。
このように、`self.report` メソッドを利用できない処理の中で変数の値を確認したい場合は、次に紹介するprintデバッグを利用する必要があります。


# printデバッグ

こちらもタイトル通り、コンソールウィンドウに文字列を出力する `print` 関数を用いたデバッグ手法です。
self.reportデバッグと同じように、確認したい変数の値を表示させてデバッグを行う方法ですが、self.reportデバッグでは確認できない `modal` メソッドなどの処理で使用している変数についても、確認することができます。
ただし、`print` 関数の出力先はコンソールウィンドウであるため、[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.html) を参考にして、コンソールウィンドウからBlenderを起動する必要があります。

次の例では、`execute` メソッド内で定義された変数 `a` と `b` の値をコンソールウィンドウに出力することで、変数に正しい値が代入されているかを確認します。

```python
def execute(self, context):
    a = 50
    b = 4.0
    print("a=%d, b=%f" % (a, b))
```

この例で `execute` メソッドが実行されると、次のように変数 `a` と `b` の値がコンソールウィンドウに出力されます。

```python
a=50, b=4.0
```

<div class="column">
Pythonコンソールウィンドウから、`bpy.ops.XXX` （XXX：オペレーションクラスのbl_idname）を実行してアドオンの処理を行った場合、`print` 関数の出力先はPythonコンソールウィンドウになります。
</div>


# 外部デバッガを利用したデバッグ

ここまでに紹介した2つのデバッグ手法は、確認したい変数を表示するための処理をソースコード内に毎回追加する必要があるため、あまり効率的ではありません。
また、デバッグが終わったあとに追加した処理を削除する必要があり、削除中に誤って別の処理を削除するなどのバグが発生してしまう可能性があります。
もちろん簡単なデバッグ目的であれば、これらの手法でデバッグしてもよいのですが、デバッグが難航している場合は、外部のデバッガを使ってデバッグすることも検討してみましょう。

ここでは外部デバッガとしてPyDevを利用し、統合開発環境（IDE）であるEclipseを利用することで、GUIベースでデバッグできるようにします。
デバッグの手順を次に示します。


1. PyDevとEclipseのインストール
2. デバッグ用Eclipseプロジョクトの作成
3. デバッグ実行のためのPythonスクリプトの作成
4. PyDevデバッグサーバの起動
5. デバッグ開始


これからそれぞれの手順について、詳細な手順を説明していきます。


## 1. EclipseとPyDevのインストール

最初に、IDEのEclipseとデバッガPyDevをインストールします。


### Eclipseのインストール

Eclipseのホームページ([https://www.eclipse.org/downloads/](https://www.eclipse.org/downloads/))から、最新版のEclipseをダウンロードします。

Eclipseは、JavaやC/C++、PHPなど様々なプログラミング言語に対応しているIDEですが、ここではJava用のEclipseを利用します。
Blenderのアドオンの言語がPythonであることから、PythonのプログラムをデバッグするのにJava用のEclipseをなぜ使うのか、疑問に思うかもしれません。
その理由は、Python向けに提供されているEclipseが存在しないからです。
このため、Java用のEclipseにPython用のデバッガPyDevを追加することで、Pythonで書かれたプログラムをEclipseでデバッグできるようにします。

Eclipseを動作させるためには、Java SEがインストールされている必要があります。
もし、読者のPCにEclipseがインストールされていない場合は、Java SEのダウンロードページ([http://www.oracle.com/technetwork/java/javase/downloads/index.html](http://www.oracle.com/technetwork/java/javase/downloads/index.html))からダウンロードして、インストールしてください。


### PyDevのインストール

続いて、Python用のデバッガPyDevをインストールします。
ダウンロードしたEclipseを起動し、次の手順に従ってPyDevをインストールします。


<div class="work"></div>

|||
|---|---|
|1|メニューから [Help] > [Install New Software...] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_1.png "PyDevのインストール 手順1")|
|2|[Available Software] ウィンドウの [Add...] をクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_2.png "PyDevのインストール 手順2")|
|3|[Name] に `PyDev` を、[Location] に `http://pydev.org/updates` を入力して [OK] ボタンをクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_3.png "PyDevのインストール 手順3")|
|4|手順3の処理は少し時間がかかりますが、処理が終わると [Available Software] ウィンドウに [PyDev] が追加されると思いますので、[PyDev] のチェックボックスにチェックを入れたあと、[Contact all update sites during install to find required software] のチェックボックスのチェックを外し、[Next >] ボタンをクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_4.png "PyDevのインストール 手順4")<br>※注意：Contact all update sites during install to find required softwareのチェックボックスのチェックを外さないと、本ステップが完了するまでに長い時間がかかってしまいます。|
|5|[Install Details] ウィンドウの [Next >] ボタンをクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_5.png "PyDevのインストール 手順5")|
|6|[Review Licenses] ウィンドウでライセンスに同意し、[Finish] をクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_6.png "PyDevのインストール 手順6")|
|7|PyDevのインストールが完了します。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_7.png "PyDevのインストール 手順7")|
|8|Eclipseを再起動します。<br>![](../../images/chapter_04/02_Debug_Add-on/install_pydev_8.png "PyDevのインストール 手順8")|


## 2. デバッグ用Eclipseプロジョクトの作成

アドオンをデバッグするためのEclipseプロジェクトを作成します。


### Eclipseプロジェクトの作成

Eclipseプロジェクトを、次の手順に従って作成します。


<div class="work"></div>

|||
|---|---|
|1|メニューから [File] > [New] > [Project...] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/setup_eclipse_project_1.png "Eclipseプロジェクトの作成 手順1")|
|2|[Select a wizard] ウィンドウから [PyDev] > [PyDev Project] を選択し、[Next >] ボタンをクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/setup_eclipse_project_2.png "Eclipseプロジェクトの作成 手順2")|
|3|[PyDev Project] ウィンドウで [Project name] にプロジェクト名を入力し（今回の例では `Blender-Addon-Debugging`）、[Grammer Version] を [3.0]、[Interpreter] を [python] に設定し、[Next >] ボタンをクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/setup_eclipse_project_3.png "Eclipseプロジェクトの作成 手順3")|
|4|[Reference page] ウィンドウが表示されたら、[Finish] をクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/setup_eclipse_project_4.png "Eclipseプロジェクトの作成 手順4")|
|5|Eclipseプロジェクトが作成されます。<br>![](../../images/chapter_04/02_Debug_Add-on/setup_eclipse_project_5.png "Eclipseプロジェクトの作成 手順5")|


### パスの設定

Eclipseプロジェクトを作成した直後では、`bpy` モジュールなどのBlender本体と一緒に提供されるPythonモジュールなどへのパスが通っていないため、Blenderが提供するAPIを使うことができません。
そこで、作成したEclipseプロジェクトに対してBlenderが提供するモジュールへのパスを設定します。


<div class="work"></div>

|||
|---|---|
|1|[Package Explorer] において作成したプロジェクトを選択した状態で、メニュー [Project] > [Properties] をクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/configure_path_1.png "パスの設定 手順1")|
|2|表示されたウィンドウの左のメニューから、[PyDev - PYTHONPATH] を選択します。<br>![](../../images/chapter_04/02_Debug_Add-on/configure_path_2.png "パスの設定 手順2")|
|3|ウィンドウ右側のタブから [External Libraries] を選択します。<br>![](../../images/chapter_04/02_Debug_Add-on/configure_path_3.png "パスの設定 手順3")|
|4|[Add source folder] ボタンをクリックし、以下のパスを追加します <br> `(BLENDER_BASE_SCRIPT_PATH)/addons` <br>  `(BLENDER_BASE_SCRIPT_PATH)/addons/modules` <br>  `(BLENDER_BASE_SCRIPT_PATH)/modules` <br>  `(BLENDER_BASE_SCRIPT_PATH)/startup`<br>![](../../images/chapter_04/02_Debug_Add-on/configure_path_4.png "パスの設定 手順4")|


ここで `BLENDER_BASE_SCRIPT_PATH` は、次に示すようにOS依存です（`BLENDER_VER` はBlenderのバージョンです）。
例えばバージョンが2.75aのBlenderを利用している場合は、`BLENDER_VER` は `2.75` となります。

|OS|Blender<br>実行ファイルのパス例|BLENDER_BASE_SCRIPT_PATH|
|---|---|---|
|Windows|`C:\path\blender.exe`|`C:\path\(BLENDER_VER)\scripts`|
|Mac|`/path/blender.app`|`/path/blender.app/Contents/Resources/` <br> `(BLENDER_VER)/scripts`|
|Linux|`/path/blender`|`/path/(BLENDER_VER)/scripts`|

また、必要に応じて個人用の作業ディレクトリのパスを追加してもよいです。
パスを追加することで、作業用ディレクトリのファイルがウィンドウ左側の [PyDev Package Explorer] に表示されるようになります。
ここでは上で示したパスに加えて、`debug.py` と `debuggee.py` が置かれたディレクトリのパスを指定します。
これらのファイルの置き場所は、本書でこれまで紹介してきたサンプルの場所と同じディレクトリです。


## 3. デバッグ実行のためのPythonスクリプト作成

デバッグを行うために必要なプロジェクトの設定は終わったため、次にデバッグ実行するための関数が定義されたPythonモジュールを作成します。
次に示すスクリプトを、ファイル名 `debug.py` として作成してください。

[@include-source pattern="full" filepath="chapter_04/sample_4_2/debug.py"]


PyDevを使うためには、`pydevd` モジュールをインポートして `pydevd.settrace` を呼び出す必要があり、作成したモジュールでは `start_debug` 関数がその役割を担っています。
このためデバッグされる側のPythonスクリプトは、`debug` をインポートして `debug.start_debug` 関数を呼び出すことでデバッグを開始することができます。

ここで `pydevd` モジュールをインポートする前に、PyDevのパスを `sys.path` に追加しています。
パスを追加しないと `pydevd` が見つからずインポートできません。
`PYDEV_SRC_DIR` にはPyDevが置かれたディレクトリを指定しますが、環境によってPyDevが置かれるディレクトリが異なるため、各自で確認する必要があります。
筆者のMac環境ではPyDevの場所は `~/.p2/pool/plugins/org.python.pydev_XXX/pysrc` でした（`XXX`はPyDevのバージョンです）。

ちなみに `debug.py` には、グローバル変数 `DEBUGGING` が定義されています。
常にデバッグしたいとは限らないと思い、`DEBUGGING` を `True` にしたときのみデバッグするようになっています。

続いて、デバッグ対象とするアドオンを作成します。
ここでは次に示すアドオンを作成し、ファイル名 `debugee.py` として作成します。
なお、`debug.py` と `debugee.py` は同じディレクトリに置く必要があり、ここでは、本書でこれまで紹介してきたサンプルの場所と同じディレクトリに保存します。
保存先は、[1-5節](../chapter_01/05_Install_own_Add-on.html) を参照してください。

[@include-source pattern="full" filepath="chapter_04/sample_4_2/debuggee.py"]


最初に、先ほど作成した `debug` モジュールをインポートします。
そして、アドオン有効化時にデバッグを開始するために、`register` 関数で `debug.start_debug` 関数を実行します。
これでアドオンを有効化したときに、デバッグが開始されるようになりました。
なお、ここで紹介したアドオンは特に新しいことは行っていないため、ソースコードの解説はしません。


## 4. PyDevデバッグサーバの起動

3で作成したデバッグ実行のためのPythonスクリプトを実行するだけでは、デバッグすることはできません。
PyDevにはデバッグサーバと呼ばれる機能があり、デバッグサーバにシグナルを送ることでデバッグを行います。
このため、スクリプト実行前にPyDevデバッグサーバを事前に起動しておく必要があります。


### EclipseからBlenderを実行できるようにする

BlenderをEclipseから実行できるように設定し、Blenderのアドオン処理中にPyDevデバッグサーバに対してシグナルを送れるようにします。


<div class="work"></div>

|||
|---|---|
|1|メニューから [Run] > [External Tools] > [External Tools Configurations...] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/register_blender_to_eclipse_1.png "EclipseにBlenderを登録 手順1")|
|2|表示されたウィンドウの左側にある、[Program]をダブルクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/register_blender_to_eclipse_2.png "EclipseにBlenderを登録 手順2")|
|3|ウィンドウ左側の [Main] タブを選択し、[Location] にBlenderの実行ファイルのパス、[Working Directory] にBlenderの実行ファイルが置かれたディレクトリを入力します。<br>[Name] には任意の名前を入力します。ここでは、`New_Configuration` を入力します。|
|4|最後に、[Apply] ボタンをクリックします。<br>![](../../images/chapter_04/02_Debug_Add-on/register_blender_to_eclipse_3.png "EclipseにBlenderを登録 手順3")|


Blenderの実行ファイルのパスは、OSごとに異なります。
Blenderのトップディレクトリ（Blenderを非インストーラ版、すなわちzip版でダウンロードした時に、ダウンロードしたファイルを解凍したディレクトリ）を `/path` としたときの、Blenderの実行ファイルのパスを次に示します。

|OS|パス|
|---|---|
|Windows|`/path/blender.exe`|
|Mac|`/path/blender.app/Contents/MacOS/blender`|
|Linux|`/path/blender`|


### デバッグサーバの起動

続いて、PyDevデバッグサーバを起動します。


<div class="work"></div>

|||
|---|---|
|1|メニューから、[Window] > [Perspective] > [Open Perspective] > [Other...] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/run_debug_server_1.png "デバッグサーバの起動 手順1")|
|2|表示されたウィンドウで [Debug] を選択し、[OK] ボタンをクリックして [Debugパースペクティブ] を開きます。<br>![](../../images/chapter_04/02_Debug_Add-on/run_debug_server_2.png "デバッグサーバの起動 手順2")|
|3|メニューから [Pydev] > [Start Debug Server] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/run_debug_server_3.png "デバッグサーバの起動 手順3")|
|4|デバッグサーバが起動します。<br>![](../../images/chapter_04/02_Debug_Add-on/run_debug_server_4.png "デバッグサーバの起動 手順4")|


## 5. デバッグ開始

ここまで順調に手順を踏めていれば、次のような画面が表示されているはずです。

![](../../images/chapter_04/02_Debug_Add-on/start_debug_1.png "デバッグ開始 手順1")

3で作成したソースコード `debug.py` と `debuggee.py` は、[PyDev Package Explorer] の [scripts/addons] から参照することができます。

なお、[PyDev Package Explorer] には2つの [scripts/addons] が表示されていますが、片方はサポートレベルがOfficialであるアドオンが配置されています。
ここでは、作成したアドオンのデバッグを行うため、`debug.py` と `debuggee.py` が配置されているほうの [scripts/addons] を参照するようにしてください。

さて、いよいよEclipseからBlenderを起動してアドオンをデバッグします。
ここでは、`debugee.py` に定義された `DebugTestOps` クラスの `execute` メソッドの処理 `debug_var = debug_var + 30.0` が実行された時にプログラムを一時的に止めて、デバッグモードに移行するようにします。


<div class="work"></div>

|||
|---|---|
|1|ソースコードの行番号の隣の灰色部分をクリックし、`debugee.py` に定義された処理 `debug_var = debug_var + 30.0` にブレークポイントを設定します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_2.png "デバッグ開始 手順2")|
|2|メニューから [Run] > [External Tools] > [External Tools Configurations...] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_3.png "デバッグ開始 手順3")|
|3|表示されたウィンドウの左側から [New_Configuration] を選択し、[Run] ボタンをクリックします。<br>なお次回以降は、[Run] > [External Tools] > [New_Configuration] からBlenderを起動することができるようになります。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_4.png "デバッグ開始 手順4")<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_5.png "デバッグ開始 手順5")|
|4|Blenderが起動します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_6.png "デバッグ開始 手順6")|
|5|作成したアドオンを有効化します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_7.png "デバッグ開始 手順7")|
|6|デバッガが起動します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_8.png "デバッグ開始 手順8")|
|7|[Debugパースペクティブ] で、[Resume] ボタンを押します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_9.png "デバッグ開始 手順9")|
|8|起動中のBlenderに戻り、[3Dビュー] エリアのメニューから、[追加] > [メッシュ] > [デバッグのテスト] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_10.png "デバッグ開始 手順10")|
|9|設定したブレークポイントで処理が止まります。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_11.png "デバッグ開始 手順11")|
|10|[Debugパースペクティブ] で変数値などを参照することができます。<br>この他にもEclipseには様々な機能が備わっていますが、ここでは割愛します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_12.png "デバッグ開始 手順12")|
|11|デバッグを終了するためには、[Debug] タブの [New_Configuration] を選択した状態で [赤い四角] のボタンを押します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_13.png "デバッグ開始 手順13")|
|12|デバッグが終了します。この時、Debug Serverは起動したままになります。もしDebug Serverを終了したい場合は、[Debug] タブの [Debug Server] を選択した状態で [赤い四角] のボタンを押します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_debug_14.png "デバッグ開始 手順14")|


# アドオン『BreakPoint』を利用したデバッグ

EclipseとPyDevを用いたデバッグは、準備に時間がかかります。
少しだけデバッガを試してみたいという方にとっては、あまり魅力的ではありません。
そこで、手間をかけずにデバッガを利用したい方のために、アドオン『BreakPoint』を利用してデバッグを行う方法を紹介します。
前準備はアドオンの導入だけでよいので、EclipseとPyDevによるデバッグと違って、比較的すぐにデバッグ環境を整えることができます。

アドオン『BreakPoint』を利用してデバッグを行う手順を、次に示します。

1. アドオン『BreakPoint』のインストール
2. アドオン『BreakPoint』の有効化
3. ブレークポイントをデバッグ対象のスクリプトに設定
4. デバッグ開始


## 1. アドオン『BreakPoint』のインストール

Webサイト((http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Development/BreakPoint)[http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Development/BreakPoint])からアドオン『BreakPoint』をダウンロードし、インストールします。
アドオンのインストールの仕方がわからない場合は、[1-4節](../chapter_01/04_Understand_Install_Uninstall_Update_Add-on.html) を参考にしてください。


## 2. アドオン『BreakPoint』の有効化

インストールしたアドオン『BreakPoint』を有効化します。

![](../../images/chapter_04/02_Debug_Add-on/enable_breakpoint.png "『BreakPoint』の有効化")


## 3. ブレークポイントをデバッグ対象のスクリプトに設定

デバッグ対象とするアドオンを作成し、`debuggee_2.py` として保存します。

[@include-source pattern="full" filepath="chapter_04/sample_4_2/debuggee_2.py"]


ブレークポイントを設定するためには、`bpy.types.bp.bp` 関数を呼び出す必要がありますが、毎回これを書くのは面倒ですので、次のようにして `breakpoint` と書くだけで呼び出せるようにすると、ブレークポイントの設定が少し楽になるかと思います。

[@include-source pattern="partial" filepath="chapter_04/sample_4_2/debuggee_2.py" block="short_call", unindent="True"]


以降、ブレークポイントを設定する時は、次のようにしてブレークポイントを設定したい場所で `breakpoint` 関数を実行します。

[@include-source pattern="partial" filepath="chapter_04/sample_4_2/debuggee_2.py" block="set_breakpoint", unindent="True"]


`breakpoint` 関数の第1引数には、変数のスコープの辞書（ローカル変数であれば `locals`、グローバル変数であれば `globals`）、第2引数には確認したい変数を指定します。
サンプルでは、ローカル変数である `debug_var` の値を出力するため、第1引数に `locals`、第2引数に `globals` を指定します。


## 4. デバッグ開始

これで、デバッグを行う準備が整いました。
それでは、アドオン『BreakPoint』を使って実際にデバッグを行ってみましょう。


<div class="work"></div>

|||
|---|---|
|1|[テキストエディター] エリアのメニューから [ビュー] > [プロパティ] を実行し、[テキストエディター] エリアのプロパティを表示します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_bp_debug_1.png "デバッグ 手順1")|
|2|[プロパティ] を表示すると、項目 [BreakPoint] が追加されていることが確認できます。<br>そして、[有効化] ボタンが選択されていることを確認します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_bp_debug_2.png "デバッグ 手順2")|
|3|[3Dビュー] エリアのメニューから、[追加] > [メッシュ] > [デバッグのテスト2] を実行します。<br>![](../../images/chapter_04/02_Debug_Add-on/start_bp_debug_3.png "デバッグ 手順3")|
|4|[テキストエディター] エリアのプロパティにブレークポイントの関数に指定した変数の値が表示されます。<br>![](../../images/chapter_04/02_Debug_Add-on/start_bp_debug_4.png "デバッグ 手順4")|


<div class="column">
[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.html) で説明した方法で、Blenderをコンソールウィンドウから開いた場合は、コンソールウィンドウにもデバッグ情報が表示されているはずです。  
また、コンソールウィンドウから起動した場合に限り、Blender本体からコンソールウィンドウに制御が移ります。
制御が移っている間は、コンソールウィンドウでPythonインタープリタを使うことができますが、Blender側ではいかなる操作も受け付けなくなります。  
Blender本体に制御を戻す（アドオンの実行を再開する）場合は、Windowsでは [Ctrl] + [Z] キーを、Mac/Linuxでは [Ctrl] + [D] キーを押してください。
</div>


# まとめ

本節では、アドオンをデバッグする方法を紹介しました。
ここでは、本節で紹介したデバッグについて簡単にまとめます。

|デバッグ方法|できること|前準備|
|---|---|---|
|self.report|スクリプト実行ログに出力可能な処理中での変数値確認|ソースコードの調べたい箇所に `self.report` メソッドを追加|
|print|すべての変数値確認|ソースコードの調べたい箇所に `print` 関数を追加し、コンソールウィンドウからBlenderを起動|
|外部デバッガ|ブレークポイント設定やコールトレース調査、変数値確認など、Eclipseが持つデバッガ機能の利用|EclipseやPyDevのインストール、EclipseとBlenderの連携、デバッグ実行用スクリプトの作成|
|アドオン『BreakPoint』|ブレークポイント設定、変数値確認|アドオン『BreakPoint』のインストール、ブレークポイント設定のためのソースコード編集|

ここで示したように、より多くの情報をデバッグで得る場合は必要な前準備が多くなる傾向があります。
解決しようとしている問題の難しさと前準備の時間を合わせて判断し、デバッグする方法を決めましょう。


## ポイント


* 確認対象の変数をスクリプト実行ログやコンソールウィンドウに出力するほかに、外部デバッガやデバッグするためのアドオンを用いることでも、アドオンをデバッグすることができる
* 前準備が多いデバッグ方法は、デバッグするときにより多くの情報を得ることができる
