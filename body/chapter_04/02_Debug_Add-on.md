<div id="sect_title_img_4_2"></div>

<div id="sect_title_text"></div>

# アドオンをデバッグする

<div id="preface"></div>

###### プログラムを作ったことがある方は知っていると思いますが、ソフトウェアにバグはつきものです。そしてそれは、Blenderアドオンでも同じことが言えます。<br>発生したバグの原因を調べて修正するためにかかる時間は、アドオン開発の大半の時間を占めることが多いため、できることならバグを修正する時間を短くし、本来の開発に注力したいと考えるのが普通です。そこで本節では、バグの原因を効率的に調べる（デバッグ）方法について説明します。


## アドオンのデバッグ手段

プログラムで発生したバグを取り除く作業は、一般的にデバッグと呼ばれます。Blenderのアドオン開発もプログラムを作ることと同じですので、ここでもバグを取り除く作業をデバッグと呼ぶことにします。Blenderのアドオン開発においてデバッグする手段はいくつかありますが、通常のプログラム開発と異なり、デバッグ手段が確立していません。このため本節では、筆者が行っている次のデバッグ方法について説明します。

* self.reportデバッグ
* printデバッグ
* 外部デバッガを利用したデバッグ
* アドオン『BreakPoint』を利用したデバッグ


## self.reportデバッグ

タイトルの通り、スクリプト実行ログに文字列を出力する ```self.report()``` メソッドを使ったデバッグ手法です。```self.report()``` メソッドの第2引数に出力する文字列を渡しますが、ここに確認したい変数の値を指定することで変数の値をスクリプト実行ログに表示させます。そして、表示された変数の値を見て、期待した値が保存されていることを確認します。

self.reportデバッグの例を次に示します。次の例では、```execute()``` メソッド内で定義された変数 ```a``` と ```b``` の値をスクリプト実行ログに表示することで、それぞれの変数に正しい値が代入されていることを確認します。

```python
def execute(self, context):
    a = 50
    b = 4.0
    self.report({'INFO'}, "a=%d, b=%f" % (a, b))
```

この例で ```execute()``` メソッドが実行されると、次のように変数 ```a``` と ```b``` の値がスクリプト実行ログに出力されます。

```python
a=50, b=4.0
```

self.reportデバッグは、変数を表示したい箇所に ```self.report()``` メソッドを記述するだけで良いため、他のデバッグ方法に比べて手軽にデバッグを行える点がメリットです。ただし、```modal()``` メソッド内などの ```self.report()``` メソッドを利用できない処理の中では、デバッグできないことに注意する必要があります。このように、```self.report()``` メソッドを利用できない処理の中で変数の値を確認したい場合は、次に紹介するprintデバッグを利用する必要があります。


## printデバッグ

こちらもタイトル通り、コンソールウィンドウに文字列を出力する ```print()``` 関数を用いたデバッグ手法です。self.reportデバッグと同じように、確認したい変数の値を表示させてデバッグを行う方法ですが、self.reportデバッグでは確認できない ```modal()``` メソッドなどの処理で使用している変数についても、確認することができます。ただし、```print()``` 関数の出力先はコンソールウィンドウであるため、[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.md)を参考にして、コンソールウィンドウからBlenderを起動する必要があります。

次の例では、```execute()``` メソッド内で定義された変数 ```a``` と ```b``` の値をコンソールウィンドウに出力することで、変数に正しい値が代入されているかを確認します。

```python
def execute(self, context):
    a = 50
    b = 4.0
    print("a=%d, b=%f" % (a, b))
```

この例で ```execute()``` メソッドが実行されると、次のように変数 ```a``` と ```b``` の値がコンソールウィンドウに出力されます。

```python
a=50, b=4.0
```

<div id="column"></div>

Pythonコンソールウィンドウから、bpy.ops.XXX（XXX：オペレーションクラスのbl_idname）を実行してアドオンの処理を行った場合、print()関数の出力先はPythonコンソールウィンドウになります。


