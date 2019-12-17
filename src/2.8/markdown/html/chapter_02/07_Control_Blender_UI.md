---
pagetitle: 2-7. BlenderのUIを制御する
subtitle: 2-7. BlenderのUIを制御する
---

BlenderのUIを自由に変えたいと思ったことはありませんか？

実はBlenderのUIの大半はPythonで記載されているため、Pythonを理解できていればある程度自由にBlenderのUIを変更できます。
本節では、PythonからBlenderのUIを制御する方法を説明します。
なお、アドオンの開発はしないけど自分の好みのUIへ改造したい、という場合にも参考になると思います。


# BlenderのUI

BlenderのUIを変更するためには、大変な労力が必要だと思っている人が多いのではないでしょうか。
しかし、BlenderのUIの大半がPythonのソースコードで書かれていることから、本書をここまで読んできた人であれば、UIを制御するための基本的な知識が身についているはずです。
BlenderのUIがPythonのソースコードで書かれていることを確認するために、*[3Dビューポート]* スペースのメニューを変更してみましょう。

以下の手順で、*[3Dビューポート]* スペースのメニューを制御するソースコードを修正します。


<div class="work"></div>

|||
|---|---|
|1|*[3Dビューポート]* スペースのSidebarに配置されているタブ *[ビュー]* より、*[3Dカーソル]* パネルの *[位置]* の下にあるテキストボックスを *[右クリック]* します。<br>![](../../images/chapter_02/07_Control_Blender_UI/change_blender_ui_1.png "BlenderのUIを変更する 手順1")|
|2|表示されたポップアップメニューから、*[ソース編集]* をクリックします。<br>![](../../images/chapter_02/07_Control_Blender_UI/change_blender_ui_2.png "BlenderのUIを変更する 手順2")|
|3|*[テキストエディター]* スペースにソースコードが表示されます。また、*[3Dカーソル]* パネルの *[位置]* の下にあるテキストボックスを表示するためのソースコードに、カーソルが自動的に移動しています。<br>![](../../images/chapter_02/07_Control_Blender_UI/change_blender_ui_3.png "BlenderのUIを変更する 手順3")|
|4|カーソルが示している行をコメントアウトします。<br>![](../../images/chapter_02/07_Control_Blender_UI/change_blender_ui_4.png "BlenderのUIを変更する 手順4")|
|5|*[テキストエディター]* スペースのメニュー *[テキスト]* > *[保存]* を実行し、上書き保存します。<br>![](../../images/chapter_02/07_Control_Blender_UI/change_blender_ui_5.png "BlenderのUIを変更する 手順5")|
|6|[1-4節](../chapter_01/04_Understand_Install_Uninstall_Update_Add-on.html) で紹介した『Reload Scripts』機能を用いてアップデートすると、*[3Dカーソル]* パネルから、*[位置]* の下にあるテキストボックスがラベルを含めて消えます。<br>![](../../images/chapter_02/07_Control_Blender_UI/change_blender_ui_6.png "BlenderのUIを変更する 手順6")|

削除したUIを元に戻すためには、先ほどコメントアウトしたソースコードの行のコメントを外して保存し、『Reload Scripts』機能でアップデートすることで、元に戻すことができます。

ここまでの説明で、BlenderのUIがPythonで制御されていることを理解できたのではないでしょうか。
以降の説明では、BlenderのUIを構築する方法をサンプルアドオンを用いながら説明します。


# 作成するアドオンの仕様

* 以下のようなタブを *[3Dビューポート]* スペースのSidebarに追加する
  * 追加したタブは、*[オブジェクトモード]* 時、かつ最低1つオブジェクトが選択されているときのみ表示される

![](../../images/chapter_02/07_Control_Blender_UI/add-on_spec.png "アドオンの仕様")


# アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして以下のソースコードを入力し、ファイル名を `sample_2-7.py` として保存してください。

[@include-source pattern="full" filepath="chapter_02/sample_2-7.py"]


# アドオンを使用する

## アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考に作成したアドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル2-7: アドオン『サンプル2-7』が有効化されました。
```

さらに、*[3Dビューポート]* スペースのSidebarに、タブ *[カスタムタブ]* が追加されます。
タブは *[オブジェクトモード]* 時、かつオブジェクトが1つ以上選択されているときのみ、表示されることに注意が必要です。


## アドオンの機能を使用する

*[3Dビューポート]* スペースのSidebarのタブ *[カスタムタブ]* をクリックし、パネル *[カスタムパネル]* を表示すると、アドオンの仕様のところで説明したパネルが表示されます。


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル2-7: アドオン『サンプル2-7』が無効化されました。
```


# ソースコードの解説


### プロパティを定義する

アドオンの機能を実行するときに使用するパラメータなどを、ユーザから指定するために必要となるプロパティを定義します。
プロパティの定義は、プロパティクラスの変数を定義することで行えます。


#### プロパティを作成する

プロパティの作成は、アドオン有効化時に `register` 関数から呼び出される `init_props` 関数で行います。
`bpy.types.Scene` にプロパティクラスの変数を追加することで定義できます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="init_props"]


#### プロパティを削除する

アドオンを無効するときには、`bpy.types.Scene` に追加したプロパティクラスの変数を削除する必要があります。
変数を削除せずにアドオンを無効化すると、プロパティクラスの変数のデータがメモリに残ったままとなり、無駄にメモリを消費してしまいます。

本節のサンプルでは、`unregister` 関数から呼び出される `clear_props` 関数により、定義したプロパティクラスの変数を削除しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="clear_props"]


## Sidebarにパネルを追加する

本節のサンプルアドオンでは、Sidebarにタブを追加し、そのタブにパネルを追加しています。
サンプルアドオンのように、アドオンの機能をパネルとしてまとめることで、ユーザはアドオンがどのような機能を持っているかを一目でわかるようになります。
また普段よく使う機能をパネルにまとめ、独自のUIを構築してBlenderの利便性を高めるのも良いかもしれません。

Sidebarにパネルを追加するためには、以下に示すような `bpy.types.Panel` クラスを継承した **パネルクラス** を定義する必要があります。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="panel_cls"]

本節のサンプルアドオンでは、パネルクラスとして `SAMPLE27_PT_CustomPanel` クラスを作成しています。
パネルクラスのクラス名は、フォーマット `XXX_PT_YYY` に従う必要があります。
`XXX` は英大文字から始まる英字/数字/アンダースコア（`_`）から構成される文字列、`YYY` は英字/数字/アンダースコア（`_`）から構成される文字列です。

パネルクラス `SAMPLE27_PT_CustomPanel` には、4つのクラス変数が定義されています。

|クラス変数|値の意味|
|---|---|
|`bl_category`|パネルを登録するタブ名|
|`bl_space_type`|パネルを登録するスペース|
|`bl_region_type`|パネルを登録するリージョン|
|`bl_label`|パネルのヘッダに表示される文字列|


`bl_label` には、パネルのヘッダに表示される文字列を指定します。
クラス変数 `bl_space_type` には、パネルを登録するスペースを指定します。
本節のサンプルでは、*[3Dビューポート]* スペースにパネルを登録することを考えて、`'VIEW_3D'` を指定しています。

クラス変数 `bl_space_type` には、Blenderのスペースに対応した、以下のような値を指定できます。

|設定値|スペース|
|---|---|
|`'VIEW_3D'`|*[3Dビューポート]* スペース|
|`'IMAGE_EDITOR'`|*[画像エディター]* スペース、*[UVエディター]* スペース|
|`'NODE_EDITOR'`|*[シェーダーエディター]* スペース、*[コンポジター]* スペース、*[テクスチャノードエディター]* スペース|
|`'SEQUENCE_EDITOR'`|*[ビデオシーケンサー]* スペース|
|`'CLIP_EDITOR'`|*[動画クリップエディター]* スペース|
|`'DOPESHEET_EDITOR'`|*[ドープシート]* スペース、*[タイムライン]* スペース|
|`'GRAPH_EDITOR'`|*[グラフエディター]* スペース、*[ドライバー]* スペース|
|`'NLA_EDITOR'`|*[ノンリニアアニメーション]* スペース|
|`'TEXT_EDITOR'`|*[テキストエディター]* スペース|
|`'CONSOLE'`|*[Pythonコンソール]* スペース|
|`'INFO'`|*[情報]* スペース|
|`'OUTLINER'`|*[アウトライナー]* スペース|
|`'PROPERTIES'`|*[プロパティ]* スペース|
|`'FILE_BROWSER'`|*[ファイルブラウザー]* スペース|
|`'PREFERENCES'`|*[プリファレンス]* スペース|


