<div id="sect_title_img_4_1"></div>

<div id="sect_title_text"></div>

# Blenderが提供する<br>アドオン向けのAPIを調べる

<div id="preface"></div>

###### これまで紹介したサンプルでは、Blenderが提供する様々なAPIを使ってきました。サンプルで用いたAPIはどこで知ることができたのでしょうか？そんな疑問に答えるのが本節で紹介するAPIの調査方法です。


## Blenderが提供するAPIの情報源

Blenderが提供するAPIの情報を収集する方法としては以下のようなものがあります。

* Blender公式のAPIリファレンスを読む
* *Pythonコンソール* でAPIを検索・実行する
* *テキストエディタ* のテンプレートを読む
* Blenderアドオン開発の参考サイトを読む
* 他者が作成したアドオンのソースコードを読む
* Blenderのコミュニティサイトで質問する


### Blender公式のAPIドキュメントを読む

Blenderが提供しているAPI一覧は、Blender公式が公開しているドキュメントから確認することができます。

<div id="webpage"></div>

|API documentation|
|---|
|http://www.blender.org/api/|
|![API documentation](https://dl.dropboxusercontent.com/s/3pgs57v7b29ngo8/blender_api_doc.png "API documentation")|

過去のBlenderのバージョンのドキュメントも参照できますが、Blenderのバージョンに応じて提供されているAPIは変わるため、開発に利用しているBlenderのバージョンのドキュメントを参照するようにしましょう。
本書のサンプルはBlenderのバージョンが2.75aであるため、バージョンが2.75aであるドキュメントを前提として解説します。

<div id="webpage"></div>

|API documentation (Blender 2.75a)|
|---|
|http://www.blender.org/api/blender_python_api_2_75a_release/|
|![API documentation 2.75a](https://dl.dropboxusercontent.com/s/hmzkcciai4ooigb/blender_api_doc_2_75a.png "API documentation 2.75a")|

*3Dビュー* ウィンドウのアクティブ状態のオブジェクトを取得するAPIを調べてみましょう。
右側のページには、提供するAPIに対してモジュールごとにメニュー化されています。
モジュールは大きく分けて以下の3つにグループ化されています。

|項目|内容|
|---|---|
|Application Modules|基本モジュール（bpyモジュール）。Blender本体のデータにアクセスするために最低限必要なモジュール|
|Standalone Modules|拡張モジュール。Application Modulesを簡単に利用したり、アドオン開発を便利にするためのモジュール|
|Game Engine Modules|Blender Game Engine向けモジュール|

最後の *Game Engine Modules* は、Blenderが提供するゲームエンジン *Blender Game Engine(BGE)* 向けのモジュールあるため、アドオンの開発では基本的に使用しません。
アドオン開発に限るのであれば、 *Application Modules* と *Standalone Modules* のみを確認すればよいでしょう。

#### Application Modules

*Application Modules* である ```bpy``` モジュールは非常に大きなモジュールであるため、複数のサブモジュールから構成されています。
以下にアドオン開発時によく利用するモジュールをまとめました。
アドオンを開発する時に必ず必要になるモジュールであるため、どのようなモジュールが提供されているか一度目を通しておくとよいでしょう。

|モジュール名|概要|
|---|---|
|```bpy.context```|現在のBlenderの実行状態（コンテキスト）を取得するためのAPI群|
|```bpy.data```|メッシュや画像データなど、Blenderで利用されているデータへアクセスするためのAPI群|
|```bpy.ops```|Blenderのデータに対する操作や、アドオンで登録した操作|
|```bpy.types```|Blenderで提供している型|
|```bpy.utils```|アドオンで利用するクラスの登録など、アドオンへ提供する便利関数群|
|```bpy.path```|Blender内でパスを簡単に扱うための関数群|
|```bpy.app```|Blenderのバージョンなど、Blender本体の情報など|
|```bpy.props```|アドオン内部で扱うプロパティ|

#### Standalone Modules

*Standalone Modules* は、 ```bpy``` モジュールを拡張するモジュールです。
*Application Modules* だけでは実装が大変な処理を簡単に行うことができるようなAPIや UIを構築するためのAPIなど、アドオン開発で役立つモジュールばかり揃っていますので、こちらも目を通しておきましょう。

|モジュール名|概要|
|---|---|
|```mathutils```|行列やベクトルなどのクラスや演算関数群。また、 ```geometry``` や ```kdtree``` サブモジュールを用いることで、図形の交差判定や3D空間内の探索を高速に行うことができます|
|```bgl```|OpenGLのラッパー関数群|
|```blf```|文字列描画を容易に行うための関数群|
|```gpu```|GLSLを扱うための関数群|
|```aud```|サウンドの読み込みや再生を行うための関数群|
|```bpy_extras```|```bpy``` モジュールに含まれない ```bpy``` 関連の便利関数群|
|```bmesh```|メッシュデータを容易に扱うための関数群|

ここでは、 *3Dビュー* でアクティブ状態のオブジェクトを取得するためのAPI  ```bpy.props.EnumProperty``` を調べてみましょう。

<div id="sidebyside"></div>

|*Application Modules* > *Property Definitions (bpy.props)* をクリックし、 ```bpy.props.EnumProperty``` を探してみましょう。<br>右図のように、APIの説明に加えて引数に指定できる値や各引数の説明を参照することができます。|![API documentation EnumProperty](https://dl.dropboxusercontent.com/s/xvi335558nxtwhi/blender_api_doc_enum_property.png "API documentation EnumProperty")|
|---|---|


### PythonコンソールでAPIを検索・実行する

[1.2節]("../chapter_02/02_Sample_2_Scaling_object_1.md")においても説明しましたが、 *Pythonコンソール* を用いることでBlenderが提供しているAPIを検索・実行することができます。

<div id="process_start_end"></div>

---

<div id="process_noimg"></div>

|1|Blender内のオブジェクト一覧を保持している ```bpy.data.objects``` を *Pythonコンソール* に入力します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|```ctrl + space``` をキーを押して補完します。|![Pythonコンソール 手順1](https://dl.dropboxusercontent.com/s/6tqu81bbk6l6qy8/python_console_1.png "Pythonコンソール 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|3|*3Dビュー* 上にあるオブジェクト名が候補として表示されるので、適当なオブジェクト名を選んで再び補完します。|![Pythonコンソール 手順2](https://dl.dropboxusercontent.com/s/yu890kcedpewpih/python_console_2.png "Pythonコンソール 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|4|候補の中にあった ```select``` を入力し、実行します。<br>選んだオブジェクトが選択状態である場合は ```True``` 、選択状態でない場合は ```False``` が表示されます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|5|```select``` に ```True``` を代入することでオブジェクトを選択状態に、  ```False``` を代入することでオブジェクトを非選択状態に変更することもできます。|![Pythonコンソール 手順3](https://dl.dropboxusercontent.com/s/0aph2y0pq6edyxf/python_console_3.png "Pythonコンソール 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


どうやら ```select``` は、オブジェクトが選択状態であるか否かを調べるAPIのようです。
実際に[Blender公式のAPIドキュメント](http://www.blender.org/api/blender_python_api_2_75a_release/bpy.types.Object.html#bpy.types.Object.select)を調べてみると、以下のように記載されています。

> Object selection state

このように、 *Pythonコンソール* を利用することでAPIを動作確認できるため、APIの効果がわかりづらい場合は、実際に動作させてAPIの効果を確認してみましょう。


### テキストエディタのテンプレートを読む

<div id="sidebyside"></div>

|Blenderの *テキストエディタ* には、アドオンのテンプレートが用意されています。|![テンプレート 手順1](https://dl.dropboxusercontent.com/s/bvnb1360j99fd1t/template_1.png "テンプレート 手順1")|
|---|---|

Blender本体が提供しているサンプルであることから動作が保証されているので、作りたいアドオンに関連するテンプレートがあれば、ぜひ確認してみるとよいでしょう。
また、Blenderが提供するAPIの概要を一通り学んでおきたい場合にも、参考になるでしょう。

<div id="sidebyside"></div>

|提供されいる中で最も簡単なテンプレートは ```Operator Simple``` です。|![テンプレート 手順2](https://dl.dropboxusercontent.com/s/8nt0v8zdkhl1egd/template_2.png "テンプレート 手順2")|
|---|---|

### Blenderアドオン開発の参考サイトを読む

Blenderが提供するAPIを調べる手段として、Blenderアドオン開発の参考サイトを読む方法もあります。
しかしBlenderを利用している人に比べBlenderのアドオンを開発している人は非常に少なく、Blender本体に比べてアドオン開発の解説サイトは格段に少なくなります。
特に日本語での解説となると、解説サイトの数は本当に限られます。
必要に応じて、海外サイトを利用することも考えましょう。

アドオン開発で筆者が参考にしているサイトをいくつかピックアップしてみました。
Blender Wiki様は海外サイト、blugjpまとめサイト様は国内サイトです。

<div id="webpage"></div>

|Blender Wiki|
|---|
|http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts|
|![Blender Wiki](https://dl.dropboxusercontent.com/s/wjaloh1eov0ij73/blender_wiki.png "Blender Wiki")|

Blenderの公式Wikiページです。
アドオン開発のチュートリアルやベストプラクティスなど、アドオン開発に必要な知識を学ぶことができます。
特にテーマに応じた簡単なサンプルが紹介されいているCode Snippetsは、アドオン開発者必見です。
また、アドオン公開方法の手順についても書かれていますので、初心者だけでなくアドオンをこれから公開しようと考えている方も参考になると思います。

<div id="webpage"></div>

|blugjpまとめサイト|
|---|
|https://sites.google.com/site/blugjp/blenderpython|
|![blugjpまとめサイト](https://dl.dropboxusercontent.com/s/7t6ho0xohl45yrv/blugjp.png "blugjpまとめサイト")|

BLUG.jpさんによるまとめサイトです。
BlenderPythonのページは現在も更新され続けているので、アドオンを開発している方はブックマークして時々見に行ってみましょう。
もしページを更新したい場合は、BLUG.jpさん（@blug_jp）に連絡してみましょう。


### 他者が作成したアドオンのソースコードを読む

他者が作成したアドオンのソースコードを読むことでも、Blenderが提供するAPIを調べることができます。
もしアドオン作成時に実現しようとしている処理が他のアドオンでも使われていれば、そのアドオンのソースコードを参照することで、実装方法や使われているAPIを知ることができるため、最もおすすめな方法です。

<div id="sidebyside"></div>

|インストール済みのアドオンのソースコードが置かれている場所は、 *ファイル* > *ユーザ設定* の *アドオン* タブから確認することができます。<br>また非公式にインストールするアドオンは、アドオンをダウンロード時のファイルを参照することにより、インストールせずに確認することもできます。|![アドオンのソースコードを読む1](https://dl.dropboxusercontent.com/s/0gkzz3ww1gjb955/read_addon_source_code_1.png "アドオンのソースコードを読む1")|
|---|---|

Blenderが標準で提供している機能の一部は、Blender内でソースコードを確認したりAPIドキュメントへ移動したりできます。
例えば、 *3Dビュー* の *オブジェクト*

#### Blender内でソースを確認する方法

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|メニューのソースをみたい場合には、メニューにマウスカーソルを置いて右クリックします。|![アドオンのソースコードを読む2](https://dl.dropboxusercontent.com/s/7gw1t5faq9eyl67/read_addon_source_code_2.png "アドオンのソースコードを読む2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|*ソース編集* を選択すると、 *テキストエディタ* にソースが表示されます。|![アドオンのソースコードを読む3](https://dl.dropboxusercontent.com/s/bdvh1yevo0m6j5s/read_addon_source_code_3.png "アドオンのソースコードを読む3")|
|---|---|---|

<div id="process_start_end"></div>

---

#### APIドキュメントへ移動する方法

<div id="process_start_end"></div>

---

<div id="process"></div>

|1|APIとして提供されている機能であれば、 *Blender PythonAPI リファレンス* のページに移動することができます。|![アドオンのソースコードを読む4](https://dl.dropboxusercontent.com/s/as7l6gpnylb8qvc/read_addon_source_code_4.png "アドオンのソースコードを読む4")|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|2|　|![アドオンのソースコードを読む5](https://dl.dropboxusercontent.com/s/15i3rc3jspnoqp3/read_addon_source_code_5.png "アドオンのソースコードを読む5")|
|---|---|

<div id="process_start_end"></div>

---

### Blenderのコミュニティサイトで質問する

ドキュメントを調べたり、他のアドオンを参考にしても実装方法が全く思いつかない場合は、コミュニティサイトで質問しましょう。
幸いなことにBlenderアドオンの開発に関して質問できるサイトはそれなりに多く、国内にもアドオン開発で質問できるコミュニティサイトはあります。
ただしアドオン開発は海外の方が積極的に行なわれている傾向のため、海外サイトで質問したほうが期待した回答が得られる可能性が高いです。
以下にBlenderのアドオン開発について、質問できるコミュニティサイトを紹介します。

<div id="webpage"></div>

|Blender Artists Community|
|---|
|http://blenderartists.org/forum/|
|![Blender Artists Community](https://dl.dropboxusercontent.com/s/0e6nkncctmwl0ak/blender_artists.png "Blender Artists Community")|

海外最大のBlenderコミュニティサイトです。
Blenderで制作したCGの投稿だけでなく、アドオン開発についても非常に活発な議論が行われています。
また、作ったアドオンの投稿や新規機能の追加要望なども行うこともできます。
Blenderを使っている方はすでにご存知のサイトかもしれませんが、まだ見たことがない方はぜひ1度サイトを覗いてみるとよいでしょう。

英語で投稿する必要がありますが、高校生程度の英語力があれば困ることはないと思います。
アドオンに関する質問はアカウント登録した上で、 *CODING* > *Python Support* から行ってください。
投稿は *POST NEW THREAD* ボタンから行えます。

<div id="webpage"></div>

|Blender Stack Exchange|
|---|
|http://blender.stackexchange.com|
|![Blender Stack Exchange](https://dl.dropboxusercontent.com/s/0zrdm4aebb5xm20/blender_stack_exchange.png "Blender Stack Exchange")|

Stack Overflow(http://stackoverflow.com)と呼ばれる、海外のプログラマ間の情報共有サイトのBlenderに特化したサイトです。
コミュニティサイトよりも質問サイトとしての位置付けとなります。
こちらもアドオン開発に関して活発な議論が行われています。
また、アドオン開発だけでなくBlenderの使い方に関する質問もできるようです。

Blender Artists Communityと同様、アカウント登録した上で英語で投稿する必要があります。
質問の投稿は、Ask Questionより行います。
アドオン開発に関する質問の場合、タグにPythonやadd-on、scripting、あとは質問内容に応じて関連するタグ（mathematicsやopenglなど）を入れておくとよいでしょう。

<div id="webpage"></div>

|Blender.jp|
|---|
|https://blender.jp|
|![Blender.jp](https://dl.dropboxusercontent.com/s/m74dd41qm8xpw7c/blender_jp.png "Blender.jp")|

国内最大のBlenderコミュニティサイトです。
コミュニティサイトにはフォーラムがあり、フォーラム中の質問板でアドオン開発について質問することができます。
ここで紹介する他のコミュニティサイトに比べ、アドオン開発に関しての質問はあまり多くないため期待した回答が得られるかわかりませんが、日本語で質問できる点はメリットでしょう。


質問の際には、質問内容をわかりやすく書くのはもちろんですが、ソースコードや実行結果を載せると問題点が相手に伝わりやすくなります。そして、質問に対する回答が返ってきたら、回答により解決したか否かに関わらずお礼を言うようにしましょう。

なお、コミュニティサイトで質問すれば、欲しい情報をストレートに得られる可能性がありますが、回答する側も回答の記事を作成するのに時間を費やすため、何でもかんでも質問するのはやめましょう。
コミュニティサイトで質問する前に、まず以下のことを全て行ったかを確認するとよいでしょう。

* ドキュメントを調べること
* 心当たりのあるアドオンのソースコードを確認すること
* Googleなどの検索で、解決策がないか確認すること
* コミュニティサイトで似たようなの質問がないか確認すること。（ただし、似たような質問があった時に回答の内容を試してもうまくいかない場合は、質問してもよいと思います。）


## まとめ

筆者がアドオンを開発する時は、似たような処理を行っているアドオンを参考にしてわからない部分を公式のAPIドキュメントを参照したり、 *Pythonコンソール* を使って動作確認したりして実装を進めていきます。
それでも欲しい情報が得られない場合は、コミュニティサイトに聞いてヘルプを求めます。

アドオン開発に限らずプログラミング全般に言えることですが、やはり他者が作成したすでに動いているソースを参考にするのが、アドオンの開発上達のための近道であると思います。
他の人のソースコードを読んで真似して改造して、わからないところは調べるようにしていきましょう。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderが提供するAPIは公式のリファレンスやサンプルを読む以外にも、他者が作成したソースコードを読んだり実際にAPIを実行して確かめることでも調査できる
* 他者が作成したアドオンのソースコードを読むことはAPIの使い方の理解にも繋がるため、APIの調査する上で一番効果的である
* コミュニティに質問する前に、自己解決可能か徹底的に調査する
