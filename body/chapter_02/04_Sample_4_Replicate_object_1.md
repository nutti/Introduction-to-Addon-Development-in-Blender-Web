# 2-4. サンプル4: オブジェクトを複製する1

本節では2節連続で使ったサンプルを使うのをやめ、オブジェクトを複製する新たなサンプルアドオンを紹介します。
前節で取り扱った **ツール・シェルフ** によるアドオン制御をもう少し詳しく解説します。
本節で作成したアドオンは次節でも利用しますので、ここでしっかり理解しておきましょう。

## 作成するアドオンの仕様

* **3Dビュー** のメニュー **オブジェクト** に *選択オブジェクトの複製* を追加する
* 追加した *選択オブジェクトの複製* を実行すると、選択中のオブジェクトを複製する
* 複製したオブジェクトの配置先は、 **ツール・シェルフ** から *3Dカーソル* または *原点* 、3Dビュー上に配置されているオブジェクトから選択可能にする
* 複製したオブジェクトの拡大率・回転角度・配置場所からのオフセットを **ツール・シェルフ** から選択可能にする

## アドオンを作成する

以下のソースコードを、 [1.4節](../chapter_01/04_Install_own_Add-on.md)を参考にして **テキスト・エディタ** に入力し、
**sample_4.py** という名前で保存してください。

{% include "../../sample/src/chapter_02/sample_4.py" %}

## アドオンを実行する

### アドオンを有効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、作成したアドオンを有効化すると **コンソール** に以下の文字列が出力されます。

```sh
サンプル 4: アドオン「サンプル4」が有効化されました。
```

### アドオンの機能を使ってみる

アドオンを有効化したら、 *3Dビュー* のメニューに *オブジェクト* > *選択オブジェクトの複製* が追加されていることを確認します。
Blender起動直後に生成される *Cube* を選択し、追加されたメニューを実行してみましょう。
実行すると、*コンソール・ウィンドウ* に以下のメッセージが表示されて選択したCubeが複製されるはずです。

```sh
サンプル 4: 「Cube」を複製しました。
```