クラス変数 `bl_region_type` には、パネルを登録するリージョンを指定します。
本節のサンプルアドオンでは、Sidebarに登録するため、`UI` を指定しています。

クラス変数 `bl_region_type` には、ほかにも以下のような値を設定することが可能です。


|設定値|リージョン|
|---|---|
|`'UI'`|Sidebar。*[N]* キーを押したときに、エリアの右側に表示される領域|
|`'TOOLS'`|Toolbar。*[T]* キーを押したときに、エリアの左側に表示される領域|
|`'TOOL_PROPS'`|オペレータプロパティ。オペレータを実行したときに、エリアの左側下部に表示される領域|
|`'WINDOW'`|エリア中央の領域で、常に表示される領域|
|`'HEADER'`|エリア上部または下部に表示されるバーで、常に表示される領域|


`SAMPLE27_PT_CustomPanel` クラスには、`poll` メソッド、`draw_header` メソッド、`draw` メソッドが定義されています。
各メソッドの処理を以下に示します。定義したメソッドの詳細については後ほど説明します。

|メソッド|処理|
|---|---|
|`poll`|本メソッドが定義されたクラスの処理について、実行可能か否かを判定するメソッド。<br>`True` を返すと実行可能と判断し、`False` を返すと実行不可能であると判断する。<br>実行不可能と判断されると、本メソッドが定義されたクラスで定義したいかなる処理も実行されない|
|`draw_header`|パネルのヘッダを描画するメソッド|
|`draw`|パネルのUIを描画するメソッド<br>本メソッドでは、ヘッダ部のUIを変更することはできない|


### パネルが表示される条件を設定する

本節のサンプルアドオンでは、*[オブジェクトモード]* 時、かつ少なくとも1つ以上のオブジェクトが選択されているときのみ、タブが表示される仕様としていました。
このように、特定の状況下でのみメニューやタブを表示したり、処理を実行できるようにしたりするためには `poll` メソッドとクラス変数 `bl_context` を活用します。

`bl_context` はパネルクラスのクラス変数として定義可能な変数で、指定したコンテキストのときのみ、パネルの描画処理を実行します。
`bl_context` には、以下のような値を設定できます。

|値|説明|
|---|---|
|`"objectmode"`|*[オブジェクトモード]* 時のみ描画する|
|`"mesh_edit"`|*[エディットモード]* 時のみ描画する|

本節のサンプルでは、オブジェクトモード時のみパネルを描画するため、`bl_context = "objectmode"` としています。

また、`poll` メソッドでは、オブジェクトが選択されているときのみ、パネルクラスの処理が実行可能になるように定義しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="poll"]

`poll` メソッドはクラス単位で定義する処理となるため、クラスメソッドとして定義する必要があります。
このため、デコレータ `@classmethod` をつけてメソッドを定義する必要があります。

`poll` メソッドに渡されてくる引数は以下の通りです。

|引数|型|意味|
|---|---|
|`cls`|パネルクラス|`poll` メソッドを実装したクラス|
|`context`|`bpy_types.Context`|`poll` メソッド実行時のコンテキスト|

`poll` メソッド内では `bpy.data.objects` から1つずつオブジェクトを参照し、選択されているオブジェクトが存在する場合は `True` を返しています。
この処理によって、選択されているオブジェクトが1つ以上存在する場合に、タブが表示されます。


### パネルのヘッダUIを変更する

パネルのヘッダのUIを変更するためには、パネルクラスの `draw_header` メソッドを定義します。
`draw` メソッドでは、ヘッダのUIを変更できない点に注意が必要です。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="draw_header"]

`draw_header` メソッドの引数は、以下の通りです。

|引数|型|値の説明|
|---|---|---|
|`self`|パネルクラス|パネルクラスのインスタンス|
|`context`|`bpy_types.Context`|`draw` メソッドが呼ばれたときのコンテキスト|

`draw_header` メソッドでは、メニューのヘッダに表示される文字列の左に、アイコンを表示する処理を定義しています。

`layout.label` の引数を以下に示します。

|引数|型|値の意味|
|---|---|---|
|`text`|str|ラベルに表示する文字列|
|`icon`|str|ラベルの隣に配置するアイコン|

