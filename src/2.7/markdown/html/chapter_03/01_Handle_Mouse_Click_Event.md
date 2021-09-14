---
pagetitle: 3-1. マウスクリックのイベントを扱う
subtitle: 3-1. マウスクリックのイベントを扱う
---

Blenderには、オブジェクトモード時に3Dビューエリア上でSキーを押すと、マウス移動でオブジェクトのサイズを変更する機能があります。
この機能は、オブジェクトのサイズを手で入力して変更するのではなく、マウスの移動に応じて変更できるため、直感的で使いやすいと思いませんか？
このように、インタラクティブ性の高い機能をアドオンで提供するためには、マウスのイベントを扱う必要があります。


# 作成するアドオンの仕様

マウスのイベントを扱う方法を理解するため、本節で作成するアドオンは次のようなマウスのイベント情報を利用した機能を持つものとします。

* [編集モード] 時に、[3Dビュー] エリア上でマウスを右クリックしたときに、マウスカーソルの位置にあるオブジェクトの面を削除する
* プロパティパネル（[3Dビュー] エリア上で [N] キーを押した時に右側に表示されるパネル）から、上記処理の開始または終了を切り替えるボタンを配置する


# アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして以下のソースコードを入力し、ファイル名 `sample_3_1.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3_1.py"]


# アドオンを使用する


## アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに次のような文字列が出力されます。

```
サンプル3-1: アドオン「サンプル3-1」が有効化されました。
```

[3Dビュー] エリア上で [N] キーを押してプロパティパネルを表示し、項目 [マウスの右クリックで面を削除] が追加されていることを確認します。

![](../../images/chapter_03/01_Handle_Mouse_Click_Event/enable_add-on_1.png "マウスの右クリックで面を削除 有効化")


## アドオンの機能を使用する

有効化したアドオンの機能を使い、動作を確認します。
マウスカーソルの位置やマウスのクリックなど、マウスからのイベント情報が使われていることを、確認してください。


<div class="work"></div>

