<div id="sect_title_img_5_2"></div>

<div id="sect_title_text"></div>

# オブジェクト名の表示サポート

<div id="preface"></div>

###### 　

本節では、*3Dビュー* エリアに表示されているオブジェクト名とマウスカーソルが重なったオブジェクトの名前を表示するアドオンを紹介します。本節のサンプルは [3-8節](../chapter_03/08_Use_Coordinate_Transformation_1.md) と [3-9節](../chapter_03/09_Use_Coordinate_Transformation_2.md) で説明した内容を使って作成したアドオンの一例です。


## アドオンのソースコード

[はじめに](../../README.md) の『本書で紹介するサンプルのソースコードについて』に記載されている本書で使用するアドオン一覧より、```chapter_05/sample_5-4.py``` を探してください。

## 関連する節

本節のアドオンに使われているAPIについて説明している節は以下の通りです。細かいところを挙げれば他の節も関係していることになりますが、ここでは重要な部分について取り上げています。

* [2-1. アドオン開発の基礎を身につける](../chapter_02/01_Basic_of_Add-on_Development.md)
  * 基本的なアドオンの作り方
* [3-1. マウスクリックのイベントを扱う](../chapter_03/01_Handle_Mouse_Click_Event.md)
  * プロパティパネルにおけるUI構築
* [3-5. blfモジュールを使ってテキストを描画する](../chapter_03/05_Render_String_with_blf_Module.md)
  * ```blf``` モジュールを利用したテキスト描画の方法
* [3-8. 座標変換を活用する①](../chapter_03/08_Use_Coordinate_Transformation_1.md)
  * 3D空間の座標をリージョン座標へ変換する方法
* [3-9. 座標変換を活用する②](../chapter_03/09_Use_Coordinate_Transformation_2.md)
  * リージョン座標を3D空間の座標へ変換する方法
  * レイとオブジェクトの交差判定方法
* [3-10. ユーザー・プリファレンスを活用する](../chapter_03/10_Use_User_Preference.md)
  * ユーザー・プリファレンスにおけるアドオン設定情報の利用方法


## アドオンの仕様

* *3Dビュー* エリアのプロパティパネルに *オブジェクト名の表示サポート* を追加し、オブジェクト名の表示を開始するためのボタンを配置する
* オブジェクト名表示中は、以下の処理を行う
  * *3Dビュー* エリアに表示されている全てのオブジェクトについて、オブジェクトの位置にオブジェクト名を表示する
  * *オブジェクトモード* 時に *3Dビュー* エリアに配置されているメッシュ型オブジェクトとマウスが重なった時に、マウスと重なった全てのオブジェクトを *3Dビュー* の *ウィンドウ* リージョンの左上に表示する
  * 表示位置とフォントサイズは、ユーザー・プリファレンスのアドオン設定から選択できる


### アドオンの機能を使用する

以下の手順に従って、作成したアドオンの機能を使ってみます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*3Dビュー* エリアのプロパティパネルに追加された *オブジェクト名の表示サポート* の *開始* ボタンをクリックします。|![オブジェクト名の表示サポート 手順1](https://dl.dropboxusercontent.com/s/i4s2mc5h10ubntq/use_add-on_1.png "オブジェクト名の表示サポート 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*3Dビュー* エリアで表示されているオブジェクトに重なるように、オブジェクト名が表示されます。|![オブジェクト名の表示サポート 手順2](https://dl.dropboxusercontent.com/s/gksjey627jwapzv/use_add-on_2.png "オブジェクト名の表示サポート 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*オブジェクトモード* 時に、*マウスカーソル* と重なったオブジェクト名が *3Dビュー* エリアの *ウィンドウ* リージョンの左上に表示されます。|![オブジェクト名の表示サポート 手順3](https://dl.dropboxusercontent.com/s/t5d6aga6euso89d/use_add-on_3.png "オブジェクト名の表示サポート 手順3")|
|---|---|---|


<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|ユーザー・プリファレンスからそれぞれの機能について、表示文字列のフォントや位置を変更することができます。|![オブジェクト名の表示サポート 手順4](https://dl.dropboxusercontent.com/s/v6i66j1qpm892cr/use_add-on_4.png "オブジェクト名の表示サポート 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|*3Dビュー* エリアのプロパティパネルの *オブジェクト名の表示サポート* から *終了* ボタンをクリックすると、オブジェクト名が表示されなくなります。|![オブジェクト名の表示サポート 手順5](https://dl.dropboxusercontent.com/s/lu6tr95ygft3k9o/use_add-on_5.png "オブジェクト名の表示サポート 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_start_end"></div>

---
