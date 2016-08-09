<div id="sect_title_img_3_1"></div>

<div id="sect_title_text"></div>

# マウスクリックの<br>イベントを扱う

<div id="preface"></div>

###### 3DビューエリアのオブジェクトモードでSキーを押した時に、マウスの移動でオブジェクトのサイズを変更する機能があります。このように、アドオンでよりインタラクティブ性の高い機能を提供するために、マウスやキーボードからのイベントを扱いたくなる時が来るかもしれません。本節ではアドオンからマウスやキーボードのイベントを扱う方法を、サンプル交えて紹介します。

## 作成するアドオンの仕様

* 3Dビューエリアの編集モード時に、マウスで右クリックしたオブジェクトの面を削除する
* プロパティパネル（3Dビューエリア上でNキーを押した時に右側に表示されるパネル）から、上記処理の開始/終了を切り替える

## アドオンを作成する

[1-4節](../chapter_01/04_Install_own_Add-on.md) を参考にして、以下のソースコードをテキスト・エディタに入力し、ファイル名 ```sample_7.py``` として保存してください。

[import](../../sample/src/chapter_03/sample_7.py)

## アドオンを使用する

### アドオンを有効化する

[1-4節](../chapter_01/04_Install_own_Add-on.md) を参考に、作成したアドオンを有効化するとコンソールに以下の文字列が出力されます。

```sh
サンプル7: アドオン「サンプル7」が有効化されました。
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

|<div id="box">4</div>|3Dビューエリアのプロパティパネル上のマウスのクリックで面を削除の終了ボタンをクリックして、処理を終了します。<br>終了時に削除した面の数がコンソール・ウィンドウに表示されます。|![マウスの右クリックで面を削除 手順4](https://dl.dropboxusercontent.com/s/vz6982lhm4ofsyp/use_add-on_4.png "マウスの右クリックで面を削除 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-4節](../chapter_01/04_Install_own_Add-on.md) を参考に有効化したアドオンを無効化すると、コンソールに以下の文字列が出力されます。

```sh
サンプル7: アドオン「サンプル7」が無効化されました。
```

## ソースコードの解説

### アドオン内で利用するプロパティ定義

本節のサンプルでは複数のクラス間でデータを共有する必要があります。アドオン内で共有するデータを ```bpy.types.PropertyGroup``` クラスを用いて定義することで、複数のクラス間でデータを共有します。

```bpy.types.PropertyGroup``` クラスは、 [2-3節](../chapter_02/03_Use_Property_on_Tool_Shelf_1.md) で紹介したプロパティクラスをグループ化するためのクラスです。　```bpy.types.PropertyGroup``` クラスを継承し、グループ化したいプロパティクラスをメンバ変数に追加して使用します。

```python
# プロパティ
class DFRC_Properties(bpy.types.PropertyGroup):
    running = BoolProperty(
        name = "動作中",
        description = "削除処理が動作中か？",
        default = False)
    right_mouse_down = BoolProperty(
        name = "右クリックされた状態",
        description = "右クリックされた状態か？",
        default = False)
    deleted = BoolProperty(
        name = "面が削除された状態",
        description = "面が削除された状態か？",
        default = False)
    deleted_count = IntProperty(
        name = "削除した面数",
        description = "削除した面の数",
        default = 0)
```

本節のサンプルにおいてグループ化したプロパティ一覧を以下に示します。

|プロパティ|意味|
|---|---|
|```running```|```True``` の時は、面を右クリックすることで削除する|
|```right_mouse_down```|```True``` の時は、右クリック中であることを示す|
|```deleted```|```True``` の時は、 右クリックにより削除された状態であることを示す。右クリックし続けた状態でマウスを動かし、複数の面が削除されないようにするために必要|
|```deleted_count```|```running``` が ```True``` から ```False``` になるまでに削除された面の数|

作成したグループは、 ```PointerProperty``` クラスを利用して登録します。

```python
def register():
# （略）
    sc = bpy.types.Scene
    sc.dfrc_props = PointerProperty(
        name = "プロパティ",
        description = "本アドオンで利用するプロパティ一覧",
        type = DFRC_Properties)
