<div id="sect_title_img_4_2"></div>

<div id="sect_title_text"></div>

# アドオンをデバッグする

<div id="preface"></div>

###### アドオン開発中にバグは必ずと言って良いほど発生します。そして発生したバグの原因究明・修正（デバッグ）は、開発の大半の時間を占めることが少なくありません。本節では、Blenderアドオンを開発する時のデバッグ方法について紹介します。

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

<div id="custom_ol"></div>

1. PyDevとEclipseのインストール
2. デバッグ用プロジョクトの作成
3. デバッグ実行のためのPythonスクリプトの作成
4. PyDevデバッグサーバの起動
5. デバッグ開始

### 1. EclipseとPyDevのインストール

デバッグを実行するために、EclipseとPyDevをインストールします。

#### Eclipseのインストール

Eclipseのホームページから、最新版のEclipseをダウンロードします。

<div id="webpage"></div>

|Eclipse ダウンロードページ|
|---|
|https://www.eclipse.org/downloads/|
|![Eclipse ダウンロードページ](https://dl.dropboxusercontent.com/s/5jk44fvtrmkat80/eclipse_download.png "Eclipse ダウンロードページ")|

EclipseはJavaやC/C++、PHPなど様々なプログラミング言語に対応していますが、ここではJava用のEclipseを利用します。
EclipseはJavaで動作しているため、必要に応じてJava SEをインストールしてください。

|Java SE ダウンロードページ|
|---|
|http://www.oracle.com/technetwork/java/javase/downloads/index.html|
|![Java SE ダウンロードページ](https://dl.dropboxusercontent.com/s/bc4nbfq66358u5h/javase_download.png "Java SE ダウンロードページ")|

#### PyDevのインストール

ダウンロードしたEclipseを起動してください。
Eclipseが起動したら、以下の手順に沿ってPyDevをインストールしましょう。

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|```Help``` > ```Install New Software...``` をクリックします|![PyDevのインストール 手順1](https://dl.dropboxusercontent.com/s/n41n3g8fa4cytvv/install_pydev_1.png "PyDevのインストール 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|```Available Software``` ウィンドウの ```Add...``` をクリックします|![PyDevのインストール 手順2](https://dl.dropboxusercontent.com/s/9hwwncn3xeie2si/install_pydev_2.png "PyDevのインストール 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|```Name``` に ```PyDev``` 、 ```Location``` に ```http://pydev.org/updates``` を入力して OK をクリックします|![PyDevのインストール 手順3](https://dl.dropboxusercontent.com/s/mcs991y9iucacz6/install_pydev_3.png "PyDevのインストール 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|4|しばらく経つと、```Available Software``` ウィンドウに ```PyDev``` が追加されるので選択した後、 ```Contact all update sites during install to find required software``` のチェックボックスを外し、 ```Next >``` をクリックします<br>※ 注意：Contact all update sites during install to find required softwareのチェックを外さないと、本ステップが完了するまでに長い時間がかかってしまいます。|![PyDevのインストール 手順4](https://dl.dropboxusercontent.com/s/xm1f3c7pytrs7j1/install_pydev_4.png "PyDevのインストール 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|5|```Install Details``` ウィンドウの ```Next >``` をクリックします|![PyDevのインストール 手順5](https://dl.dropboxusercontent.com/s/uogvhp6ltvsdt88/install_pydev_5.png "PyDevのインストール 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|6|```Review Licenses``` ウィンドウでライセンスに同意した後、 ```Finish``` をクリックします|![PyDevのインストール 手順6](https://dl.dropboxusercontent.com/s/7qldtykqtvktsn3/install_pydev_6.png "PyDevのインストール 手順6")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|7|PyDevのインストールが完了します|![PyDevのインストール 手順7](https://dl.dropboxusercontent.com/s/pw6z8p67qk2tr3u/install_pydev_7.png "PyDevのインストール 手順7")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|8|Eclipseを再起動します|![PyDevのインストール 手順8](https://dl.dropboxusercontent.com/s/onj8yjj4723yl0j/install_pydev_8.png "PyDevのインストール 手順8")|
|---|---|---|

<div id="process_start_end"></div>

---

### 2. デバッグ用プロジョクトの作成

デバッグ用のEclipse用プロジェクトを作成します。

#### Eclipseプロジェクトの作成

Eclipseプロジェクトを以下の手順に沿って作成します。

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|```File``` - ```New``` - ```Project...``` をクリックします|![Eclipseプロジェクトの作成 手順1](https://dl.dropboxusercontent.com/s/htzmf81c1umkg3m/setup_eclipse_project_1.png "Eclipseプロジェクトの作成 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|```Select a wizard``` ウィンドウから、 ```PyDev``` - ```PyDev Project``` を選択し、 ```Next >``` をクリックします|![Eclipseプロジェクトの作成 手順2](https://dl.dropboxusercontent.com/s/xzd20c7dj4oi4m8/setup_eclipse_project_2.png "Eclipseプロジェクトの作成 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|```PyDev Project``` ウィンドウで ```Project name``` に適当な名前をつけ（今回の例では ```Blender-Addon-Debugging``` ）、 ```Grammer Version``` を ```3.0``` 、 ```Interpreter``` を ```python``` に設定し ```Next >``` をクリックします|![Eclipseプロジェクトの作成 手順3](https://dl.dropboxusercontent.com/s/ono341pj3yl1cnf/setup_eclipse_project_3.png "Eclipseプロジェクトの作成 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|4|```Finish``` をクリックします|![Eclipseプロジェクトの作成 手順4](https://dl.dropboxusercontent.com/s/o7vngybzvl4h4c5/setup_eclipse_project_4.png "Eclipseプロジェクトの作成 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|5|eclipseプロジェクトが作成されます|![Eclipseプロジェクトの作成 手順5](https://dl.dropboxusercontent.com/s/1qurjvwmtbmxbkw/setup_eclipse_project_5.png "Eclipseプロジェクトの作成 手順5")|
|---|---|---|

<div id="process_start_end"></div>

---

#### パスの設定

プロジェクト作成後、Blender標準のPythonスクリプト等が置かれているパスを設定します。

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|作成したプロジェクトを選択した状態で、 ```Project``` > ```Properties``` をクリックします|![パスの設定 手順1](https://dl.dropboxusercontent.com/s/rxpoqtgrmbpr4rl/configure_path_1.png "パスの設定 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|左のメニューから ```PyDev - PYTHONPATH``` を選択します|![パスの設定 手順2](https://dl.dropboxusercontent.com/s/tkaqudo3ougnen2/configure_path_2.png "パスの設定 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|```External Libraries``` を選択します|![パスの設定 手順3](https://dl.dropboxusercontent.com/s/itz2hzqa9q3oq9i/configure_path_3.png "パスの設定 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|4|```Add source folder``` をクリックし、以下のパスを追加します <br> * (BLENDER_BASE_SCRIPT_PATH)/addons <br> * (BLENDER_BASE_SCRIPT_PATH)/addons/modules <br> * (BLENDER_BASE_SCRIPT_PATH)/modules <br> * (BLENDER_BASE_SCRIPT_PATH)/startup <br> * （必要に応じて個人用の作業ディレクトリ）|![パスの設定 手順4](https://dl.dropboxusercontent.com/s/uko6g5ltb04yhqo/configure_path_4.png "パスの設定 手順4")|
|---|---|---|

BLNEDER_BASE_SCRIPT_PATHはOS依存で以下のようになります。
なお、Blenderの実行ファイルのパスは環境に応じて変更になります。
BLENDER_VERはBlenderのバージョンが入ります。マイナーバージョンまでで、2.75aを利用している場合は、BLENDER_VERは2.75になります。

|OS|Blender実行ファイルのパス例|BLENDER_BASE_SCRIPT_PATH|
|---|---|---|
|Windows|```C:\path\blender.exe```|　|
|Mac|```/path/blender.app```|```/path/blender.app/Contents/Resources/(BLENDER_VER)/scripts```|
|Linux|```/path/blender```|　|

今回は上記に加えて、3.で保存する ```debug.py``` と ```debuggee.py``` の保存先を指定します。
保存先は、 [1.4節](../chapter_01/04_Install_own_Add-on.md) を参照してください。

<div id="process_start_end"></div>

---

### 3. デバッグ実行のためのPythonスクリプトの作成

デバッグ実行するためのPythonスクリプトを作成しましょう。
以下のようなスクリプトを、ファイル名 ```debug.py``` として作成してください。

[import](../../sample/src/chapter_04/debug.py)

ここで ```PYDEV_SRC_DIR``` にはPyDevのプラグインディレクトリを指定しますが、環境により異なるため、各自確認してみてください。
筆者のMacではPyDevの場所は ```~/.p2/pool/plugins/org.python.pydev_XXX/pysrc``` でした。（```XXX```はPyDevのバージョンです。）

次に、デバッグしたいアドオンを用意します。
今回は以下のようなアドオンをデバッグ対象とします。
ファイル名 ```debugee.py``` として作成してください。
なお、```debug.py``` と ```debugee.py``` は同じディレクトリに置く必要があります。
今回は本書で紹介してきたサンプルの場所と同様のディレクトリに保存します。
保存先は、 [1.4節](../chapter_01/04_Install_own_Add-on.md) を参照してください。

[import](../../sample/src/chapter_04/debuggee.py)

デバッグするためには、 ```debug.py``` をインポートし、デバッグを開始する場所に ```debug.start_debug()``` を追加します。
上記では、アドオン有効化時にデバッグを開始しています。

### 4. PyDevデバッグサーバの起動

#### EclipseにBlenderを登録

PyDevデバッグサーバをEclipseから起動するために、以下の方法でBlenderをEclipseの外部ツールとして追加します。

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|```Run``` > ```External Tools``` > ```External Tools Configurations...``` をクリックします|![EclipseにBlenderを登録 手順1](https://dl.dropboxusercontent.com/s/yudnrn16tz821op/register_blender_to_eclipse_1.png "EclipseにBlenderを登録 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|表示されたウィンドウで、 ```Program``` をダブルクリックします|![EclipseにBlenderを登録 手順2](https://dl.dropboxusercontent.com/s/cjybhosb2649upd/register_blender_to_eclipse_2.png "EclipseにBlenderを登録 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|```Main``` タブを選択し、 ```Location``` にBlenderの実行ファイルのパス、 ```Working Directory``` にBlenderの実行ファイルが置かれたディレクトリを入力します。<br> ```Name``` には任意の名前を入力します。（ここでは ```New_Configuration``` を入力しています）|
|---|---|---|

OSごとのblender実行ファイルのパスを以下に示します。
Blenderのトップディレクトリ（Blenderを非インストーラ版でダウンロードした時に、ダウンロードしたファイルを解答したディレクトリ）を ```/path``` とします。

|OS|パス|
|---|---|
|Windows|```/path/blender.exe```|
|Mac|```/path/blender.app/Contents/MacOS/blender```|
|Linux|```/path/blender```|

<div id="process"></div>

|4|```Apply``` をクリックします。|![EclipseにBlenderを登録 手順3](https://dl.dropboxusercontent.com/s/305zw5lym8bhoja/register_blender_to_eclipse_3.png "EclipseにBlenderを登録 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---

#### デバッグサーバの起動

デバッグの準備もいよいよ最後で、PyDevデバッグサーバを起動します。
PyDevデバッグサーバの起動手順を以下に示します。

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|```Window```　> ```Perspective``` > ```Open Perspective``` > ```Other...``` をクリックします|![デバッグサーバの起動 手順1](https://dl.dropboxusercontent.com/s/srlqpa41rwqtcbg/run_debug_server_1.png "デバッグサーバの起動 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|```Debug``` を選択し、Debugパースペクティブを開きます|![デバッグサーバの起動 手順2](https://dl.dropboxusercontent.com/s/z2aqd3b3i8e1u3c/run_debug_server_2.png "デバッグサーバの起動 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|```Pydev``` > ```Start Debug Server``` をクリックします|![デバッグサーバの起動 手順3](https://dl.dropboxusercontent.com/s/zxrckr9gfrxrkxd/run_debug_server_3.png "デバッグサーバの起動 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|4|デバッグサーバが起動します|![デバッグサーバの起動 手順4](https://dl.dropboxusercontent.com/s/stxtk3q6glfo925/run_debug_server_4.png "デバッグサーバの起動 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---

### 5. デバッグ開始

ここまで順調に設定できていれば、以下のような画面になっているはずです。
先ほど作成した ```debug.py``` と ```debuggee.py``` は ```PyDev Package Explorer``` から参照することができます。

![デバッグ開始 手順1](https://dl.dropboxusercontent.com/s/a4ktv1sy6bv7duc/start_debug_1.png "デバッグ開始 手順1")

以下の手順に従って、EclipseからBlenderを起動してアドオンをデバッグしましょう。
今回はデバッグができたことの確認として、 ```debugee.py``` の28行目にブレークポイントを設定してみました。

![デバッグ開始 手順2](https://dl.dropboxusercontent.com/s/yo1ij0wqrf6fzw5/start_debug_2.png "デバッグ開始 手順2")

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|```Run``` > ```External Tools``` > ```External Tools Configurations...``` をクリックします|![デバッグ開始 手順3](https://dl.dropboxusercontent.com/s/ma36nv5q2br1hvb/start_debug_3.png "デバッグ開始 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|```New_Configuration``` を選択し、 ```Run``` ボタンをクリックします。<br>以降は、 ```Run``` > ```External Tools``` > ```New_Configuration``` からBlenderの起動が行えるようになります|![デバッグ開始 手順4](https://dl.dropboxusercontent.com/s/wdphxp2edjuvees/start_debug_4.png "デバッグ開始 手順4")<br>![デバッグ開始 手順5](https://dl.dropboxusercontent.com/s/wir3l0phuez9v1b/start_debug_5.png "デバッグ開始 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|Blenderが起動します|![デバッグ開始 手順6](https://dl.dropboxusercontent.com/s/lcy17hstd76pfe5/start_debug_6.png "デバッグ開始 手順6")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|4|作成したアドオンを有効化します|![デバッグ開始 手順7](https://dl.dropboxusercontent.com/s/w0en5mwd5fgpmm6/start_debug_7.png "デバッグ開始 手順7")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|5|デバッガが起動します|![デバッグ開始 手順8](https://dl.dropboxusercontent.com/s/876yphkm0qjolcp/start_debug_8.png "デバッグ開始 手順8")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|6|Debugパースペクティブで、 ```Resume``` ボタンを押します|![デバッグ開始 手順9](https://dl.dropboxusercontent.com/s/d211w8m59e5tubf/start_debug_9.png "デバッグ開始 手順9")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|7|*3Dビュー* のメニューで ```追加``` > ```メッシュ``` > ```デバッグのテスト``` を実行します|![デバッグ開始 手順10](https://dl.dropboxusercontent.com/s/mg5rywpsvq17s0w/start_debug_10.png "デバッグ開始 手順10")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|8|設定したブレークポイントでプログラムが止まります。|![デバッグ開始 手順11](https://dl.dropboxusercontent.com/s/b51idbmcjdjyiuz/start_debug_11.png "デバッグ開始 手順11")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|9|```Debug``` パースペクティブで変数値などを参照することができます。<br>その他基本的なEclipse上でのデバッグの仕方を説明すると長くなってしまいますので、必要に応じてWebページなどを参考にしてください|![デバッグ開始 手順12](https://dl.dropboxusercontent.com/s/m95irzuut9ngloh/start_debug_12.png "デバッグ開始 手順12")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|10|　|![デバッグ開始 手順13](https://dl.dropboxusercontent.com/s/3kjwzrvham4yxtd/start_debug_13.png "デバッグ開始 手順13")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|11|　|![デバッグ開始 手順14](https://dl.dropboxusercontent.com/s/70nztthhb4hm7wo/start_debug_14.png "デバッグ開始 手順14")|
|---|---|---|

<div id="process_start_end"></div>

---

## デバッガアドオン『BreakPoint』を利用したデバッグ

外部デバッガを用いたデバッグはEclipseのデバッガ機能が使えるため非常に強力ですが、デバッグ実行するまでの準備に非常に手間がかかります。
手間をかけずにデバッグしたい方は、アドオン **『BreakPoint』** の利用を検討しましょう。
デバッグ実行するまでの準備はアドオンのインストールとブレークポイントの設定のみで、非常に少ない手間でデバッグすることができます。

アドオン『BreakPoint』を利用したデバッグの手順は以下のようになります。

<div id="custom_ol"></div>

1. アドオン『BreakPoint』のインストール
2. アドオン『BreakPoint』の有効化
3. ブレークポイントをデバッグ対象のスクリプトに設定
4. デバッグ開始

### 1. アドオン『BreakPoint』のインストール

アドオン『BreakPoint』を以下のWebサイトからダウンロードし、インストールします。

<div id="webpage"></div>

|Blender Wiki (Scripts: BreakPoint)|
|---|
|http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Development/BreakPoint|
|![『BreakPoint』のインストール](https://dl.dropboxusercontent.com/s/220ubjo2o4t0t4n/install_breakpoint.png "『BreakPoint』のインストール")|

### 2. アドオン『BreakPoint』の有効化

<div id="sidebyside"></div>

|インストールしたアドオンを有効化します。|![『BreakPoint』の有効化](https://dl.dropboxusercontent.com/s/b6ofwmbcsw4qkyj/enable_breakpoint.png "『BreakPoint』の有効化")|
|---|---|


### 3. ブレークポイントをデバッグ対象のスクリプトに設定

以下のようなデバッグ対象のアドオンを作成し、 ```debuggee_2.py``` として保存します。

[import](../../sample/src/chapter_04/debuggee_2.py)

ブレークポイントを設定する関数は ```bpy.types.bp.bp()``` ですが、簡単のため ```breakpoint()``` で呼び出せるようしています。

```py:debuggee_2_part_1.py
# ブレークポイント関数
breakpoint = bpy.types.bp.bp
```

ブレークポイントの設定は、ブレークポイントを設定したい場所で ```breakpoint()``` 関数を実行することで行えます。
第1引数には変数のスコープの辞書（ローカル変数であれば ```locals()``` 、グローバル変数であれば ```globals()```）、第2引数には確認したい変数を指定します。

### 4. デバッグ開始

以下の手順に従って、デバッグを開始します。

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|*テキストエディタ* エリアのメニューで *ビュー* > *プロパティ* を実行し、 *テキストエディタ* エリアのプロパティを表示してください。|![デバッグ 手順1](https://dl.dropboxusercontent.com/s/bu01qdhpcstfb16/start_bp_debug_1.png "デバッグ 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|プロパティを表示すると、BreakPointメニューが追加されていることがわかります。<br>BreakPointメニューを確認し、有効化されていることを確認しておきましょう。|![デバッグ 手順2](https://dl.dropboxusercontent.com/s/quxp3yhoj9r9q01/start_bp_debug_2.png "デバッグ 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|*3Dビュー* エリアのメニューで *追加* > *メッシュ* > *デバッグのテスト2* を実行します。|![デバッグ 手順3](https://dl.dropboxusercontent.com/s/wmmy34dyq4ktvvj/start_bp_debug_3.png "デバッグ 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|4|*テキストエディタ* エリアのプロパティにブレークポイントの関数に指定した変数の値が表示されます。|![デバッグ 手順4](https://dl.dropboxusercontent.com/s/fmfykni3dax1vgt/start_bp_debug_4.png "デバッグ 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

[1.3節](../chapter_01/03_Prepare_Add-on_development_environment.md) のように、Blenderを *コンソール* から開いた場合は、 *コンソール* にも表示されているはずです。  また、 *コンソール* から起動した場合に限り、Blender本体から *コンソール* に制御が渡ってBlenderが操作できなくなります。  *コンソール* 制御が移っている間はPythonインタープリタを使うことができます。  Blender本体に制御を戻す（アドオンの実行を再開する）場合は、Windowsでは ```Ctrl+Z```、 Mac/Linuxでは ```Ctrl+D``` キーを押してください。


## まとめ

Blenderをデバッグする方法を紹介しましたが、本節で紹介したそれぞれのデバッグについてまとめてみました。

|デバッグ方法|得られる情報|前準備|
|---|---|---|
|self.report|*コンソール・ウィンドウ* に出力可能な処理中の変数値確認|ソースコードの調べたい箇所に ```self.report()``` 関数を追加|
|print|すべての変数値確認|*コンソール* からBlenderを起動し、ソースコードの調べたい箇所に ```print()``` 関数を追加|
|外部デバッガ|ブレークポイント設定やコールトレース調査、変数値確認など *Eclipse* が持つデバッガ機能を利用可能|EclipseやPyDevのインストール、EclipseとBlenderの連携、デバッグ実行用スクリプトの作成|
|デバッガアドオン『BreakPoint』|ブレークポイント設定、変数値確認|アドオン『BreakPoint』のインストール、ブレークポイント設定のためのソースコード編集|

多くの情報を得ることのできるデバッグは、必要な前準備が基本的に多くなります。
問題解決の難しさと準備時間を見極めて適宜デバッグ方法を変えていきましょう。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderをデバッグする方法として、確認対象の変数を出力する他に、外部デバッガやデバッグ用アドオンを用いる方法がある
* デバッグ実行のための前準備が多いデバッグ方法は、デバッグ時に多くの情報を得ることができる
