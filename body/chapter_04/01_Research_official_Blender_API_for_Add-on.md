<div id="sect_title_img_4_1"></div>

<div id="sect_title_text"></div>

# Blenderが提供するアドオン向けのAPIを調べる

<div id="preface"></div>

###### これまで紹介したサンプルでは、Blenderが提供する様々なAPIを使ってきましたが、サンプルで用いたAPIはどのようにして知ることができたのでしょうか？本節ではこの疑問に答えるため、Blenderが提供するAPIを調べる方法を紹介します。


## Blenderが提供するAPIの情報源

Blenderが提供するAPIの情報を収集する方法としては、以下のようなものがあります。

* Blender公式のAPIリファレンスを読む
* PythonコンソールウィンドウでAPIを検索・実行する
* *テキストエディター* のテンプレートを読む
* Blenderアドオン開発の参考サイトを読む
* 他者が作成したアドオンのソースコードを読む
* Blenderのコミュニティサイトで質問する


## Blender公式のAPIドキュメントを読む

Blenderが提供しているAPI一覧は、Blender公式が公開しているドキュメントから確認することができます。

<div id="webpage"></div>

|API documentation|
|---|
|http://www.blender.org/api/|
|![API documentation](https://dl.dropboxusercontent.com/s/3pgs57v7b29ngo8/blender_api_doc.png "API documentation")|

Blender公式では、過去のBlenderのバージョン含め、すべてのバージョンのAPIがドキュメント化されていますが、Blenderのバージョンに応じて提供されるAPIは変わるため、開発に利用しているBlenderのバージョンのドキュメントを参照する必要があります。

本書のサンプルは2.75aのBlenderをベースとしているため、Blenderのバージョンが2.75aのドキュメントを前提として解説します。

<div id="webpage"></div>

|API documentation (Blender 2.75a)|
|---|
|http://www.blender.org/api/blender_python_api_2_75a_release/|
|![API documentation 2.75a](https://dl.dropboxusercontent.com/s/hmzkcciai4ooigb/blender_api_doc_2_75a.png "API documentation 2.75a")|

ここでは例として、3Dビューエリアのアクティブ状態のオブジェクトを取得するAPIを調べてみます。

APIドキュメントの右側のページには、提供されているAPIがモジュールごとにメニュー化されて表示されていて、大きく分けて以下の3つのモジュールのグループに分けることができます。

|項目|内容|
|---|---|
|Application Modules|基本モジュール(bpyモジュール)。<br>Blender本体のデータにアクセスするために最低限必要なモジュール|
|Standalone Modules|拡張モジュール。<br>Application Modulesを簡単に利用できるようにするものなど、アドオン開発の際に便利なモジュール|
|Game Engine Modules|Blender Game Engine向けモジュール|

Game Engine Modulesは、Blenderが提供するゲームエンジンBlender Game Engine(BGE)を利用するためのモジュールであるため、アドオン開発時は使用しません。このため、アドオン開発に限るのであれば、Application ModulesとStandalone Modulesのみを確認すればよいと思います。

### Application Modules

Application Modulesである ```bpy``` モジュールは非常に大きなモジュールであるため、複数のサブモジュールから構成されています。

以下に ```bpy``` モジュールのサブモジュールの概要についてまとめました。アドオン開発時に必ず必要となるモジュールであるため、どのようなモジュールが提供されているかを一度目を通しておきましょう。

|モジュール名|概要|
|---|---|
|```bpy.context```|現在のBlenderの実行状態（コンテキスト）を取得するためのAPI群|
|```bpy.data```|メッシュや画像データなど、Blender内で利用されているデータへアクセスするためのAPI群|
|```bpy.ops```|Blender内で利用されているデータに対する操作や、アドオンで登録した操作|
|```bpy.types```|Blender内のデータを表す型|
|```bpy.utils```|アドオンのクラス登録など、アドオンへ提供する便利関数群|
|```bpy.path```|ファイルパスを簡単に扱うための関数群|
|```bpy.app```|BlenderのバージョンなどのBlender本体の情報|
|```bpy.props```|アドオン内部で扱うプロパティクラス|

<div id="space_s"></div>


### Standalone Modules

Standalone Modulesは、```bpy``` モジュールを拡張するモジュールです。Application Modulesを使っただけでは実装が大変な処理を簡単かつ効率的に行うことができるAPIが提供されています。

|モジュール名|概要|
|---|---|
|```mathutils```|行列やベクトルなどのクラスや、行列やベクトル演算を簡単に行うことができる関数群<br> ```geometry``` や ```kdtree``` サブモジュールを用いることで、図形の交差判定や3D空間内の探索を高速に行うことも可能|
|```bgl```|PythonからOpenGLへアクセスするためのラッパー関数群|
|```blf```|文字列描画を簡単に行うための関数群|
|```gpu```|GLSLを扱うための関数群|
|```aud```|サウンドの読み込みや再生を行うための関数群|
|```bpy_extras```|```bpy``` モジュールを補助する目的で提供される便利関数群|
|```bmesh```|メッシュデータを容易に扱うための関数群|

ここでは、3Dビューエリアでアクティブ状態のオブジェクトを取得するためのAPI ```bpy.props.EnumProperty``` を調べます。

<div id="sidebyside"></div>

|Application Modules > Property Definitions (bpy.props) をクリックし、 ```bpy.props.EnumProperty``` を探します。<br>すると右図のように、APIの説明に加えて引数や各引数の説明を見ることができます。|![API documentation EnumProperty](https://dl.dropboxusercontent.com/s/xvi335558nxtwhi/blender_api_doc_enum_property.png "API documentation EnumProperty")|
|---|---|


## PythonコンソールウィンドウでAPIを検索・実行する

[2-2節](../chapter_02/02_Register_Multiple_Operation_Classes.md)でも説明しましたが、 Pythonコンソールウィンドウを用いることでBlenderが提供するAPIを検索し、実行することができます。

ここでは、Pythonコンソールウィンドウを使ってAPIを調査する例を紹介します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|3Dビューエリア上にあるオブジェクト一覧を参照できる変数 ```bpy.data.objects``` をPythonコンソールウィンドウに入力します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|ctrl+spaceをキーを押して補完します。|![Pythonコンソールウィンドウ 手順1](https://dl.dropboxusercontent.com/s/6tqu81bbk6l6qy8/python_console_1.png "Pythonコンソールウィンドウ 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|3Dビューエリア上にあるオブジェクト名が候補として表示されるため、適当なオブジェクト名を選んで再び補完します。|![Pythonコンソールウィンドウ 手順2](https://dl.dropboxusercontent.com/s/yu890kcedpewpih/python_console_2.png "Pythonコンソールウィンドウ 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|候補の中にある ```select``` を入力し、実行します。<br>すると、選んだオブジェクトが選択状態である場合は ```True``` 、選択状態でない場合は ```False``` が表示されます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|```select``` に ```True``` を代入することでオブジェクトを選択状態に、  ```False``` を代入することでオブジェクトを非選択状態に変更することができます。|![Pythonコンソールウィンドウ 手順3](https://dl.dropboxusercontent.com/s/0aph2y0pq6edyxf/python_console_3.png "Pythonコンソールウィンドウ 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


以上のことから、```select``` はオブジェクトが選択状態であるか否かを調べるためのAPIであると判断できます。

実際にBlender公式のAPIドキュメント(```http://www.blender.org/api/blender_python_api_2_75a_release/bpy.types.Object.html#bpy.types.Object.select```)を調べてみると、以下のように記載されています。

<div id="quote"></div>

> Object selection state

このように、Pythonコンソールウィンドウを利用することでAPIの動作を確認できます。APIの効果がわからない場合はPythonコンソールウィンドウを用いて実際に動作させてAPIの効果を確認することで、よりAPIへの理解が深まると思いますので積極的に活用していきましょう。


## テキストエディターのテンプレートを読む

<div id="sidebyside"></div>

|BlenderでPythonスクリプトを書く人向けに、Blenderはアドオンのテンプレートを用意しています。これらのサンプルはBlender本体が提供しているため、正常に動作することが保証されています。<br>作りたいアドオンに関連するテンプレートがあれば、一度確認することをお勧めします。また、Blenderが提供するAPIの概要を一通り学んでおきたい場合にも、本サンプルは参考になります。|![テンプレート 手順1](https://dl.dropboxusercontent.com/s/bvnb1360j99fd1t/template_1.png "テンプレート 手順1")|
|---|---|



<div id="sidebyside"></div>

|提供されいる中で最も簡単なテンプレートは、右図で示す ```Operator Simple``` です。```Operator Simple``` は、3Dビューエリアにあるオブジェクト一覧をコンソールウィンドウに表示するサンプルです。|![テンプレート 手順2](https://dl.dropboxusercontent.com/s/8nt0v8zdkhl1egd/template_2.png "テンプレート 手順2")|
|---|---|

<div id="space_m"></div>


## Blenderアドオン開発の参考サイトを読む

Blenderが提供するAPIを調べる手段として、Blenderアドオン開発の参考サイトを読む方法もあります。<br>

しかし、この方法はあまり効率が良いとは言えません。なぜなら、Blender自体の使い方を解説しているサイトに比べてアドオン開発の解説サイトは非常に少ないからです(このことが本書を執筆したきっかけになったのですが・・・)。特に日本語での解説となると、解説サイトは数を数えられるくらいに少なくなります。

ここでは、アドオン開発で筆者がよく参考にするサイトをピックアップしてみました。Blender Wiki様は海外サイト、blugjpまとめサイト様は国内サイトです。

<div id="webpage"></div>

|Blender Wiki|
|---|
|http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts|
|![Blender Wiki](https://dl.dropboxusercontent.com/s/wjaloh1eov0ij73/blender_wiki.png "Blender Wiki")|

Blenderの公式Wikiページです。

アドオン開発のチュートリアルやベストプラクティスなど、アドオン開発に必要な知識を学ぶことができます。特にテーマに応じて簡単なサンプルが紹介されいているCode Snippetsは必見です。

アドオンの公開手順についても書かれていますので、初心者のみならずある程度アドオン開発に慣れた方も参考になるサイトです。

<div id="webpage"></div>

|blugjpまとめサイト|
|---|
|https://sites.google.com/site/blugjp/blenderpython|
|![blugjpまとめサイト](https://dl.dropboxusercontent.com/s/7t6ho0xohl45yrv/blugjp.png "blugjpまとめサイト")|

BLUG.jpさんによるまとめサイトです。

BlenderPythonのページにアドオン開発の情報があります。BlenderPythonのページは現在も更新され続けていますので、アドオン開発者はブックマークして時々見に行きましょう。もしページを更新したい場合は、BLUG.jpさん（@blug_jp）に連絡すれば、編集権限を与えてもらえるかもしれません。


## 他者が作成したアドオンのソースコードを読む

他者が作成したアドオンのソースコードを読むことでも、Blenderが提供するAPIを調べることができます。

もしアドオン作成時に実現しようとしている処理が他のアドオンでも使われていれば、そのアドオンのソースコードを参照することで、実装方法や使われているAPIを知ることができます。

<div id="sidebyside"></div>

|インストール済みのアドオンのソースコードが置かれている場所は、ファイル > ユーザ設定で開くウィンドウのアドオンタブから確認することができます。<br>非公式にインストールするアドオンの場合は、ダウンロードしたアドオンのソースコードを直接参照することができます。|![アドオンのソースコードを読む1](https://dl.dropboxusercontent.com/s/0gkzz3ww1gjb955/read_addon_source_code_1.png "アドオンのソースコードを読む1")|
|---|---|

なお、Blenderが標準で提供している機能の一部は、Blender内でソースコードを確認したりAPIドキュメントへ移動したりできます。

### Blender内でソースコードを確認する方法

Blender内でソースコードを確認する例として、3Dビューエリアのオブジェクトメニューを構築するためのソースコードを確認します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|3Dビューエリアのメニューである、オブジェクトメニューにマウスカーソルを置いて右クリックし、ソース編集をクリックします。|![アドオンのソースコードを読む2](https://dl.dropboxusercontent.com/s/7gw1t5faq9eyl67/read_addon_source_code_2.png "アドオンのソースコードを読む2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*テキストエディター* にソースコードが表示されます。|![アドオンのソースコードを読む3](https://dl.dropboxusercontent.com/s/bdvh1yevo0m6j5s/read_addon_source_code_3.png "アドオンのソースコードを読む3")|
|---|---|---|

<div id="process_start_end"></div>

---

### APIドキュメントへ移動する方法

確認したいAPIのドキュメントへ移動する例として、3Dビューエリアのメニューである、メッシュ > ミラー > ローカルX軸のAPIドキュメントを表示します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|3Dビューエリアのメニューである、メッシュ > ミラー > ローカルX軸を右クリックして表示されるメニューから、Blender PythonAPI リファレンスをクリックします。|![アドオンのソースコードを読む4](https://dl.dropboxusercontent.com/s/as7l6gpnylb8qvc/read_addon_source_code_4.png "アドオンのソースコードを読む4")|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|BlenderがAPIとして提供している機能であれば、該当するAPIのページが表示されます。　|![アドオンのソースコードを読む5](https://dl.dropboxusercontent.com/s/15i3rc3jspnoqp3/read_addon_source_code_5.png "アドオンのソースコードを読む5")|
|---|---|

<div id="process_start_end"></div>

---

## Blenderのコミュニティサイトで質問する

ドキュメントを調べたり、他のアドオンを参考にしたりしても実装方法が全く思いつかない場合は、コミュニティサイトで質問することも検討しましょう。

幸いなことにBlenderアドオンの開発に関して質問できるサイトはいくつかあり、国内にもアドオン開発で質問できるコミュニティサイトがあります。ただし母数の違いもありますが、アドオン開発は国内に比べて海外のほうがより積極的に行なわれている傾向があるため、海外サイトで質問したほうが期待した回答が得られる可能性が高いです。

以下に、Blenderのアドオン開発について質問できるコミュニティサイトを紹介します。

<div id="webpage"></div>

|Blender Artists Community|
|---|
|http://blenderartists.org/forum/|
|![Blender Artists Community](https://dl.dropboxusercontent.com/s/0e6nkncctmwl0ak/blender_artists.png "Blender Artists Community")|

海外最大のBlenderコミュニティサイトです。

Blenderで制作した作品を投稿する場だけでなく、アドオン開発についても非常に活発な議論が行われる場でもあります。また、作ったアドオンの投稿や既存のアドオンへの要望を出したり、Pythonスクリプトに関する質問したりすることもできます。

非常に有名なサイトであるため、Blenderを使っている方はすでにご存知かもしれませんが、まだ一度も閲覧したことがない方はぜひ1度サイトを見てみるとよいと思います。なお海外サイトですので英語で投稿する必要がありますが、高校生程度の英語力があれば困ることはないと思います。

アカウント登録後、CODING > Python SupportのPOST NEW THREADボタンからアドオンに関して質問することができます。

<div id="webpage"></div>

|Blender Stack Exchange|
|---|
|http://blender.stackexchange.com|
|![Blender Stack Exchange](https://dl.dropboxusercontent.com/s/0zrdm4aebb5xm20/blender_stack_exchange.png "Blender Stack Exchange")|

Stack Overflow( http://stackoverflow.com )と呼ばれる、プログラマ間では非常に有名な情報共有サイトがありますが、本サイトはその派生サイトでBlenderに特化した質問サイトです。

本サイトでは、アドオン開発に関して活発な議論が行われています。また、アドオン開発だけでなくBlenderの使い方に関する質問もできます。

質問するためにはBlender Artists Communityと同様、アカウントを登録した上で英語で投稿する必要があります。質問の投稿は、Ask Questionより行います。

アドオン開発に関する質問の場合、タグにPythonやadd-on、scripting、あとは質問内容に応じて関連するタグ（mathematicsやopenglなど）を入れると回答されやすくなります。

本サイトでは、質問したり他人の質問に回答したり誤字や脱字などを編集したりすることで各ユーザがポイントを得られる仕組みがあり、各ユーザの貢献度を見ることができます。さらに、ポイントを獲得していくことでPS4のトロフィーやXBoxの実績のようなバッジを獲得することができ、初期の段階で利用制限されていた機能を使えるような仕組みもあります。

<div id="webpage"></div>

|Blender.jp|
|---|
|https://blender.jp|
|![Blender.jp](https://dl.dropboxusercontent.com/s/m74dd41qm8xpw7c/blender_jp.png "Blender.jp")|

国内最大のBlenderコミュニティサイトです。

コミュニティサイトには、アカウント登録したユーザがBlenderについて議論できるフォーラムがあり、フォーラム内の質問板でアドオン開発について質問することができます。

これまで紹介してきた他のコミュニティサイトに比べて、アドオン開発に関しての質問はあまり多くないため期待した回答が得られるかはわかりません。しかし日本語で質問できる点がメリットであるため、英語が苦手な方は活用してみると良いかもしれません。

### コミュニティサイトで質問する前に

質問する時には、質問内容をわかりやすく書くのはもちろんですが、ソースコードや実行結果を載せると問題点が相手に伝わりやすくなります。相手がわかりやすい質問の仕方を心がけましょう。そして、質問に対する回答が返ってきたら、回答により解決したか否かに関わらずお礼を言うようにしましょう。

なお、コミュニティサイトで質問すれば、欲しい情報をストレートに得られる可能性がありますが、回答する側も回答の記事を作成するのに時間を費やすため、何でもかんでも質問するのは控えるべきです。コミュニティサイトで質問する前に、まず以下のことを全て行ったかを確認してから質問することを心がけましょう。

* 公式のAPIドキュメントを調べること
* 心当たりのあるアドオンのソースコードを確認すること
* Googleなどの検索で、解決策がないか確認すること
* コミュニティサイトで似たような質問がないか確認すること。（ただし、似たような質問があった時に回答の内容を試してもうまくいかない場合は、再度質問してもよいと思います。）


## まとめ

筆者は、似たような処理を行っているアドオンを参考にしつつ、わからない部分を公式のAPIドキュメントで使用を確認したり、Pythonコンソールウィンドウを使って動作確認したりしてアドオンの開発を進めます。それでも欲しい情報が得られない場合は、コミュニティサイトで質問します。

アドオン開発に限らずプログラミング全般に言えることですが、やはり他者が作成したプログラムのソースコードを参考にするのが、アドオン開発に慣れる近道であると思います。
他の人のソースコードを読んで真似して改造しつつ、わからないところは調べながらアドオンの開発に慣れましょう。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderが提供するAPIは公式のリファレンスやサンプルを読む以外にも、他者が作成したソースコードを読んだり実際にAPIを実行して確かめたりすることでも調査できる
* 一番効果的なAPIの調査方法は、他者が作成したアドオンのソースコードを読んでAPIの具体的な使い方を知ることである。
* わからないからといってすぐにコミュニティに質問する前に、自己解決可能か徹底的に調査すべきである

<div id="space_page"></div>
