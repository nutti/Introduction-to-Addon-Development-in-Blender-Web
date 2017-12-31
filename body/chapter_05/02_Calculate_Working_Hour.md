<div id="sect_title_img_5_2"></div>

<div id="sect_title_text"></div>

# 作業時間計測ツール

<div id="preface"></div>

###### 　


<div id="space_s"></div>


本節では、メッシュ型のオブジェクトを選択した時間を、オブジェクトごとに計測するアドオンを紹介します。本節のサンプルは、タイマを扱うわかりやすい例であることから、もともと[3-3節](../chapter_03/03_Handle_Timer_Event.md)のサンプルとして紹介することを考えていました。しかし、ソースコードの規模が比較的大きいことと、他の節で説明する内容を多く含むことから、ここで紹介することにしました。


## アドオンのソースコード

本節で紹介するアドオンは、[はじめに](../../README.md)の『本書で紹介するサンプルのソースコードについて』に記載したサンプルアドオンのダウンロード先から、ダウンロードできます。```chapter_05/sample_5_2.py``` を探してダウンロードしてください。

## 関連する節

本節のサンプルに使われているAPIについて説明している箇所は、次の通りです。細かいところも含めると他の箇所も関係していますが、ここでは特に関連が深い箇所に絞って記載します。

* [2-1. アドオン開発の基礎を身につける](../chapter_02/01_Basic_of_Add-on_Development.md)
  * 基本的なアドオンの作り方
* [2-4. ツール・シェルフのオプションを活用する②](../chapter_02/04_Use_Property_on_Tool_Shelf_2.md)
  * ```EnumProperty``` クラスで作成するセレクトボックスに、項目を動的に追加する方法
* [3-1. マウスクリックのイベントを扱う](../chapter_03/01_Handle_Mouse_Click_Event.md)
  * プロパティパネルにおけるUI構築
* [3-3. タイマのイベントを扱う](../chapter_03/03_Handle_Timer_Event.md)
  * タイマイベントの扱い方
* [3-5. blfモジュールを使ってテキストを描画する](../chapter_03/05_Render_String_with_blf_Module.md)
  * ```blf``` モジュールを利用したテキスト描画の方法
* [3-10. ユーザー・プリファレンスを活用する](../chapter_03/10_Use_User_Preference.md)
  * ユーザー・プリファレンスにアドオン設定情報を配置する方法

## アドオンの仕様

* *3Dビュー* エリアのプロパティパネルの項目 *作業時間計測* に、作業時間計測モードを開始/終了するためのボタンを配置する
* 作業時間計測モード中は、選択中のメッシュ型のオブジェクトについて、*オブジェクトモード* と *エディットモード* 中であった時間をそれぞれ計測する
* 計測した時間は、デフォルトで *3Dビュー* の *ウィンドウ* リージョンの左上に表示する
  * 表示位置とフォントサイズは、ユーザー・プリファレンスのアドオン設定から設定できる
  * 作業時間を表示するオブジェクトは、*3Dビュー* エリアのプロパティパネルの項目 *作業時間計測* に配置されているセレクトボックス *オブジェクト* から選択できる


<div id="space_m"></div>


### アドオンの機能を使用する

次の手順に従って、アドオンの動作を確認します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*3Dビュー* エリアのプロパティパネルの項目 *作業時間計測* に配置されている *開始* ボタンをクリックします。|![作業時間計測ツール 手順1](https://dl.dropboxusercontent.com/s/mskhmi6jomimy9r/use_add-on_1.png "作業時間計測ツール 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*3Dビュー* エリア上に配置されているセレクトボックス *オブジェクト* から、作業時間を表示したいオブジェクトを選択します。|![作業時間計測ツール 手順2](https://dl.dropboxusercontent.com/s/vyxov95xx3724pj/use_add-on_2.png "作業時間計測ツール 手順2")|
|---|---|---|


<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|選択したオブジェクトに関する作業時間が、*ウィンドウ* リージョンに表示されます。|![作業時間計測ツール 手順3](https://dl.dropboxusercontent.com/s/cwuhsydrgsq3kw6/use_add-on_3.png "作業時間計測ツール 手順3")|
|---|---|---|


<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|ユーザー・プリファレンスのアドオン設定から、表示位置やフォントサイズを変更することができます。|![作業時間計測ツール 手順4](https://dl.dropboxusercontent.com/s/vdx506zccdjwvds/use_add-on_4.png "作業時間計測ツール 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|*3Dビュー* エリアのプロパティパネルの項目 *作業時間計測* に配置されている *終了* ボタンをクリックすると、作業時間の計測が停止し、作業時間が *ウィンドウ* リージョンに表示されなくなります。|![作業時間計測ツール 手順5](https://dl.dropboxusercontent.com/s/wx4r06m51km2khd/use_add-on_5.png "作業時間計測ツール 手順5")|
|---|---|---|


<div id="process_start_end"></div>

---

<div id="space_page"></div>