|||
|---|---|
|1|[3Dビュー] エリア上でモードを [編集モード] に変更し、選択方法を面選択に変更します。<br>![](../../images/chapter_03/01_Handle_Mouse_Click_Event/use_add-on_1.png "マウスの右クリックで面を削除 手順1")|
|2|[3Dビュー] エリアのプロパティパネルにある項目 [マウスの右クリックで面を削除] に配置されている、[開始] ボタンをクリックします。<br>![](../../images/chapter_03/01_Handle_Mouse_Click_Event/use_add-on_2.png "マウスの右クリックで面を削除 手順2")|
|3|選択中のオブジェクトの任意の面にマウスカーソルを当てて [右クリック] すると、マウスカーソルを当てている面が削除されます。<br>![](../../images/chapter_03/01_Handle_Mouse_Click_Event/use_add-on_3.png "マウスの右クリックで面を削除 手順3")|
|4|[3Dビュー] エリアのプロパティパネルの項目 [マウスのクリックで面を削除] 上に配置されている [終了] ボタンをクリックして、処理を終了します。終了時に削除した面の数がスクリプト実行ログに表示されます。<br>![](../../images/chapter_03/01_Handle_Mouse_Click_Event/use_add-on_4.png "マウスの右クリックで面を削除 手順4")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル3-1: アドオン「サンプル3-1」が無効化されました。
```


# ソースコードの解説

本節で紹介したアドオンのソースコードについて解説します。
サンプルのソースコードに関して、ポイントとなる点を次に示します。

* アドオンで共通利用するプロパティ定義のグループ化と、定義したプロパティの参照方法
* アドオンの機能を利用するためのUI作成
* `invoke` メソッドや `modal` メソッドに渡されてくるイベント情報の扱い方
* bmeshモジュールの扱い方


## アドオン内で利用するプロパティを定義する

本節のサンプルでは、オペレータクラス `DeleteFaceByRClick` と パネルクラス `OBJECT_PT_DFRC` が定義されており、これら2つのクラス間でデータを共有する必要があります。
本節のサンプルでは、アドオン内で共有するデータ全てを `bpy.types.PropertyGroup` クラスを継承したクラスのクラス変数として追加し、複数のクラス間でこれらのデータを共有します。

`bpy.types.PropertyGroup` クラスは、[2-3節](../chapter_02/03_Use_Property_on_Tool_Shelf_1.html) で紹介したプロパティクラスをグループ化するためのクラスです。
`bpy.types.PropertyGroup` クラスを継承し、グループ化したいプロパティクラスをクラス変数に追加して使用します。
なお、定義したプロパティの参照方法は後述します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="define_properties", unindent="True"]


本節のサンプルにおいてグループ化したプロパティの一覧を次に示します。

|プロパティ|意味|
|---|---|
|`running`|値が `True` の時にマウスを右クリックすると、マウスカーソルの位置にある面を削除する。|
|`right_mouse_down`|値が `True` の時は、マウスの右クリック中であることを示す。マウスを右クリックし続けた状態でマウスカーソルを移動した時に、他の面が削除できてしまう問題を解消するために使用する（後述）。|
|`deleted`|値が `True` の時は、右クリックにより面が削除された状態であることを示す。マウスを右クリックし続けた状態でマウスカーソルを移動した時に、他の面が削除できてしまう問題を解消するために使用する（後述）。|
|`deleted_count`|`running` の値が `True` から `False` に変更されるまでに削除された面の数。|


作成したプロパティグループ `DFRC_Properties` は、`register` 関数の処理内で `PointerProperty` クラスを利用して登録します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="register_properties", unindent="True"]


アドオン有効時に、`PointerProperty` の引数 `type` にプロパティをグループ化したクラス `DFRC_Properties` を指定してインスタンスを生成し、`bpy.types.Scene.dfrc_props` 変数に代入します。
以降、各プロパティには `bpy.types.Scene` を通してアクセスすることができます。
例えば、プロパティ `running` にアクセスする場合は、`bpy.types.Scene.dfrc_props.running` とすることでアクセスすることができます。

アドオン無効時には、次のコードにより、追加したプロパティのグループを削除します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="unregister_properties", unindent="True"]


<div class="column">
本節のサンプルでは、`bpy.types.PropertyGroup` を使ってクラス間で共有するプロパティを定義しました。
ここで、[2-9節](../chapter_02/09_Control_Blender_UI_2.html) で説明したツール・シェルフへのプロパティ追加時にも、`bpy.types.PropertyGroup` を使えるのではないかと思うかもしれません。
しかし、`layout.prop` に指定するのが「プロパティ変数名の文字列」であることから、プロパティをグループ化すると正しく動作しません。
このため、プロパティをツール・シェルフやプロパティパネルに追加する場合は、`bpy.types.PropertyGroup` でグループ化せず、個別にプロパティを宣言する必要があります。
一方、プロパティをツール・シェルフやプロパティパネルに追加しない場合は、`bpy.types.PropertyGroup` を使ってプロパティをグループ化してもよいです。
</div>


## UIを作成する

[2-7節](../chapter_02/07_Divide_Add-on_Source_into_Multiple_Files.html) までに紹介したサンプルは、アドオンの機能を実行するためのUIをメニューに追加するのみでしたが、処理の開始と終了のような排他的な項目をメニューに両方追加するのはUIとしてよいとは言えません。
そこで本節のサンプルでは、[2-9節](../chapter_02/09_Control_Blender_UI_2.html) で説明した方法を使って、[3Dビュー] エリアのプロパティパネルにオペレータクラス `DeleteFaceByRClick` の処理を開始または終了を切りかえるためのボタンを作成します。

プロパティパネルにボタンを追加するためには、[2-8節](../chapter_02/08_Control_Blender_UI_1.html) で説明したツールシェルフのタブに追加した方法と同様に `bpy.types.Panel` クラスを継承してパネルクラスを作成し、`draw` メソッド内でUIを定義します。

本節のサンプルでは、次に示すコードでクラス変数を追加します。
パネルクラスの各クラス変数の意味は、[2-8節](../chapter_02/08_Control_Blender_UI_1.html) を参照してください。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="define_panel_class", unindent="True"]


続いて、UIの構築処理を定義する `draw` メソッドを作成します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="define_draw_method", unindent="True"]


`draw` メソッドに渡されてくる引数 `context` には、`draw` メソッドが呼ばれた時のコンテキスト情報が含まれています。
そして、`context.scene` は `bpy.types.Scene` と同じものです。
このため `register` 関数内からは、`context.scene.dfrc_props` を利用することで `bpy.types.Scene.dfrc_props` に登録したアドオン内のプロパティグループ `DFRC_Properties` を参照することができます。

そして、`DFRC_Properties` クラスのクラス変数 `context.scene.dfrc_props.running` により、面の削除処理が実行中か否かを確認した上で、`DeleteFaceByRClick` の処理開始と処理終了のボタンを切り替えます。
`DFRC_Properties` クラスのクラス変数 `running` が `False` の場合は、削除処理が開始されていないため、[開始] ボタンを表示します。
`running` が `True` の時は、削除処理がすでに開始されている状態であるため、[終了] ボタンを表示します。


## オペレータクラスの作成

最後に、オペレータクラス `DeleteFaceByRClick` を作成します。

本節のアドオンのオペレータクラスは、これまでのサンプルで作成したオペレータクラスに毎回定義していた `execute` メソッドが定義されていません。
その代わり、`modal` メソッドと `invoke` メソッドを定義します。
それぞれのメソッドについて説明します。


### invokeメソッド

本節のサンプルでは、ボタンが押した時に処理を開始または終了する処理を `invoke` メソッドに記述します。
本節のサンプルにおける `invoke` メソッドの処理でポイントとなるのは、モーダルモードへの移行処理です。
モーダルモードとは、マウスやキーボードなどからイベントを受け取り続けるモードです。
モーダルモード時は、`modal` メソッドが `{'FINISHED'}` または `{'CANCELLED'}` を返すまで、`context.window_manager.modal_handler_add` 関数に指定したクラスの  `modal` メソッドが継続して呼び出されます。

さて、本節の `invoke` メソッドに関する処理について説明します。

プロパティグループ `DFRC_Properties` を `invoke` メソッドの引数 `context` から取得する方法は、UIの作成で説明した方法と同様、`context.scene.dfrc_props` で取得することができます。
ここで取得したプロパティグループ `DFRC_Properties` のクラス変数 `running` が `True` の場合と `False` の場合とで、処理を変えます。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="press_start_button", unindent="True"]


最初に、[開始] ボタンが押されたとき（`props.running` の値が `False` の状態でボタンが押されたとき）の処理について説明します。

面の削除処理中は、変数 `props.running` の値が `True` に設定されていなければならないため、変数 `props.running` を `True` に設定した後、`DFRC_Properties` の各クラス変数を初期値に設定します。
そして、`context.window_manager.modal_handler_add` 関数を実行してオペレータクラスを登録し、`{'RUNNING_MODAL'}` を返してモーダルモードへ移行します。

本節のアドオンでは、`invoke` メソッドと `modal` メソッドを同一のクラスで定義しているため、`context.window_manager.modal_handler_add` 関数の引数に自身のインスタンスである `self` を指定します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="press_stop_button", unindent="True"]


次に、[終了] ボタンが押されたとき（`props.running` の値が `True` の状態でボタンが押されたとき）の処理について説明します。

面の削除処理中でない場合は、変数 `props.running` の値が `False` に設定されていなければなりません。
このため、変数 `props.running` を `False` に設定します。そして、面の削除処理中に削除した面の数を出力します。

最後に `invoke` メソッドは、 `{'FINISHED'}` を返して処理を完了します。


### modalメソッド

続いて、モーダルモード中に呼ばれる `modal` メソッドの処理について説明します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="redraw_view3d", unindent="True"]


最初に `context.area.tag_redraw` 関数を実行し、[3Dビュー] エリアの画面を更新します。
これは、Blenderの画面更新処理が常に行われているわけではなく、視点変更などの特定のイベント時にしか行われないことへの対策です。
もしこの画面更新処理を行わない場合、`modal` 処理でオブジェクトに対して行った処理が直ちに反映されない、という現象が発生してしまいます。

`context.area` には `modal` メソッドが実行されているエリア情報が保存されています。
本節のサンプルでは、[開始] ボタンを押した時に呼ばれる `invoke` メソッドの処理の中でモーダルモードに移行するため、`context.area` には [3Dビュー] エリアのエリア情報が保存されています。
このため、`context.area.tag_redraw` 関数を実行することで、[3Dビュー] エリアを更新することができます。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="exit_modal_mode", unindent="True"]


続いて面の削除処理が終了している状態であるか否かを調べ、削除処理が終了していた場合はモーダルモードを終了します。サンプルでは、`props.running` が `False` である場合は面の削除処理が終了したことになるため、`{'FINISHED'}` を返して `modal` メソッドを終了し、モーダルモードを終了します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="update_click_status", unindent="True"]


次に、`modal` メソッドの引数 `event` を用いて、マウスのクリックイベントを取得します。
`event.type` には発生したイベントの種類が識別子として保存されており、例えば、次のようにマウスやキーボードのイベントを取得することができます（他にもさまざまなイベントを取得することができます）。

|値|値の意味|
|---|---|
|`RIGHTMOUSE`|マウス右ボタン|
|`LEFTMOUSE`|マウス左ボタン|
|`A`|キーボードAキー|
|`B`|キーボードBキー|

`event.value` には、イベントの種類に対する発生したイベントの値が保存されています。例えば次のような値が `event.value` に設定されます。

|値|値の意味|
|---|---|
|`PRESS`|ボタンやキーが押された|
|`RELEASE`|ボタンやキーが離された|

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="delete_face", unindent="True"]


右クリックされ、面を削除できると判断する処理について、説明します。

面を削除できるか否かは、`if props.right_mouse_down is True and props.deleted is False` によって判断しています。
この処理には少し工夫しているので、詳しく説明します。

マウスが右クリックされたことを検出するためには、一見すると `event.type` が `'RIGHTMOUSE'` 、`event.value` が `'PRESS'` であることを判定するだけで問題ないように思えます。
しかし仮にこの方法でクリックを検出する場合、右クリックされている状態でマウスカーソルを動かすと、面を削除できてしまいます。
これは、本来期待する動作（右クリックを行った直後の1回だけ面を削除）とは異なります。
そこで、マウスを右クリックした後に1回でも面を削除した場合に `Ture` が設定される変数、`props.deleted` が `True` である場合は、削除処理を行わないようにします。
なお `props.right_mouse_down` は、便宜的に右クリックしたことを示すための変数です。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="clear_restrict_status", unindent="True"]


ちなみに、`props.deleted` が `True` の間は面を削除することができないため、`props.right_mouse_down` が `False` に変わった時に `props.deleted` を `False` に戻すことで、再度右クリックされた時に面を削除できるような処理があることに注意してください。

続いて面を削除する処理について説明します。
面を削除するためには、削除対象の面が属するメッシュデータにアクセスする必要があります。

メッシュデータにアクセスするためには、`bpy.data.meshes` からアクセスする方法と `bmesh` モジュールを用いる方法があります。
本節のサンプルでは、`bmesh` モジュールを用いて面の削除処理を実装しています。

`bmesh` は比較的最近（バージョン2.63より）導入されたモジュールで、メッシュデータを簡単に扱う関数が数多く提供されています。
最近作成されているアドオンでは、`bmesh` を使ってメッシュデータにアクセスしている場合がほとんどですので、基本的に `bmesh` を使ってメッシュデータを扱うようにしましょう。
`bmesh` を利用するためには、次のように `bmesh` モジュールをインポートする必要があります。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="import_bmesh", unindent="True"]


インポートした `bmesh` モジュールを使って面を削除する処理について説明します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="build_bmesh", unindent="True"]


メッシュデータにアクセスするためには、`bmesh` 用のメッシュデータを構築する必要があります。
`bmesh` 用のメッシュデータを構築するためには、編集中のオブジェクトデータ `context.edit_object.data` を `bmesh.from_edit_mesh` 関数の引数に渡す必要があります。
ここで、`context.edit_object` は編集中のオブジェクト情報を持つ変数で、`data` 変数によりオブジェクトのデータを取得することができます。
勘のよい方であれば気がつかれたかと思いますが、`bmesh` 用のメッシュデータを構築するためには [エディットモード] である必要があります。
仮に、[オブジェクトモード] で `bmesh` を構築しようとすると、エラーが発生して構築することができないことに注意が必要です。

次に、クリックされた面を削除する処理について説明します。
クリックされた面を削除するためには、次のような3段階の処理を行う必要があります。

1. クリック時にマウスカーソルの位置にある面を選択
2. 選択された面を取得
3. 面を削除


#### 1. クリック時にマウスカーソルの位置にある面を選択

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="select_clicked_face", unindent="True"]


クリック時のマウスカーソルの位置は、`modal` メソッドの引数 `event` から取得できます。
サンプルでは、クリック時のマウスカーソルの [ウィンドウ] リージョンのリージョン座標が必要であるため、`event` のメンバ変数 `event.mouse_region_x` （X座標）と `event.mouse_region_y` （Y座標）から取得しています。
取得した座標は変数 `loc` に保存します。

次に面を選択するために `bpy.ops.view3d.select` 関数を呼び出します。
`bpy.ops.view3d.select` 関数の引数 `location` にマウスクリック時のウインドウリージョン座標 `loc` を指定することで、マウスカーソルの位置にある面を選択することができます。
もしマウスカーソルの位置に面が1つもなければ、`bpy.ops.view3d.select` 関数は `{'PASS_THROUGH'}` を返します。
このため、`bpy.ops.view3d.select` 関数の戻り値 `ret` が `{'PASS_THROUGH'}` である場合は、マウスカーソルの位置に面がないことをコンソールウィンドウ出力したあとに処理を終了します。


#### 2. 選択された面を取得

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="get_selected_face", unindent="True"]


選択された面を取得するために、`bmesh` の履歴情報を利用します。
`bmesh` には面・辺・頂点の選択履歴が保存されており、選択履歴の最後の要素を確認することで1で選択した面を取得することができます。
頂点・辺・面の選択履歴は `bm.select_history` に保存されていますが、頂点・辺・面の全ての選択履歴が混ざった状態で保存されていることに注意が必要です。
例えば、面を選択した後に辺を選択した場合、「面選択」→「辺選択」の順に選択履歴が保存されています。

1の処理の直後であるため、選択履歴の最後の要素が面であることは保証されていますが、念のために最後の選択履歴が面であるか否かを確認しています。
確認の結果、選択履歴の最後の要素が面でなければ `{'PASS_THROUGH'}` を返して処理を終了します。


#### 3. 面を削除

クリック時にマウスの位置にある面を取得できたところで、いよいよ面を削除します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="delete_selected_face", unindent="True"]


面は `bmesh.ops.delete` 関数で削除することができ、以下に示す引数を指定します。

|引数|値の意味|
|---|---|
|第1引数|`bmesh` 用のメッシュデータ|
|`geom`|削除するデータ|
|`context`|削除するデータの種類|

第1引数には `bmesh` 用のメッシュデータである `bm` 、引数 `geom` には2で取得した面のデータ、`context` に面データであることを示す `5` を指定しています。
`context` に数値を入力するのは少し違和感がありますが、今のところ数値を指定するしかないようです。
`context` に指定する値と値を指定した時の効果を調べてみましたので、参考にしてみてください。
数値ではわかりづらいので、いつか数値ではなく文字列で指定できるようになることを期待したいです。

|値|効果|
|---|---|
|`1`|頂点を削除する|
|`2`|辺を削除する（辺を構成する頂点も削除する）|
|`3`|面を削除する（面を構成する頂点や辺は削除しない）|
|`4`|辺を削除する（辺を構成する頂点は削除しない）|
|`5`|面を削除する（面を構成する頂点や辺も削除する）|
|`6`|`geom` に面を指定した時は値に `3` を入力した時と同じ効果<br>辺を指定した時は値に `4` を入力した時と同じ効果<br>頂点を指定した時は値に `1` を入力した時と同じ効果|


<div class="column">
Blender本体のソースコードを参照することで、contextに指定する値を調べることができます。
対象となるソースコードは `source/blender/bmesh/intern/bmesh_operator_api.h` で、`enum` として値が定義されています。
頂点の削除であれば、`DEL_VERTS = 1` と書かれています。
いずれにせよ、値を直に入力する方法は移植性が低いので、文字列などで入力できるようになることを期待します。
</div>

ここまでの処理で面を削除することができました。
しかし、ここで `modal` メソッドの処理を終了してしまうと、面の削除がメッシュに反映されないことに注意が必要です。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="update_bmesh", unindent="True"]


面を削除したことをメッシュに反映させるためには、`bmesh.update_edit_mesh` 関数を実行して面の削除をメッシュに反映する必要があります。
面の削除に限らず、`bmesh` 用のメッシュデータを更新した場合は必ず `bmesh.update_edit_mesh` 関数を実行して更新内容を反映するようにしましょう。

面の削除処理の説明はこれで終わりです。

[@include-source pattern="partial" filepath="chapter_03/sample_3_1.py" block="post_process", unindent="True"]


最後に、削除した面数をカウントアップします。
そして、変数 `props.deleted` を `True` に変更し、マウスが右クリックされた状態で連続して面が削除されないようにします。

そして `modal` メソッドは `{'PASS_THROUGH'}` を返します。
`{'PASS_THROUGH'}` を返すことで、イベントを本モーダル処理に閉じず、別の処理に対しても通知しながら `modal` メソッドの処理を続けることができます。
イベントを受け取り続けるのであれば `{'RUNNING_MODAL'}` でも問題なさそうですが、`{'RUNNING_MODAL'}` を返すと `modal` メソッド処理後にイベントが捨てられてしまい、マウスやキーボードからのイベントに対する他の処理が発生しなくなってしまいます。

`{'PASS_THROUGH'}` と `{'RUNNING_MODAL'}` を理解するために、`modal` メソッドの `return {'PASS_THROUGH'}` を `return {'RUNNING_MODAL'}` に変更してみましょう。
プロパティパネルから面の削除処理を実行した後にボタンを押すことができなくなり、処理を終えることができなくなります。
これにより、`modal` メソッドが `'RUNNING_MODAL'` を返した時は、`DeleteFaceByRClick` の `modal` メソッドでイベントが捨てられ、他の処理へイベントが通知されていないことがわかります。


# まとめ

本節では、マウスから発生したイベントを扱う方法を説明しました。
[2章](../chapter_02/index.html) で説明していない内容がたくさん出てきました。
特に `invoke` メソッドや `modal` メソッドは、メソッド内で処理が完結する `execute` メソッドとは動作が大きく異なるため、理解するまでに時間がかかるかと思います。
説明を聞いただけではわからないことも多いかと思いますので、何度か使ってみて実際に動作を確認してみてください。

マウスのイベントを扱うために覚えることは多いですが、マウスのイベントを利用することでインタラクティブ性の高い機能を実現することができますので、ぜひ積極的に活用していきましょう。


## ポイント


* `bpy.types.PropertyGroup` クラスを継承したクラスのクラス変数にプロパティクラスを指定することで、プロパティをグループ化することができる
* プロパティパネルへメニューを追加するためには、`bpy.types.Panel` クラスを継承し、`draw` メソッド内でUIを定義する必要がある
*  `invoke` メソッドや `execute` メソッドで `{'RUNNING_MODAL'}` を返すとモーダルモードへ移行し、登録されたオペレータクラスの `modal` メソッドが実行される
* モーダルモードは、`{'FINISHED'}` または `{'CANCELLED'}` を返すまで処理を終えずに、イベントを受け取り続けるモードである
* `modal` メソッドで `{'PASS_THROUGH'}` を返すことで、他の処理にもイベントを通知しつつモーダルモードを継続できる
* `modal` メソッドで `{'RUNNING_MODAL'}` を返すと、他の処理にイベントを通知せずにモーダルモードを継続する
* `invoke` メソッドや `modal` メソッドの引数 `event` を参照することで、発生したイベントやイベント時の状態を取得できる
* `bmesh` モジュールには、メッシュデータを簡単に扱うための関数が多数用意されている