本節のサンプルアドオンでは文字列を表示せずにアイコンのみを表示するため、引数 `text` に空の文字列、引数 `icon` にプラグインのアイコンID `'PLUGIN'` を指定しています。


## UIパーツ

Blenderは、ボタンやリストボックスなどのさまざまなUIパーツを提供しています。
これらのUIパーツは、アドオンからも利用できます。


### ラベル

![ラベル](src/image/chapter_02/07_Control_Blender_UI/ui_label.png)

**ラベル** は、ユーザが編集できないテキストボックスで、主にテキストを表示するために使用します。
`layout.label` メソッドを利用することで、ラベルを配置できます。
引数については、`draw_header` メソッドで説明しましたので、そちらを参照ください。


### ボタン

![ボタン](src/image/chapter_02/07_Control_Blender_UI/ui_button.png)

**ボタン** は `layout.operator` メソッドで追加することができ、以下の引数を指定します。

|引数|型|値の意味|
|---|---|---|
|第1引数|str|オペレータクラスの `bl_idname`|
|`text`|str|ボタンに表示する文字列（指定しない場合は、第1引数に指定した `bl_idname` に対応するオペレータクラスに定義されている、`bl_label` の値が表示される|
|`icon`|str|ボタンに表示するアイコン|
|`emboss`|bool|`False` の場合、文字列の周りの装飾が消える|

ボタンを押すと、`layout.operator` メソッドの第1引数に指定したオペレータクラスの `bl_idname` を持つオペレータクラスの処理が実行されます。
本節のサンプルでは、以下の処理により2種類のボタン（標準のボタンと文字列の周りの装飾が消えたボタン）を追加しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="add_button"]


### セパレータ

`layout.separator` メソッドを呼ぶことで、上下のスペースを空けることができます（**セパレータと呼びます**）。
メニューに対して `layout.separator` メソッドを実行したときの動作については、[2-1節](01_Basic_of_Add-on_Development.html) を参考にしてください。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="add_separator"]


### ドロップダウンメニュー

![ドロップダウンメニュー](src/image/chapter_02/07_Control_Blender_UI/ui_dropdown_menu.png)

`layout.menu` メソッドを利用することで、**ドロップダウンメニュー** を追加できます。

|引数|型|値の意味|
|---|---|---|
|第1引数|str|メニュークラスの `bl_idname`|
|`text`|str|ボタンに表示する文字列（指定しない場合は、第1引数に指定した `bl_idname` に対応するメニュークラスに定義されている、`bl_label` の値が表示される|

メニュー名は、第1引数に指定したメニュークラスのクラス変数 `bl_label` がデフォルトになりますが、`text` 引数に文字列を指定することで変更できます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="add_dropdown_menu"]


### テキストボックス

![テキストボックス](src/image/chapter_02/07_Control_Blender_UI/ui_textbox.png)

ユーザが値を変更可能な **テキストボックス** を配置するためには、`layout.prop` メソッドを使います。
`layout.prop` メソッドの引数を以下に示します。

|引数|型|意味|
|---|---|---|
|第1引数|`bpy.types.Scene`|プロパティクラスの変数を持つオブジェクト|
|第2引数|str|プロパティクラスの変数名|
|`text`|str|表示する文字列（指定しない場合は、プロパティクラスを定義したときに指定したnameの値が表示される）|

サンプルアドオンでは、`bpy.types.Scene` にプロパティクラスの変数を登録したため、`context.scene` を第1引数に指定します。
第2引数には、`bpy.types.Scene` に登録したプロパティクラスの変数名を文字列で指定します。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="add_textbox"]


### ドロップダウンプロパティ

![ドロップダウンプロパティ](src/image/chapter_02/07_Control_Blender_UI/ui_dropdown_property.png)

**ドロップダウンプロパティ** は、登録された項目の中からユーザが値を設定可能なUIパーツです。
`self.layout.prop` メソッドの第2引数に、`bpy.props.EnumProperty` クラスの変数を指定することで、ドロップダウンプロパティを作成できます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="add_dropdown_property"]


### チェックボックス

![チェックボックス](src/image/chapter_02/07_Control_Blender_UI/ui_checkbox.png)

