# 4-2. アドオンをデバッグする

アドオン開発中にバグは必ずと言って良いほど発生します。
そして発生したバグの原因究明・修正（デバッグ）は、開発の大半の時間を占めることが少なくありません。
本節では、Blenderアドオンを開発する時のデバッグ方法について紹介します。

## アドオンのデバッグ手段

アドオンのデバッグ手段としては、以下の方法があります。

* self.reportデバッグ
* printデバッグ
* 外部デバッガを利用したデバッグ
* デバッガアドオン『BreakPoint』を利用したデバッグ

## self.reportデバッグ

読んで字のごとく、 ```self.report()``` 関数を用いたデバッグ手法です。
第2引数には任意の文字列が入力できることを利用して、確認したい変数の値を *コンソール・ウィンドウ* に表示させることでデバッグを行います。
self.reportデバッグの例を以下に示します。
以下の例では、 ```execute()``` メソッド内で定義された変数 ```a``` と ```b``` の値を表示しています。

```py:debug_self_report.py
def execute(self, context):
    a = 50
    b = 4.0
    self.report({'INFO'}, "a=%d, b=%f" % (a, b))
```

この状態で ```execute()``` メソッドが実行されると、 *コンソール・ウィンドウ* に以下のように表示されます。

```py:debug_self_report_result.py
a=50, b=4.0
```

変数を表示したい箇所に ```self.report()``` 関数を記述するだけで良いため、他のデバッグ方法に比べて最も手軽にデバッグを行える点がメリットになります。
ただし、 *modal()* メソッドなどの ```self.report()``` を利用できない処理のデバッグができない点がデメリットです。

## printデバッグ

読んで字のごとく、 ```print()``` 関数を用いたデバッグ手法です。
self.reportデバッグと同じく、確認したい変数の値を表示させてデバッグを行う方法ですが、self.reportデバッグでは確認できなかった処理中の変数も確認することができます。
ただし ```print()``` 関数の出力先は *コンソール* になるため、 [1.3節](../chapter_01/03_Prepare_Add-on_development_environment.md) を参考にして、 *コンソール* からBlenderを起動する必要があります。

以下の例では、 ```execute()``` メソッド内で定義された変数 ```a``` と ```b``` の値を表示しています。

```py:debug_self_report.py
def execute(self, context):
    a = 50
    b = 4.0
    print("a=%d, b=%f" % (a, b))
```

この状態で ```execute()``` メソッドが実行されると、 *コンソール* に以下のように表示されます。

```py:debug_self_report_result.py
a=50, b=4.0
```

また、 *Pythonコンソール* から *bpy.ops.XXX* （XXX： *オペレーションクラス* の ```bl_idname``` ）によりアドオンの処理を実行した場合、 ```print()``` 関数の出力先は *Pythonコンソール* になります。

## 外部デバッガを利用したデバッグ

上記2つのデバッグ手法は、確認したい変数を表示するためのコードをいちいち入れる必要があるためあまり効率的とはいえません。
上記のデバッグ方式でも開発は可能ですが、デバッグ時間を短縮して開発に注力するために外部のデバッガを利用してデバッグすることを検討しましょう。

ここでは、外部デバッガとして **PyDev** を利用します。
さらに、統合開発環境(IDE)である **Eclipse** を利用することで、GUIベースでデバッグできるようにします。

外部デバッガを利用したデバッグの手順を要約すると以下のようになります。

1. PyDevとEclipseのインストール
2. デバッグ用プロジョクトの作成
3. デバッグ実行のためのPythonスクリプトの作成
4. PyDevデバッグサーバの起動
5. デバッグ開始

### 1. EclipseとPyDevのインストール

デバッグを実行するために、EclipseとPyDevをインストールします。

#### Eclipseのインストール

Eclipseのホームページから、最新版のEclipseをダウンロードします。

* Eclipse ダウンロードページ - https://www.eclipse.org/downloads/

