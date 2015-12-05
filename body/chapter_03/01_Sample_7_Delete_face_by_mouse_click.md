# 3-1. サンプル7: マウスの右クリックで面を削除する

アドオン開発に慣れてくると、よりインタラクティブ性の高い機能を提供するため、マウスやキーボードからのイベントを扱いたくなると思います。
例えば *3Dビュー* の *オブジェクトモード* で *S* キーを押した時に、マウスの移動でオブジェクトのサイズを変更する機能は、マウスからのイベントを扱っています。
本節ではアドオンでマウスやキーボードのイベントを扱う方法を、サンプル交えて紹介します。

## 作成するアドオンの仕様

* *3Dビュー* の *編集モード* 時に、マウスで *右クリック* したオブジェクトの面を削除する
* **プロパティパネル**（ *3Dビュー* 上で *N* キーを押した時に右側に表示されるパネル）から、処理の開始/終了を切り替える

## アドオンを作成する

以下のソースコードを、 [1.4節](../chapter_01/04_Install_own_Add-on.md)を参考にして **テキスト・エディタ** に入力し、
**sample_7.py** という名前で保存してください。

{% include "../../sample/src/chapter_03/sample_7.py" %}

## アドオンを実行する

### アドオンを有効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、作成したアドオンを有効化すると **コンソール** に以下の文字列が出力されます。

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

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、有効化したアドオンを無効化すると **コンソール** に以下の文字列が出力されます。

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
プロパティグループを削除しないと、アドオン無効化時にもプロパティグループのデータが残ることになるため、メモリを圧迫してしまいます。

```py:sample_7_part3
def unregister():
    del bpy.types.Scene.dfrc_props
# （略）
```

## まとめ



### ポイント

*
