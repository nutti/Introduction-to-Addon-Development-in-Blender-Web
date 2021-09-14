---
pagetitle: 3-1. マウスのイベントを扱う
subtitle: 3-1. マウスのイベントを扱う
---

Blenderには、*[オブジェクトモード]* 時に *[3Dビューポート]* スペース上で *[S]* キーを押すと、マウス移動でオブジェクトのサイズを変更する機能があります。
この機能は、オブジェクトのサイズをキーボードから入力して変更するのではなく、マウスの移動に応じて変更できるため、直感的で使いやすいと思いませんか？
このように、インタラクティブ性の高い機能をアドオンで提供するためには、マウスのイベントを扱う必要があります。


# 作成するアドオンの仕様

マウスのイベントを扱う方法を理解するため、本節で作成するサンプルアドオンは、次のようなマウスのイベント情報を利用した機能を持つものとします。

* *[3Dビューポート]* スペース上で、マウスを右クリックしながらマウスをドラッグしたとき、アクティブなオブジェクトを回転する
* 上記処理の開始または終了を切り替えるボタンを、Sidebarに配置する


# アドオンを作成する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして次に示すソースコードを入力し、ファイル名 `sample_3-1.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3-1.py"]


# アドオンを使用する


## アドオンを有効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに次のような文字列が出力されます。

```
サンプル 3-1: アドオン『サンプル 3-1』が有効化されました。
```

*[3Dビューポート]* スペース上で *[N]* キーを押してSidebarを表示し、*[サンプル 3-1]* パネルに *[オブジェクトを回転]* が追加されていることを確認します。

![](../../images/chapter_03/01_Handle_Mouse_Event/enable_add-on_1.png "サンプルアドオン3-1 有効化")


## アドオンの機能を使用する

有効化したサンプルアドオンの機能を使い、動作を確認します。
マウスカーソルの位置やクリックされたボタンなど、マウスからのイベント情報が使われていることを、確認してください。


<div class="work"></div>

|||
|---|---|
|1|*[3Dビューポート]* スペースのSidebarの *[サンプル 3-1]* > *[オブジェクトを回転]* に配置されている、*[開始]* ボタンをクリックします。<br>![](../../images/chapter_03/01_Handle_Mouse_Event/use_add-on_1.png "サンプルアドオン3-1 手順1")|
|2|*[右クリック]* した状態でマウスをドラッグすると、オブジェクトが回転します。<br>![](../../images/chapter_03/01_Handle_Mouse_Event/use_add-on_2.png "サンプルアドオン3-1 手順2")|
|3|*[3Dビューポート]* スペースのSidebarの *[サンプル 3-1]* > *[オブジェクトを回転]* に配置されている、*[終了]* ボタンをクリックして、処理を終了します。<br>![](../../images/chapter_03/01_Handle_Mouse_Event/use_add-on_3.png "サンプルアドオン3-1 手順3")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに次の文字列が出力されます。

```
サンプル 3-1: アドオン『サンプル 3-1』が無効化されました。
```


# ソースコードの解説

本節で紹介したアドオンのソースコードについて解説します。


## UIを作成する

[2-6節](../chapter_02/06_Divide_Add-on_Source_Code_Into_Multiple_Files.html) までに紹介したサンプルアドオンは、アドオンの機能を実行するためのUIをメニューに追加するのみでしたが、処理の開始と終了のような排他的な項目をメニューに両方追加するのは、UIとしてよいとは言えません。
そこで本節のサンプルアドオンでは、[2-7節](../chapter_02/07_Control_Blender_UI.html) で説明した方法を使って、*[3Dビューポート]* スペースのSidebarに、オペレータクラス `SAMPLE31_OT_RotateObjectByMouseDragging` の処理（オブジェクトの回転処理）を開始する、または終了するためのボタンを作成します。

パネルにボタンを追加するためには、`bpy.types.Panel` クラスを継承してパネルクラスを作成し、`draw` メソッド内でUIを定義します。

本節のサンプルアドオンでは、次に示すコードによりクラス変数を追加します。
パネルクラスの各クラス変数の意味は、[2-7節](../chapter_02/07_Control_Blender_UI.html) を参照してください。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="define_panel_class", unindent="True"]

続いて、UIの描画処理を定義する `draw` メソッドを作成します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="define_draw_method", unindent="True"]

