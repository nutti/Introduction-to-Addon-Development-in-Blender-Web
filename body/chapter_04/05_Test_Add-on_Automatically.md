<div id="sect_title_img_4_5"></div>

<div id="sect_title_text"></div>

# アドオンの動作テストを自動化する

<div id="preface"></div>

###### [4-3節](03_Publish_your_Add-on.md) にて説明しましたが、アドオンを公開した後はバグ修正や機能追加などアドオンのサポートをきちんと行うべきです。しかし、アドオンのソースコードを修正する度にアドオンの動作テストを毎回行うのは、特にアドオンの規模が大きくなってくると大変です。本節では、Blenderのコマンドライン実行を活用してアドオンの動作テストを自動化する方法を紹介します。


## アドオンの動作テストを自動化する利点

バグ修正や新機能追加によりソースコードを修正したことで、これまで正しく動作していた既存の機能が正しく動かなくなることは、ソフトウェアでバグが発生する原因の1つです。ソースコードを修正しなければこのようなことは起こりませんが、これでは根本的な問題解決になりません。ソースコードを修正したことでバグが発生するのは、修正の影響がどこまで及んでいるのかをきちんと把握できていないことが原因です。しかし、ソースコードを修正するたびに既存の機能のテストを毎回手作業で行っていたのでは、時間がいくらあっても足りません。一方、Blenderのアドオンの場合は一般のソフトウェアと異なり、BlenderのバージョンによってAPIが変更されてしまうことで今まで動作していた機能が正しく動作しなくなるという問題もあります。新しいバージョンのBlenderがリリースされる度に、アドオンのすべての機能をテストするのも非常に大変です。

このように、アドオンのテストには想像しているよりも非常に手間がかかることが分かると思います。そこで、毎回同じことを繰り返すようなテストは自動化してしまい、本来の修正作業に集中しましょう。


## コマンドラインからBlenderを実行

BlenderはGUIベースのソフトウェアですので、アドオンの機能が正しく動作していることを動作確認するためにはマウスやキーボードを使った操作が必要になるため、テストを自動化することが難しいと感じるかもしれません。しかし幸いなことに、BlenderはコマンドラインでPythonスクリプトを実行するモード（CUIモード）が標準で備わっているため、CUIモードを活用してアドオンのテストを自動化することができます。

Blenderをコマンドラインから実行するためには、[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.md) で紹介した通り、ターミナルを開きBlenderの実行ファイルを実行します。しかし、[1-3節](../chapter_01/03_Prepare_Add-on_development_environment.md) で紹介した方法では、BlenderがGUIモードで起動してしまいます。CUIモードで起動するためには、```--background``` オプションをつけて実行します。以降の説明では、Blenderの実行ファイルが置かれているパスが ```/path/blender``` とします。

```sh
$ /path/blender --background
```

上記のコマンドを実行すると、BlenderがCUIモードで起動後にBlenderが終了します。しかしこれだけでは、CUIモードでBlenderが起動して終了するだけで意味がありません。CUIモードが強力なのは、オプション ```--python``` の引数に指定したPythonスクリプトを実行できることにあります。例えば、レンダリング処理を実行するPythonスクリプトを作成し、高性能なレンダリングを行うサーバでCUI実行することで、ネットワークレンダリングを行うことができます。また、過去に作成した.blendファイルに対してPythonスクリプトを使って同じ処理を繰り返したい場合にも、コマンドラインから実行することで作業時間を短縮することができます。

ここでは試しに簡単なPythonスクリプトを作成し、BlenderのCUIモードで作成したスクリプトを実行してみましょう。次のスクリプトを作成し、```/path/blender``` と同一ディレクトリに、```run_script_on_cui_mode.py``` の名前で保存します。

```python
a = 50
b = 12
print("a+b=%d" % (a+b) )
```

次にターミナルから以下のコマンドを実行します。

```sh
$ /path/blender --background --python run_script_on_cui_mode.py
```

コマンドを実行すると次のメッセージが出力された後、Blenderが終了します。

```sh
a+b=62
```

このように、BlenderのCUIモードでPythonスクリプトを実行することができます。CUIモードでPythonスクリプトが実行できることを利用し、アドオンの機能をテストするスクリプトを実行することで、GUIモードでマウスやキーボードを用いることなくアドオンのテストを行うことができます。しかし、CUIモードでBlenderを起動しただけではアドオンが有効化されていません。作成したアドオンをCUIモードで有効化してBlenderを実行するためには、```--addons``` オプションの引数に有効化したいアドオンのパッケージまたはモジュール名を指定します。例えば、モジュール名が ```addon_test``` であれば以下のコマンドを実行することで、アドオン ```addon_test``` が有効化された状態でスクリプト ```run_script_on_cui_mode.py``` を実行します。