**チェックボックス** は、ユーザがON/OFFを切りかえることができるUIパーツです。
`self.layout.prop` メソッドの第2引数に、`bpy.props.BoolProperty` の変数を指定することで、チェックボックスを作成できます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="add_checkbox"]


## 整列


### 一行配置（アライメントなし）

![一行に配置（アライメントなし）](src/image/chapter_02/07_Control_Blender_UI/ui_arrange_row_without_align.png)

`layout.operator` メソッドを用いると、横幅が100%のボタンが配置されます。
このため、単純に `layout.operator` メソッドを複数回実行すると、実行した回数分だけ縦方向にボタンが配置されてしまいます。

ボタンを横に並べるためには、`layout.row` メソッドを使って行成分を取得し、取得した行成分に対して `operator` メソッドを使ってボタンを配置する必要があります。
本節のサンプルでは、以下のようにして3つのボタンを一行に並べています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="arrange_column"]

なお、`operator` メソッドの代わりに `label` メソッド、`prop` メソッドや `menu` メソッドを使うことによって、ラベルやボタンなどを一行に並べて配置できます。


### 一行配置（アライメントあり）

![一行に配置（アライメントあり）](src/image/chapter_02/07_Control_Blender_UI/ui_arrange_row_with_align.png)

`layout.row` メソッドの引数に `align=True` を指定すると、ボタンとボタンの間に隙間がなくなるように配置されます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="arrange_column_align"]


### 一列配置（アライメントなし）

![一列に配置（アライメントなし）](src/image/chapter_02/07_Control_Blender_UI/ui_arrange_column_without_align.png)

`layout.operator` メソッドを複数回実行することでボタンを一列に配置できますが、隙間が広くて気に入らない人もいると思います。
隙間を縮めた状態でボタンを縦に並べるためには、`layout.column` メソッドを使って列成分を取得し、取得した列成分に対して `operator` メソッドを使ってボタンを配置します。

本節のサンプルでは、以下のように3つのボタンを一列に並べています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="arrange_row"]

なお、`operator` メソッドの代わりに `label` メソッド、`prop` メソッドや `menu` メソッドを使うことによって、ラベルやボタンなどを一列に並べて配置できます。


### 一列配置（アライメントあり）

![一列に配置（アライメントあり）](src/image/chapter_02/07_Control_Blender_UI/ui_arrange_column_with_align.png)

`layout.column ` メソッドの引数に `align=True` を指定すると、ボタンとボタンの間に隙間がなくなるように配置されます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="arrange_row_align"]


### 複数行、複数列配置

![複数行、複数列に配置](src/image/chapter_02/07_Control_Blender_UI/ui_arrange_multi.png)

`layout.column` メソッドや `layout.row` メソッドで取得した行成分や列成分に対して、さらに行成分や列成分を取得することで、より複雑なボタンの配置を実現することができます。

本節のサンプルでは、以下のようにして2行2列にボタンを配置しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="arrange_row_multi"]


### 領域分割

![領域分割](src/image/chapter_02/07_Control_Blender_UI/ui_split_region.png)

`layout.row` メソッドを用いて行成分を取得することで、一行にボタンを配置することができますが、ボタンはすべて等幅になっていました。
ボタンの横幅を変えたいときは、`layout.split` メソッドを用いて領域を分割します。

`layout.split` メソッドの引数 `factor` に値を指定することで、領域の横幅を決めることができます。
引数 `factor` の値はfloat型で指定し、`1.0` で横幅100%、`0.0` で横幅0%となります。
例えば、Sidebarの横幅に対して70%の横幅を持つ領域を分割する場合は、`layout.split(factor=0.7)` とします。

本節のサンプルでは、以下のような処理で領域を3分割しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="divide_region"]

分割後の各領域では、縦並びにボタンを2つ表示しています。

`layout.split` メソッドによって分割した領域の変数 `split` に対して、`split.split` メソッドを実行することで、2つ以上の領域に分割できます。
なお、`split.split` メソッドに指定する引数 `factor` について注意が必要です。
最初の領域分割で `layout.split` メソッドを実行するときは、引数に指定した `factor` がSidebarの横幅に対する割合を示しますが、2回目の領域分割で `split.split` メソッドを実行したときは、`layout.split` メソッドで分割した残りの領域、つまりサンプルアドオンではSidebarの横幅70%の領域に対する割合を指定します。
同様に3回目の領域分割では、2回目に分割した残りの領域に対する割合を指定します。
したがって、Sidebarに対する横幅はそれぞれ、領域1で30%、領域2で70%×0.7=49%、領域3で70%×0.3=21%となります。


