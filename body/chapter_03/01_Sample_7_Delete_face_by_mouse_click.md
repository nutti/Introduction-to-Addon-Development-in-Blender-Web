# 3-1. サンプル7: マウスの右クリックで面を削除する

アドオン開発に慣れてくると、よりインタラクティブ性の高い機能を提供するため、マウスやキーボードからのイベントを扱いたくなると思います。
例えば *3Dビュー* の *オブジェクトモード* で *S* キーを押した時に、マウスの移動でオブジェクトのサイズを変更する機能は、マウスからのイベントを扱っています。
本節ではアドオンでマウスやキーボードのイベントを扱う方法を、サンプル交えて紹介します。

## 作成するアドオンの仕様

* *3Dビュー* の *編集モード* 時に、マウスで *右クリック* したオブジェクトの面を削除する
* **プロパティパネル**（ *3Dビュー* 上で *N* キーを押した時に右側に表示されるパネル）から、処理の開始/終了を切り替える

## アドオンを作成する

以下のソースコードを、 [1.4節](../chapter_01/04_Install_own_Add-on.md)を参考にして *テキスト・エディタ* に入力し、
```sample_7.py``` という名前で保存してください。

{% include "../../sample/src/chapter_03/sample_7.py" %}

## アドオンを実行する

### アドオンを有効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、作成したアドオンを有効化すると *コンソール* に以下の文字列が出力されます。

```sh
サンプル 7: アドオン「サンプル7」が有効化されました。
```

### アドオンを使ってみる

*3Dビュー* 上で *N* キーを押して、 *プロパティパネル* を表示し、 *マウスの右クリックで面を削除* という項目が作成されてることを確認します。

