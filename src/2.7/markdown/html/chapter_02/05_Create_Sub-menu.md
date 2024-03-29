---
pagetitle: 2-5. サブメニューを作成する
subtitle: 2-5. サブメニューを作成する
---

ここまで紹介したアドオンは1階層分のメニューを追加するだけでしたが、サブメニュー（マウスオーバーすると展開されるメニュー）を作成して2階層以上のメニューを作ることもできます。
例えば、[3Dビュー] エリアのメニュー [追加] > [メッシュ] は、追加の親メニューの下にメッシュという子メニューがある2階層のメニューとなっています。
本節では [2-4節](04_Use_Property_on_Tool_Shelf_2.html) のサンプルを改良し、複製するオブジェクトをメニューから選択できるようなメニューを構築することで、多階層のメニューを作成する方法を解説します。


# 作成するアドオンの仕様

* [2-4節](04_Use_Property_on_Tool_Shelf_2.html) で作成したサンプルを改良し、複製するオブジェクトをメニューから選択できるようにする


# アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして以下のソースコードを入力し、ファイル名を `sample_2_5.py` で保存してください。

[@include-source pattern="full" filepath="chapter_02/sample_2_5.py"]


# アドオンを使用する


## アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル2-5: アドオン「サンプル2-5」が有効化されました。
```

アドオンを有効化後、[3Dビュー] エリアのメニューである [オブジェクト] > [オブジェクトの複製] にサブメニューが追加されていることを確認します。
サブメニューには、[3Dビュー] エリアに存在するオブジェクト名が追加されています。

![](../../images/chapter_02/05_Create_Sub-menu/use_add-on.png "オブジェクトの複製1")


## アドオンの機能を使用する

<div class="work"></div>

|||
|---|---|
|1|[3Dビュー] エリアのメニューである [オブジェクト] > [オブジェクトの複製] から複製するオブジェクト名を選んで実行すると、選択したオブジェクトが複製されます。|
|2|[2-4節](04_Use_Property_on_Tool_Shelf_2.html) と同様、複製されたオブジェクトの拡大率・回転角度・配置先を [ツール・シェルフ] の [オプション] から変更することができます。<br>![](../../images/chapter_02/05_Create_Sub-menu/use_add-on_2.png "オブジェクトの複製2")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル2-5: アドオン「サンプル2-5」が無効化されました。
```


# ソースコードの解説

サブメニューを作成するコードを追加したことを除き、ソースコードの大部分は [2-4節](04_Use_Property_on_Tool_Shelf_2.html) からの流用です。
ここでは、新規で追加した部分について解説します。


## サブメニューの追加

サブメニューを追加するためには、`bpy.types.Menu` クラスを継承した **メニュークラスを作成する** 必要があります。

[@include-source pattern="partial" filepath="chapter_02/sample_2_5.py" block="menu_cls", unindent="True"]

オペレータクラスと同様、メニュークラスにはクラス変数 `bl_idname` , `bl_label` , `bl_description` を定義する必要がありますが、`bl_options` を指定する必要はありません。

メニュークラスでは、メニューの描画に必要な `draw` メソッドを実装する必要があります。
メニューが表示される度に `draw` メソッドが呼ばれ、以下の引数が渡されてきます。

|引数|型|値の説明|
|---|---|---|
|`self`|呼ばれた `draw` メソッドが定義されているメニュークラス|メニュークラスのインスタンス|
|`context`|`bpy.types.Context`|`draw` メソッドが呼ばれた時のコンテキスト|

オペレータクラスをメニューに登録した時と同様、サブメニューへの項目追加は `self.layout.operator` 関数で行うことができます。
本節のサンプルでは、[3Dビュー] エリア上の全てのオブジェクト名をメニュー項目に追加するため、`layout.operator` 関数の第1引数にオペレータクラスの `bl_idname` を指定し、引数 `text` にオブジェクト名を指定しています。

オペレータクラスは、複製するオブジェクトをオブジェクト名で判定するため、オペレータクラスのクラス変数 `src_obj_name` にオブジェクト名を代入します。
`src_obj_name` は `StringProperty` クラスの変数で定義します。

[@include-source pattern="partial" filepath="chapter_02/sample_2_5.py" block="string_prop", unindent="True"]

オペレータクラスの `execute` メソッドでは、クラス変数 `src_obj_name` に代入されたオブジェクト名を用いてオブジェクトを複製するように処理を変更しています。
本書については説明しませんが、ソースコードのコメントに処理内容を細かく記載しているため確認してください。

最後に、[3Dビュー] エリアのメニューである [オブジェクト] へ項目を追加します。

[@include-source pattern="partial" filepath="chapter_02/sample_2_5.py" block="build_menu", unindent="True"]

これまでオペレータクラスをメニューに追加する時は `self.layout.operator` 関数を利用していましたが、メニュークラスをメニューに追加する場合は `self.layout.menu` 関数を利用します。
`self.layout.menu` 関数にメニュークラスのクラス変数 `bl_idname` を引数として渡すことで、メニューをメニューの項目に追加することができます。


## 3階層以上のメニュー

サブメニューにさらにサブメニュー（サブサブメニュー）を追加するなど、3階層以上のメニューを作成することもできます。

以下のサンプルでは、先ほど作成したサンプルのメニューとサブメニューの間に新たなメニューとして、[オブジェクトの複製（サブメニュー）] を追加しています。

[@include-source pattern="full" filepath="chapter_02/sample_2_5_alt.py"]

アドオンを作成し有効化すると、図のように3階層のメニューが作成されていることが確認できます。

![](../../images/chapter_02/05_Create_Sub-menu/multilevel_menu.png "多階層メニュー")

サンプルのソースコードを見るとわかると思いますが、3階層のメニューは2階層のメニューを作成した時の応用であることがわかります。

[@include-source pattern="partial" filepath="chapter_02/sample_2_5_alt.py" block="sub_menu_cls", unindent="True"]

[@include-source pattern="partial" filepath="chapter_02/sample_2_5_alt.py" block="main_menu_cls", unindent="True"]

サブメニュー登録時に `self.layout.operator` 関数の代わりに `self.layout.menu` 関数を用い、サブメニュー用に作成したメニュークラスのクラス変数 `bl_idname` を指定します。
そしてサブメニュー用に作成したクラスの中で、オペレータクラスを登録することで、3階層のメニューを作成することができます。

同様の手順を踏むことで、4階層、5階層、・・・とメニューの階層を増やすことができます。


# まとめ

[2-4節](04_Use_Property_on_Tool_Shelf_2.html) で紹介したサンプルを改造し、複製するオブジェクトをメニューから選択できるようにしました。
また、サブメニューから複製するオブジェクトを選べるようにしました。

サブメニューを用いることで、本節のサンプルのように処理対象を選択できるようにしたり、メニュー項目を機能ごとに整理することができるようになります。
ぜひここでサブメニューの作り方を習得し、わかりやすいUI作りに活かしましょう。


## ポイント

* メニュークラスは、`bpy.types.Menu` クラスを継承して作成する
* メニュークラスの `draw` メソッド内でオペレータクラスのクラス変数 `bl_idname ` を `self.layout.operation` 関数の引数に指定し、メニュークラスのクラス変数 `bl_idname` を引数にして `self.layout.menu` 関数を呼び出すことで、サブメニューを作成できる
* メニュークラスの `draw` メソッド内でサブメニュー用に作成したクラスのクラス変数 `bl_idname` を `self.layout.menu` 関数の引数に指定することで、3階層以上のメニューを作成することができる