## 外部デバッガを利用したデバッグ

ここまでに紹介した2つのデバッグ手法は、確認したい変数を表示するための処理をソースコード内に毎回追加する必要があるため、あまり効率的ではありません。また、デバッグが終わったあとに追加した処理を削除する必要があり、削除中に誤って別の処理を削除するなどのバグが発生してしまう可能性があります。もちろん簡単なデバッグ目的であれば、これらの手法でデバッグしてもよいのですが、デバッグが難航している場合は、外部のデバッガを使ってデバッグすることも検討してみましょう。

ここでは外部デバッガとしてPyDevを利用し、統合開発環境（IDE）であるEclipseを利用することで、GUIベースでデバッグできるようにします。デバッグの手順を次に示します。


<div id="custom_ol"></div>

1. PyDevとEclipseのインストール
2. デバッグ用Eclipseプロジョクトの作成
3. デバッグ実行のためのPythonスクリプトの作成
4. PyDevデバッグサーバの起動
5. デバッグ開始


これからそれぞれの手順について、詳細な手順を説明していきます。


### 1. EclipseとPyDevのインストール

最初に、IDEのEclipseとデバッガPyDevをインストールします。


#### Eclipseのインストール

Eclipseのホームページから、最新版のEclipseをダウンロードします。


<div id="webpage"></div>

