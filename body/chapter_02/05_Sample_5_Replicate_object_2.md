# 2-5. サンプル5: オブジェクトを複製する2

これまで紹介したアドオンでは1階層のメニューを追加するのみでしたが、BlenderのUIはサブメニュー（マウスオーバーすると展開されるメニュー）を作成して2階層以上のメニューを作ることができます。
例えば、 *3Dビュー* の *追加* > *メッシュ* は2階層のメニューとなっています。
本節では [2.4節](04_Sample_4_Replicate_object_1.md) のサンプルを改良し、複製するオブジェクトをメニューから選択できるよう2階層のメニューを構築します。

## 作成するアドオンの仕様

* [2.4節](04_Sample_4_Replicate_object_1.md)で作成したサンプルついて、複製するオブジェクトをメニューより選択できるようにする

## アドオンを作成する

以下のソースコードを、 [1.4節](../chapter_01/04_Install_own_Add-on.md)を参考にして **テキスト・エディタ** に入力し、
**sample_5.py** という名前で保存してください。

[import](../../sample/src/chapter_02/sample_5.py)

## アドオンを実行する

### アドオンを有効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、作成したアドオンを有効化すると **コンソール** に以下の文字列が出力されます。

```sh
サンプル 5: アドオン「サンプル5」が有効化されました。
```

### アドオンを使ってみる

アドオンを有効化したら、 *3Dビュー* のメニューの *オブジェクト* > *オブジェクトの複製* にサブメニューが追加されていることを確認しましょう。


![オブジェクトの複複1](https://dl.dropboxusercontent.com/s/suhwkprgpkrrwqh/use_add-on_1.png "オブジェクトの複製1")

追加されたサブメニューから複製するオブジェクト名を選んで実行すると、選択したオブジェクトが複製されます。
複製されたオブジェクトは、 [2.4節](04_Sample_4_Replicate_object_1.md) と同様、拡大率・回転角度・配置先をツール・シェルフのオプションから変更できます。

![オブジェクトの複複2](https://dl.dropboxusercontent.com/s/o0ten4sgfm8jter/use_add-on_2.png "オブジェクトの複製2")

### アドオンを無効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、有効化したアドオンを無効化すると **コンソール** に以下の文字列が出力されます。

```sh
サンプル 5: アドオン「サンプル 5」が無効化されました。
```

## ソースコードの解説

サブメニューを作成するコードを除いてソースコードの大部分は、 [2.4節](04_Sample_4_Replicate_object_1.md) からの流用です。

### サブメニューの追加

サブメニューを追加するためには、 ```bpy.types.Menu``` クラスを継承したメニュー用クラスを作成する必要があります。

```py:sample_5_part1.py
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

オペレーション用クラスと同様、メニュー用クラスにはメンバ変数 ```bl_idname``` 、 ```bl_label``` 、 ```bl_description``` を含める必要があります。
メニュー用クラスは、メニューを表示するためだけのクラスであるため、 ```bl_options``` は含める必要がありません。

メニュー用クラスには、メニューの描画に必要な ```draw()``` メソッドを実装する必要があります。
```draw()``` メソッドはメニューが表示される度に呼ばれ、以下の引数がBlender本体から渡されてきます。

|引数|型|値の説明|
|---|---|---|
|```self```|呼ばれた ```draw()``` が定義されている型|メニュー用クラスのインスタンス|
|```context```|```bpy_types.Context```|メニューが表示された時のコンテキスト|

サブメニューへの項目追加は、オペレーション用クラスをメニューに登録した時と同様、 ```self.layout.operator()``` 関数で行うことができます。
今回は3Dビュー上の全てのオブジェクト名でメニュー項目を追加するため、 ```layout.operator()``` の第1引数にオペレーション用クラスの ```bl_idname``` を指定し、 引数 ```text``` にオブジェクト名を指定しています。
オペレーション用クラスは複製するオブジェクトをオブジェクト名で判定するようにするため、オペレーション用クラスのメンバ変数 ```src_obj_name``` にもオブジェクト名を代入しています。

オペレーション用クラスでは、メニュー用クラスから代入するための変数 ```src_obj_name``` を ```StringProperty()``` として用意します。

```py:sample_5_part2.py
    src_obj_name = bpy.props.StringProperty()
```

オペレーションクラスの ```execute()``` メソッドでは、 ```src_obj_name``` に代入されたオブジェクト名を用いて、オブジェクトを複製するように処理を変更していますので、ソースコードのコメントを参考に確認してみてください。

最後に、3Dビューのメニューのオブジェクトへ項目を追加します。

```py:sample_5_part3.py
def menu_fn(self, context):
    self.layout.separator()
    self.layout.menu(ReplicateObjectMenu.bl_idname)
```

オペレーション用クラスをメニューに追加した時は ```self.layout.operator()``` 関数を利用していましたが、メニュー用クラスをメニューに登録する場合は ```self.layout.menu()``` 関数を利用します。
```self.layout.menu()``` 関数にメニュー用クラスの ```bl_idname``` を引数として渡すことで、メニューを項目に追加することができます。

### 3階層以上のメニュー

サブメニューにさらにサブメニュー（サブサブメニュー）を追加するなど、3階層以上のメニューを作成することもできます。
以下のサンプルでは、先ほど作成したサンプルのメニューとサブメニューの間に *オブジェクトの複製（サブメニュー）* を追加します。

[import](../../sample/src/chapter_02/sample_5_alt.py)

アドオンを作成して実行してみましょう。
以下のように3階層のメニューが作成されていることを確認することができます。

![多階層メニュー](https://dl.dropboxusercontent.com/s/rrpepaa9eygx9qt/multilevel_menu.png "多階層メニュー")

サンプルを見てもらえばわかる通り、3階層のメニューを作成する場合は2階層のメニューを作成する場合の応用になります。

```py:sample_5_alt_part1.py
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

サブメニューを登録する時に ```self.layout.operator()``` の代わりに ```self.layout.menu()``` を用い、サブメニュー用に作成したメニュー用クラスの ```bl_idname``` を指定します。サブメニュー用に作成したクラスの中で、オペレーション用クラスを登録することで、3階層のメニューを作成することができます。
このような手順を踏むことで、4階層、5階層、・・・とメニューの階層を増やすことができますので、ぜひ試してみてください。

## まとめ

[2.4節](04_Sample_4_Replicate_object_1.md) を改造し、複製するオブジェクトをメニューから選択できるようにしました。
この時にサブメニューから複製するオブジェクトを選べるようにしました。
サブメニューを用いることで、今回のサンプルのように処理対象を選択できるようにしたり、メニュー項目を機能ごとに整理することができるようになります。
サブメニューの作り方は、これまでの内容が理解できている方であればそこまで難しいと思いますので、ぜひここで作り方を習得してユーザがわかりやすいUI作りに活かしましょう。

### ポイント

* メニュー用クラスは、 ```bpy.types.Menu``` クラスを継承して作成する
* メニュー用クラスの ```draw()``` メソッド内で、 オペレーション用クラスの ```bl_idname ``` を ```self.layout.operation()``` 関数の引数に指定し、メニュー用クラスの ```bl_idname``` を引数にして ```self.layout.menu()``` を呼び出すことで、サブメニューを作成できる
* メニュー用クラスの ```draw()``` メソッド内でサブメニュー用に作成したクラスの ```bl_idname``` を ```self.layout.menu()``` 関数の引数に指定することで、3階層以上のメニューを作成することができる