### 明示的な横幅最大化

![明示的な横幅の最大化](src/image/chapter_02/07_Control_Blender_UI/ui_explicit_expantion.png)

`layout.operator` メソッドを使ってボタンを配置すると、ボタンの横幅が自動的に領域全体へ拡大されますが、ボタンの横幅を明示的に領域全体に最大化する方法もあります。

サンプルアドオンでは、以下のように `row.alignment` に `EXPAND` を設定し、明示的にボタンの横幅を自動的に最大化しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="align_expand"]


### 左寄せ

![左寄せ](src/image/chapter_02/07_Control_Blender_UI/ui_aligh_left.png)

ボタンの横幅を自動的に最大化せず、右や左に寄せて配置することもできます。

サンプルアドオンでは、以下のように `row.alignment` に `LEFT` を指定し、ボタンを左寄せ配置しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="align_left"]


### 右寄せ

![右寄せ](src/image/chapter_02/07_Control_Blender_UI/ui_aligh_right.png)

`row.alignment` に `RIGHT` を指定することで右寄せ配置も可能です。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="align_right"]


### グループ化

![グループ化](src/image/chapter_02/07_Control_Blender_UI/ui_grouping.png)

複数のUIパーツをグループ化することもできます。
`layout.box` メソッドの戻り値に対して `operator` メソッドや `menu` メソッドなどを呼び出すことで、作成したUIがグループ化されます。

サンプルアドオンでは、以下のソースコードにより4つのボタンをグループ化しています。
グループ内のUIは、通常のUIと同様の方法でUIを構築できます。

[@include-source pattern="partial" filepath="chapter_02/sample_2-7.py" block="grouping"]


# まとめ

本節では、BlenderのUIをPythonから制御できることを確認しました。
また、*[3Dビューポート]* スペースのSidebarへパネルを追加する方法について説明し、UIパーツの配置方法や整列方法も説明しました。

BlenderのUIを変更すると聞くと難しそうに思えますが、Pythonさえ理解できていればなんとかなりそうだと思えてきたのではないでしょうか？
最後に、本節で紹介したUIパーツの配置や整理に使用するAPIをまとめます。

|UI|API|
|---|---|
|ラベル|`layout.label`|
|ボタン|`layout.operator`|
|セパレータ|`layout.separator`|
|ドロップダウンメニュー|`layout.menu`|
|テキストボックス|`layout.prop`|
|ドロップダウンプロパティ|`layout.prop` （`bpy.props.EnumProperty`）|
|チェックボックス|`layout.prop` （`bpy.props.BoolProperty`）|
|行成分取得（アライメントなし）|`layout.row` <br> `layout.row(align=False)`|
|行成分取得（アライメントあり）|`layout.row(align=True)`|
|列成分取得（アライメントなし）|`layout.column` <br> `layout.column(align=False)`|
|列成分取得（アライメントあり）|`layout.column(align=True)`|
|領域分割|`layout.split`|
|明示的な横幅最大化|`row.alignment = 'EXPAND'`|
|左寄せ|`row.alignment = 'LEFT'`|
|右寄せ|`row.alignment = 'RIGHT'`|
|グループ化|`layout.box`|


## ポイント

* BlenderはボタンやメニューなどのUIパーツを追加するためのAPIを用意しているため、APIを活用することで独自のUIを構築できる
* Sidebarにパネルを追加するためには、`bpy.types.Panel` クラスを継承したパネルクラスを定義し、クラス変数 `bl_region_type` に `UI` を指定する必要がある
* 特定の状況下でのみメニューを表示したり、処理を実行を許可したりするなど、定義した処理の実行を制限する場合は、`poll` メソッドを定義する
* パネルクラスのクラス変数 `bl_context` を定義することで、パネルクラスの処理を実行するコンテキストを指定できる
* Sidebarに追加したパネルのヘッダのUIを変更するためには、パネルクラスに `draw_header` メソッドを定義する
* Sidebarに追加したパネルのメニューのUIを変更するためには、パネルクラスに `draw` メソッドを定義する