![マウスの右クリックで面を削除 手順1](https://dl.dropboxusercontent.com/s/6pyxmbf4mak9o8j/use_add-on_1.png "マウスの右クリックで面を削除 手順1")

*編集モード* に変更し、選択方法を *面選択* にします。
*マウスの右クリックで面を削除* の *開始* ボタンをクリックします。

![マウスの右クリックで面を削除 手順2](https://dl.dropboxusercontent.com/s/ltuh1pmujq0hbrf/use_add-on_2.png "マウスの右クリックで面を削除 手順2")

適当な面にマウスカーソルを当てて、 *右クリック* しましょう。
マウスカーソルを当てた面が削除されていることがわかります。

![マウスの右クリックで面を削除 手順3](https://dl.dropboxusercontent.com/s/1ntqeqbtx5ni0ym/use_add-on_3.png "マウスの右クリックで面を削除 手順3")

最後に、 *マウスのクリックで面を削除* の *終了* ボタンをクリックして、処理を終了します。
処理を終了すると、削除した面の数が表示されます。

![マウスの右クリックで面を削除 手順4](https://dl.dropboxusercontent.com/s/vz6982lhm4ofsyp/use_add-on_4.png "マウスの右クリックで面を削除 手順4")


### アドオンを無効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、有効化したアドオンを無効化すると *コンソール* に以下の文字列が出力されます。

```sh
サンプル 7: アドオン「サンプル 7」が無効化されました。
```

## ソースコードの解説

### アドオン内で利用するプロパティ定義

今回のサンプルでは複数のクラス間でデータを共有します。
今回はアドオン内で利用するデータを ```bpy.types.PropertyGroup``` を用いて定義します。
```bpy.types.PropertyGroup``` は、 [2.3節](../chapter_02/03_Sample_3_Scaling_object_2.md) で紹介した *プロパティ用クラス* をグループ化するためのクラスです。
使い方は簡単で、 ```bpy.types.PropertyGroup``` クラスを継承し、グループ化したい *プロパティ用クラス* をメンバ変数に追加するだけです。

```py:sample_7_part1.py
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

今回プロパティグループに登録したメンバ変数一覧を以下に示します。

|メンバ変数|変数の意味|
|---|---|
|```running```|```True``` の時は、面を右クリックすることで削除する|
|```right_mouse_down```|```True``` の時は、右クリック中であることを示す|
|```deleted```|```True``` の時は、 右クリックにより削除された状態であることを示す。右クリックし続けた状態でマウスを動かし、複数の面が削除されないことを示す|
|```deleted_count```|```running``` が ```True``` から ```False``` になるまでに削除された面の数|

作成したプロパティグループは、 ```PointerProperty``` クラスを利用して登録します。

```py:sample_7_part2.py
def register():
# （略）
    sc = bpy.types.Scene
    sc.dfrc_props = PointerProperty(
        name = "プロパティ",
        description = "本アドオンで利用するプロパティ一覧",
        type = DFRC_Properties)
# （略）
```

アドオン有効時に、 ```PointerProperty``` の引数 ```type``` に、 作成したプロパティグループを定義したクラス名を指定することで、 ```bpy.types.Scene.dfrc_props``` にプロパティグループを追加しています。
これ以降、各プロパティには ```bpy.types.Scene.dfrc_props.running``` 等でアクセスすることができます。

アドオン無効時には、```bpy.types.Scene``` に追加したプロパティグループを削除する必要があります。
ここできちんと削除しておかないと、アドオン無効化時にもプロパティグループのデータが残ることになるため、無駄にメモリを圧迫してしまいます。

```py:sample_7_part3
def unregister():
    del bpy.types.Scene.dfrc_props
# （略）
```


### UIを作成する

処理を開始/終了するためのUIを作成します。
これまでのサンプルではメニューに追加するだけでしたが、今回のように処理の開始と終了という排他的な項目をメニューに追加するのは少し煩わしいです。
そこで今回のサンプルでは、 *プロパティパネル* に開始/終了が切り替わるボタンを作成します。

*プロパティパネル* の追加は、 ```bpy.types.Panel``` クラスを継承し、 ```draw()``` メソッド内でUIを定義することで可能となります。

```py:sample_7_part4
# UI
class OBJECT_PT_DFRC(bpy.types.Panel):
    bl_label = "マウスの右クリックで面を削除"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

# ・・・（略）・・・
```

```bpy.types.Panel``` クラスを継承したクラスのメンバ変数には、以下のメンバ変数を定義する必要があります。

|メンバ変数|値の意味|
|---|---|
|```bl_label```|パネルに登録した時に、項目として表示される文字列|
|```bl_space_type```|パネルを登録するウィンドウ|
|```bl_region_type```|パネルを登録するリージョン|

```bl_space_type``` はパネルの登録先 *ウィンドウ* で、今回は *3Dビュー* に登録したいため ```VIEW_3D``` を指定しています。
```bl_space_type``` には例えば以下のような値を設定することが可能です。

|設定値|値の意味|
|---|---|
|```VIEW_3D```|*3Dビュー*|
|```IMAGE_EDITOR```|*UV/画像エディター*|
|```NLA_EDITOR```|*NLAエディター*|
|```NODE_EDITOR```|*ノードエディター*|
|```LOGIC_EDITOR```|*ロジックエディター*|
|```SEQUENCE_EDITOR```|*ビデオシーケンスエディター*|
|```GRAPH_EDITOR```|*グラフエディター*|

```bl_region_type``` はパネルの登録先 *リージョン* で、今回は *プロパティパネル* に登録するため、　```UI``` を指定しています。
```bl_space_type``` には例えば以下のような値を設定することが可能です。

|設定値|値の意味|
|---|---|
|```UI```|*プロパティパネル*|
|```TOOLS```|*ツール・シェルフ*|
|```TOOL_PROPS```|*ツール・シェルフ* のプロパティ|


```py:sample_7_part5
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
```draw()``` メソッドに渡されてくる引数 ```context``` は、 ```draw()``` メソッドが呼ばれた時のコンテキスト情報が含まれています。
```context.scene.dfrc_props``` により、 ```register()``` 関数内で登録したアドオン内のプロパティグループ ```DFRC_Properties``` を取得しています。
```DFRC_Properties``` のメンバ変数 ```running``` が ```False``` の時は、削除処理が開始していないため、開始ボタンを表示します。
同様に、 ```running``` が ```True``` の時は、削除処理がすでに開始している状態であるため、終了ボタンを表示します。
ボタンの表示は ```layout.operator()``` 関数を用いて行います。
新たに出てきた ```layout.operator()``` 関数の引数を以下に示します。

|引数|値の意味|
|---|---|
|```text```|ボタンに表示される文字列|
|```icon```|ボタンに表示されるアイコン|


### オペレーション用クラスの作成

最後に、 *オペレーション用クラス* を作成します。
今回のアドオンでは、これまで紹介してきたサンプルにあった ```execute()``` メソッドが定義されていません。
その代わり、 ```modal()``` メソッドと ```invoke()``` メソッドが定義されています。

最初に、 ```invoke()``` メソッドを見てみましょう。
```invoke()``` メソッドは、 *オペレーション用クラス* が実行された時に呼ばれるメソッドです。
これまで使ってきた ```execute()``` も *オペレーション用クラス* が実行された時に呼ばれますが、 ```execute()``` 関数の前に ```invoke()``` 関数が呼ばれます。
このため、 ```execute()``` で利用するデータの初期化などを ```invoke()``` 関数で行うのが主な利用法となります。

```py:sample_7_part6.py
def invoke(self, context, event):
    props = context.scene.dfrc_props
    if context.area.type == 'VIEW_3D':
        # 処理開始
        if props.running is False:
            props.running = True
            props.deleted = False
            props.right_mouse_down = False
            props.deleted_count = 0
            # modal処理クラスを追加
            context.window_manager.modal_handler_add(self)
            print("サンプル 7: 削除処理を開始しました。")
            return {'RUNNING_MODAL'}
        # 処理停止
        else:
            props.running = False
            self.report({'INFO'}, "サンプル 7: %d個の面を削除しました。" % (props.deleted_count))
            print("サンプル 7: %d個の面を削除しました。" % (props.deleted_count))
            return {'FINISHED'}
    else:
        return {'CANCELLED'}
```

今回は、ボタンが押した時に処理を開始/終了する処理を ```invoke()``` メソッドで行っています。
プロパティグループ ```DFRC_Properties``` の取得方法は、UIの作成時に説明した方法と同じです。

処理開始時の処理は ```props.running``` が ```False``` の時に行い、 ```props.running``` を ```True``` に設定した後、 ```DFRC_Properties``` を実行開始時の初期値に設定します。
最後に、 ```context.window_manager.modal_handler_add()``` を実行して **モーダル処理用クラス** を登録し、 ```{'RUNNING_MODAL'}``` を返して、 **モーダルモード** へ移行します。
*モーダルモード* とは、 ```{'FINISHED'}``` または ```{'CANCELLED'}``` を返すまで、処理を終えずにイベントを受け取り続けるモードです。
今回のアドオンでは、 ```invoke()``` メソッドと ```modal()``` メソッドを同一のクラスで定義しているため、 ```context.window_manager.modal_handler_add()``` の引数に ```self``` を指定します。

処理終了時の処理は ```props.running``` が ```True``` の時に行い、```props.running``` を ```False``` に設定後、 *モーダルモード* 中に削除した面の数を出力します。
その後 ```{'FINISHED'}``` を返すことで、 *モーダルモード* を終了します。

続いて、 *モーダルモード* 中に呼ばれる ```modal()``` メソッドを説明します。

```py:sample_7_part7.py
def modal(self, context, event):
    props = context.scene.dfrc_props

    # 3Dビューの画面を更新
    if context.area:
        context.area.tag_redraw()

    # 起動していない場合は終了
    if props.running is False:
        return {'PASS_THROUGH'}

    # クリック状態を更新
    if event.type == 'RIGHTMOUSE':
        if event.value == 'PRESS':
            props.right_mouse_down = True
        elif event.value == 'RELEASE':
            props.right_mouse_down = False

    # 右クリックされた面を削除
    if props.right_mouse_down is True and props.deleted is False:
        # bmeshの構築
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)
        # クリックされた面を選択
        loc = event.mouse_region_x, event.mouse_region_y
        ret = bpy.ops.view3d.select(extend=True, location=loc)
        if ret == {'PASS_THROUGH'}:
            print("サンプル 7: 選択範囲外です。")
            return {'PASS_THROUGH'}
        # 選択面を取得
        e = bm.select_history[-1]
        if not isinstance(e, bmesh.types.BMFace):
            bm.select_history.remove(e)
            print("サンプル 7: 面以外を選択しました。")
            return {'PASS_THROUGH'}
        # 選択面を削除
        bm.select_history.remove(e)
        bmesh.ops.delete(bm, geom=[e], context=5)
        # bmeshの更新
        bmesh.update_edit_mesh(me, True)
        # 削除面数をカウントアップ
        props.deleted_count = props.deleted_count + 1
        # マウスクリック中に連続して面が削除されることを防ぐ
        props.deleted = True
        print("サンプル 7: 面を削除しました。")

    # マウスがクリック状態から解除された時に、削除禁止状態を解除
    if props.right_mouse_down is False:
        props.deleted = False

    return {'PASS_THROUGH'}
```

最初に、 ```context.area.tag_redraw()``` 関数を実行して *3Dビュー* を更新します。
次に ```props.running``` を確認し、処理が開始されていない場合は ```{'PASS_THROUGH'}``` を返して ```modal()``` メソッドを終了します。
```{'PASS_THROUGH'}``` はイベントを別の処理に対しても通知する処理です。
```{'PASS_THROUGH'}``` が指定されていないと、マウスやキーボードのイベントが発生した時に ```DeleteFaceByRClick``` の処理後にイベントが捨てられてしまい、マウスやキーボードからのイベントに対する処理が発生しなくなってしまいます。
試しに、 ```modal()``` メソッドの最終行である ```return {'PASS_THROUGH'}``` を ```return {'RUNNING_MODAL'}``` に変更してみてください。
*プロパティパネル* から処理を開始した後にボタンを押すことができなくなり、処理を終えることができなくなります。

## まとめ



### ポイント

*
