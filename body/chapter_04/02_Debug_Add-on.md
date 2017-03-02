<div id="sect_title_img_4_2"></div>

<div id="sect_title_text"></div>

# アドオンをデバッグする

<div id="preface"></div>

###### アドオン開発だけではなく、ソフトウェア開発にバグはつきものです。そして発生したバグの原因究明・修正（デバッグ）は、開発の大半の時間を占めることが少なくありません。そこで本節では、アドオンを開発する時のデバッグ方法について紹介します。

## アドオンのデバッグ手段

アドオンのデバッグ手段は色々ありますが、ここでは以下のデバッグ手段について紹介します。

* self.reportデバッグ
* printデバッグ
* 外部デバッガを利用したデバッグ
* アドオン『BreakPoint』を利用したデバッグ

## self.reportデバッグ

読んで字のごとく、 ```self.report()``` メソッドを用いたデバッグ手法です。
```self.report()``` メソッドの第2引数に任意の文字列を入力できることを利用し、確認したい変数の値をスクリプト実行ログに表示させることでデバッグを行います。

self.reportデバッグの例を以下に示します。以下の例では、 ```execute()``` メソッド内で定義された変数 ```a``` と ```b``` の値をスクリプト実行ログに表示することで、変数に正しい値が代入されていることを確認します。

```python
def execute(self, context):
    a = 50
    b = 4.0
    self.report({'INFO'}, "a=%d, b=%f" % (a, b))
```

```execute()``` メソッドが実行されると、スクリプト実行ログに以下のように表示されます。

```python
a=50, b=4.0
```

self.reportデバッグは、変数を表示したい箇所に ```self.report()``` メソッドを記述するだけで良いため、他のデバッグ方法に比べて最も手軽にデバッグを行える点がメリットです。一方、 ```modal()``` メソッドなどの ```self.report()``` メソッドを利用できない処理中ではデバッグできない点がデメリットです。

## printデバッグ

読んで字のごとく、```print()``` 関数を用いたデバッグ手法です。

self.reportデバッグと同じように、確認したい変数の値を表示させてデバッグを行う方法ですが、self.reportデバッグでは確認できなかった処理中の変数も確認することができます。ただし ```print()``` 関数の出力先はコンソールウィンドウであるため、[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.md) を参考にして、コンソールウィンドウからBlenderを起動する必要があります。

以下の例では、```execute()``` メソッド内で定義された変数 ```a``` と ```b``` の値をコンソールウィンドウに出力することで、変数に正しい値が代入されているかを確認します。

```python
def execute(self, context):
    a = 50
    b = 4.0
    print("a=%d, b=%f" % (a, b))
```

```execute()``` メソッドが実行されると、コンソールウィンドウには以下のように表示されます。

```python
a=50, b=4.0
```

<div id="column"></div>

Pythonコンソールウィンドウからbpy.ops.XXX（XXX：オペレーションクラスのbl_idname）を実行してアドオンの処理を行った場合、print()関数の出力先はPythonコンソールウィンドウになります。

<div id="space_m"></div>


## 外部デバッガを利用したデバッグ

これまで紹介した2つのデバッグ手法は、確認したい変数を表示するための処理をソースコード内に記載する必要があるため、あまり効率的ではありません。これらのデバッグ手法を採用した場合でもデバッグすることはできますが、デバッグが難航している場合は、外部のデバッガを利用してデバッグすることも検討するべきです。

ここでは外部デバッガとしてPyDevを利用し、統合開発環境(IDE)であるEclipseを利用することで、GUIベースでデバッグできるようにします。外部デバッガを利用したデバッグの手順を以下に示します。

<div id="custom_ol"></div>

1. PyDevとEclipseのインストール
2. デバッグ用プロジョクトの作成
3. デバッグ実行のためのPythonスクリプトの作成
4. PyDevデバッグサーバの起動
5. デバッグ開始

これから各手順について詳細な手順を説明していきます。

### 1. EclipseとPyDevのインストール

デバッグを実行するために、EclipseとPyDevをインストールします。

#### Eclipseのインストール

Eclipseのホームページから、最新版のEclipseをダウンロードします。

<div id="webpage"></div>