```sh
$ /path/blender --background --addons addon_test --python run_script_on_cui_mode.py
```

## アドオンの機能をスクリプトから実行する

有効化されているアドオンの機能は、[2-2節](../chapter_02/02_Register_Multiple_Operation_Classes.md) で紹介したように、オペレータクラスの ```bl_idname``` が ```bpy.ops.<オペレーションクラスのbl_idname>``` として登録されることを利用し、スクリプトから実行することができます。

テストするアドオンを有効化した状態でBlenderを実行し、アドオンの機能をスクリプトから実行することで、アドオンのテストを行うことになります。すなわち、アドオンの動作確認を行うためにマウスやキーボードを用いて行なっていたことを、Blenderが提供するAPIを使って実現する必要があります。このため、処理によってはスクリプトで実現できない可能性があることに注意が必要です。


## アドオンの動作テストを自動化する方法

CUIモードでスクリプトを実行する方法を紹介しましたが、これを用いてアドオンの動作テストを自動化する方法を紹介します。アドオンの動作テストを自動化する方法として、ここではGitHubとTravis CIを連携してアドオンをGitHubのリポジトリにコミットした時にテストを行うための方法を紹介します。

### GitHubに登録する

GitHubについては、[4-3節](03_Publish_your_Add-on.md) にて紹介しましたが、GitHubの機能の1つに外部サービスとの連携があります。外部サービスと連携することにより、更新したソースコードをコミットした時に外部サービスを利用し、そのコミットが正常であるかを確認することができます。GitHubの登録の仕方についてはすでに多くの情報がWeb上で紹介されているため、本書では割愛します。

Web上などの情報を参考にして、GitHubにリポジトリを作成します。本節では、```Testing_Blender_Addon_With_Travis_CI``` というリポジトリを作成することを前提に説明します。作成したリポジトリはTravis CIと連携することで、リポジトリに対してコミットされるとテストが自動的に行われるようにします。

### Travis CIに登録する

GitHubについてはアドオンをよく利用されている方であれば、知っている方も多いと思います。一方、Travis CIについては名前すら知らないという方もいるかと思いますので簡単に紹介します。

CIとはContinuous Integration(継続的インテグレーション)の略で、ソースコードのビルドやテストをソースコード更新のたびに行うことを示しています。ソースコードを修正すると、これまで動作していた機能が動作しなくなるといった問題が生じることがあると書きましたが、このようなことが起こらないようにするために、常にソースコードをテストして問題の発生をできるだけ早く見つけるというのがCIを行う理由の1つです。CIサービスはCIの実践を支援するサービスで、ソースコードをリポジトリにコミットした時にテストやビルドを自動的に行い、その結果を表示するサービスです。Travis CIはCIを支援するサービスの1つでCIサービスには他にもJenkinsなどがありますが、本書ではGitHubと連携が簡単なTravis CIを使って説明します。

<div id="webpage"></div>