`SAMPLE31_OT_RotateObjectByMouseDragging` クラスのクラスメソッド `is_running` により、オブジェクトの回転処理が実行中か否かを確認したうえで、表示するボタンを切り替えます。
`SAMPLE31_OT_RotateObjectByMouseDragging` クラスのクラスメソッド `is_running` が `False` の場合は、*[開始]* ボタンを表示します。
`is_running` が `True` の場合は、*[終了]* ボタンを表示します。


## オペレータクラスの作成

オペレータクラス `SAMPLE31_OT_RotateObjectByMouseDragging` を作成します。

作成するオペレータクラスは、これまでのサンプルアドオンのオペレータクラスに定義していた、`execute` メソッドが定義されていません。
その代わり、`modal` メソッドと `invoke` メソッドが定義されています。
また、オペレータクラス `SAMPLE31_OT_RotateObjectByMouseDragging` には、次に示す4つのクラス変数が定義されています。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="class_variable", unindent="True"]

これらのクラス変数は、`invoke` メソッドや `modal` メソッドで使用します。


### invokeメソッド

サンプルアドオンでは、ボタンを押したときに処理を開始または終了する処理を、`invoke` メソッドに記述します。
`invoke` メソッドの処理のポイントとなるのは、モーダルモードへの移行処理です。
**モーダルモード** とは、マウスやキーボードなどからイベントを受け取り続けるモードです。
モーダルモード時は、`modal` メソッドが `{'FINISHED'}` または `{'CANCELLED'}` を返すまで、`context.window_manager.modal_handler_add` 関数に指定したクラスの `modal` メソッドが継続して呼び出されます。

さて、サンプルアドオンの `invoke` メソッドに関する処理に話を戻します。
`invoke` メソッドでは、`SAMPLE31_OT_RotateObjectByMouseDragging` のクラスメソッド `is_running` が `True` の場合と `False` の場合とで、処理を変えます。

最初に、*[開始]* ボタンが押されたとき（`SAMPLE31_OT_RotateObjectByMouseDragging` のクラスメソッド `is_running` が `False` の状態でボタンが押されたとき）の処理について説明します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="press_start_button", unindent="True"]

最初に各クラス変数に初期値を設定し、`context.window_manager.modal_handler_add` 関数を実行してオペレータクラスを登録します。
サンプルアドオンでは、`invoke` メソッドと `modal` メソッドを同一のクラスで定義しているため、`context.window_manager.modal_handler_add` 関数の引数に自身のインスタンスである `self` を指定します。
オブジェクトの回転処理中は、`SAMPLE31_OT_RotateObjectByMouseDragging` のクラスメソッド `is_running` が `True` を返す必要があるため、クラス変数 `__running` を `True` に設定します。
最後に `{'RUNNING_MODAL'}` を返して、モーダルモードへ移行します。

次に、*[終了]* ボタンが押されたとき（`SAMPLE31_OT_RotateObjectByMouseDragging` のクラスメソッド `is_running` が `True` の状態でボタンが押されたとき）の処理について説明します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="press_stop_button", unindent="True"]

オブジェクトの回転処理中ではない場合は、クラス変数 `__running` の値が `False` に設定されていなければなりません。
このため、クラス変数 `__running` を `False` に設定し、`{'FINISHED'}` を返して処理を終えます。


### modalメソッド

モーダルモード中に呼ばれる `modal` メソッドの処理について説明します。
最初に `context.area.tag_redraw` メソッドを実行し、エリアを再描画します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="redraw_view3d", unindent="True"]

この処理が必要なのは、Blenderの画面更新処理が常に行われているわけではなく、視点変更などのイベントが発生したときにしか画面更新されないことへの対策です。
ここで明示的に画面を更新しない場合、`modal` メソッドの処理でオブジェクトに対して行った処理が直ちに反映されない、という現象が発生してしまいます。

`context.area` には、`modal` メソッドが実行されているエリア情報が保存されています。
サンプルアドオンでは、*[開始]* ボタンを押したときに呼ばれる `invoke` メソッドの処理の中でモーダルモードに移行するため、`context.area` には *[3Dビューポート]* スペースを持つエリア情報が保存されています。

続いて、オブジェクトの回転処理が終了している状態か否かを調べ、処理が終了していた場合はモーダルモードを終了します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="exit_modal_mode", unindent="True"]