![Eclipse ダウンロードページ](https://dl.dropboxusercontent.com/s/5jk44fvtrmkat80/eclipse_download.png "Eclipse ダウンロードページ")

EclipseはJavaやC/C++、PHPなど様々なプログラミング言語に対応していますが、ここではJava用のEclipseを利用します。
EclipseはJavaで動作しているため、必要に応じてJava SEをインストールしてください。

* Java SE ダウンロードページ - http://www.oracle.com/technetwork/java/javase/downloads/index.html

![Java SE ダウンロードページ](https://dl.dropboxusercontent.com/s/bc4nbfq66358u5h/javase_download.png "Java SE ダウンロードページ")

#### PyDevのインストール

ダウンロードしたEclipseを起動してください。
Eclipseが起動したら、以下の手順に沿ってPyDevをインストールしましょう。

1. ```Help``` > ```Install New Software...``` をクリックします

![PyDevのインストール 手順1](https://dl.dropboxusercontent.com/s/n41n3g8fa4cytvv/install_pydev_1.png "PyDevのインストール 手順1")

2. ```Available Software``` ウィンドウの ```Add...``` をクリックします

＠＠＠図を追加＠＠＠


3. ```Name``` に ```PyDev``` 、 ```Location``` に ```http://pydev.org/updates``` を入力して OK をクリックします

![PyDevのインストール 手順3](https://dl.dropboxusercontent.com/s/mcs991y9iucacz6/install_pydev_3.png "PyDevのインストール 手順3")

4. しばらく経つと、```Available Software``` ウィンドウに ```PyDev``` が追加されるので選択した後、 ```Contact all update sites during install to find required software``` のチェックボックスを外し、 ```Next >``` をクリックします
※ 注意：Contact all update sites during install to find required softwareのチェックを外さないと、本ステップが完了するまでに長い時間がかかってしまいます。

![PyDevのインストール 手順4](https://dl.dropboxusercontent.com/s/xm1f3c7pytrs7j1/install_pydev_4.png "PyDevのインストール 手順4")

5. ```Install Details``` ウィンドウの ```Next >``` をクリックします

![PyDevのインストール 手順5](https://dl.dropboxusercontent.com/s/uogvhp6ltvsdt88/install_pydev_5.png "PyDevのインストール 手順5")

6. ```Review Licenses``` ウィンドウでライセンスに同意した後、 ```Finish``` をクリックします

![PyDevのインストール 手順6](https://dl.dropboxusercontent.com/s/7qldtykqtvktsn3/install_pydev_6.png "PyDevのインストール 手順6")

7. PyDevがインストールされるので、インストール後に Eclipseを再起動します

![PyDevのインストール 手順7](https://dl.dropboxusercontent.com/s/pw6z8p67qk2tr3u/install_pydev_7.png "PyDevのインストール 手順7")

![PyDevのインストール 手順8](https://dl.dropboxusercontent.com/s/onj8yjj4723yl0j/install_pydev_8.png "PyDevのインストール 手順8")


### 2. デバッグ用プロジョクトの作成

デバッグ用のEclipse用プロジェクトを作成します。

#### Eclipseプロジェクトの作成

Eclipseプロジェクトを以下の手順に沿って作成します。

1. ```File``` - ```New``` - ```Project...``` をクリックします

![Eclipseプロジェクトの作成 手順1](https://dl.dropboxusercontent.com/s/htzmf81c1umkg3m/setup_eclipse_project_1.png "Eclipseプロジェクトの作成 手順1")

2. ```Select a wizard``` ウィンドウから、 ```PyDev``` - ```PyDev Project``` を選択し、 ```Next >``` をクリックします

![Eclipseプロジェクトの作成 手順2](https://dl.dropboxusercontent.com/s/xzd20c7dj4oi4m8/setup_eclipse_project_2.png "Eclipseプロジェクトの作成 手順2")

3. ```PyDev Project``` ウィンドウで ```Project name``` に適当な名前をつけ（今回の例では ```Blender-Addon-Debugging``` ）、 ```Grammer Version``` を ```3.0``` 、 ```Interpreter``` を ```python``` に設定し ```Next >``` をクリックします

![Eclipseプロジェクトの作成 手順3](https://dl.dropboxusercontent.com/s/ono341pj3yl1cnf/setup_eclipse_project_3.png "Eclipseプロジェクトの作成 手順3")

4. ```Finish``` をクリックすると、eclipseプロジェクトが作成されます

![Eclipseプロジェクトの作成 手順4](https://dl.dropboxusercontent.com/s/o7vngybzvl4h4c5/setup_eclipse_project_4.png "Eclipseプロジェクトの作成 手順4")

![Eclipseプロジェクトの作成 手順5](https://dl.dropboxusercontent.com/s/1qurjvwmtbmxbkw/setup_eclipse_project_5.png "Eclipseプロジェクトの作成 手順5")


#### パスの設定

プロジェクト作成後、Blender標準のPythonスクリプト等が置かれているパスを設定します。

1. 作成したプロジェクトを選択した状態で、 ```Project``` > ```Properties``` をクリックします

＠＠＠図を追加＠＠＠

2. 左のメニューから ```PyDev - PYTHONPATH``` を選択します

＠＠＠図を追加＠＠＠

3. ```External Libraries``` を選択します

＠＠＠図を追加＠＠＠

4. ```Add source folder``` をクリックし、以下のパスを追加します
  * (BLENDER_BASE_SCRIPT_PATH)/addons
  * (BLENDER_BASE_SCRIPT_PATH)/addons/modules
  * (BLENDER_BASE_SCRIPT_PATH)/modules
  * (BLENDER_BASE_SCRIPT_PATH)/startup
  * （必要に応じて個人用の作業ディレクトリ）
ここで、BLNEDER_BASE_SCRIPT_PATHはOS依存で以下のようになります。
なお、Blenderの実行ファイルのパスは環境に応じて変更になります。
BLENDER_VERはBlenderのバージョンが入ります。マイナーバージョンまでで、2.75aを利用している場合は、BLENDER_VERは2.75になります。

|OS|Blender実行ファイルのパス例|BLENDER_BASE_SCRIPT_PATH|
|---|---|---|
|Windows|```C:\path\blender.exe```|``````|
|Mac|```/path/blender.app```|```/path/blender.app/Contents/Resources/(BLENDER_VER)/scripts```|
|Linux|```/path/blender```||

今回は上記に加えて、3.で保存する ```debug.py``` と ```debuggee.py``` の保存先を指定します。
保存先は、 [1.4節](../chapter_01/04_Install_own_Add-on.md) を参照してください。

＠＠＠図を追加＠＠＠

### 3. デバッグ実行のためのPythonスクリプトの作成

デバッグ実行するためのPythonスクリプトを作成しましょう。
以下のようなスクリプトを、ファイル名 ```debug.py``` として作成してください。

{% include "../../sample/src/chapter_04/debug.py" %}

次に、デバッグしたいアドオンを用意します。
今回は以下のようなアドオンをデバッグ対象とします。
ファイル名 ```debugee.py``` として作成してください。
なお、```debug.py``` と ```debugee.py``` は同じディレクトリに置く必要があります。
今回は本書で紹介してきたサンプルの場所と同様のディレクトリに保存します。
保存先は、 [1.4節](../chapter_01/04_Install_own_Add-on.md) を参照してください。

{% include "../../sample/src/chapter_04/debugee.py" %}

デバッグするためには、 ```debug.py``` をインポートし、デバッグを開始する場所に ```debug.start_debug()``` を追加します。
上記では、アドオン有効化時にデバッグを開始しています。

### 4. PyDevデバッグサーバの起動

#### EclipseにBlenderを登録

PyDevデバッグサーバをEclipseから起動するために、以下の方法でBlenderをEclipseの外部ツールとして追加します。

1. ```Run``` > ```External Tools``` > ```External Tools Configurations...``` をクリックします

＠＠＠図を追加＠＠＠

2. 表示されたウィンドウで、 ```Program``` をダブルクリックします

＠＠＠図を追加＠＠＠

3. ```Main``` タブを選択し、 ```Location``` にBlenderの実行ファイルのパス、 ```Working Directory``` にBlenderの実行ファイルが置かれたディレクトリを入力します。
なお、 ```Name``` には任意の名前を入力します。（ここでは ```New_Configuration``` を入力しています）

OSごとのblender実行ファイルのパスを以下に示します。
Blenderのトップディレクトリ（Blenderを非インストーラ版でダウンロードした時に、ダウンロードしたファイルを解答したディレクトリ）を ```/path``` とします。

|OS|パス|
|---|---|
|Windows|```/path/blender.exe```|
|Mac|```/path/blender.app/Contents/MacOS/blender```|
|Linux|```/path/blender```|

入力後 ```Apply``` をクリックします。

＠＠＠図を追加＠＠＠


#### デバッグサーバの起動

デバッグの準備もいよいよ最後で、PyDevデバッグサーバを起動します。
PyDevデバッグサーバの起動手順を以下に示します。

1. ```Window```　> ```Perspective``` > ```Open Perspective``` > ```Other...``` をクリックします

＠＠＠図を追加＠＠＠

2. ```Debug``` を選択し、Debugパースペクティブを開きます

＠＠＠図を追加＠＠

3. ```Pydev``` > ```Start Debug Server``` をクリックし、デバッグサーバを起動します

＠＠＠図を追加＠＠＠


### 5. デバッグ開始

ここまで順調に設定できていれば、以下のような画面になっているはずです。
先ほど作成した ```debug.py``` と ```debuggee.py``` は ```PyDev Package Explorer``` から参照することができます。

＠＠＠図を追加＠＠＠

＠＠＠図を追加＠＠＠

以下の手順に従って、EclipseからBlenderを起動してアドオンをデバッグしましょう。
今回はデバッグができたことの確認として、 ```debugee.py``` の28行目にブレークポイントを設定してみました。

＠＠＠図を追加＠＠＠

1. ```Run``` > ```External Tools``` > ```External Tools Configurations...``` をクリックします

2. ```New_Configuration``` を選択し、 ```Run``` ボタンをクリックします
以降は、 ```Run``` > ```External Tools``` > ```New_Configuration``` からBlenderの起動が行えるようになります

3. Blenderが起動します

＠＠＠図を追加＠＠＠

4. 作成したアドオンを有効化すると、デバッガが起動します

＠＠＠図を追加＠＠＠

＠＠＠図を追加＠＠＠

5. Debugパースペクティブで、 ```Resume``` ボタンを押します

＠＠＠図を追加＠＠＠

6. ```追加``` > ```メッシュ``` > ```デバッグのテスト``` を実行します

＠＠＠図を追加＠＠＠

7. 設定したブレークポイントでプログラムが止まり、 ```Debug``` パースペクティブで変数値などを参照することができます。
その他基本的なEclipse上でのデバッグの仕方を説明すると長くなってしまいますので、必要に応じてWebページなどを参考にしてください

＠＠＠図を追加＠＠＠

## まとめ



### ポイント
