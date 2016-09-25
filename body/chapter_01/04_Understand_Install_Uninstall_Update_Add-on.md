<div id="sect_title_img_1_3"></div>

<div id="sect_title_text"></div>

# アドオンのインストール・アンインストール・<br>アップデート方法を理解する

<div id="preface"></div>

###### [1-2節](02_Use_Blender_Add-on.md) では実際にアドオンをインストールして使ってみました。しかし [1-2節](02_Use_Blender_Add-on.md) で説明した方法は、数あるインストールの仕方の 1 つにすぎません。 [1-2節](02_Use_Blender_Add-on.md) でも少し触れましたが、アドオンのソースコードが複数ファイルで構成されるかされないかなど、ソースコードの構成によってインストールやアンインストールの方法が異なります。本節では、アドオンのインストール・アンインストールの方法に加えてアップデートの方法についてまとめます。

## アドオンが複数のソースコードで構成されるかどうかを見極める

[1-2節](02_Use_Blender_Add-on.md) のtipsでも少し説明しましたが、これからアドオンのインストール方法を説明する前に必ず覚えておいて欲しいこととして、アドオンがのソースコードで構成されるかどうかを見極める方法を説明します。

アドオンが複数ソースコードで構成されるかどうかを知るためには、アドオンのソースコードに ```__init__.py``` というファイルが存在するかを確認します。 ```__init__.py``` が存在すれば、アドオンが複数のソースコードで構成されていることになります。

実際に筆者が作成したアドオンを用いて確認してみましょう。
またここで使用するアドオンは、後の説明でも使用します。

### 例1: 複数のソースコードで構成されるアドオン

https://github.com/nutti/Magic-UV/releases/download/v4.0/uv_magic_uv.zip から、筆者が作成したアドオン『Magic UV』をダウンロードします。
アドオン『Magic UV』のソースコード本体は zip を解凍した後の ```uv_magic_uv``` ディレクトリ以下の一式です。拡張子が ```.py``` であるファイルが複数あり、ファイル ```__init__.py``` が存在しているため、アドオン『Magic UV』は複数のソースコードで構成されるアドオンと判断できます。

### 例2: 単一のソースコードで構成されるアドオン

https://github.com/nutti/Mouse-Click-Merge/releases/download/v0.3/Mouse-Click-Merge-0.3.zip から、筆者が作成したアドオン『Mouse Click Merge』をダウンロードします。
アドオン『Mouse Click Merge』のソースコード本体は zip を解凍した後の ```mouse_click_merge.py``` のみです。

このように、アドオンが複数のソースコードで構成されているか単一のソースコードで構成されているかを見極めるには、 ソースコードにファイル ```__init__.py``` が含まれているかを確認すればよいことになります。


## アドオンのインストール方法

アドオンをインストールする方法は、以下の2通りがあります。

* Blender のアドオンインストール機能を用いる
* Blender アドオン用フォルダにソースコードを直接配置する

### 方法1: Blender のアドオンインストール機能を用いる

Blender 本体にはアドオンのインストール機能が備わっています。
アドオンをインストールするための標準的なインストール方法ですが、アドオンのソースコードによってはインストールすることができません。
ソースコードが単一のファイルで構成されている場合はアドオンを問題なくインストールできると思いますが、ソースコードが複数のファイルで構成されている場合は、 ```__init__.py``` が置かれたディレクトリが .zip 形式で圧縮されている必要があります。

