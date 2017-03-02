<div id="sect_title_img_3_1"></div>

<div id="sect_title_text"></div>

# マウスクリックのイベントを扱う

<div id="preface"></div>

###### 3DビューエリアのオブジェクトモードでSキーを押した時に、マウスの移動でオブジェクトのサイズを変更する機能があります。このように、アドオンでよりインタラクティブ性の高い機能を提供するために、マウスやキーボードからのイベントを扱いたくなる時が来るかもしれません。本節ではアドオンからマウスのイベントを扱う方法を、サンプル交えて紹介します。

## 作成するアドオンの仕様

* 3Dビューエリアの編集モード時に、マウスで右クリックしたオブジェクトの面を削除する
* プロパティパネル（3Dビューエリア上でNキーを押した時に右側に表示されるパネル）から、上記処理の開始/終了を切り替えるボタンを配置する

## アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考にして、以下のソースコードをテキスト・エディタに入力し、ファイル名 ```sample_3-1.py``` として保存してください。

[import](../../sample/src/chapter_03/sample_3-1.py)

## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に、作成したアドオンを有効化するとコンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル3-1: アドオン「サンプル3-1」が有効化されました。
```

<div id="sidebyside"></div>

|アドオンを有効化します。<br>右図のように、3Dビューエリア上でNキーを押してプロパティパネルを表示し、 新たな項目としてマウスの右クリックで面を削除が作成されていることを確認します。|![マウスの右クリックで面を削除 手順1](https://dl.dropboxusercontent.com/s/6pyxmbf4mak9o8j/use_add-on_1.png "マウスの右クリックで面を削除 手順1")|
|---|---|


### アドオンの機能を使用する

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|3Dビューエリア上で編集モードに変更し、選択方法を面選択にします。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|3Dビューエリアのプロパティパネルから、マウスの右クリックで面を削除の開始ボタンをクリックします。|![マウスの右クリックで面を削除 手順2](https://dl.dropboxusercontent.com/s/ltuh1pmujq0hbrf/use_add-on_2.png "マウスの右クリックで面を削除 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|適当な面にマウスカーソルを当てて右クリックすると、マウスカーソルを当てた面が削除されます。|![マウスの右クリックで面を削除 手順3](https://dl.dropboxusercontent.com/s/1ntqeqbtx5ni0ym/use_add-on_3.png "マウスの右クリックで面を削除 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|3Dビューエリアのプロパティパネル上のマウスのクリックで面を削除の終了ボタンをクリックして、処理を終了します。<br>終了時に削除した面の数がスクリプト実行ログに表示されます。|![マウスの右クリックで面を削除 手順4](https://dl.dropboxusercontent.com/s/vz6982lhm4ofsyp/use_add-on_4.png "マウスの右クリックで面を削除 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル3-1: アドオン「サンプル3-1」が無効化されました。
```

## ソースコードの解説

### アドオン内で利用するプロパティ定義

本節のサンプルでは複数のクラス間でデータを共有する必要があります。アドオン内で共有するデータを ```bpy.types.PropertyGroup``` クラスを用いて定義することで、複数のクラス間でデータを共有します。

```bpy.types.PropertyGroup``` クラスは、 [2-3節](../chapter_02/03_Use_Property_on_Tool_Shelf_1.md) で紹介したプロパティクラスをグループ化するためのクラスです。　```bpy.types.PropertyGroup``` クラスを継承し、グループ化したいプロパティクラスをクラス変数に追加して使用します。

