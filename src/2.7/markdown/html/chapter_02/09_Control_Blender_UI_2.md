---
pagetitle: 2-9. BlenderのUIを制御する②
subtitle: 2-9. BlenderのUIを制御する②
---

[2-8節](08_Control_Blender_UI_1.html) に引き続き、BlenderのUIを制御する方法を説明します。
本節ではボタンの配置やメニューなどのUI部品の配置方法に加え、UI部品の整列方法についても説明します。
また本節のサンプルは、アドオンで利用可能なアイコンの一覧を表示する機能もありますので、アドオンでアイコンを使うことを考えている方は、どのようなアイコンが使えるかを確認しておくと良いかもしれません。


# 作成するアドオンの仕様

* 以下のようなタブを [3Dビュー] エリアのツール・シェルフに追加する

![](../../images/chapter_02/09_Control_Blender_UI_2/add-on_spec.png "アドオンの仕様")

* [利用可能なアイコンをすべて表示] ボタンをクリックすると、アドオンから利用可能なアイコンをツール・シェルフのオプションに表示する
* [利用可能なアイコンをすべて表示] 以外のボタンやメニューなどを操作しても、基本的に何も起こらない


# アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして以下のソースコードを入力し、ファイル名を `sample_2_9.py` として保存してください。

[@include-source pattern="full" filepath="chapter_02/sample_2_9.py"]


# アドオンを使用する

## アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考に作成したアドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル2-9: アドオン「サンプル2-9」が有効化されました。
```

そして、[3Dビュー] エリアのツール・シェルフにタブ [カスタムメニュー] が追加されます。


## アドオンの機能を使用する

[3Dビュー] エリアのツール・シェルフのタブ [カスタムメニュー] をクリックすると、メニューが表示されます。

[カスタムメニュー] に表示されたボタンやメニューなどをクリックしたり選択したりできますが、[利用可能なアイコンをすべて表示] ボタンをクリックした時を除いて基本的に何も起こりません。


### 利用可能なアイコンをすべて表示ボタン

[利用可能なアイコンをすべて表示] ボタンをクリックすると、アドオンで利用可能なアイコンの一覧がツール・シェルフに表示されます。


<div class="work"></div>

|||
|---|---|
|1|タブ [カスタムメニュー] の [利用可能なアイコンをすべて表示] ボタンをクリックします。<br>![](../../images/chapter_02/09_Control_Blender_UI_2/icon_list_1.png "利用可能なアイコンをすべて表示ボタン 手順1")|
|2|ツール・シェルフのオプションに、アドオンから利用可能なアイコン一覧と、それぞれのアイコンを表示するためのキーコード（識別子）が表示されます。<br>![](../../images/chapter_02/09_Control_Blender_UI_2/icon_list_2.png "利用可能なアイコンをすべて表示ボタン 手順2")|
|3|[一行に表示するアイコン数] の値を変えることで、一行に表示するアイコンの数を変更することができます。<br>![](../../images/chapter_02/09_Control_Blender_UI_2/icon_list_3.png "利用可能なアイコンをすべて表示ボタン 手順3")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル2-9: アドオン「サンプル2-9」が無効化されました。
```


# ソースコードの解説

本節のサンプルプログラムは説明するUIの種類が多いためソースコードの規模は大きいです。
幸いなことに各UIを構築するソースコードは短く、かつUIごとに区切って説明しますので、規模が大きさに惑わされずに少しずつ理解していきましょう。


## メニューを構築する

タブのメニューを構築するためには、`draw` メソッドを定義する必要があります。
`draw` メソッドの引数などの詳細については、[2-5節](05_Create_Sub-menu.html) を参考にしてください。

本節のサンプルの `draw` メソッドのコードは非常に長いので、それぞれのUIごとに説明していきます。


### ボタンを追加する

本節のサンプルでは、以下の処理により2種類のボタン（標準のボタンと文字列の周りの装飾が消えたボタン）を追加しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="add_button", unindent="True"]


ボタンは `layout.operator` 関数で追加することができ、以下の引数を指定します。
ボタンを押すと、`layout.operator` 関数の第1引数に指定したオペレータクラスの `bl_idname` を持つオペレータクラスの処理が実行されます。

|引数|値の意味|
|---|---|
|第1引数|オペレータクラスの `bl_idname`|
|`text`|ボタンに表示する文字列|
|`icon`|ボタンに表示するアイコン|
|`emboss`|`False` の場合、文字列の周りの装飾が消える|


### メニューを追加する

メニューを追加する処理の前に `layout.separator` 関数を呼ぶことで、上下のスペースを空けることができます。
ドロップダウンメニューでも `layout.separator` が使われていましたが、ドロップダウンの時の動作については、[2-1節](01_Basic_of_Add-on_Development.html) を参考にしてください。

本節のサンプルでは以下の処理により、メニューを追加しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="add_menu", unindent="True"]