|Travis CI|
|---|
|https://travis-ci.org/|
|![Travis CI](https://dl.dropboxusercontent.com/s/d5wmzeuhv93nufx/travis_ci.png "Travis CI")|


GitHubと同様、Travis CIへの登録の仕方についても、本書では割愛します。すでにGitHubアカウントを持っていれば特別必要な作業は不要かと思います。

### GitHubとTravis CIを連携する

GitHubとTravis CIとの連携は、次の手順で行います。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|右上のユーザのアイコンから *Accounts* をクリックしてアカウント情報を表示すると、GitHubで作成したリポジトリの一覧が表示されますので、テスト対象のリポジトリを有効化します。|![GitHubとTravis CIの連携 手順1](https://dl.dropboxusercontent.com/s/zh7p3nmnt9sx6u7/link_to_travis_ci_1.png "GitHubとTravis CIの連携 手順1")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">2</div>|リポジトリ有効化ボタンの隣にある歯車マークをクリックすると、テスト（ビルド）を実行する契機を確認することができます。|![GitHubとTravis CIの連携 手順2](https://dl.dropboxusercontent.com/s/h7vf50tbmyzivi6/link_to_travis_ci_2.png "GitHubとTravis CIの連携 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|デフォルトでは *Build pushes* （プッシュ時に実行）と *Build pull requests* （プルリクエスト時に実行）の2つが有効化されています。|![GitHubとTravis CIの連携 手順3](https://dl.dropboxusercontent.com/s/f836k1u4ab1j9z3/link_to_travis_ci_3.png "GitHubとTravis CIの連携 手順3")|
|---|---|---|


<div id="process_start_end"></div>

---


上記の手順を見てもらえばわかると思いますが、GitHubとTravis CIとの連携はクリックを数回行うことで完了します。

### テスト対象のアドオンの作成

本節でテスト対象とするアドオンを作成します。ファイル名 ```testee.py``` として作成します。

[import](../../sample/src/chapter_04/sample_4-5/testee.py)

テスト対象のアドオンでは、2つのオペレータクラスが定義されています。```TestOps1``` は何もせずに ```{'FINISHED'}``` を返すオペレーションが定義されています。```TestOps2``` はオブジェクト名がCubeであるオブジェクトが存在する場合に ```{'FINISHED'}``` 、存在しない場合に ```{'CANCELLED'}``` を返すオペレーションが定義されています。

### アドオンテスト用スクリプトの作成

アドオンをテストするためのスクリプトを作成します。本節では、ファイル名 ```test.py``` として作成します。

[import](../../sample/src/chapter_04/sample_4-5/test.py)


スクリプト自体は単純で、```testee.py``` で登録するオペレータクラスの ```bl_idname``` を使ってアドオンの機能を呼び出すだけです。アドオンの機能を呼び出した後は、その戻り値を ```assert``` 文で判定します。第1引数の条件が偽の場合には ```AssertionError``` 例外オブジェクトが発生し、```except``` 処理の中で第2引数に指定した文字列が表示されたあと、```sys.exit(1)``` によりBlenderが復帰値 ```1``` で終了することでテストがエラー終了します。Travis CIはテストのコマンドの結果が ```0``` 以外の場合には、テストが失敗したと判断します。アドオンの機能を実行した時の戻り値が期待したものではなかった場合にBlenderが ```0``` 以外で終了するようなスクリプトを作成することで、アドオンが正常に動作しているのか否かを確認することができます。

Blender実行開始時にはオブジェクト名がCubeであるオブジェクトが最初から作られているため、作成したアドオン ```testee.py``` で定義した全てのオペレーションは ```{'FINISHED'}``` で返ります。また、アドオンが正常に読み込まれていれば、```bpy.ops.object.test_ops_1``` や ```bpy.ops.object.test_ops_2``` は ```None``` 以外となるため、全ての ```assert``` 文の第1引数は ```True``` となり、テストが正常に終了します。


### .travis.ymlの作成

Travis CIでテストを実行するためには、```.travis.yml``` ファイルというYAML形式の設定ファイルを作成する必要があります。

[import](../../sample/src/chapter_04/sample_4-5/.travis.yml)

設定ファイルには、次に示す5つの項目について記載します。```.travis.yml``` に記載したコメントも参照してください。なお、コメントで★を記載した部分は、テスト対象とするBlenderのバージョンにより修正が必要な箇所です。

|項目|概要|
|---|---|
|```language```|Travis CIでテストする対象のソースコードのプログラミング言語を指定します。BlenderのアドオンやスクリプトはPythonであるため、pythonを指定します|
|```python```|Pythonのバージョンを指定します。ここには、Blenderが採用するPythonのバージョンを指定します。Blenderが採用するPythonのバージョンを調べる方法については、後ほど紹介します。|
|```before_install```|```install``` 前に実行する処理を、Linuxのコマンドで記述します。Blenderを動作させるために必要なLinuxのパッケージを取得するため、パッケージマネージャの更新とパッケージマネージャからBlenderのインストールを行なっています。パッケージマネージャでインストールしたBlenderは、パッケージマネージャで管理するBlenderのバージョンに依存するため、基本的には利用しません。|
|```install```|```script``` 前（テスト実行前）に実行する処理です。```before_install``` と同様、Linuxのコマンドで記述します。本節のサンプルでは、バージョンが2.75であるBlenderをダウンロードしたあと、アドオンをインストールしています。|
|```script```|テスト実行時に実行する処理を、Linuxのコマンドで記述します。|

Blenderをコマンドラインから実行する方法で記載したように ```script``` には、```--python``` , ```--addons``` と ```--background``` オプションを指定して、アドオン ```testee``` を有効化した上でテストスクリプト ```test.py``` をCUIモードで実行しています。他にも、オーディオを無効化する ```-noaudio``` オプションや初期状態で起動する ```--factory-startup``` オプションを追加しています。```-noaudio``` オプションを指定しないで実行すると、オーディオライブラリ関連のエラーがログに出力されてしまいます。ダウンロードを実行した直後にBlenderを実行するため初期状態での起動となり ```--factory-startup``` は本来不要ですが、念のために指定しています。


<div id="tips">

Blenderのコマンドラインオプションの一覧は、```--help``` オプションを指定して実行することで表示することができます。


#### Blenderが採用しているPythonのバージョンを調べる方法

Blenderが採用するPythonのバージョンを調べるためには、次のスクリプトを *Pythonコンソール* で実行します。実行結果の ```<major>.<minor>.<micro>``` が、Blenderが採用7エルPythonのバージョンとなります。バージョンが2.75であるBlenderは、バージョンが3.4.2であるPythonが使われていることが次のスクリプトからわかりました。

```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=4, micro=2, releaselevel='final', serial=0)
```


### 作成したアドオンのソースコードをコミット

ここまでで作成したファイルを、以下のようにローカルリポジトリへ以下のように配置します。
なお、事前にGitHub上のリモートリポジトリをローカルに持ってくる(cloneする)必要があります。

```
/    # ローカルリポジトリのディレクトリ
├ .travis.yml   # Travis CIの設定ファイル
├ test.py       # テストスクリプト
└ testee.py     # テスト対象のアドオン
```

上記のファイル一式をGitHub上のリモートリポジトリにコミットします。

```sh
$ cd Testing_Blender_Addon_With_Travis_CI
$ git add .
$ git commit -m "Test add-on with Travis CI"
$ git push origin master
```

リモートリポジトリにコミットすると、Travis CI上で ```before_install``` 、```install``` 、```script``` の順番で実行されます。

### テスト結果を確認する

テストの実行結果は、Travis CIで確認することができます。Travis CI上でテスト結果を確認する方法を次に示します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|右上のユーザのアイコンから *Accounts* をクリックしてアカウント情報を表示し、リポジトリ名をクリックします。。|![テスト結果の確認 手順1](https://dl.dropboxusercontent.com/s/eowughm4ekq90vv/check_test_result_1.png "テスト結果の確認 手順1")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">2</div>|テストが正常に終了すれば、passedと表示されます。|![テスト結果の確認 手順2](https://dl.dropboxusercontent.com/s/8zpzlg5jz7gtesn/check_test_result_2.png "テスト結果の確認 手順2")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">3</div>|*Job log* から、テストの実行ログを確認することができます。|![テスト結果の確認 手順3](https://dl.dropboxusercontent.com/s/162cqvaq0fqq9e4/check_test_result_3.png "テスト結果の確認 手順3")|
|---|---|---|



<div id="process_start_end"></div>

---


#### テスト失敗時の表示を確認する

テスト失敗時にTravis CIではどのように表示されるか確認します。
テストを失敗させるために、```test.py``` を次のように書き換えます（```test.py``` から変更された箇所はコメントの先頭に ```$``` を記載しています）。オブジェクト名が「Cube」のオブジェクトを削除して、```bpy.ops.object.test_ops_2()``` の戻り値が ```{'CANCELLED'}``` になるようにして、テストが失敗するようにします。

[import](../../sample/src/chapter_04/sample_4-5/test_alt.py)

修正後にアドオンのソースコードをリポジトリにコミットし、テストを実行します。


<div id="sidebyside"></div>

|テストは期待した通り失敗し、Travis CIのテスト結果では左図のように失敗したことが表示されます。|![テスト失敗時の表示確認1](https://dl.dropboxusercontent.com/s/3cfuwl2hkmhnyd0/check_test_failed_result_1.png "テスト失敗時の表示確認1")|
|---|---|

|ログには失敗した原因が表示されています。|![テスト失敗時の表示確認2](https://dl.dropboxusercontent.com/s/ljo7ty7uin68v58/check_test_failed_result_2.png "テスト失敗時の表示確認2")|
|---|---|


## まとめ

GitHubとTravis CIを利用して、アドオンのテストを自動化する方法を紹介しました。すでにGitHubでアドオンを公開している方や、これから公開することを考えている方は、本節で紹介したテストの自動化はアドオンの品質や開発効率の向上に役立つと思います。GitHubにアドオンを公開しない方でも、BlenderをCUIモードで起動してテストスクリプトを実行することでもアドオンをテストすることができることを覚えておきましょう。

本節で紹介したテスト自動化は、修正時に他の機能への影響が見えづらくかつテスト量が多くなりがちな、ソースコードの規模が大きいアドオンに対して効果を発揮します。一方数百行程度のアドオンの場合、テストスクリプトや設定ファイル作成などのテスト自動化の手続きにより、かえって手間がかかってしまう可能性があります。また今後のサポートを考えていないなど、あくまで個人用途で作成したアドオンであれば、テストを行う必要がないかもしれません。作成したアドオンの規模やサポート範囲を踏まえ、アドオンの自動テスト化を行うか判断すると良いと思います。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* アドオンのテストを自動化することで、ソースコードを修正したことによるバグの発生を早期に発見できる
* *ターミナル* からBlenderを実行する時にオプション ```--background``` を指定することでCUIモードでBlenderを実行することができる
* CUIモードでPythonスクリプトを実行するためには、```--python``` オプションの引数に実行するスクリプト名を指定する
* CUIモードでアドオンを有効化するためには、```--addons``` オプションの引数に有効化したいアドオンのパッケージまたはモジュール名を指定する
* GitHubをTravis CIと連携することで、GitHubのリポジトリにコミットした時に ```.travis.yml``` に記載した内容に従ってビルドやテストを行い、その結果をTravis CI上で確認することができる
