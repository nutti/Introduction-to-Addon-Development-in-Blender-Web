<div id="sect_title_img_5_2"></div>

<div id="sect_title_text"></div>

# オーディオプレイヤー

<div id="preface"></div>

###### 　

本節では、mp3やwavなどのオーディオファイルを再生するためのオーディオプレイヤーアドオンを紹介します。オーティオファイルの再生については、[3-6節](../chapter_03/06_Play_Audio_File.md) のサンプルで説明しました。本節のサンプルでは [3-3節](../chapter_03/06_Play_Audio_File.md) のサンプルに機能を追加し、最低限オーディオプレイヤーと呼ばれるようなアドオンにしました。


## アドオンのソースコード

[はじめに](../../README.md) の『本書で紹介するサンプルのソースコードについて』に記載されている本書で使用するアドオン一覧より、```chapter_05/sample_5-3.py``` を探してください。

## 関連する節

本節のアドオンに使われているAPIについて説明している節は以下の通りです。細かいところを挙げれば他の節も関係していることになりますが、ここでは重要な部分について取り上げています。

* [2-1. アドオン開発の基礎を身につける](../chapter_02/01_Basic_of_Add-on_Development.md)
  * 基本的なアドオンの作り方
* [2-8. BlenderのUIを制御する①](../chapter_02/08_Control_Blender_UI_1.md)
  * ツール・シェルフのタブの追加方法
* [2-9. BlenderのUIを制御する②](../chapter_02/09_Control_Blender_UI_2.md)
  * ツール・シェルフのタブのUI構築方法
* [2-10. BlenderのUIを制御する③](../chapter_02/10_Control_Blender_UI_3.md)
  * ファイルブラウザの扱い方
* [3-3. タイマのイベントを扱う](../chapter_03/03_Handle_Timer_Event.md)
  * タイマイベントの扱い方
* [3-6. オーディオファイルを再生する](../chapter_03/06_Play_Audio_File.md)
  * プロパティクラスの値を変更した時に呼ばれる関数



## アドオンの仕様

* *3Dビュー* エリアのツール・シェルフに *オーディオプレイヤー* パネルを追加し、選択したオーディオファイルを再生する簡易オーディオプレイヤーを作成する
* オーディオプレイヤーは以下の機能を持つ
  * 選択したファイルの再生/一時停止・再開/停止
  * ループ再生
  * 音量変更
  * ピッチ変更
* 選択中のオーディオファイル名と再生中の再生時間を表示する


### アドオンの機能を使用する

以下の手順に従って、作成したアドオンの機能を使ってみます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*3Dビュー* エリアのツール・シェルフの *オーディオプレイヤー* パネルを選択します。|![オーディオプレイヤー 手順1](https://dl.dropboxusercontent.com/s/ipuyehmoe54sh95/use_add-on_1.png "オーディオプレイヤー 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*オーディオファイルを選択* ボタンをクリックします。|![オーディオプレイヤー 手順2](https://dl.dropboxusercontent.com/s/6uryy1g0vh9r5hn/use_add-on_2.png "オーディオプレイヤー 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|Blenderのファイルブラウザが開くため、再生したいオーディオファイルを選択して *オーディオファイルの選択* をクリックします。|![オーディオプレイヤー 手順3](https://dl.dropboxusercontent.com/s/kcca4od6dakirae/use_add-on_3.png "オーディオプレイヤー 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|選択したオーディオファイル名が表示されます。この状態で *再生* ボタンをクリックすると、選択したオーティオファイルが再生されます。|![オーディオプレイヤー 手順4](https://dl.dropboxusercontent.com/s/zv0nnd474ddthgq/use_add-on_4.png "オーディオプレイヤー 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|オーディオファイル再生中は、*音量* や *ピッチ* を変更したり *一時停止* や *再生再開* したりできます。また、再生中は再生時間が表示され、再生を停止したい場合は *停止* ボタンをクリックします。*ループ再生* にチェックを入れると、曲が終わっても再生を停止するまで再生され続けます。|![オーディオプレイヤー 手順5](https://dl.dropboxusercontent.com/s/qov3eqy8psfazz5/use_add-on_5.png "オーディオプレイヤー 手順5")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process_start_end"></div>

---