# （略）
```

アドオン有効時に ```PointerProperty``` の引数 ```type``` へグループ化のために定義したクラス名を指定することで、 ```bpy.types.Scene.dfrc_props``` 変数にプロパティのグループを登録します。以降、各プロパティには ```bpy.types.Scene.dfrc_props.running``` 等でアクセスすることができます。

アドオン無効時には、```bpy.types.Scene``` に追加したプロパティのグループを削除する必要があります。削除しないとアドオン無効化時にもプロパティのデータが残ることになるため、無駄にメモリを使用した状態になるので、忘れずに削除するようにしましょう。

```python
def unregister():
    del bpy.types.Scene.dfrc_props
# （略）
```


### UIを作成する

アドオン機能の処理を開始/終了するためのUIを作成します。

メニューに追加するだけで問題なかった今までのサンプルとは異なり、本節のサンプルのように処理の開始と終了という排他的な項目をメニューに両方追加するのはUIとして良いとは言えません。そこで本節のサンプルでは、3Dビューエリアのプロパティパネルに開始/終了を切り替えるためのボタンを作成します。

プロパティパネルにボタンを追加するためには ```bpy.types.Panel``` クラスを継承してパネルクラスを作成し、 ```draw()``` メソッド内でUIを定義します。

```python
# UI
class OBJECT_PT_DFRC(bpy.types.Panel):
    bl_label = "マウスの右クリックで面を削除"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