|Eclipse ダウンロードページ|
|---|
|https://www.eclipse.org/downloads/|
|![Eclipse ダウンロードページ](https://dl.dropboxusercontent.com/s/5jk44fvtrmkat80/eclipse_download.png "Eclipse ダウンロードページ")|


Eclipseは、JavaやC/C++、PHPなど様々なプログラミング言語に対応しているIDEですが、ここではJava用のEclipseを利用します。Blenderのアドオンの言語がPythonであることから、PythonのプログラムをデバッグするのにJava用のEclipseをなぜ使うのか、疑問に思うかもしれません。その理由は、Python向けに提供されているEclipseが存在しないからです。このため、Java用のEclipseにPython用のデバッガPyDevを追加することで、Pythonで書かれたプログラムをEclipseでデバッグできるようにします。

Eclipseを動作させるためには、Java SEがインストールされている必要があります。もし、読者のPCにEclipseがインストールされていない場合は、Java SEのダウンロードページからダウンロードして、インストールしてください。


<div id="webpage"></div>

|Java SE ダウンロードページ|
|---|
|http://www.oracle.com/technetwork/java/javase/downloads/index.html|
|![Java SE ダウンロードページ](https://dl.dropboxusercontent.com/s/bc4nbfq66358u5h/javase_download.png "Java SE ダウンロードページ")|


#### PyDevのインストール

続いて、Python用のデバッガPyDevをインストールします。ダウンロードしたEclipseを起動し、次の手順に従ってPyDevをインストールします。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|メニューから *Help* > *Install New Software...* を実行します。|![PyDevのインストール 手順1](https://dl.dropboxusercontent.com/s/n41n3g8fa4cytvv/install_pydev_1.png "PyDevのインストール 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*Available Software* ウィンドウの *Add...* をクリックします。|![PyDevのインストール 手順2](https://dl.dropboxusercontent.com/s/9hwwncn3xeie2si/install_pydev_2.png "PyDevのインストール 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*Name* に ```PyDev``` を、*Location* に ```http://pydev.org/updates``` を入力して *OK* ボタンをクリックします。|![PyDevのインストール 手順3](https://dl.dropboxusercontent.com/s/mcs991y9iucacz6/install_pydev_3.png "PyDevのインストール 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|手順3の処理は少し時間がかかりますが、処理が終わると *Available Software* ウィンドウに *PyDev* が追加されると思いますので、*PyDev* のチェックボックスにチェックを入れたあと、*Contact all update sites during install to find required software* のチェックボックスのチェックを外し、*Next >* ボタンをクリックします。|![PyDevのインストール 手順4](https://dl.dropboxusercontent.com/s/xm1f3c7pytrs7j1/install_pydev_4.png "PyDevのインストール 手順4")|
|---|---|---|

<div id="tips"></div>

Contact all update sites during install to find required softwareのチェックボックスのチェックを外さないと、本ステップが完了するまでに長い時間がかかってしまいます。

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|*Install Details* ウィンドウの *Next >* ボタンをクリックします。|![PyDevのインストール 手順5](https://dl.dropboxusercontent.com/s/uogvhp6ltvsdt88/install_pydev_5.png "PyDevのインストール 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|*Review Licenses* ウィンドウでライセンスに同意し、*Finish* をクリックします。|![PyDevのインストール 手順6](https://dl.dropboxusercontent.com/s/7qldtykqtvktsn3/install_pydev_6.png "PyDevのインストール 手順6")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">7</div>|PyDevのインストールが完了します。|![PyDevのインストール 手順7](https://dl.dropboxusercontent.com/s/pw6z8p67qk2tr3u/install_pydev_7.png "PyDevのインストール 手順7")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">8</div>|Eclipseを再起動します。|![PyDevのインストール 手順8](https://dl.dropboxusercontent.com/s/onj8yjj4723yl0j/install_pydev_8.png "PyDevのインストール 手順8")|
|---|---|---|

<div id="process_start_end"></div>

---


<div id="space_m"></div>


### 2. デバッグ用Eclipseプロジョクトの作成

アドオンをデバッグするためのEclipseプロジェクトを作成します。


#### Eclipseプロジェクトの作成

Eclipseプロジェクトを、次の手順に従って作成します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|メニューから *File* > *New* > *Project...* を実行します。|![Eclipseプロジェクトの作成 手順1](https://dl.dropboxusercontent.com/s/htzmf81c1umkg3m/setup_eclipse_project_1.png "Eclipseプロジェクトの作成 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*Select a wizard* ウィンドウから *PyDev* > *PyDev Project* を選択し、*Next >* ボタンをクリックします。|![Eclipseプロジェクトの作成 手順2](https://dl.dropboxusercontent.com/s/xzd20c7dj4oi4m8/setup_eclipse_project_2.png "Eclipseプロジェクトの作成 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*PyDev Project* ウィンドウで *Project name* にプロジェクト名を入力し（今回の例では ```Blender-Addon-Debugging```）、*Grammer Version*を *3.0*、*Interpreter* を *python* に設定し、*Next >* ボタンをクリックします。|![Eclipseプロジェクトの作成 手順3](https://dl.dropboxusercontent.com/s/ono341pj3yl1cnf/setup_eclipse_project_3.png "Eclipseプロジェクトの作成 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*Reference page* ウィンドウが表示されたら、*Finish* をクリックします。|![Eclipseプロジェクトの作成 手順4](https://dl.dropboxusercontent.com/s/o7vngybzvl4h4c5/setup_eclipse_project_4.png "Eclipseプロジェクトの作成 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|Eclipseプロジェクトが作成されます。|![Eclipseプロジェクトの作成 手順5](https://dl.dropboxusercontent.com/s/1qurjvwmtbmxbkw/setup_eclipse_project_5.png "Eclipseプロジェクトの作成 手順5")|
|---|---|---|

<div id="process_start_end"></div>

---


#### パスの設定

Eclipseプロジェクトを作成した直後では、```bpy``` モジュールなどのBlender本体と一緒に提供されるPythonモジュールなどへのパスが通っていないため、Blenderが提供するAPIを使うことができません。そこで、作成したEclipseプロジェクトに対してBlenderが提供するモジュールへのパスを設定します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*Package Explorer* において作成したプロジェクトを選択した状態で、メニュー *Project* > *Properties* をクリックします。|![パスの設定 手順1](https://dl.dropboxusercontent.com/s/rxpoqtgrmbpr4rl/configure_path_1.png "パスの設定 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|表示されたウィンドウの左のメニューから、*PyDev - PYTHONPATH* を選択します。|![パスの設定 手順2](https://dl.dropboxusercontent.com/s/tkaqudo3ougnen2/configure_path_2.png "パスの設定 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|ウィンドウ右側のタブから *External Libraries* を選択します。|![パスの設定 手順3](https://dl.dropboxusercontent.com/s/itz2hzqa9q3oq9i/configure_path_3.png "パスの設定 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*Add source folder* ボタンをクリックし、以下のパスを追加します <br> ```(BLENDER_BASE_SCRIPT_PATH)/addons``` <br>  ```(BLENDER_BASE_SCRIPT_PATH)/addons/modules``` <br>  ```(BLENDER_BASE_SCRIPT_PATH)/modules``` <br>  ```(BLENDER_BASE_SCRIPT_PATH)/startup```|![パスの設定 手順4](https://dl.dropboxusercontent.com/s/uko6g5ltb04yhqo/configure_path_4.png "パスの設定 手順4")|
|---|---|---|

ここで ```BLENDER_BASE_SCRIPT_PATH``` は、次に示すようにOS依存です（```BLENDER_VER``` はBlenderのバージョンです）。例えばバージョンが2.75aのBlenderを利用している場合は、```BLENDER_VER``` は ```2.75``` となります。

|OS|Blender<br>実行ファイルのパス例|BLENDER_BASE_SCRIPT_PATH|
|---|---|---|
|Windows|```C:\path\blender.exe```|```C:\path\(BLENDER_VER)\scripts```|
|Mac|```/path/blender.app```|```/path/blender.app/Contents/Resources/``` <br> ```(BLENDER_VER)/scripts```|
|Linux|```/path/blender```|```/path/(BLENDER_VER)/scripts```|

また、必要に応じて個人用の作業ディレクトリのパスを追加してもよいです。パスを追加することで、作業用ディレクトリのファイルがウィンドウ左側の *PyDev Package Explorer* に表示されるようになります。ここでは上で示したパスに加えて、```debug.py``` と ```debuggee.py``` が置かれたディレクトリのパスを指定します。これらのファイルの置き場所は、本書でこれまで紹介してきたサンプルの場所と同じディレクトリです。

<div id="process_start_end"></div>

---


### 3. デバッグ実行のためのPythonスクリプト作成

デバッグを行うために必要なプロジェクトの設定は終わったため、次にデバッグ実行するための関数が定義されたPythonモジュールを作成します。次に示すスクリプトを、ファイル名 ```debug.py``` として作成してください。

[import](../../sample/src/chapter_04/sample_4_2/debug.py)

PyDevを使うためには、```pydevd``` モジュールをインポートして ```pydevd.settrace()``` を呼び出す必要があり、作成したモジュールでは ```start_debug()``` 関数がその役割を担っています。このためデバッグされる側のPythonスクリプトは、```debug``` をインポートして ```debug.start_debug()``` 関数を呼び出すことでデバッグを開始することができます。

ここで ```pydevd``` モジュールをインポートする前に、PyDevのパスを ```sys.path``` に追加しています。パスを追加しないと ```pydevd``` が見つからずインポートできません。```PYDEV_SRC_DIR``` にはPyDevが置かれたディレクトリを指定しますが、環境によってPyDevが置かれるディレクトリが異なるため、各自で確認する必要があります。筆者のMac環境ではPyDevの場所は ```~/.p2/pool/plugins/org.python.pydev_XXX/pysrc``` でした（```XXX```はPyDevのバージョンです）。

ちなみに ```debug.py``` には、グローバル変数 ```DEBUGGING``` が定義されています。常にデバッグしたいとは限らないと思い、```DEBUGGING``` を ```True``` にしたときのみデバッグするようになっています。

続いて、デバッグ対象とするアドオンを作成します。ここでは次に示すアドオンを作成し、ファイル名 ```debugee.py``` として作成します。なお、```debug.py``` と ```debugee.py``` は同じディレクトリに置く必要があり、ここでは、本書でこれまで紹介してきたサンプルの場所と同じディレクトリに保存します。保存先は、 [1-5節](../chapter_01/05_Install_own_Add-on.md)を参照してください。

[import](../../sample/src/chapter_04/sample_4_2/debuggee.py)

最初に、先ほど作成した ```debug``` モジュールをインポートします。そして、アドオン有効化時にデバッグを開始するために、```register()``` 関数で ```debug.start_debug()``` 関数を実行します。これでアドオンを有効化したときに、デバッグが開始されるようになりました。なお、ここで紹介したアドオンは特に新しいことは行っていないため、ソースコードの解説はしません。


<div id="space_s"></div>


### 4. PyDevデバッグサーバの起動

3で作成したデバッグ実行のためのPythonスクリプトを実行するだけでは、デバッグすることはできません。PyDevにはデバッグサーバと呼ばれる機能があり、デバッグサーバにシグナルを送ることでデバッグを行います。このため、スクリプト実行前にPyDevデバッグサーバを事前に起動しておく必要があります。


#### EclipseからBlenderを実行できるようにする

BlenderをEclipseから実行できるように設定し、Blenderのアドオン処理中にPyDevデバッグサーバに対してシグナルを送れるようにします。


<div id="process_title"></div>

##### Work


<div id="process"></div>

|<div id="box">1</div>|メニューから *Run* > *External Tools* > *External Tools Configurations...* を実行します。|![EclipseにBlenderを登録 手順1](https://dl.dropboxusercontent.com/s/yudnrn16tz821op/register_blender_to_eclipse_1.png "EclipseにBlenderを登録 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|表示されたウィンドウの左側にある、*Program*をダブルクリックします。|![EclipseにBlenderを登録 手順2](https://dl.dropboxusercontent.com/s/cjybhosb2649upd/register_blender_to_eclipse_2.png "EclipseにBlenderを登録 手順2")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process_noimg"></div>

|<div id="box">3</div>|ウィンドウ左側の *Main* タブを選択し、*Location* にBlenderの実行ファイルのパス、*Working Directory* にBlenderの実行ファイルが置かれたディレクトリを入力します。<br>*Name* には任意の名前を入力します。ここでは、```New_Configuration``` を入力します。|
|---|---|---|

Blenderの実行ファイルのパスは、OSごとに異なります。Blenderのトップディレクトリ（Blenderを非インストーラ版、すなわちzip版でダウンロードした時に、ダウンロードしたファイルを解凍したディレクトリ）を ```/path``` としたときの、Blenderの実行ファイルのパスを次に示します。

|OS|パス|
|---|---|
|Windows|```/path/blender.exe```|
|Mac|```/path/blender.app/Contents/MacOS/blender```|
|Linux|```/path/blender```|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">4</div>|最後に、*Apply* ボタンをクリックします。|![EclipseにBlenderを登録 手順3](https://dl.dropboxusercontent.com/s/305zw5lym8bhoja/register_blender_to_eclipse_3.png "EclipseにBlenderを登録 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---

#### デバッグサーバの起動

続いて、PyDevデバッグサーバを起動します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|メニューから、*Window* > *Perspective* > *Open Perspective* > *Other...* を実行します。|![デバッグサーバの起動 手順1](https://dl.dropboxusercontent.com/s/srlqpa41rwqtcbg/run_debug_server_1.png "デバッグサーバの起動 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|表示されたウィンドウで *Debug* を選択し、*OK* ボタンをクリックして *Debugパースペクティブ* を開きます。|![デバッグサーバの起動 手順2](https://dl.dropboxusercontent.com/s/z2aqd3b3i8e1u3c/run_debug_server_2.png "デバッグサーバの起動 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|メニューから *Pydev* > *Start Debug Server* を実行します。|![デバッグサーバの起動 手順3](https://dl.dropboxusercontent.com/s/zxrckr9gfrxrkxd/run_debug_server_3.png "デバッグサーバの起動 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|デバッグサーバが起動します。|![デバッグサーバの起動 手順4](https://dl.dropboxusercontent.com/s/stxtk3q6glfo925/run_debug_server_4.png "デバッグサーバの起動 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---


### 5. デバッグ開始

ここまで順調に手順を踏めていれば、次のような画面が表示されているはずです。

![デバッグ開始 手順1](https://dl.dropboxusercontent.com/s/a4ktv1sy6bv7duc/start_debug_1.png "デバッグ開始 手順1")

3で作成したソースコード ```debug.py``` と ```debuggee.py``` は、*PyDev Package Explorer* の *scripts/addons* から参照することができます。

なお、*PyDev Package Explorer* には2つの *scripts/addons* が表示されていますが、片方はサポートレベルがOfficialであるアドオンが配置されています。ここでは、作成したアドオンのデバッグを行うため、```debug.py``` と ```debuggee.py``` が配置されているほうの *scripts/addons* を参照するようにしてください。

さて、いよいよEclipseからBlenderを起動してアドオンをデバッグします。ここでは、```debugee.py``` に定義された ```DebugTestOps``` クラスの ```execute()``` メソッドの処理 ```debug_var = debug_var + 30.0``` が実行された時にプログラムを一時的に止めて、デバッグモードに移行するようにします。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|ソースコードの行番号の隣の灰色部分をクリックし、```debugee.py``` に定義された処理 ```debug_var = debug_var + 30.0``` にブレークポイントを設定します。|![デバッグ開始 手順2](https://dl.dropboxusercontent.com/s/yo1ij0wqrf6fzw5/start_debug_2.png "デバッグ開始 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|メニューから *Run* > *External Tools* > *External Tools Configurations...* を実行します。|![デバッグ開始 手順3](https://dl.dropboxusercontent.com/s/ma36nv5q2br1hvb/start_debug_3.png "デバッグ開始 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|表示されたウィンドウの左側から *New_Configuration* を選択し、*Run* ボタンをクリックします。<br>なお次回以降は、*Run* > *External Tools* > *New_Configuration* からBlenderを起動することができるようになります。|![デバッグ開始 手順4](https://dl.dropboxusercontent.com/s/wdphxp2edjuvees/start_debug_4.png "デバッグ開始 手順4")<br><br>![デバッグ開始 手順5](https://dl.dropboxusercontent.com/s/wir3l0phuez9v1b/start_debug_5.png "デバッグ開始 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|Blenderが起動します。|![デバッグ開始 手順6](https://dl.dropboxusercontent.com/s/lcy17hstd76pfe5/start_debug_6.png "デバッグ開始 手順6")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|作成したアドオンを有効化します。|![デバッグ開始 手順7](https://dl.dropboxusercontent.com/s/w0en5mwd5fgpmm6/start_debug_7.png "デバッグ開始 手順7")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|デバッガが起動します。|![デバッグ開始 手順8](https://dl.dropboxusercontent.com/s/876yphkm0qjolcp/start_debug_8.png "デバッグ開始 手順8")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">7</div>|*Debugパースペクティブ* で、*Resume* ボタンを押します。|![デバッグ開始 手順9](https://dl.dropboxusercontent.com/s/d211w8m59e5tubf/start_debug_9.png "デバッグ開始 手順9")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">8</div>|起動中のBlenderに戻り、*3Dビュー* エリアのメニューから、*追加* > *メッシュ* > *デバッグのテスト* を実行します。|![デバッグ開始 手順10](https://dl.dropboxusercontent.com/s/mg5rywpsvq17s0w/start_debug_10.png "デバッグ開始 手順10")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">9</div>|設定したブレークポイントで処理が止まります。|![デバッグ開始 手順11](https://dl.dropboxusercontent.com/s/b51idbmcjdjyiuz/start_debug_11.png "デバッグ開始 手順11")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">10</div>|*Debugパースペクティブ* で変数値などを参照することができます。<br>この他にもEclipseには様々な機能が備わっていますが、ここでは割愛します。|![デバッグ開始 手順12](https://dl.dropboxusercontent.com/s/m95irzuut9ngloh/start_debug_12.png "デバッグ開始 手順12")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">11</div>|デバッグを終了するためには、*Debug* タブの *New_Configuration* を選択した状態で *赤い四角* のボタンを押します。|![デバッグ開始 手順13](https://dl.dropboxusercontent.com/s/3kjwzrvham4yxtd/start_debug_13.png "デバッグ開始 手順13")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">12</div>|デバッグが終了します。この時、Debug Serverは起動したままになります。もしDebug Serverを終了したい場合は、*Debug* タブの *Debug Server* を選択した状態で *赤い四角* のボタンを押します。|![デバッグ開始 手順14](https://dl.dropboxusercontent.com/s/70nztthhb4hm7wo/start_debug_14.png "デバッグ開始 手順14")|
|---|---|---|

<div id="process_start_end"></div>

---


## アドオン『BreakPoint』を利用したデバッグ

EclipseとPyDevを用いたデバッグは、準備に時間がかかります。少しだけデバッガを試してみたいという方にとっては、あまり魅力的ではありません。そこで、手間をかけずにデバッガを利用したい方のために、アドオン『BreakPoint』を利用してデバッグを行う方法を紹介します。前準備はアドオンの導入だけでよいので、EclipseとPyDevによるデバッグと違って、比較的すぐにデバッグ環境を整えることができます。

アドオン『BreakPoint』を利用してデバッグを行う手順を、次に示します。


<div id="custom_ol"></div>

1. アドオン『BreakPoint』のインストール
2. アドオン『BreakPoint』の有効化
3. ブレークポイントをデバッグ対象のスクリプトに設定
4. デバッグ開始


### 1. アドオン『BreakPoint』のインストール

Webサイトからアドオン『BreakPoint』をダウンロードし、インストールします。アドオンのインストールの仕方がわからない場合は、[1-4節](../chapter_01/04_Understand_Install_Uninstall_Update_Add-on.md)を参考にしてください。


<div id="webpage"></div>

|Blender Wiki (Scripts: BreakPoint)|
|---|
|http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Development/BreakPoint|
|![『BreakPoint』のインストール](https://dl.dropboxusercontent.com/s/220ubjo2o4t0t4n/install_breakpoint.png "『BreakPoint』のインストール")|


### 2. アドオン『BreakPoint』の有効化

<div id="sidebyside"></div>

|インストールしたアドオン『BreakPoint』を有効化します。|![『BreakPoint』の有効化](https://dl.dropboxusercontent.com/s/b6ofwmbcsw4qkyj/enable_breakpoint.png "『BreakPoint』の有効化")|
|---|---|


### 3. ブレークポイントをデバッグ対象のスクリプトに設定

デバッグ対象とするアドオンを作成し、```debuggee_2.py``` として保存します。

[import](../../sample/src/chapter_04/sample_4_2/debuggee_2.py)

ブレークポイントを設定するためには、```bpy.types.bp.bp()``` 関数を呼び出す必要がありますが、毎回これを書くのは面倒ですので、次のようにして ```breakpoint()``` と書くだけで呼び出せるようにすると、ブレークポイントの設定が少し楽になるかと思います。

[import:"short_call", unindent:"true"](../../sample_raw/src/chapter_04/sample_4_2/debuggee_2.py)

以降、ブレークポイントを設定する時は、次のようにしてブレークポイントを設定したい場所で ```breakpoint()``` 関数を実行します。

[import:"set_breakpoint", unindent:"true"](../../sample_raw/src/chapter_04/sample_4_2/debuggee_2.py)

```breakpoint()``` 関数の第1引数には、変数のスコープの辞書（ローカル変数であれば ```locals()``` 、グローバル変数であれば ```globals()```）、第2引数には確認したい変数を指定します。サンプルでは、ローカル変数である ```debug_var``` の値を出力するため、第1引数に ```locals()``` 、第2引数に ```globals()``` を指定します。


### 4. デバッグ開始

これで、デバッグを行う準備が整いました。それでは、アドオン『BreakPoint』を使って実際にデバッグを行ってみましょう。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*テキストエディター* エリアのメニューから *ビュー* > *プロパティ* を実行し、*テキストエディター* エリアのプロパティを表示します。|![デバッグ 手順1](https://dl.dropboxusercontent.com/s/bu01qdhpcstfb16/start_bp_debug_1.png "デバッグ 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*プロパティ* を表示すると、項目 *BreakPoint* が追加されていることが確認できます。<br>そして、*有効化* ボタンが選択されていることを確認します。|![デバッグ 手順2](https://dl.dropboxusercontent.com/s/quxp3yhoj9r9q01/start_bp_debug_2.png "デバッグ 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*3Dビュー* エリアのメニューから、*追加* > *メッシュ* > *デバッグのテスト2* を実行します。|![デバッグ 手順3](https://dl.dropboxusercontent.com/s/wmmy34dyq4ktvvj/start_bp_debug_3.png "デバッグ 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*テキストエディター* エリアのプロパティにブレークポイントの関数に指定した変数の値が表示されます。|![デバッグ 手順4](https://dl.dropboxusercontent.com/s/fmfykni3dax1vgt/start_bp_debug_4.png "デバッグ 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.md)で説明した方法で、Blenderをコンソールウィンドウから開いた場合は、コンソールウィンドウにもデバッグ情報が表示されているはずです。  
また、コンソールウィンドウから起動した場合に限り、Blender本体からコンソールウィンドウに制御が移ります。制御が移っている間は、コンソールウィンドウでPythonインタープリタを使うことができますが、Blender側ではいかなる操作も受け付けなくなります。  
Blender本体に制御を戻す（アドオンの実行を再開する）場合は、Windowsでは *Ctrl* + *Z* キーを、 Mac/Linuxでは *Ctrl* + *D* キーを押してください。


## まとめ

本節では、アドオンをデバッグする方法を紹介しました。ここでは、本節で紹介したデバッグについて簡単にまとめます。

|デバッグ方法|できること|前準備|
|---|---|---|
|self.report|スクリプト実行ログに出力可能な処理中での変数値確認|ソースコードの調べたい箇所に ```self.report()``` メソッドを追加|
|print|すべての変数値確認|ソースコードの調べたい箇所に ```print()``` 関数を追加し、コンソールウィンドウからBlenderを起動|
|外部デバッガ|ブレークポイント設定やコールトレース調査、変数値確認など、Eclipseが持つデバッガ機能の利用|EclipseやPyDevのインストール、EclipseとBlenderの連携、デバッグ実行用スクリプトの作成|
|アドオン『BreakPoint』|ブレークポイント設定、変数値確認|アドオン『BreakPoint』のインストール、ブレークポイント設定のためのソースコード編集|

ここで示したように、より多くの情報をデバッグで得る場合は必要な前準備が多くなる傾向があります。解決しようとしている問題の難しさと前準備の時間を合わせて判断し、デバッグする方法を決めましょう。


<div id="space_l"></div>


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* 確認対象の変数をスクリプト実行ログやコンソールウィンドウに出力するほかに、外部デバッガやデバッグするためのアドオンを用いることでも、アドオンをデバッグすることができる
* 前準備が多いデバッグ方法は、デバッグするときにより多くの情報を得ることができる
