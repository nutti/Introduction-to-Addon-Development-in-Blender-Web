<div id="sect_title_img_4_1"></div>

<div id="sect_title_text"></div>

# Blenderが提供する<br>アドオン向けのAPIを調べる

<div id="preface"></div>

###### これまで紹介したサンプルでは、Blenderが提供する様々なAPIを使ってきましたが、サンプルで用いたAPIはどのようにして知ることができたのでしょうか？本節ではこの疑問に答えるため、Blenderが提供するAPIを調べる方法を紹介します。

## Blenderが提供するAPIの情報源

Blenderが提供するAPIの情報を収集する方法としては、以下のようなものがあります。

* Blender公式のAPIリファレンスを読む
* PythonコンソールでAPIを検索・実行する
* テキストエディタのテンプレートを読む
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

#### Application Modules

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

#### Standalone Modules

Standalone Modulesは、 ```bpy``` モジュールを拡張するモジュールです。Application Modulesを使っただけでは実装が大変な処理を簡単かつ効率的に行うことができるAPIが提供されています。

|モジュール名|概要|
|---|---|
|```mathutils```|行列やベクトルなどのクラスや、行列やベクトル演算を簡単に行うことができる関数群<br> ```geometry``` や ```kdtree``` サブモジュールを用いることで、図形の交差判定や3D空間内の探索を高速に行うことも可能|
|```bgl```|PythonからOpenGLへアクセスするためのラッパー関数群|
|```blf```|文字列描画を簡単に行うための関数群|
|```gpu```|GLSLを扱うための関数群|
|```aud```|サウンドの読み込みや再生を行うための関数群|
|```bpy_extras```|```bpy``` モジュールを補助する目的で提供される便利関数群|
|```bmesh```|メッシュデータを容易に扱うための関数群|

ここでは、3Dビューエリアでアクティブ状態のオブジェクトを取得するためのAPI  ```bpy.props.EnumProperty``` を調べます。

<div id="sidebyside"></div>

|Application Modules > Property Definitions (bpy.props) をクリックし、 ```bpy.props.EnumProperty``` を探します。<br>すると右図のように、APIの説明に加えて引数や各引数の説明を見ることができます。|![API documentation EnumProperty](https://dl.dropboxusercontent.com/s/xvi335558nxtwhi/blender_api_doc_enum_property.png "API documentation EnumProperty")|
|---|---|


### PythonコンソールでAPIを検索・実行する

[2.2節](../chapter_02/02_Register_Multiple_Operation_Classes.md)でも説明しましたが、 Pythonコンソールを用いることでBlenderが提供するAPIを検索し、実行することができます。

ここでは、Pythonコンソールを使ってAPIを調査する例を紹介します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|3Dビューエリア上にあるオブジェクト一覧を参照できる変数 ```bpy.data.objects``` をPythonコンソールに入力します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|ctrl+spaceをキーを押して補完します。|![Pythonコンソール 手順1](https://dl.dropboxusercontent.com/s/6tqu81bbk6l6qy8/python_console_1.png "Pythonコンソール 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|3Dビューエリア上にあるオブジェクト名が候補として表示されるため、適当なオブジェクト名を選んで再び補完します。|![Pythonコンソール 手順2](https://dl.dropboxusercontent.com/s/yu890kcedpewpih/python_console_2.png "Pythonコンソール 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|候補の中にある ```select``` を入力し、実行します。<br>すると、選んだオブジェクトが選択状態である場合は ```True``` 、選択状態でない場合は ```False``` が表示されます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|```select``` に ```True``` を代入することでオブジェクトを選択状態に、  ```False``` を代入することでオブジェクトを非選択状態に変更することができます。|![Pythonコンソール 手順3](https://dl.dropboxusercontent.com/s/0aph2y0pq6edyxf/python_console_3.png "Pythonコンソール 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


以上のことから、 ```select``` はオブジェクトが選択状態であるか否かを調べるためのAPIであると判断できます。

実際にBlender公式のAPIドキュメント(```http://www.blender.org/api/blender_python_api_2_75a_release/bpy.types.Object.html#bpy.types.Object.select```)を調べてみると、以下のように記載されています。

<div id="quote"></div>

> Object selection state

このように、Pythonコンソールを利用することでAPIの動作を確認できます。APIの効果がわからない場合はPythonコンソールを用いて実際に動作させてAPIの効果を確認することで、よりAPIへの理解が深まると思いますので積極的に活用していきましょう。


### テキストエディタのテンプレートを読む

<div id="sidebyside"></div>

|BlenderでPythonスクリプトを書く人向けに、Blenderはアドオンのテンプレートを用意しています。これらのサンプルはBlender本体が提供しているため、正常に動作することが保証されています。<br>作りたいアドオンに関連するテンプレートがあれば、一度確認することをお勧めします。また、Blenderが提供するAPIの概要を一通り学んでおきたい場合にも、本サンプルは参考になります。|![テンプレート 手順1](https://dl.dropboxusercontent.com/s/bvnb1360j99fd1t/template_1.png "テンプレート 手順1")|
|---|---|



<div id="sidebyside"></div>

|提供されいる中で最も簡単なテンプレートは、右図で示す ```Operator Simple``` です。```Operator Simple``` は、3Dビューエリアにあるオブジェクト一覧をコンソールに表示するサンプルです。|![テンプレート 手順2](https://dl.dropboxusercontent.com/s/8nt0v8zdkhl1egd/template_2.png "テンプレート 手順2")|
|---|---|