# ・・・（略）・・・
```

パネルクラスのメンバ変数には、以下のメンバ変数を定義する必要があります。

|メンバ変数|値の意味|
|---|---|
|```bl_label```|パネルに登録時に、項目として表示される文字列|
|```bl_space_type```|登録先のエリア|
|```bl_region_type```|登録先のリージョン|

メンバ変数 ```bl_space_type``` には登録先のエリアを指定します。今回は3Dビューエリアに登録することを考えて ```VIEW_3D``` を指定しています。

メンバ変数 ```bl_space_type``` には、他にも以下のような値を指定することができます。

|設定値|値の意味|
|---|---|
|```VIEW_3D```|*3Dビュー*|
|```IMAGE_EDITOR```|*UV/画像エディター*|
|```NLA_EDITOR```|*NLAエディター*|
|```NODE_EDITOR```|*ノードエディター*|
|```LOGIC_EDITOR```|*ロジックエディター*|
|```SEQUENCE_EDITOR```|*ビデオシーケンスエディター*|
|```GRAPH_EDITOR```|*グラフエディター*|

メンバ変数 ```bl_region_type``` には登録先のリージョンを指定します。今回はプロパティパネルに登録するため、　```UI``` を指定しています。

メンバ変数 ```bl_space_type``` には、他にも以下のような値を設定することが可能です。

|設定値|値の意味|
|---|---|
|```UI```|*プロパティパネル*|
|```TOOLS```|*ツール・シェルフ*|
|```TOOL_PROPS```|*ツール・シェルフ* のプロパティ|


```python
# UI
class OBJECT_PT_DFRC(bpy.types.Panel):
# ・・・（略）・・・

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        props = context.scene.dfrc_props
        # 開始/停止ボタンを追加
        if props.running is False:
            layout.operator(DeleteFaceByRClick.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(DeleteFaceByRClick.bl_idname, text="終了", icon="PAUSE")
```

続いて、 ```draw()``` メソッドを定義します。

```draw()``` メソッドに渡されてくる引数 ```context``` には、 ```draw()``` メソッドが呼ばれた時のコンテキスト情報が含まれています。

```context.scene.dfrc_props``` から、 ```register()``` 関数内で登録したアドオン内のプロパティグループ ```DFRC_Properties``` を取得できます。

```DFRC_Properties``` クラスのメンバ変数 ```running``` が ```False``` の時は、削除処理が開始されていないため、開始ボタンを表示します。```running``` が ```True``` の時は、削除処理がすでに開始されている状態であるため、終了ボタンを表示します。

ボタンは ```layout.operator()``` 関数で表示でき、以下の引数を指定します。

|引数|値の意味|
|---|---|
|```text```|ボタンに表示する文字列|
|```icon```|ボタンに表示するアイコン|


### オペレータクラスの作成

最後に、 *オペレータクラス* を作成します。

本節のアドオンでは、これまで紹介したサンプル内のオペレータクラスで毎回定義した ```execute()``` メソッドが定義されていません。その代わり、 ```modal()``` メソッドと ```invoke()``` メソッドが定義されています。

#### invoke()メソッド

最初に、 ```invoke()``` メソッドについて解説します。

```invoke()``` メソッドは、処理が実行された時に呼ばれるメソッドです。これまで使ってきた ```execute()``` メソッドも処理が実行された時に呼ばれますが、 ```execute()``` メソッドの前に ```invoke()``` メソッドが呼ばれる点が異なります。このため、 ```execute()``` メソッドの実行前に行いたい処理がある場合は、 ```invoke()``` メソッドを使用します。

```python
def invoke(self, context, event):
    props = context.scene.dfrc_props
    if context.area.type == 'VIEW_3D':
# ・・・（略）・・・
    else:
        return {'CANCELLED'}
```

本節のサンプルでは、ボタンが押した時に処理を開始/終了する処理を ```invoke()``` メソッドに記述します。

プロパティグループ ```DFRC_Properties``` の取得方法は、UIの作成時に説明した方法と同じで、 ```context.scene.dfrc_props``` で取得できます。

```python
        if props.running is False:
            props.running = True
            props.deleted = False
            props.right_mouse_down = False
            props.deleted_count = 0
            # modal処理クラスを追加
            context.window_manager.modal_handler_add(self)
            print("サンプル7: 削除処理を開始しました。")
            return {'RUNNING_MODAL'}
```

アドオンの機能実行開始時の処理は変数 ```props.running``` が ```False``` の時に行い、変数 ```props.running``` を ```True``` に設定した後、 ```DFRC_Properties``` の各メンバ変数を初期値に設定します。最後に ```context.window_manager.modal_handler_add()``` 関数を実行してモーダルクラスを登録し、 ```{'RUNNING_MODAL'}``` を返してモーダルモードへ移行します。

モーダルモードとは、 ```{'FINISHED'}``` または ```{'CANCELLED'}``` を返すまで、処理を終えずにマウスやキーボードなどからイベントを受け取り続けるモードを指します。

本節のアドオンでは、 ```invoke()``` メソッドと ```modal()``` メソッドを同一のクラスで定義しているため、 ```context.window_manager.modal_handler_add()``` 関数の引数に ```self``` を指定します。

```python
        # 処理停止
        else:
            props.running = False
            self.report({'INFO'}, "サンプル7: %d個の面を削除しました。" % (props.deleted_count))
            print("サンプル7: %d個の面を削除しました。" % (props.deleted_count))
            return {'FINISHED'}
```

アドオンの機能実行終了時の処理は変数 ```props.running``` が ```True``` の時に行い、変数 ```props.running``` を ```False``` に設定後、モーダルモード中に削除した面の数を出力します。

その後 ```{'FINISHED'}``` を返します。

<div id="space_l"></div>


#### modal()メソッド

続いて、 *モーダルモード* 中に呼ばれる ```modal()``` メソッドについて説明します。

```python
def modal(self, context, event):
    props = context.scene.dfrc_props

    # 3Dビューの画面を更新
    if context.area:
        context.area.tag_redraw()

    # 起動していない場合は終了
    if props.running is False:
        return {'PASS_THROUGH'}

# ・・・（略）・・・

    return {'PASS_THROUGH'}
```

最初に ```context.area.tag_redraw()``` 関数を実行し、3Dビューエリアを更新します。次に変数 ```props.running``` を確認し、アドオンの機能開始時の処理が開始されていない場合は ```{'PASS_THROUGH'}``` を返して ```modal()``` メソッドを終了します。

```{'PASS_THROUGH'}``` が返されるとイベントを本処理に閉じず、別の処理に対しても通知することができます。```{'PASS_THROUGH'}``` が指定されていないと、マウスやキーボードのイベントが発生した時に行う ```DeleteFaceByRClick``` の処理後にイベントが捨てられてしまい、マウスやキーボードからのイベントに対する他の処理が発生しなくなってしまいます。

試しに、 ```modal()``` メソッドの最終行である ```return {'PASS_THROUGH'}``` を ```return {'RUNNING_MODAL'}``` に変更してみましょう。

プロパティパネルからアドオンの機能を実行開始した後はボタンを押すことができなくなり、処理を終えることができなくなります。これは ```DeleteFaceByRClick``` の ```modal()``` メソッドでイベントが捨てられ、他の処理へイベントが通知されていないことを示します。

```python
    # クリック状態を更新
    if event.type == 'RIGHTMOUSE':
        if event.value == 'PRESS':
            props.right_mouse_down = True
        elif event.value == 'RELEASE':
            props.right_mouse_down = False
```

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


```python
    # 右クリックされた面を削除
    if props.right_mouse_down is True and props.deleted is False:

# ・・・（略）・・・

    # マウスがクリック状態から解除された時に、削除禁止状態を解除
    if props.right_mouse_down is False:
        props.deleted = False
```

右クリックされた時の処理を実装します。

削除処理の前に、 ```if props.right_mouse_down is True and props.deleted is False``` により、削除処理を行うか否かを確認しています。この確認処理には少し工夫を加えています。

右クリックをされたことを検出するためには、 ```props.right_mouse_down``` が ```True``` であることの判定だけで問題ないように思えます。しかし、右クリックが押されたいる間は ```props.right_mouse_down``` が常に ```True``` になるため、クリック中にマウスを移動させると面を削除できてしまいます。これは、本来期待する動作(右クリックを行った直後の1回だけ面を削除)とは少し異なります。そこで変数 ```props.deleted``` が ```True``` であることを確認し、すでに面を一度削除した状態であれば、削除処理を行わないようにします。そして ```props.right_mouse_down``` が ```False``` に変わった時に ```props.deleted``` を ```False``` に戻すことで、次に右クリックが行われた時に面を削除できるようにします。

続いて面を削除の処理の説明をします。

面を削除するためには、削除対象のメッシュデータにアクセスする必要があります。

メッシュデータにアクセスするためには、```bpy.data.meshes``` からアクセスする方法と ```bmesh``` モジュールを用いる方法があります。今回のサンプルでは、 ```bmesh``` モジュールを用いて面の削除処理を実装しています。

```bmesh``` は比較的最近（バージョン2.63より）導入されたモジュールで、メッシュデータを簡単に扱う関数が多く提供されています。

```bmesh``` を利用するためには、以下のように ```bmesh``` モジュールをインポートする必要があります。

```python
import bmesh
```

面の削除処理本体を説明します。

最初にメッシュデータにアクセスするため、 ```bmesh``` 用のメッシュデータを構築します。編集中のオブジェクトデータ ```context.edit_object.data``` を ```bmesh.from_edit_mesh()``` 関数の引数に渡すことで、 ```bmesh``` 用のメッシュデータを構築できます。

```python
        # bmeshの構築
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
```

次に、クリックされた面を削除する処理について説明します。

クリックされた面の削除処理の流れを以下に示します。

<div id="custom_ol"></div>

1. クリック時にマウスの位置にある面を選択
2. 選択された面を取得
3. 面を削除

最初に1のクリック時のマウス位置にある面選択ですが、 ```event``` 変数からマウスの位置情報を取得します。

```bpy.ops.view3d.select()``` 関数の引数 ```location``` にマウスの位置を指定することで、マウスの位置にある面を選択することができます。もしマウスの位置に面がなければ ```bpy.ops.view3d.select()``` 関数は ```{'PASS_THROUGH'}``` を返すため、マウスの位置に面がないことを出力した後に処理を終了します。

```python
        # クリックされた面を選択
        loc = event.mouse_region_x, event.mouse_region_y
        ret = bpy.ops.view3d.select(location=loc)
        if ret == {'PASS_THROUGH'}:
            print("サンプル7: 選択範囲外です。")
            return {'PASS_THROUGH'}

```

続いて2の選択された面を取得する手順について説明します。

選択された面は、 ```bmesh``` の履歴情報のうち最後に選択された面として取得できます。頂点・辺・面の選択履歴 ```bm.select_history``` の最後の要素が面であるか否かを確認し、面であれば処理を継続します。面でなければ ```{'PASS_THROUGH'}``` を返して処理を終了します。

```python
        # 選択面を取得
        e = bm.select_history[-1]
        if not isinstance(e, bmesh.types.BMFace):
            bm.select_history.remove(e)
            print("サンプル7: 面以外を選択しました。")
            return {'PASS_THROUGH'}
```

最後に選択した面を削除します。

面の削除は ```bmesh.ops.delete()``` 関数で行い、以下に示す引数を指定します。

|引数|値の意味|
|---|---|
|第1引数|```bmesh``` 用のメッシュデータ|
|```geom```|削除するデータ|
|```context```|削除するデータの種類|

今回は面を削除するため、 ```context``` に ```5``` を指定しています。

```python
        # 選択面を削除
        bm.select_history.remove(e)
        bmesh.ops.delete(bm, geom=[e], context=5)
```

面を削除したことをメッシュに反映させるため、 ```bmesh.update_edit_mesh()``` 関数を実行します。この関数を実行しないとメッシュが更新されませんので、 ```bmesh``` 用のメッシュデータを修正した時は必ず実行するようにしましょう。

```python
        # bmeshの更新
        bmesh.update_edit_mesh(me, True)
```

面の削除処理の説明はこれで終わりです。

最後に、削除した面数をカウントアップして変数 ```props.deleted``` を ```True``` に変更し、マウスの右ボタンが押された状態で連続して面が削除されないようにします。

```python
        # 削除面数をカウントアップ
        props.deleted_count = props.deleted_count + 1
        # マウスクリック中に連続して面が削除されることを防ぐ
        props.deleted = True
        print("サンプル7: 面を削除しました。")
```

## まとめ

マウスから発生したイベントを扱う方法を紹介しました。これまでに説明していない内容がたくさん出てきましたが、理解できましたでしょうか？

マウスのイベントを用いることで、 アドオンで実現出来ることが広がると思いますので、ぜひ積極的に活用していきましょう。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* ```bpy.types.PropertyGroup``` クラスを継承したクラスのメンバ変数にプロパティクラスを指定することで、プロパティをグループ化することができる
* プロパティパネルへメニューを追加するためには、 ```bpy.types.Panel``` クラスを継承し、 ```draw()``` メソッド内でUIを定義する必要がある
* オペレータクラスに定義する ```invoke()``` メソッドは、オペレータクラスが実行された時に呼ばれるメソッドで、 ```execute()``` メソッドより前に呼ばれる
*  ```invoke()``` メソッドや ```execute()``` メソッドで ```{'RUNNING_MODAL'}``` を返すとモーダルモードへ移行し、登録されたモーダルクラスの ```modal()``` メソッドが実行される
* モーダルモードは、 ```{'FINISHED'}``` または ```{'CANCELLED'}``` を返すまで処理を終えずにイベントを受け取り続けるモードである
* ```modal()``` メソッドで ```{'PASS_THROUGH'}``` を返すことで、他の処理にもイベントを通知できる
* ```invoke()``` メソッドや ```modal()``` メソッドの引数 ```event``` を参照することで、発生したイベントやイベント時の状態を取得できる
* ```bmesh``` モジュールには、メッシュデータを簡単に扱うための関数が多数用意されている