[2-5節](05_Create_Sub-menu.html) で説明したサブメニューを追加するための関数 `layout.menu` により、メニューを追加します。
追加したメニューは、セレクトボックスのUIとなります。
表示されるメニュー名は、デフォルトで第1引数に指定したメニュークラスの `bl_label` が表示されますが、`text` 引数に表示したい文字列を指定することで変更することができます。


### プロパティを追加する

アドオンの機能実行時のパラメータなどを、ユーザ指定するためのプロパティを追加します。


#### プロパティを定義する

プロパティを追加するためには、プロパティの定義を行う必要があります。

プロパティの定義は、アドオン有効化時に `register` 関数から呼び出される `init_props` 関数で行います。
プロパティは、`bpy.types.Scene` に変数を追加することで定義できます。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="init_props", unindent="True"]


#### プロパティを削除する

アドオンを無効する時には、`bpy.types.Scene` に追加したプロパティのグループを削除する必要があります。
プロパティを削除せずにアドオンを無効すると、**プロパティのデータがメモリに残ったままとなり無駄にメモリを消費してしまう** ので、忘れずに削除するようにしましょう。

本節のサンプルでは、`unregister` 関数から呼び出される `clear_props` 関数により、定義したプロパティを削除しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="clear_props", unindent="True"]


#### プロパティを変更するためのUIを構築する

定義したプロパティをユーザが変更するためのUIを表示するためには、`layout.prop` 関数を使います。
`layout.prop` 関数の引数を以下に示します。

|引数|意味|
|---|---|
|第1引数|プロパティを持つオブジェクト|
|第2引数|プロパティ変数名|
|第3引数（`text`）|表示文字列|

本節のサンプルでは `bpy.types.Scene` にプロパティを登録したため、`context.scene` を第1引数に指定します。
第2引数には、`bpy.types.Scene` に登録したプロパティ変数名を文字列で指定します。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="add_prop", unindent="True"]


### ボタンを一行に並べる

`layout.operator` 関数を用いると、横幅が100%のボタンが配置されます。
このため、単純に `layout.operator` を複数回実行すると実行した回数分、縦方向にボタンが配置されてしまいます。

ボタンを横に並べるためには `layout.row` 関数を使って行成分を取得し、取得した行成分に対して `operator` 関数を使ってボタンを配置する必要があります。
本節のサンプルでは、以下のようにして3つのボタンを一行に並べています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="arrange_column", unindent="True"]


なお、`layout.row` 関数の引数に `align=False` を指定すると、ボタンとボタンの間に隙間が空くようにして配置されるようになります。
一方、以下のコードのように、`align=True` を指定すると、この隙間がなくなります。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="arrange_column_align", unindent="True"]


なお、`operator` の代わりに `label` 関数、`prop` 関数や `menu` 関数を使うことによって、ラベル、プロパティやメニューを一行に並べて配置することができます。


### ボタンを一列に並べる

`layout.operator` 関数を複数回実行することでボタンを一列に配置することができますが、隙間が広く気に入らない方もいると思います。
隙間を縮めた状態でボタンを縦に並べるためには、`layout.column` 関数を使って列成分を取得し、取得した列成分に対して `operator` 関数を使ってボタンを配置します。

本節のサンプルでは、以下のように3つのボタンを一列に並べています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="arrange_row", unindent="True"]


ボタン間の隙間を無くすために `align=True` を指定できる点は、`layout.row` 関数と同様です。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="arrange_row_align", unindent="True"]


なお、`operator` 関数の代わりに `label` 関数、`prop` 関数や `menu` 関数を使うことによって、ラベル、プロパティやメニューを一列に並べて配置することができます。


### ボタンを複数列に配置する

`layout.column` 関数や `layout.row` 関数で取得した行成分や列成分に対してさらに行成分や列成分を取得することで、より複雑なボタンの配置を実現することができます。

本節のサンプルでは、以下のようにして2行2列にボタンを配置しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="arrange_row_multi", unindent="True"]


### 領域を分割する

`layout.row` 関数を用いて行成分を取得することで一行にボタンを配置することができますが、ボタンはすべて等幅になっていました。
ボタンの横幅を変えたい時は、`layout.split` 関数を用いて領域を分割します。

`layout.split` 関数の引数 `percentage` に値を指定することで、領域の横幅を決めることができます。
引数 `percentage` の値は浮動小数点数で指定し、`1.0` で横幅100%、`0.0` で横幅0%となります。
例えば、ツール・シェルフの横幅に対して70%の横幅を持つ領域を分割する場合は、`layout.split(percentage=0.7)` とします。

本節のサンプルでは、以下のような処理で領域を3分割しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="divide_region", unindent="True"]


分割後の各領域では、縦並びにボタンを2つ表示しています。

`layout.split` 関数により分割した領域の変数 `split` に対して `split.split` 関数を実行することで、2つ以上の領域に分割することができます。
なお、`split.split` 関数に指定する引数 `percentage` について注意が必要です。
最初の領域分割で `layout.split` 関数を実行する時は、引数に指定した `percentage` がツール・シェルフの横幅に対する割合を示しますが、2回目の領域分割で `split.split` 関数を実行した時は、`layout.split` で分割した残りの領域、つまり本節のサンプルではツール・シェルフの横幅 70% の領域に対する割合を指定します。
同様に3回目の領域分割では、2回目に分割した残りの領域に対する割合を指定します。
従って、ツール・シェルフに対する横幅はそれぞれ、**領域1で 30%、領域2で 70% × 0.7 = 49% 、領域3で 70% × 0.3 = 21%** となります。


