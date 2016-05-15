<div id="sect_title_img_2_5"></div>

<div id="sect_title_text"></div>

# サブメニューを作成する

<div id="preface"></div>

###### これまで紹介したアドオンでは1階層分のメニューを追加するだけでしたが、サブメニュー（マウスオーバーすると展開されるメニュー）を作成して2階層以上のメニューを作ることもできます。例えば、 *3Dビュー* エリアの *追加* > *メッシュ* は、 *追加* の親メニューの下に *メッシュ* という子メニューがある2階層のメニューとなっています。本節では [2-4節](04_Use_Property_on_Tool_Shelf_2.md) のサンプルを改良し、複製するオブジェクトをメニューから選択できるようなメニューを構築することで、複数階層のメニューを作成する方法を紹介します。

## 作成するアドオンの仕様

* [2-4節](04_Use_Property_on_Tool_Shelf_2.md) で作成したサンプルを改良し、複製するオブジェクトをメニューから選択できるようにする

## アドオンを作成する

以下のソースコードを、 [1-4節](../chapter_01/04_Install_own_Add-on.md) を参考にして *テキスト・エディタ* に入力し、```sample_5.py``` という名前で保存してください。

[import](../../sample/src/chapter_02/sample_5.py)

## アドオンを実行する

### アドオンを有効化する

[1-4節](../chapter_01/04_Install_own_Add-on.md) を参考に、作成したアドオンを有効化すると *コンソール* に以下の文字列が出力されます。

```sh
サンプル5: アドオン「サンプル5」が有効化されました。
```

アドオンを有効化後 *3Dビュー* エリアのメニュー *オブジェクト* > *オブジェクトの複製* にサブメニューが追加されていることを確認しましょう。
サブメニューには、 *3Dビュー* エリアに存在するオブジェクト名が追加されているはずです。