[import:"define_properties", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

本節のサンプルにおいてグループ化したプロパティ一覧を以下に示します。

|プロパティ|意味|
|---|---|
|```running```|```True``` の時は、面を右クリックすることで削除する|
|```right_mouse_down```|```True``` の時は、右クリック中であることを示す|
|```deleted```|```True``` の時は、 右クリックにより削除された状態であることを示す。右クリックし続けた状態でマウスを動かし、複数の面が削除されないようにするために必要|
|```deleted_count```|```running``` が ```True``` から ```False``` になるまでに削除された面の数|

作成したグループは、```register()``` 関数の処理内で ```PointerProperty``` クラスを利用して登録します。

[import:"register_properties", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

アドオン有効時に ```PointerProperty``` の引数 ```type``` へグループ化のために定義したクラス名を指定することで、```bpy.types.Scene.dfrc_props``` 変数にプロパティのグループを登録します。以降、各プロパティには ```bpy.types.Scene.dfrc_props.running``` 等でアクセスすることができます。

アドオン無効時には、```bpy.types.Scene``` に追加したプロパティのグループを削除しています。

[import:"unregister_properties", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)


### UIを作成する

アドオン機能の処理を開始/終了するためのUIを作成します。

メニューに追加するだけで問題なかった今までのサンプルとは異なり、本節のサンプルのように処理の開始と終了という排他的な項目をメニューに両方追加するのはUIとして良いとは言えません。そこで本節のサンプルでは、3Dビューエリアのプロパティパネルに開始/終了を切り替えるためのボタンを作成します。

プロパティパネルにボタンを追加するためには、 [2-8節](../chapter_02/08_Control_Blender_UI_1.md) で説明したツールシェルフのタブに追加した時と同様、 ```bpy.types.Panel``` クラスを継承してパネルクラスを作成し、 ```draw()``` メソッド内でUIを定義します。

パネルクラスのクラス変数については、[2-8節](../chapter_02/08_Control_Blender_UI_1.md) を参照してください。

[import:"define_panel_class", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

続いて、 ```draw()``` メソッドを定義します。

[import:"define_draw_method", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)


```draw()``` メソッドに渡されてくる引数 ```context``` には、 ```draw()``` メソッドが呼ばれた時のコンテキスト情報が含まれています。

```context.scene.dfrc_props``` から、 ```register()``` 関数内で登録したアドオン内のプロパティグループ ```DFRC_Properties``` を取得できます。

```DFRC_Properties``` クラスのクラス変数 ```running``` が ```False``` の時は、削除処理が開始されていないため、開始ボタンを表示します。```running``` が ```True``` の時は、削除処理がすでに開始されている状態であるため、終了ボタンを表示します。


### オペレータクラスの作成

最後に、 *オペレータクラス* を作成します。

本節のアドオンでは、これまで紹介したサンプル内のオペレータクラスで毎回定義した ```execute()``` メソッドが定義されていません。その代わり、```modal()``` メソッドと ```invoke()``` メソッドが定義されています。

#### invoke()メソッド

本節のサンプルでは、ボタンが押した時に処理を開始/終了する処理を ```invoke()``` メソッドに記述します。

プロパティグループ ```DFRC_Properties``` の取得方法は、UIの作成時に説明した方法と同じで、 ```context.scene.dfrc_props``` で取得できます。

[import:"press_start_button", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

アドオンの機能実行開始時の処理は変数 ```props.running``` が ```False``` の時に行い、変数 ```props.running``` を ```True``` に設定した後、 ```DFRC_Properties``` の各クラス変数を初期値に設定します。最後に ```context.window_manager.modal_handler_add()``` 関数を実行してモーダルクラスを登録し、 ```{'RUNNING_MODAL'}``` を返してモーダルモードへ移行します。

モーダルモードとは、 ```{'FINISHED'}``` または ```{'CANCELLED'}``` を返すまで、処理を終えずにマウスやキーボードなどからイベントを受け取り続けるモードを指します。

本節のアドオンでは、 ```invoke()``` メソッドと ```modal()``` メソッドを同一のクラスで定義しているため、 ```context.window_manager.modal_handler_add()``` 関数の引数に ```self``` を指定します。

[import:"press_stop_button", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

アドオンの機能実行終了時の処理は変数 ```props.running``` が ```True``` の時に行い、変数 ```props.running``` を ```False``` に設定後、モーダルモード中に削除した面の数を出力します。

その後 ```{'FINISHED'}``` を返します。

<div id="space_l"></div>


#### modal()メソッド

続いて、 *モーダルモード* 中に呼ばれる ```modal()``` メソッドについて説明します。

最初に ```context.area.tag_redraw()``` 関数を実行し、3Dビューエリアを更新します。

[import:"redraw_view3d", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

次に変数 ```props.running``` を確認し、アドオンの機能開始時の処理が開始されていない場合は ```{'FINISHED'}``` を返して ```modal()``` メソッドを終了します。

[import:"update_click_status", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

次に、```modal()``` メソッドの引数 ```event``` を用いて、マウスのクリックやキーボードが押された状態を取得します。```event.type``` には発生した様々なイベントの種類が保存されていて、例えば以下のようなイベントの種類があります。

|値|値の意味|
|---|---|
|```RIGHTMOUSE```|マウス右ボタン|
|```LEFTMOUSE```|マウス左ボタン|
|```A```|キーボードAキー|
|```B```|キーボードBキー|

```event.value``` はイベントの種類に対する、イベントの値を示しています。例えば以下の値が ```event.value``` に設定されます。

|値|値の意味|
|---|---|
|```PRESS```|ボタンやキーが押された|
|```RELEASE```|ボタンやキーが離された|

右クリックされた時の処理を実装します。削除処理の前に、 ```if props.right_mouse_down is True and props.deleted is False``` により、削除処理を行うか否かを確認しています。この確認処理には少し工夫を加えています。

[import:"delete_face", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)


右クリックをされたことを検出するためには、 ```props.right_mouse_down``` が ```True``` であることの判定だけで問題ないように思えます。しかし、右クリックが押されたいる間は ```props.right_mouse_down``` が常に ```True``` になるため、クリック中にマウスを移動させると面を削除できてしまいます。これは、本来期待する動作(右クリックを行った直後の1回だけ面を削除)とは少し異なります。そこで変数 ```props.deleted``` が ```True``` であることを確認し、すでに面を一度削除した状態であれば、削除処理を行わないようにします。そして ```props.right_mouse_down``` が ```False``` に変わった時に ```props.deleted``` を ```False``` に戻すことで、次に右クリックが行われた時に面を削除できるようにします。

[import:"clear_restrict_status", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)


続いて面を削除の処理の説明をします。

面を削除するためには、削除対象のメッシュデータにアクセスする必要があります。

メッシュデータにアクセスするためには、```bpy.data.meshes``` からアクセスする方法と ```bmesh``` モジュールを用いる方法があります。今回のサンプルでは、 ```bmesh``` モジュールを用いて面の削除処理を実装しています。

```bmesh``` は比較的最近（バージョン2.63より）導入されたモジュールで、メッシュデータを簡単に扱う関数が多く提供されています。

```bmesh``` を利用するためには、以下のように ```bmesh``` モジュールをインポートする必要があります。

[import:"import_bmesh", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

面の削除処理本体を説明します。

最初にメッシュデータにアクセスするため、 ```bmesh``` 用のメッシュデータを構築します。編集中のオブジェクトデータ ```context.edit_object.data``` を ```bmesh.from_edit_mesh()``` 関数の引数に渡すことで、 ```bmesh``` 用のメッシュデータを構築できます。

[import:"build_bmesh", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

次に、クリックされた面を削除する処理について説明します。

クリックされた面の削除処理の流れを以下に示します。

<div id="custom_ol"></div>

1. クリック時にマウスの位置にある面を選択
2. 選択された面を取得
3. 面を削除

最初に1のクリック時のマウス位置にある面選択ですが、 ```event``` 変数からマウスの位置情報を取得します。

```bpy.ops.view3d.select()``` 関数の引数 ```location``` にマウスの位置を指定することで、マウスの位置にある面を選択することができます。もしマウスの位置に面がなければ ```bpy.ops.view3d.select()``` 関数は ```{'PASS_THROUGH'}``` を返すため、マウスの位置に面がないことを出力した後に処理を終了します。

[import:"select_clicked_face", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

続いて2の選択された面を取得する手順について説明します。

選択された面は、 ```bmesh``` の履歴情報のうち最後に選択された面として取得できます。頂点・辺・面の選択履歴 ```bm.select_history``` の最後の要素が面であるか否かを確認し、面であれば処理を継続します。面でなければ ```{'PASS_THROUGH'}``` を返して処理を終了します。

[import:"get_selected_face", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

最後に選択した面を削除します。

面の削除は ```bmesh.ops.delete()``` 関数で行い、以下に示す引数を指定します。

|引数|値の意味|
|---|---|
|第1引数|```bmesh``` 用のメッシュデータ|
|```geom```|削除するデータ|
|```context```|削除するデータの種類|

今回は面を削除するため、 ```context``` に ```5``` を指定しています。

[import:"delete_selected_face", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

面を削除したことをメッシュに反映させるため、 ```bmesh.update_edit_mesh()``` 関数を実行します。この関数を実行しないとメッシュが更新されませんので、 ```bmesh``` 用のメッシュデータを修正した時は必ず実行するようにしましょう。

[import:"update_bmesh", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

面の削除処理の説明はこれで終わりです。

最後に、削除した面数をカウントアップして変数 ```props.deleted``` を ```True``` に変更し、マウスの右ボタンが押された状態で連続して面が削除されないようにします。

[import:"post_process", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-1.py)

最後に、```modal``` メソッドは ```{'PASS_THROUGH'}``` を返します。```{'PASS_THROUGH'}``` が返されるとイベントを本処理に閉じず、別の処理に対しても通知することができます。```{'PASS_THROUGH'}``` が指定されていないと、マウスやキーボードのイベントが発生した時に行う ```DeleteFaceByRClick``` の処理後にイベントが捨てられてしまい、マウスやキーボードからのイベントに対する他の処理が発生しなくなってしまいます。

試しに、 ```modal()``` メソッドの最終行である ```return {'PASS_THROUGH'}``` を ```return {'RUNNING_MODAL'}``` に変更してみましょう。

プロパティパネルからアドオンの機能を実行開始した後はボタンを押すことができなくなり、処理を終えることができなくなります。これは ```DeleteFaceByRClick``` の ```modal()``` メソッドでイベントが捨てられ、他の処理へイベントが通知されていないことを示します。

## まとめ

マウスから発生したイベントを扱う方法を紹介しました。これまでに説明していない内容がたくさん出てきましたが、理解できましたでしょうか？

マウスのイベントを用いることで、 アドオンで実現出来ることが広がると思いますので、ぜひ積極的に活用していきましょう。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* ```bpy.types.PropertyGroup``` クラスを継承したクラスのクラス変数にプロパティクラスを指定することで、プロパティをグループ化することができる
* プロパティパネルへメニューを追加するためには、 ```bpy.types.Panel``` クラスを継承し、 ```draw()``` メソッド内でUIを定義する必要がある
*  ```invoke()``` メソッドや ```execute()``` メソッドで ```{'RUNNING_MODAL'}``` を返すとモーダルモードへ移行し、登録されたモーダルクラスの ```modal()``` メソッドが実行される
* モーダルモードは、 ```{'FINISHED'}``` または ```{'CANCELLED'}``` を返すまで処理を終えずにイベントを受け取り続けるモードである
* ```modal()``` メソッドで ```{'PASS_THROUGH'}``` を返すことで、他の処理にもイベントを通知できる
* ```invoke()``` メソッドや ```modal()``` メソッドの引数 ```event``` を参照することで、発生したイベントやイベント時の状態を取得できる
* ```bmesh``` モジュールには、メッシュデータを簡単に扱うための関数が多数用意されている