### ボタンの横幅を自動的に拡大する

`layout.operator` 関数を使ってボタンを配置すると、ボタンの横幅が自動的に領域全体へ拡大されますが、ボタンの横幅を明示的に領域全体に拡大する方法もあります。

本節のサンプルでは、以下のように `row.alignment` に `EXPAND` を設定し、明示的にボタンの横幅を自動的に拡大しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="align_expand", unindent="True"]


### ボタンを右寄せ・左寄せ配置にする

ボタンの横幅を自動的に拡大せず、右や左に寄せて配置することもできます。

本節のサンプルでは、以下のように `row.alignment` に `LEFT` を設定し、ボタンを左寄せ配置しています。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="align_left", unindent="True"]

また、`row.alignment` に `RIGHT` を設定することで右寄せ配置も可能です。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="align_right", unindent="True"]


### グループ化する

複数のUI部品をグループ化することもできます。
`layout.box` 関数の戻り値に対して `operator` 関数や `menu` 関数などを実行することで、作成したUIがグループ化されます。

本節のサンプルでは、以下のコードにより4つのボタンをグループ化しています。グループ内のUIは、通常のUIと同様のコードで構築することができます。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="group", unindent="True"]


### オプションの UI をカスタマイズする

[2-3節](../chapter_02/03_Use_Property_on_Tool_Shelf_1.html) で説明したツール・シェルフのオプションのUIもカスタマイズすることができます。

オプションのUIをカスタマイズするために本節のサンプルでは、オペレータクラス `ShowAllIcons` を作成しています。
`ShowAllIcons` クラスは、Pythonから利用できるすべてのアイコンをツール・シェルフのオプションに表示する処理を定義しています。

オプションのUIをカスタマイズする処理を以下に示します。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="customize_option_UI", unindent="True"]


オプションのUIの構築は、オペレータクラスの `draw` メソッドで行います。
メソッドで定義している処理は、メニュークラスやパネルクラスで定義する `draw` メソッドと同じように、`self.layout` を通して行います。

利用可能なアイコンの識別子一覧は、`bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items.keys` により取得できます。
取得したアイコンの識別子を、`row.label` 関数の引数 `icon` に指定することで、アイコンを表示することができます。
本節のサンプルでは、今後アドオンを作る人がアイコンを作る時の参考になるように、アイコンと識別子の対応関係がわかるようにしています。
このため、引数 `text` にアイコンの識別子を代入して表示しています。
また見やすさを考慮し、一行に表示可能なアイコンの数をオプションから指定することができます。ぜひ活用してください。

最後に、以下のコードにより、[利用可能なアイコンをすべて表示] ボタンを配置します。

[@include-source pattern="partial" filepath="chapter_02/sample_2_9.py" block="show_all_icons", unindent="True"]


# まとめ

本節では、ボタンやメニューなどのUI部品の配置方法について説明しました。

Blenderに限らず、UIはボタンやメニューなど数多くの部品により構成されるため、一度に多くのAPIが登場し混乱された方も多いと思います。
しかし、個々の部品を制御するためのソースコードは数行～数十行の規模で、それぞれのソースコードも似たようなパターンであるため、ここまで読み進めてきた方であれば理解できると思います。
またUIの制御に限っては、分量が多い代わりに常に知っておくべきことが少ないため、本節の内容をすべて理解するよりも、必要な時のみ本節を参照しても問題はありません。

本節で紹介したUI部品とUI部品を追加するためのAPIの対応関係を、次にまとめます。

|UI|API|
|---|---|
|間隔をあける|`layout.separator`|
|ラベル|`layout.label`|
|ボタン|`layout.operator`|
|メニュー（セレクトボックス）|`layout.menu`|
|プロパティ|`layout.prop`|
|行成分取得(アライメント無)|`layout.row` <br> `layout.row(align=False)`|
|行成分取得(アライメント有)|`layout.row(align=True)`|
|列成分取得(アライメント無)|`layout.column` <br> `layout.column(align=False)`|
|列成分取得(アライメント有)|`layout.column(align=True)`|
|UI部品の横幅を自動的に拡大|`row.alignment = 'EXPAND'`|
|UI部品を左寄せ|`row.alignment = 'LEFT'`|
|UI部品を右寄せ|`row.alignment = 'RIGHT'`|
|領域を分割|`layout.split`|
|グループ化|`layout.box`|


## ポイント

* Blenderが提供するUI部品は、メニュークラスやパネルクラス、オペレーションクラスが持つメンバ変数 `layout` を用いて配置することができる
* 本節のサンプルはアドオンから利用可能なアイコンの一覧を表示する機能を持つため、アドオン開発時に使いたいアイコンを調べたいときに活用できる