Blender のアドオンインストール機能を用いた場合について、アドオンのインストール方法を説明します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*情報* エリアの *ファイル* > *ユーザ設定* を実行します。|![アドオンのインストール方法1 手順1](https://dl.dropboxusercontent.com/s/oqbezirt4qwlm87/install_1_use_default_add-on_installation_feature_1.png "アドオンのインストール方法1 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*アドオン* タブを選択します。|![アドオンのインストール方法1 手順2](https://dl.dropboxusercontent.com/s/x4r2551bsbtty06/install_1_use_default_add-on_installation_feature_2.png "アドオンのインストール方法1 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*ファイルからインストール* ボタンをクリックします。|![アドオンのインストール方法1 手順3](https://dl.dropboxusercontent.com/s/m3lvp21jn7z029r/install_1_use_default_add-on_installation_feature_3.png "アドオンのインストール方法1 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|ファイル選択画面でインストールするアドオンのソースコード（ ```.py``` か、```.zip``` ）を選択し、 **ファイルからインストール** ボタンをクリックします。|![アドオンのインストール方法1 手順4](https://dl.dropboxusercontent.com/s/ptcm64jx4xzbfh9/install_1_use_default_add-on_installation_feature_4.png "アドオンのインストール方法1 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|インストールが完了します。|![アドオンのインストール方法1 手順5](https://dl.dropboxusercontent.com/s/h9k2ru59j50rey6/install_1_use_default_add-on_installation_feature_5.png "アドオンのインストール方法1 手順5")|
|---|---|---|

<div id="process_start_end"></div>

---


### 方法2: Blender アドオン用フォルダにソースコードを直接配置する

Blender にインストール済のアドオンが配置されているアドオン用フォルダにソースコードを直接配置する方法です。
ソースコードを直接配置するため、ソースコード自体に問題がなければ単一のファイルで構成されているか複数のファイルで構成されているかにかかわらず、インストールすることができます。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|```.py``` または ```__init__.py``` を含めてソースコードが入ったディレクトリ一式を Blender アドオン用フォルダに配置します。|![アドオンのインストール方法2 手順1](https://dl.dropboxusercontent.com/s/u9wc9fat2d8mcj9/install_2_deploy_to_blender_add-on_folder_1.png "アドオンのインストール方法2 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|Blender を再起動するか、 *情報* エリアの *ファイル* > *ユーザ設定* 実行時に開くウィンドウから、 *アドオン* タブにある *更新* ボタンをクリックします。|![アドオンのインストール方法2 手順2](https://dl.dropboxusercontent.com/s/xcfm8zpp1aq7f4v/install_2_deploy_to_blender_add-on_folder_2.png "アドオンのインストール方法2 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|インストールが完了します。|![アドオンのインストール方法2 手順3](https://dl.dropboxusercontent.com/s/majf5bb22cumsbq/install_2_deploy_to_blender_add-on_folder_3.png "アドオンのインストール方法2 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


## アドオンのアップデート方法

アドオンをアップデートする方法は、3通りあります。

* Blender のアドオンインストール機能を使用する
* Blender アドオン用フォルダにソースコードを直接配置し、 Blender を再起動する
* Blender の機能『Reload Scripts』を利用する

### 方法1: Blender のアドオンインストール機能を使用する

アドオンのインストールと同様、 Blender 本体のアドオンインストール機能を用いてアドオンをアップデートすることができます。
インストール時と同様、ソースコードが複数のファイルで構成されている場合は、 ```__init__.py``` が置かれたディレクトリが .zip 形式で圧縮されている必要があります。

具体的なアップデートの方法はインストールの方法1と同様ですので、ここでは説明を省略します。


### 方法2: Blender アドオン用フォルダにソースコードを直接配置し、 Blender を再起動する

こちらもアドオンのインストールと同様、アドオン用フォルダに配置されているソースコードを直接置き換えることで、アップデートすることができます。
インストール時と同様、単一のファイルで構成されているか複数のファイルで構成されているかにかかわらず、アップデートすることができます。

基本的には、インストールの方法2と同様の方法でアップデートできます。しかし、 *情報* エリアの *ファイル* > *ユーザ設定* 実行時に開くウィンドウから、 *アドオン* タブにある *更新* ボタンをクリックしてもアップデートされない点に注意が必要です。このため、置き換えたソースコードをBlenderに反映するためには、Blenderを再起動してアップデートを完了する必要があります。


### 方法3: Blender の機能『Reload Scripts』を利用する

方法2では、複数のソースコードから構成されるアドオンをアップデートする度に毎回Blenderを再起動する必要があります。例えばアドオン開発時ではソースコードの一部を修正して Blender に反映することが多くなるため、ソースコードを修正するたびにBlenderを再起動するのは非常に時間がもったいないです。

この煩わしさを解決してくれるのが、 Blender が標準で持っている機能 **Reload Scripts** です。
Reload Scripts 機能を利用することで、 Blender を再起動せずにアドオンをアップデートすることができます。
Reload Scripts 機能を使った、アドオンのアップデート方法について説明します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|方法2と同様に、ソースコードをアドオン用ディレクトリに配置します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*スペース* キーを押して *検索ボックス* を表示します。|![アドオンのアップデート方法3 手順2](https://dl.dropboxusercontent.com/s/yqhtx4bm0cdih1q/update_3_use_reload_scripts_2.png "アドオンのアップデート方法3 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*Reload Scripts* （日本語では *スクリプトを再読み込み* ）を検索して実行します。|![アドオンのアップデート方法3 手順3](https://dl.dropboxusercontent.com/s/1de4kze37ruoma5/update_3_use_reload_scripts_3.png "アドオンのアップデート方法3 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|アドオンのアップデートが完了します。|
|---|---|

<div id="process_start_end"></div>

---


<div id="column"></div>

*Reload Scripts* 機能には、デフォルトで *F8* キーが割り当てられています。

このように *Reload Scripts* は非常に便利な機能ですが、複数のファイルで構成されるアドオンではソースコードによって正しくアップデートされない可能性があります。
詳しくは、 [2-7節](../chapter_02/07_Divide_Add-on_Source_into_Multiple_Files.md) を参照してください。


## アドオンのアンインストール方法

アドオンをアンインストールする方法は、2通りあります。

### Blender のアドオンアンインストール機能を使用する

アドオンのインストール/アップデートと同様、 Blender 本体のアドオンインストール機能を用いてアドオンをアンインストールすることができます。
アドオンのソースコードが単一のファイルで構成されているか複数のファイルで構成されているかにかかわらずアンインストールできますが、最初から Blender にインストールされているアドオン（アドオンのサポートレベルが Release または Contrib）は削除することができません。

アドオンのアンインストール方法を説明します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*情報* エリアの *ファイル* > *ユーザ設定* を実行します。|![アドオンのアンインストール方法1 手順1](https://dl.dropboxusercontent.com/s/25fooodw4luzou7/uninstall_1_use_default_add-on_uninstallation_feature_1.png "アドオンのアンインストール方法1 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*アドオン* タブを選択します。|![アドオンのアンインストール方法1 手順2](https://dl.dropboxusercontent.com/s/vrq1q44n4npw33h/uninstall_1_use_default_add-on_uninstallation_feature_2.png "アドオンのアンインストール方法1 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|アンインストールしたいアドオンの左側の矢印をクリックし、アドオンの詳細情報を表示します。|![アドオンのアンインストール方法1 手順3](https://dl.dropboxusercontent.com/s/qanpsbi7c1brwvz/uninstall_1_use_default_add-on_uninstallation_feature_3.png "アドオンのアンインストール方法1 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*削除* ボタンをクリックします。|![アドオンのアンインストール方法1 手順4](https://dl.dropboxusercontent.com/s/eq0c7pfqbk861kd/uninstall_1_use_default_add-on_uninstallation_feature_4.png "アドオンのアンインストール方法1 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|アンインストールが完了します。|![アドオンのアンインストール方法1 手順5](https://dl.dropboxusercontent.com/s/5xa6z515h6lufi2/uninstall_1_use_default_add-on_uninstallation_feature_5.png "アドオンのアンインストール方法1 手順5")|
|---|---|---|

<div id="process_start_end"></div>

---



### Blender アドオン用フォルダからソースコードを直接削除する

アドオン用フォルダに配置されているソースコードを直接削除することで、アンインストールすることができます。
単一のファイルで構成されているか複数のファイルで構成されているかにかかわらず、アンインストールすることができます。
また、最初から Blender にインストールされているアドオン（アドオンのサポートレベルが Release または Contrib）についても削除することができます。

以下にその方法を示します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|アドオンのソースコードの場所が分からない場合は、 *Blenderユーザ設定* ウィンドウの *アドオン* タブから確認します。|![アドオンのアンインストール方法2 手順1](https://dl.dropboxusercontent.com/s/4tonmdusbfvobqv/uninstall_2_delete_sources_on_blender_add-on_folder_1.png "アドオンのアンインストール方法2 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|アンインストールしたいアドオンの左側の矢印をクリックし、アドオンの詳細情報を表示します。|![アドオンのアンインストール方法2 手順2](https://dl.dropboxusercontent.com/s/anpf60e5atb2njz/uninstall_2_delete_sources_on_blender_add-on_folder_2.png "アドオンのアンインストール方法2 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|詳細情報の *ファイル* がアドオンのソースコードが置かれた場所を示しています。|![アドオンのアンインストール方法2 手順3](https://dl.dropboxusercontent.com/s/lhsn6qarkux4bok/uninstall_2_delete_sources_on_blender_add-on_folder_3.png "アドオンのアンインストール方法2 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|ソースコードを削除します。アドオンが複数のソースコードで構成されている場合は、 *ファイル* にはディレクトリではなく ```__init__.py``` のファイルパスが表示されています。完全にアンインストールするためには ```__init__.py``` が置かれたディレクトリごと削除する必要があります。|
|---|---|

<div id="process_start_end"></div>

---


## まとめ

アドオンをインストール・アップデート・アンインストールする方法について説明しました。
アドオンのソースコードの構成によって、説明した方法が利用できるかどうかが変わります。
ここでは、説明した方法がどのような条件で使えるのかをまとめます。

### インストール

|方法|ソースコードが単一の<br>ファイルで構成される|ソースコードが複数の<br>ファイルで構成される|
|---|---|---|
|Blender のアドオン<br>インストール機能を使用する|○|```__init__.py``` を含むディレクトリが zip 形式で圧縮されている場合のみ|
|Blender アドオン用フォルダに<br>ソースコードを直接配置する|○|○|

### アップデート

|方法|ソースコードが単一の<br>ファイルで構成される|ソースコードが複数の<br>ファイルで構成される|
|---|---|---|
|Blender のアドオンインストール機能を使用する|○|<br> ```__init__.py``` を含むディレクトリが zip 形式で圧縮されている場合のみ|
|Blender アドオン用フォルダにソースコードを直接配置し、 Blender を再起動する|○|○|
|Blender の機能『Reload Scripts』を利用する|アドオンが *Reload Scripts* 機能へ<br>対応している場合のみ|（同左）|

### アンインストール

|方法|ソースコードが単一の<br>ファイルで構成される|ソースコードが複数の<br>ファイルで構成される|
|---|---|---|
|Blender のアドオンアンインストール機能を使用する|○|○|
|Blender アドオン用フォルダからソースコードを直接削除する|○|○|

### ポイント

<div id="point_item"></div>

* アドオンのソースコードは単一のファイルで構成される場合と、複数のファイルで構成される場合がある
* アドオンをインストール・アップデート・アンインストールする方法はそれぞれ複数あるが、ソースコードが複数のファイルで構成されるか否かなど、使用条件がそれぞれ異なることに注意が必要である
* アドオンを開発する時は頻繁にアップデートを行うことが多いため、 *Reload Scripts* 機能を活用しよう