![オブジェクトの複製1](https://dl.dropboxusercontent.com/s/p2vi68nprlto5gc/use_add-on_1.png "オブジェクトの複製1")

*3Dビュー* の *ツール・シェルフ* からオプションをいろいろ変更してみましょう。
今回のサンプルでは、以下に示すオプションを変更可能です。

|オプション名|操作への影響|
|---|---|
|*配置位置*|*3Dカーソル* : 3Dカーソルの位置に複製オブジェクトを配置します <br> *原点* : 3Dビューの原点に複製オブジェクトを配置します <br> *オブジェクト名* : 選択したオブジェクトに複製オブジェクトを配置します|
|*拡大率*|複製したオブジェクトについて、複製元のオブジェクトに対する拡大率を設定します|
|*回転角度*|複製したオブジェクトについて、複製元オブジェクトからの回転角度の差分をオイラー角で設定します|
|*オフセット*|複製したオブジェクトについて、配置位置からのオフセット位置を指定します|

![オブジェクトの複製2](https://dl.dropboxusercontent.com/s/if9ztwmoc09nqt1/use_add-on_2.png "オブジェクトの複製2")

### アドオンを無効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、有効化したアドオンを無効化すると **コンソール** に以下の文字列が出力されます。

```sh
サンプル 4: アドオン「サンプル 4」が無効化されました。
```

## ソースコードの解説

今回作成したアドオンは、[2-3節](03_Sample_3_Scaling_object_2.md) の応用となります。
ここでは [2-3節](03_Sample_3_Scaling_object_2.md) にて解説できていなかった点について解説します。
なお、新しく登場したBlender APIについては、ソースコードのコメントに追加しています。

### EnumPropertyの選択項目を動的に追加

```EnumProperty``` を用いると、セレクトボックスによりユーザが値を選択することが可能なUIを作成することできます。
```EnumProperty``` を用いてセレクトボックスの選択項目を設定するためには、```EnumProperty``` クラス作成時に引数 ```items``` に選択項目のリストを渡す必要があります。
まず最初に、今回のサンプルで *3Dカーソル* と *原点* のみ追加するだけのコードを以下に示します。

```py:sample_4_part1_alt.py
location_list = [
    ('3D_CURSOR', "3Dカーソル", "3Dカーソル上に配置します"),
    ('ORIGIN', "原点", "原点に配置します")]

location = EnumProperty(
    name = "配置位置",
    description = "複製したオブジェクトの配置位置",
    items = location_list
)
```

リストに渡す要素は、以下の要素からなるタプルを渡します。

|||
|---|---|
|第1要素|識別子 <br> 項目が選択時に変数に設定される値|
|第2要素|セレクトボックスに表示される項目名|
|第3要素|セレクトボックスに表示される項目の説明|

ただしこれでセレクトボックスを作ることはできましたが、複製オブジェクトを3Dビュー上に配置されているオブジェクトへ配置することができません。
3Dビュー上に配置されているオブジェクトは、アドオンを実行した状況に応じて変化するからです。
例えば、*オブジェクト* > *選択オブジェクトの複製* 実行後に *オブジェクト* > *選択オブジェクトの複製* を再度実行した場合、最初に複製されたオブジェクトも配置先として選べる必要があります。

この問題に対し、紹介したサンプルでは以下のように ```EnumProperty``` により作ることのできるセレクトボックスの選択項目を動的に追加するようにしています。

```py:sample_4_part1.py
# EnumPropertyで表示したい項目リストを作成する関数
def location_list_fn(scene, context):
    items = [
        ('3D_CURSOR', "3Dカーソル", "3Dカーソル上に配置します"),
        ('ORIGIN', "原点", "原点に配置します")]
    items.extend([('OBJ_' + o.name, o.name, "オブジェクトに配置します") for o in bpy.data.objects])

    return items

# 選択したオブジェクトを複製するアドオン
class ReplicateObject(bpy.types.Operator):

    bl_idname = "object.replicate_object"
    bl_label = "選択オブジェクトの複製"
    bl_description = "選択中のオブジェクトを複製します"
    bl_options = {'REGISTER', 'UNDO'}

    location = EnumProperty(
        name = "配置位置",
        description = "複製したオブジェクトの配置位置",
        items = location_list_fn
    )
```

サンプルでは ```EnumProperty``` の ```items``` にリストの代わりに ```location_list_fn()``` 関数を渡しています。
```location_list_fn()``` は、3Dカーソルと原点についてセレクトボックスの選択項目リストを作成した後、 ```items.extend([('OBJ_' + o.name, o.name, "オブジェクトに配置します") for o in bpy.data.objects])``` により、3Dビュー上に置かれている全オブジェクトについてセレクトボックスの選択項目を作成し、リストに追加しています。
最後に ```location_list_fn()``` は作成したリストを返しています。
このように、セレクトボックス選択項目のリストを返す関数を ```EnumProperty``` の ```items``` に指定することで ```EnumProperty``` の選択項目を動的に追加することができます。

### FloatVectorPropertyの引数subtypeとunit

サンプルでは、配置位置の他にも拡大率・回転角度・配置位置からのオフセットを、ツール・シェルフから指定できるようになっています。
ソースコードでは ```FloatVectorProperty``` の ```subtype``` を指定することで、要素数等を指定することなく、目的に沿った浮動小数点型のプロパティグループを作成できます。
```subtype``` には、例えば以下のような値を指定可能です。

|値|値の説明|UI例|
|---|---|---|
|```NONE```|3要素から構成されるプロパティグループ|![オプション SUBTYPE NONE](https://dl.dropboxusercontent.com/s/2zcjq2iq5rrn85g/option_subtype_none.png "オプション SUBTYPE NONE")|
|```COLOR```|カラーパレット|![オプション SUBTYPE NONE](https://dl.dropboxusercontent.com/s/90sezitg7jsjhy8/option_subtype_color.png "オプション SUBTYPE COLOR")|
|```TRANSLATION```|X軸、Y軸、Z軸の3要素から構成されるプロパティグループ（単位はcm、mなど）|![オプション SUBTYPE TRANSLATION](https://dl.dropboxusercontent.com/s/a6fqhmw68vn6sqh/option_subtype_translation.png "オプション SUBTYPE TRANSLATION")|
|```VELOCITY```|X軸、Y軸、Z軸の3要素から構成されるプロパティグループ（単位はm/s）|![オプション SUBTYPE VELOCITY](https://dl.dropboxusercontent.com/s/mbb7er5ubn1no1f/option_subtype_velocity.png "オプション SUBTYPE VELOCITY")|
|```ACCELERATION```|X軸、Y軸、Z軸の3要素から構成されるプロパティグループ（単位はm/s<sup>2</sup>）|![オプション SUBTYPE ACCELERATION](https://dl.dropboxusercontent.com/s/pg3swy8nbk8p8ih/option_subtype_acceleration.png "オプション SUBTYPE ACCELERATION")|
|```EULER```|X軸、Y軸、Z軸の3要素から構成されるプロパティグループ（単位は°）|![オプション SUBTYPE EULER](https://dl.dropboxusercontent.com/s/r63sl5mv09v5f3h/option_subtype_euler.png "オプション SUBTYPE EULER")|
|```QUATERNION```|3要素（W、X、Y）から構成されるプロパティグループ|![オプション SUBTYPE QUATERNION](https://dl.dropboxusercontent.com/s/r82kz22g3eaba7h/option_subtype_quaternion.png "オプション SUBTYPE QUATERNION")|
|```AXISANGLE```|3要素（W、X、Y）から構成されるプロパティグループ（単位は°）|![オプション SUBTYPE AXISANGLE](https://dl.dropboxusercontent.com/s/5f8jn9423abkp5d/option_subtype_axisangle.png "オプション SUBTYPE AXISANGLE")|
|```XYZ```|X軸、Y軸、Z軸の3要素から構成されるプロパティグループ|![オプション SUBTYPE XYZ](https://dl.dropboxusercontent.com/s/p7rp8m1wiamr85n/option_subtype_xyz.png "オプション SUBTYPE XYZ")|

また ```unit``` を指定すると、以下のような単位をプロパティに表示させることができます。

|値|値の説明|UI上での表示単位（表示単位を度数表記・メートル法にした場合）|
|---|---|---|
|```NONE```||```subtype```に指定した値に応じて表示される単位が決定|
|```LENGTH```|長さ|cm|
|```AREA```|面積|cm<sup>2</sup>、m<sup>2</sup>など|
|```VOLUME```|長さ|cm<sup>3</sup>、m<sup>3</sup>など|
|```ROTATION```|角度|°|
|```TIME```|時間|（単位なし）|
|```VELOCITY```|速度|m/s|
|```ACCELERATION```|加速度|m/s<sup>2</sup>|

## まとめ

[2-3節](03_Sample_3_Scaling_object_2.md) で紹介したツール・シェルフのプロパティを用いて、やや複雑なアドオンを作成してみました。
ツール・シェルフのプロパティを用いることで、機能に対してユーザがより細かい指示を出せることが理解できたのではないでしょうか。
ただ特定の機能に対してプロパティを追加しすぎると、指示できる項目が多すぎてかえってわかりづらくなるという問題もありますので、本当に必要な項目であるかを意識しながらプロパティを追加していきましょう。

### ポイント

* ```EnumProperty``` の ```items``` に選択項目リストを返す関数を指定することで、セレクトボックスの選択項目を動的に追加できる
* 〜Propertyクラス作成時に、 ```subtype``` を指定することで、目的に沿ったプロパティを簡単に作成できる
* 〜Propertyクラス作成時に、 ```unit``` を指定することで、プロパティに単位を表示することができる