|Eclipse ダウンロードページ|
|---|
|https://www.eclipse.org/downloads/|
|![Eclipse ダウンロードページ](https://dl.dropboxusercontent.com/s/5jk44fvtrmkat80/eclipse_download.png "Eclipse ダウンロードページ")|

Eclipseは、JavaやC/C++、PHPなど様々なプログラミング言語に対応しているIDEですが、ここではJava用のEclipseを利用します。

Eclipseを利用するためにはJava SEがインストールされている必要があるため、もしインストールされていない場合はJava SEをインストールしてください。

<div id="webpage"></div>

|Java SE ダウンロードページ|
|---|
|http://www.oracle.com/technetwork/java/javase/downloads/index.html|
|![Java SE ダウンロードページ](https://dl.dropboxusercontent.com/s/bc4nbfq66358u5h/javase_download.png "Java SE ダウンロードページ")|

#### PyDevのインストール

ダウンロードしたEclipseを起動します。

Eclipseが起動したら、以下の手順に沿ってPyDevをインストールします。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|Help > Install New Software...をクリックします|![PyDevのインストール 手順1](https://dl.dropboxusercontent.com/s/n41n3g8fa4cytvv/install_pydev_1.png "PyDevのインストール 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|Available SoftwareウィンドウのAdd...をクリックします|![PyDevのインストール 手順2](https://dl.dropboxusercontent.com/s/9hwwncn3xeie2si/install_pydev_2.png "PyDevのインストール 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|NameにPyDevを、Locationに http://pydev.org/updates を入力して OK をクリックします|![PyDevのインストール 手順3](https://dl.dropboxusercontent.com/s/mcs991y9iucacz6/install_pydev_3.png "PyDevのインストール 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|しばらく経つと、Available SoftwareウィンドウにPyDevが追加されると思いますので、選択後にContact all update sites during install to find required softwareのチェックボックスを外し、Next >をクリックします|![PyDevのインストール 手順4](https://dl.dropboxusercontent.com/s/xm1f3c7pytrs7j1/install_pydev_4.png "PyDevのインストール 手順4")|
|---|---|---|

<div id="column"></div>

注意：Contact all update sites during install to find required softwareのチェックボックスのチェックを外さないと、本ステップが完了するまでに長い時間がかかってしまいます。

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|Install DetailsウィンドウのNext >をクリックします|![PyDevのインストール 手順5](https://dl.dropboxusercontent.com/s/uogvhp6ltvsdt88/install_pydev_5.png "PyDevのインストール 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|Review Licensesウィンドウでライセンスに同意した後、Finishをクリックします|![PyDevのインストール 手順6](https://dl.dropboxusercontent.com/s/7qldtykqtvktsn3/install_pydev_6.png "PyDevのインストール 手順6")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">7</div>|PyDevのインストールが完了します|![PyDevのインストール 手順7](https://dl.dropboxusercontent.com/s/pw6z8p67qk2tr3u/install_pydev_7.png "PyDevのインストール 手順7")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">8</div>|Eclipseを再起動します|![PyDevのインストール 手順8](https://dl.dropboxusercontent.com/s/onj8yjj4723yl0j/install_pydev_8.png "PyDevのインストール 手順8")|
|---|---|---|

<div id="process_start_end"></div>

---

### 2. デバッグ用プロジョクトの作成

デバッグ用のEclipseプロジェクトを作成します。

#### Eclipseプロジェクトの作成

Eclipseプロジェクトを以下の手順に沿って作成します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|File - New - Project...をクリックします|![Eclipseプロジェクトの作成 手順1](https://dl.dropboxusercontent.com/s/htzmf81c1umkg3m/setup_eclipse_project_1.png "Eclipseプロジェクトの作成 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|Select a wizardウィンドウから、PyDev - PyDev Projectを選択し、Next >をクリックします|![Eclipseプロジェクトの作成 手順2](https://dl.dropboxusercontent.com/s/xzd20c7dj4oi4m8/setup_eclipse_project_2.png "Eclipseプロジェクトの作成 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|PyDev ProjectウィンドウでProject nameにプロジェクト名を入力し（今回の例ではBlender-Addon-Debugging）、Grammer Versionを3.0、Interpreterをpythonに設定してNext >をクリックします|![Eclipseプロジェクトの作成 手順3](https://dl.dropboxusercontent.com/s/ono341pj3yl1cnf/setup_eclipse_project_3.png "Eclipseプロジェクトの作成 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|Finishをクリックします|![Eclipseプロジェクトの作成 手順4](https://dl.dropboxusercontent.com/s/o7vngybzvl4h4c5/setup_eclipse_project_4.png "Eclipseプロジェクトの作成 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|Eclipseプロジェクトが作成されます|![Eclipseプロジェクトの作成 手順5](https://dl.dropboxusercontent.com/s/1qurjvwmtbmxbkw/setup_eclipse_project_5.png "Eclipseプロジェクトの作成 手順5")|
|---|---|---|

<div id="process_start_end"></div>

---

#### パスの設定

プロジェクト作成後、Blenderに標準で備わっているPythonスクリプト等が置かれているパスを設定します。

<div id="space_xl"></div>


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|作成したプロジェクトを選択した状態で、Project > Propertiesをクリックします|![パスの設定 手順1](https://dl.dropboxusercontent.com/s/rxpoqtgrmbpr4rl/configure_path_1.png "パスの設定 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|左のメニューからPyDev - PYTHONPATHを選択します|![パスの設定 手順2](https://dl.dropboxusercontent.com/s/tkaqudo3ougnen2/configure_path_2.png "パスの設定 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|External Librariesを選択します|![パスの設定 手順3](https://dl.dropboxusercontent.com/s/itz2hzqa9q3oq9i/configure_path_3.png "パスの設定 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|Add source folderをクリックし、以下のパスを追加します <br> ```(BLENDER_BASE_SCRIPT_PATH)/addons``` <br>  ```(BLENDER_BASE_SCRIPT_PATH)/addons/modules``` <br>  ```(BLENDER_BASE_SCRIPT_PATH)/modules``` <br>  ```(BLENDER_BASE_SCRIPT_PATH)/startup```|![パスの設定 手順4](https://dl.dropboxusercontent.com/s/uko6g5ltb04yhqo/configure_path_4.png "パスの設定 手順4")|
|---|---|---|

BLNEDER_BASE_SCRIPT_PATHは、以下に示すようにOS依存です。BLENDER_VERはBlenderのバージョンです。例えばバージョンが2.75aのBlenderを利用している場合は、BLENDER_VERは2.75となります。

|OS|Blender<br>実行ファイルのパス例|BLENDER_BASE_SCRIPT_PATH|
|---|---|---|
|Windows|```C:\path\blender.exe```|```C:\path\(BLENDER_VER)\scripts```|
|Mac|```/path/blender.app```|```/path/blender.app/Contents/Resources/``` <br> ```(BLENDER_VER)/scripts```|
|Linux|```/path/blender```|```/path/(BLENDER_VER)/scripts```|

必要に応じて個人用の作業ディレクトリのパスを追加しても良いです。ここでは上で示したパスに加えて、 ```debug.py``` と ```debuggee.py``` が置かれたディレクトリのパスを指定します。

保存先は、[1-5節](../chapter_01/05_Install_own_Add-on.md) を参照してください。

<div id="process_start_end"></div>

---

### 3. デバッグ実行のためのPythonスクリプト作成

デバッグ実行するためのPythonスクリプトを作成します。

以下のようなスクリプトを、ファイル名 ```debug.py``` として作成してください。

[import](../../sample/src/chapter_04/sample_4-2/debug.py)

ここで ```PYDEV_SRC_DIR``` にはPyDevが置かれたディレクトリを指定しますが、環境によりPyDevが置かれたディレクトリが異なるため、各自で確認する必要があります。筆者のMac環境ではPyDevの場所は ```~/.p2/pool/plugins/org.python.pydev_XXX/pysrc``` でした。（```XXX```はPyDevのバージョンです。）

次に、デバッグ対象とするアドオンを用意します。本節のサンプルでは以下のデバッグ対象するアドオンを作成し、ファイル名 ```debugee.py``` として作成します。

なお、```debug.py``` と ```debugee.py``` は同じディレクトリに置く必要があります。本節のサンプルは、本書でこれまで紹介してきたサンプルの場所と同じディレクトリに保存します。保存先は、 [1-5節](../chapter_01/05_Install_own_Add-on.md) を参照してください。

[import](../../sample/src/chapter_04/sample_4-2/debuggee.py)

アドオン有効化時にデバッグを開始するために、 ```debug.py``` をインポートし、デバッグを開始する場所に ```debug.start_debug()``` 関数を追加します。

これで ```debug.start_debug()``` 関数を通ると、デバッグが開始されるようになりました。

### 4. PyDevデバッグサーバの起動

#### EclipseにBlenderを登録

PyDevデバッグサーバをEclipseから起動するために、以下の方法でBlenderをEclipseから実行できるようにします。

<div id="space_m"></div>


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|Run > External Tools > External Tools Configurations...をクリックします|![EclipseにBlenderを登録 手順1](https://dl.dropboxusercontent.com/s/yudnrn16tz821op/register_blender_to_eclipse_1.png "EclipseにBlenderを登録 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|表示されたウィンドウで、Programをダブルクリックします|![EclipseにBlenderを登録 手順2](https://dl.dropboxusercontent.com/s/cjybhosb2649upd/register_blender_to_eclipse_2.png "EclipseにBlenderを登録 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|Mainタブを選択し、LocationにBlenderの実行ファイルのパス、Working DirectoryにBlenderの実行ファイルが置かれたディレクトリを入力します。<br>Nameには任意の名前を入力します。（ここでは、New_Configurationを入力しています）|
|---|---|---|

OSごとのBlender実行ファイルのパスを以下に示します。Blenderのトップディレクトリ（Blenderを非インストーラ版(zip版)でダウンロードした時に、ダウンロードしたファイルを解凍したディレクトリ）を ```/path``` とした時のBlenderの実行ファイルのパスを示しています。

|OS|パス|
|---|---|
|Windows|```/path/blender.exe```|
|Mac|```/path/blender.app/Contents/MacOS/blender```|
|Linux|```/path/blender```|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|Applyをクリックします。|![EclipseにBlenderを登録 手順3](https://dl.dropboxusercontent.com/s/305zw5lym8bhoja/register_blender_to_eclipse_3.png "EclipseにBlenderを登録 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---

#### デバッグサーバの起動

最後に以下の手順で、PyDevデバッグサーバを起動します。

<div id="space_xxxl"></div>


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|Window > Perspective > Open Perspective > Other...をクリックします|![デバッグサーバの起動 手順1](https://dl.dropboxusercontent.com/s/srlqpa41rwqtcbg/run_debug_server_1.png "デバッグサーバの起動 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|Debugを選択し、OKボタンをクリックしてDebugパースペクティブを開きます|![デバッグサーバの起動 手順2](https://dl.dropboxusercontent.com/s/z2aqd3b3i8e1u3c/run_debug_server_2.png "デバッグサーバの起動 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|Pydev > Start Debug Serverをクリックします|![デバッグサーバの起動 手順3](https://dl.dropboxusercontent.com/s/zxrckr9gfrxrkxd/run_debug_server_3.png "デバッグサーバの起動 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|デバッグサーバが起動します|![デバッグサーバの起動 手順4](https://dl.dropboxusercontent.com/s/stxtk3q6glfo925/run_debug_server_4.png "デバッグサーバの起動 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---

### 5. デバッグ開始

ここまで順調に設定できていれば、以下のような画面が表示されているはずです。

![デバッグ開始 手順1](https://dl.dropboxusercontent.com/s/a4ktv1sy6bv7duc/start_debug_1.png "デバッグ開始 手順1")

先ほど作成した ```debug.py``` と ```debuggee.py``` は、 ```PyDev Package Explorer``` の ```scripts/addons``` から参照することができます。

なお、 ```PyDev Package Explorer``` には2つの ```scripts/addons``` が表示されていますが、片方はサポートレベルがOfficialであるアドオン群が格納されています。ここでは自分が作成したアドオンを参照する必要があるので、 ```debug.py``` と ```debuggee.py``` が格納されている ```scripts/addons``` を参照するようにしてください。

以下の手順に従って、EclipseからBlenderを起動してアドオンをデバッグします。ここでは、 ```debugee.py``` の28行目が実行された時にプログラムを一時的に止めて、デバッグモードになるようにします。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|ソースコードの行番号の隣の灰色部分をクリックし、 ```debugee.py``` の28行目にブレークポイントを設定します。|![デバッグ開始 手順2](https://dl.dropboxusercontent.com/s/yo1ij0wqrf6fzw5/start_debug_2.png "デバッグ開始 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|Run > External Tools > External Tools Configurations...をクリックします|![デバッグ開始 手順3](https://dl.dropboxusercontent.com/s/ma36nv5q2br1hvb/start_debug_3.png "デバッグ開始 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|New_Configurationを選択し、Runボタンをクリックします。<br>以降は、Run > External Tools > New_ConfigurationからBlenderを起動することができるようになります|![デバッグ開始 手順4](https://dl.dropboxusercontent.com/s/wdphxp2edjuvees/start_debug_4.png "デバッグ開始 手順4")<br><br>![デバッグ開始 手順5](https://dl.dropboxusercontent.com/s/wir3l0phuez9v1b/start_debug_5.png "デバッグ開始 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|Blenderが起動します|![デバッグ開始 手順6](https://dl.dropboxusercontent.com/s/lcy17hstd76pfe5/start_debug_6.png "デバッグ開始 手順6")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|作成したアドオンを有効化します|![デバッグ開始 手順7](https://dl.dropboxusercontent.com/s/w0en5mwd5fgpmm6/start_debug_7.png "デバッグ開始 手順7")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|デバッガが起動します|![デバッグ開始 手順8](https://dl.dropboxusercontent.com/s/876yphkm0qjolcp/start_debug_8.png "デバッグ開始 手順8")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">7</div>|Debugパースペクティブで、Resumeボタンを押します|![デバッグ開始 手順9](https://dl.dropboxusercontent.com/s/d211w8m59e5tubf/start_debug_9.png "デバッグ開始 手順9")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">8</div>|3Dビューのメニューで、追加 > メッシュ > デバッグのテストを実行します|![デバッグ開始 手順10](https://dl.dropboxusercontent.com/s/mg5rywpsvq17s0w/start_debug_10.png "デバッグ開始 手順10")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">9</div>|設定したブレークポイントでプログラムが止まります。|![デバッグ開始 手順11](https://dl.dropboxusercontent.com/s/b51idbmcjdjyiuz/start_debug_11.png "デバッグ開始 手順11")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">10</div>|Debugパースペクティブで変数値などを参照することができます。<br>この他にもEclipseには様々な機能が備わっていますが、ここでは割愛します。|![デバッグ開始 手順12](https://dl.dropboxusercontent.com/s/m95irzuut9ngloh/start_debug_12.png "デバッグ開始 手順12")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">11</div>|デバッグを終了するためには、DebugタブのNew_Configurationを選択した状態で赤い四角のボタンを押します。|![デバッグ開始 手順13](https://dl.dropboxusercontent.com/s/3kjwzrvham4yxtd/start_debug_13.png "デバッグ開始 手順13")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">12</div>|デバッグが終了します。この時、Debug Serverは起動したままになります。もしDebug Serverも終了する場合は、DebugタブのDebug Serverを選択した状態で赤い四角のボタンを押します。|![デバッグ開始 手順14](https://dl.dropboxusercontent.com/s/70nztthhb4hm7wo/start_debug_14.png "デバッグ開始 手順14")|
|---|---|---|

<div id="process_start_end"></div>

---

## アドオン『BreakPoint』を利用したデバッグ

Eclipseを用いたデバッグは準備が非常に大変です。手間をかけずにデバッグしたい方は、アドオン『BreakPoint』の利用を検討しましょう。

アドオン『BreakPoint』を利用したデバッグは、以下の手順で行います。

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

<div id="space_xxl"></div>


### 2. アドオン『BreakPoint』の有効化

<div id="sidebyside"></div>

|インストールしたアドオンを有効化します。|![『BreakPoint』の有効化](https://dl.dropboxusercontent.com/s/b6ofwmbcsw4qkyj/enable_breakpoint.png "『BreakPoint』の有効化")|
|---|---|


### 3. ブレークポイントをデバッグ対象のスクリプトに設定

以下のようなデバッグ対象のアドオンを作成し、 ```debuggee_2.py``` として保存します。

[import](../../sample/src/chapter_04/sample_4-2/debuggee_2.py)

ブレークポイントを設定する関数は ```bpy.types.bp.bp()``` ですが、毎回関数名を書くのは冗長ですので、以下のように ```breakpoint()``` と書くだけで呼び出せるようにします。

```python
# ブレークポイント関数
breakpoint = bpy.types.bp.bp
```

以降ブレークポイントを設定する時は、ブレークポイントを設定したい場所で ```breakpoint()``` 関数を実行すれば良いです。

```breakpoint()``` 関数の第1引数には変数のスコープの辞書（ローカル変数であれば ```locals()``` 、グローバル変数であれば ```globals()```）、第2引数には確認したい変数を指定します。

### 4. デバッグ開始

以下の手順に従って、デバッグを開始します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*テキストエディター* エリアのメニューで、ビュー > プロパティを実行し、*テキストエディター* エリアのプロパティを表示します。|![デバッグ 手順1](https://dl.dropboxusercontent.com/s/bu01qdhpcstfb16/start_bp_debug_1.png "デバッグ 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|プロパティを表示すると、BreakPointメニューが追加されていることが確認できます。<br>BreakPointメニューを確認し、有効化されていることを確認します。|![デバッグ 手順2](https://dl.dropboxusercontent.com/s/quxp3yhoj9r9q01/start_bp_debug_2.png "デバッグ 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|3Dビューエリアのメニューで、追加 > メッシュ > デバッグのテスト2を実行します。|![デバッグ 手順3](https://dl.dropboxusercontent.com/s/wmmy34dyq4ktvvj/start_bp_debug_3.png "デバッグ 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*テキストエディター* エリアのプロパティにブレークポイントの関数に指定した変数の値が表示されます。|![デバッグ 手順4](https://dl.dropboxusercontent.com/s/fmfykni3dax1vgt/start_bp_debug_4.png "デバッグ 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.md) で紹介した方法でBlenderをコンソールウィンドウから開いた場合は、コンソールウィンドウにもデバッグ情報が表示されているはずです。  
またコンソールウィンドウから起動した場合に限り、Blender本体からコンソールウィンドウに制御が移ります。制御が移っている間は、コンソールウィンドウでPythonインタープリタを使うことができますが、Blenderでいかなる操作も受け付けなくなります。  
Blender本体に制御を戻す（アドオンの実行を再開する）場合は、WindowsではCtrl+Zキーを、 Mac/LinuxではCtrl+Dキーを押してください。


## まとめ

本節ではアドオンをデバッグする方法を紹介しましたが、本節で紹介したそれぞれのデバッグについて簡単にまとめました。

|デバッグ方法|できること|前準備|
|---|---|---|
|self.report|スクリプト実行ログに出力可能な処理の中での変数値確認|ソースコードの調べたい箇所に ```self.report()``` メソッドを追加|
|print|すべての変数値確認|コンソールウィンドウからBlenderを起動、ソースコードの調べたい箇所に ```print()``` 関数を追加|
|外部デバッガ|ブレークポイント設定やコールトレース調査、変数値確認などEclipseが持つデバッガ機能の利用|EclipseやPyDevのインストール、EclipseとBlenderの連携、デバッグ実行用スクリプトの作成|
|デバッガアドオン『BreakPoint』|ブレークポイント設定、変数値確認|アドオン『BreakPoint』のインストール、ブレークポイント設定のためのソースコード編集|

多くの情報を得ることのできるデバッグ方法は、必要な前準備が基本的に多くなる傾向があります。問題解決の難しさと準備時間を見極めて適宜デバッグ方法を選択すべきです。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderをデバッグする方法として、確認対象の変数を出力する他に、外部デバッガやデバッグ用アドオンを用いる方法がある
* 前準備が多いデバッグ方法は準備が大変な分、より多くの情報をデバッグ時に得ることができる

<div id="space_page"></div>