`SAMPLE31_OT_RotateObjectByMouseDragging` のクラスメソッド `is_running` が `False` を返した場合は、オブジェクトの回転処理が終了したことになるため、`{'FINISHED'}` を返して `modal` メソッドを終了し、モーダルモードを終了します。

次に、`modal` メソッドの引数 `event` を用いて、マウスのクリックイベントを取得します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="update_click_status", unindent="True"]

`event.type` には、発生したイベントの種類が識別子として保存されています。
例えば、次のようにマウスやキーボードのイベントを取得できます。
なお、ここで示しているイベントの他にも、さまざまなイベントを取得できます。

|値|値の意味|
|---|---|
|`RIGHTMOUSE`|マウス 右ボタン|
|`LEFTMOUSE`|マウス 左ボタン|
|`MOUSEMOVE`|マウス 移動|
|`A`|キーボード Aキー|
|`B`|キーボード Bキー|

`event.value` には、イベントの種類に対する発生したイベントの値が保存されています。
例えば、次のような値が `event.value` に保存されています。

|値|値の意味|
|---|---|
|`PRESS`|ボタンやキーが押された|
|`RELEASE`|ボタンやキーが離された|

これを踏まえ、マウスの右ボタンが押されたときには、クラス変数 `__right_mouse_down` に `True` を設定します。
また、クラス変数 `__initial_rotation_x` と `__initial_mouse_x` には、それぞれアクティブなオブジェクトのX軸回転角度と、マウスのリージョン座標でのX座標を保存します。
一方、マウスの右ボタンが離されたときには、クラス変数 `__right_mouse_down` を `False` に設定します。

最後に、マウスのドラッグイベント発生時にオブジェクトが回転するようにします。
マウスの右ボタンが押されている状態で、ドラッグしたときにオブジェクトを回転させるため、`op_cls.__right_mouse_down` が `True` のときを考えます。
`event.mouse_region_x` には、リージョン座標におけるマウスのX座標の値が保存されているため、モーダルモード開始時のマウス座標値 `op_cls.__right_mouse_down` との差分から、回転角度を求めます。
そして、モーダルモード開始時のオブジェクトのX軸回転角度に対して、求めた回転角度を加算させることで、マウスのドラッグでオブジェクトを回転させることができます。

[@include-source pattern="partial" filepath="chapter_03/sample_3-1.py" block="update_object_rotation", unindent="True"]

サンプルアドオンにおいて `modal` メソッドは、`{'PASS_THROUGH'}` または `{'RUNNING_MODAL'}` を戻り値として返しています。
`{'PASS_THROUGH'}` を返すことで、イベントを本モーダル処理に閉じずに、別の処理に対してもイベントを通知しつつモーダルモードを継続できます。
一方、`{'RUNNING_MODAL'}` を返す場合は、モーダルモードは継続するものの、`modal` メソッド処理後にイベントが捨てられてしまうため、マウスやキーボードからのイベントに対して、他の処理へイベントが通知されません。

最後に、`is_running` クラスメソッドが `False` を返した場合、`modal` メソッドは `{'FINISHED'}` を返してモーダルモードを終了します。


# まとめ

本節では、マウスから発生したイベントを扱う方法を説明しました。
[2章](../chapter_02/index.html) で説明していない内容がたくさん出てきました。
特に `invoke` メソッドや `modal` メソッドは、メソッド内で処理が完結する `execute` メソッドとは動作が大きく異なります。
マウスのイベントを扱うために覚えることは多いですが、マウスのイベントを利用することで、インタラクティブ性の高い機能を実現できますので、ぜひ積極的に活用していきましょう。


## ポイント

*  `invoke` メソッドや `execute` メソッドで `{'RUNNING_MODAL'}` を返すとモーダルモードへ移行する
* モーダルモードは、イベント発生時に `modal` メソッドが呼ばれるモードであり、`{'FINISHED'}` または `{'CANCELLED'}` を返すまでモーダルモードは終了しない
* `modal` メソッドで `{'PASS_THROUGH'}` を返すことで、他の処理にもイベントを通知しつつ、モーダルモードを継続できる
* `modal` メソッドで `{'RUNNING_MODAL'}` を返すことで、他の処理にイベントを通知せず、モーダルモードを継続する
* `invoke` メソッドや `modal` メソッドの引数 `event` を参照することで、発生したイベントやイベント時の状態を取得できる