![オブジェクトの複複1](https://dl.dropboxusercontent.com/s/suhwkprgpkrrwqh/use_add-on_1.png "オブジェクトの複製1")


### アドオンを使ってみる

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*3Dビュー* エリアのメニュー *オブジェクト* > *オブジェクトの複製* から複製するオブジェクト名を選んで実行すると、選択したオブジェクトが複製されます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|複製されたオブジェクトは [2-4節](04_Use_Property_on_Tool_Shelf_2.md) と同様、拡大率・回転角度・配置先を *ツール・シェルフ* の *オプション* から変更することができます。|![オブジェクトの複複2](https://dl.dropboxusercontent.com/s/o0ten4sgfm8jter/use_add-on_2.png "オブジェクトの複製2")|
|---|---|---|

<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-4節](../chapter_01/04_Install_own_Add-on.md)を参考に、有効化したアドオンを無効化すると *コンソール* に以下の文字列が出力されます。

```sh
サンプル5: アドオン「サンプル5」が無効化されました。
```

## ソースコードの解説

サブメニューを作成するコードを除き、ソースコードの大部分は [2-4節](04_Use_Property_on_Tool_Shelf_2.md) からの流用です。
このため、新規で追加した部分について解説します。

### サブメニューの追加

サブメニューを追加するためには、 ```bpy.types.Menu``` クラスを継承したメニュークラスを作成する必要があります。

```python
# メインメニュー
class ReplicateObjectMenu(bpy.types.Menu):
    bl_idname = "uv.replicate_object_menu"
    bl_label = "オブジェクトの複製"
    bl_description = "オブジェクトを複製します"

    def draw(self, context):
        layout = self.layout
        # サブメニューの登録＋出力文字列の登録
        # bpy.data.objects：オブジェクト一覧
        for o in bpy.data.objects:
            layout.operator(ReplicateObject.bl_idname, text=o.name).src_obj_name = o.name
```

オペレータクラスと同様、メニュークラスにはメンバ変数 ```bl_idname``` 、 ```bl_label``` 、 ```bl_description``` を指定する必要があります。
メニュークラスは、メニューを表示するためだけのクラスであるため、 ```bl_options``` を指定する必要はありません。

メニュークラスには、メニューの描画に必要な ```draw()``` メソッドを実装する必要があります。
```draw()``` メソッドはメニューが表示される度に呼ばれ、以下の引数がBlender本体から渡されてきます。

|引数|型|値の説明|
|---|---|---|
|```self```|呼ばれた ```draw()``` メソッドが定義されているメニュークラス|メニュークラスのインスタンス|
|```context```|```bpy.types.Context```|```draw()``` メソッドが呼ばれた時のコンテキスト|

オペレータクラスをメニューに登録した時と同様、サブメニューへの項目追加は ```self.layout.operator()``` 関数で行うことができます。
今回は *3Dビュー* エリア上の全てのオブジェクト名をメニュー項目に追加するため、 ```layout.operator()``` の第1引数にオペレータクラスの ```bl_idname``` を指定し、 引数 ```text``` にオブジェクト名を指定しています。
オペレータクラスは、複製するオブジェクトをオブジェクト名で判定するため、オペレータクラスのメンバ変数 ```src_obj_name``` にもオブジェクト名を代入しています。

オペレータクラスでは、メニュークラスから複製されたオブジェクト名を代入するための変数 ```src_obj_name``` を ```StringProperty()``` クラスとして用意します。

```python
    src_obj_name = bpy.props.StringProperty()
```

オペレータクラスの ```execute()``` メソッドでは、 ```src_obj_name``` に代入されたオブジェクト名を用いてオブジェクトを複製するように処理を変更していますので、ソースコードのコメントを参考に確認してみてください。

最後に、 *3Dビュー* エリアのメニュー *オブジェクト* へ項目を追加します。

```python
def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(ReplicateObjectMenu.bl_idname)
```

オペレータクラスをメニューに追加する時は ```self.layout.operator()``` 関数を利用していましたが、メニュークラスをメニューに追加する場合は ```self.layout.menu()``` 関数を利用します。
```self.layout.menu()``` 関数にメニュークラスの ```bl_idname``` を引数として渡すことで、メニューをメニュー項目に追加することができます。

### 3階層以上のメニュー

サブメニューにさらにサブメニュー（サブサブメニュー）を追加するなど、3階層以上のメニューを作成することもできます。
以下のサンプルでは、先ほど作成したサンプルのメニューとサブメニューの間に *オブジェクトの複製（サブメニュー）* を追加しています。

[import](../../sample/src/chapter_02/sample_5_alt.py)

アドオンを作成し有効化すると、以下のように3階層のメニューが作成されていることを確認できます。

![多階層メニュー](https://dl.dropboxusercontent.com/s/rrpepaa9eygx9qt/multilevel_menu.png "多階層メニュー")

サンプルを見てもらえばわかると思いますが、3階層のメニューを作成する場合は2階層のメニューを作成した時の応用になります。

```python
# サブメニュー
class ReplicateObjectSubMenu(bpy.types.Menu):
    bl_idname = "uv.replicate_object_sub_menu"
    bl_label = "オブジェクトの複製（サブメニュー）"
    bl_description = "オブジェクトを複製します（サブメニュー）"

    def draw(self, context):
        layout = self.layout
        # サブサブメニューの登録
        for o in bpy.data.objects:
            layout.operator(ReplicateObject.bl_idname, text=o.name).src_obj_name = o.name


# メインメニュー
class ReplicateObjectMenu(bpy.types.Menu):
    bl_idname = "uv.replicate_object_menu"
    bl_label = "オブジェクトの複製"
    bl_description = "オブジェクトを複製します"

    def draw(self, context):
        layout = self.layout
        # サブメニューの登録
        layout.menu(ReplicateObjectSubMenu.bl_idname)
```

サブメニューを登録する時に ```self.layout.operator()``` 関数の代わりに ```self.layout.menu()``` 関数を用い、サブメニュー用に作成したメニュークラスの ```bl_idname``` を指定します。そしてサブメニュー用に作成したクラスの中で、オペレータクラスを登録することで、3階層のメニューを作成することができます。
このような手順を踏むことで、4階層、5階層、・・・とメニューの階層を増やすことができるので、ぜひ試してみてください。

## まとめ

[2-4節](04_Use_Property_on_Tool_Shelf_2.md) を改造し、複製するオブジェクトをメニューから選択できるようにしました。
また、サブメニューから複製するオブジェクトを選べるようにしました。
サブメニューを用いることで、今回のサンプルのように処理対象を選択できるようにしたり、メニュー項目を機能ごとに整理することができるようになります。
ぜひここでサブメニューの作り方を習得し、ユーザにとってわかりやすいUI作りに活かしましょう。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* メニュークラスは、 ```bpy.types.Menu``` クラスを継承して作成する
* メニュークラスの ```draw()``` メソッド内で、 オペレータクラスの ```bl_idname ``` を ```self.layout.operation()``` 関数の引数に指定し、メニュークラスの ```bl_idname``` を引数にして ```self.layout.menu()``` を呼び出すことで、サブメニューを作成できる
* メニュークラスの ```draw()``` メソッド内でサブメニュー用に作成したクラスの ```bl_idname``` を ```self.layout.menu()``` 関数の引数に指定することで、3階層以上のメニューを作成することができる
