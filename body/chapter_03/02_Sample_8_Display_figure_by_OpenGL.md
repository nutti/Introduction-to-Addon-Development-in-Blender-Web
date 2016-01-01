# 3-2. サンプル8: OpenGL向けのAPIを利用して図形を表示する

これまでにボタンやメニューなどのBlenderの決まったフレームワークの中で、UIを構築する方法を紹介しました。しかし、アドオンの機能によっては独自のUIを構築したいと考える方もいると思います。
独自のUIを構築したい人のため、Blenderは **OpenGL (Open Graphic Library)** へアクセスするためのAPIを提供しています。3DCGに何かしら関わっている方にとってはご存知の方も多いと思いますが、OpenGLとは2D/3DCG向けのグラフィックAPIのことを指します。
本節では、Blenderが提供しているOpenGL向けのAPIを利用し、 *3Dビュー* 上に図形を表示するサンプルを紹介します。

## 作成するアドオンの仕様

* *3Dビュー* に図形を表示する
* 表示する図形は、 *プロパティパネル* から選択できるようにする

## アドオンを作成する

以下のソースコードを、 [1.4節](../chapter_01/04_Install_own_Add-on.md)を参考にして *テキスト・エディタ* に入力し、```sample_8.py``` という名前で保存してください。

{% include "../../sample/src/chapter_03/sample_8.py" %}

## アドオンを実行する

### アドオンを有効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、作成したアドオンを有効化すると *コンソール* に以下の文字列が出力されます。

```sh
サンプル 8: アドオン「サンプル8」が有効化されました。
```

### アドオンを使ってみる

アドオンを有効化すると、 *3Dビュー* の *プロパティパネル* に開始ボタンが表示されます。

![図の表示 手順1](https://dl.dropboxusercontent.com/s/uf0xneikowb5ozz/use_addon_1.png "図の表示 手順1")

開始ボタンをクリックすると、 *3Dビュー* 上に三角形が表示されます。
また *プロパティパネル* には、表示する図形と図形の頂点を変更するためのUIが表示されます。

![図の表示 手順2](https://dl.dropboxusercontent.com/s/056sg7b9x96mdjf/use_addon_2.png "図の表示 手順2")

三角形の頂点を変更してみましょう。
*3Dビュー* 上に表示されている三角形が頂点の変更に合わせて変形することがわかります。

![図の表示 手順3](https://dl.dropboxusercontent.com/s/vlua7b5aiptcc4m/use_addon_3.png "図の表示 手順3")

次に、表示する図形を三角形から四角形へ変更してみましょう。
表示する図形を四角形へ変更すると4つの頂点を編集できるようになり、変更と同時に *3Dビュー* 上に表示されている図形も変更されます。

![図の表示 手順4](https://dl.dropboxusercontent.com/s/1wr0l6uddp64emk/use_addon_4.png "図の表示 手順4")

### アドオンを無効化する

[1.4節](../chapter_01/04_Install_own_Add-on.md)を参考に、有効化したアドオンを無効化すると *コンソール* に以下の文字列が出力されます。

```sh
サンプル 8: アドオン「サンプル 8」が無効化されました。
```

## ソースコードの解説

### OpenGLへアクセスするためのAPIを利用する

今回のサンプルでは、Blenderが提供するOpenGL向けのAPIを利用しています。
OpenGLへアクセスするAPIをアドオンから利用するためには、 ```bgl``` モジュールをインポートする必要があります。

```py:sample_8_part1.py
import bgl
```

### アドオンで利用するプロパティを定義する

[4.1節](01_Sample_7_Delete_face_by_mouse_click.md)でも説明しましたが、今回もクラス間で以下のようなデータを共有します。

|変数|意味|
|---|---|
|```rf_running```|実行中の場合は ```True```|
|```rf_figure```|表示する図形（三角形、四角形）|
|```rf_vert_1```|頂点1の座標（2次元）|
|```rf_vert_2```|頂点2の座標（2次元）|
|```rf_vert_3```|頂点3の座標（2次元）|
|```rf_vert_4```|頂点4の座標（2次元）、四角形表示時のみに利用|

```py:sample_8_part2.py
sc = bpy.types.Scene
sc.rf_running = BoolProperty(
    name = "実行中",
    description = "実行中か？",
    default = False
)
sc.rf_figure = EnumProperty(
    name = "図形",
    description = "表示する図形",
    items = [
        ('TRIANGLE', "三角形", "三角形を表示します"),
        ('RECTANGLE', "四角形", "四角形を表示します")]
)
sc.rf_vert_1 = FloatVectorProperty(
    name = "頂点1",
    description = "図形の頂点",
    size = 2,
    default = (50.0, 50.0)
)
sc.rf_vert_2 = FloatVectorProperty(
    name = "頂点2",
    description = "図形の頂点",
    size = 2,
    default = (50.0, 100.0)
)
sc.rf_vert_3 = FloatVectorProperty(
    name = "頂点3",
    description = "図形の頂点",
    size = 2,
    default = (100.0, 100.0)
)
sc.rf_vert_4 = FloatVectorProperty(
    name = "頂点4",
    description = "図形の頂点",
    size = 2,
    default = (100.0, 50.0)
)
```

定義したプロパティは、アドオン無効化時に削除するようにします。

```py:sample_8_part3.py
sc = bpy.types.Scene
del sc.rf_running
del sc.rf_figure
del sc.rf_vert_1
del sc.rf_vert_2
del sc.rf_vert_3
del sc.rf_vert_4
```

### 図形を描画する関数を登録する

*3Dビュー* 上で図形を描画する関数を登録するための静的メソッド ```RenderFigure.handle_add()``` を作成します。
```RenderFigure.handle_add()``` は静的メソッドとして作成する必要があるため、でコレータ ```@staticmethod``` をメソッド定義の前につける必要があります。

```py:sample_8_part4.py
# 画像描画関数を登録
@staticmethod
def handle_add(self, context):
    if RenderFigure.__handle is None:
        RenderFigure.__handle = bpy.types.SpaceView3D.draw_handler_add(
            RenderFigure.render,
            (self, context), 'WINDOW', 'POST_PIXEL')
```

描画関数の登録は ```bpy.types.SpaceView3D.draw_handler_add()``` 関数で行います。
ここで、 ```SpaceView3D``` は描画する *エリア* により変わります。
関数の引数に指定する値は以下の通りです。

|引数|意味|
|---|---|
|第1引数|描画関数（描画関数は静的メソッド、または通常の関数）|
|第2引数|描画関数に渡す引数リスト|
|第3引数|描画する *リージョン*|
|第4引数|描画モード（深度バッファの扱いを指定、基本は ```POST_PIXEL```）|

今回のサンプルでは描画する静的メソッドを ```RenderFigure.render``` 、描画する *リージョン* を ```WINDOW``` に指定しています。
描画関数に渡す引数は、自身のクラスインスタンスと実行時コンテキストを渡しています。

戻り値としてハンドルが返ってくるため、登録解除時に利用するために返ってきたハンドルを保存しておきます。

### 図形を描画する関数を作成する

図形を描画する静的メソッド ```RenderFigure.render``` を作成します。

```py:sample_8_part5.py
@staticmethod
def render(self, context):
    sc = context.scene

    # OpenGLの設定
    bgl.glEnable(bgl.GL_BLEND)

    # 図形を表示
    if sc.rf_figure == 'TRIANGLE':
        bgl.glBegin(bgl.GL_TRIANGLES)
        bgl.glColor4f(1.0, 1.0, 1.0, 0.7)
        bgl.glVertex2f(sc.rf_vert_1[0], sc.rf_vert_1[1])
        bgl.glVertex2f(sc.rf_vert_2[0], sc.rf_vert_2[1])
        bgl.glVertex2f(sc.rf_vert_3[0], sc.rf_vert_3[1])
        bgl.glEnd()
    elif sc.rf_figure == 'RECTANGLE':
        bgl.glBegin(bgl.GL_QUADS)
        bgl.glColor4f(1.0, 1.0, 1.0, 0.7)
        bgl.glVertex2f(sc.rf_vert_1[0], sc.rf_vert_1[1])
        bgl.glVertex2f(sc.rf_vert_2[0], sc.rf_vert_2[1])
        bgl.glVertex2f(sc.rf_vert_3[0], sc.rf_vert_3[1])
        bgl.glVertex2f(sc.rf_vert_4[0], sc.rf_vert_4[1])
        bgl.glEnd()
```

プロパティを取得した後は、基本的にOpenGLを用いた描画手順に沿うことで図形を表示します。

最初にOpenGLの設定として、 ```bgl.glEnable(bgl.GL_BLEND)``` により半透明処理を有効化します。
この処理がないと図形描画時に透過が無効になり、期待した結果にならないでしょう。

続いて表示する図形の判定を行った後、 ```bgl.glBegin()``` 関数により図形描画を開始します。
引数には描画モードを指定します。
```bgl.GL_TRIANGLES``` を指定することで三角形を、 ```bgl.GL_QUADS``` を指定することで四角形の描画を開始します。

次に ```bgl.glColor4f()``` 関数により図形の色を指定しています。
引数は順に、赤(R)、緑(G)、青(B)、アルファ値(A)となります。
今回はやや半透明の白色の設定とした。

最後に ```bgl.glVertex2f()``` 関数により、図形の頂点を設定した後に ```bgl.glEnd()``` 関数により描画を完了します。
```bgl.glVertex2f()``` 関数の引数には、X座標、Y座標の順で浮動小数点値で指定します。
三角形の場合は3つの頂点を指定すればよいため3回 ```bgl.glVertex2f()``` を呼び、四角形の場合は4つの頂点を指定するため4回 ```bgl.glVertex2f()``` を呼びます。

### 図形を描画する関数を登録解除する

登録した図形を描画する関数はアドオン無効化時に登録解除する必要があります。

```py:sample_8_part6.py
@staticmethod
def handle_remove(self, context):
    if RenderFigure.__handle is not None:
        bpy.types.SpaceView3D.draw_handler_remove(
            RenderFigure.__handle, 'WINDOW')
        RenderFigure.__handle = None
```

描画関数の登録解除は、 ```bpy.types.SpaceView3D.draw_handler_remove()``` 関数で行います。
描画関数の登録時に使用した ```bpy.types.SpaceView3D.draw_handler_add()``` 関数と同様、 ```SpaceView3D``` は対象の *エリア* を指定します。
関数の引数は以下の通りです。

|引数|意味|
|---|---|
|第1引数|ハンドル（```draw_handler_add()``` の戻り値）|
|第2引数|描画する *リージョン*|

### UIを構築する

最後に本アドオンのUIを構築しましょう。

```py:sample_8_part7.py
class OBJECT_PT_RF(bpy.types.Panel):
    bl_label = "図形を表示"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        sc = context.scene
        layout = self.layout
        if context.area:
            context.area.tag_redraw()
        if sc.rf_running is True:
            layout.operator(RenderingButton.bl_idname, text="Stop", icon="PAUSE")
            layout.prop(sc, "rf_figure", "図形")
            layout.prop(sc, "rf_vert_1", "頂点1")
            layout.prop(sc, "rf_vert_2", "頂点2")
            layout.prop(sc, "rf_vert_3", "頂点3")
            if sc.rf_figure == 'RECTANGLE':
                layout.prop(sc, "rf_vert_4", "頂点4")
        elif sc.rf_running is False:
            layout.operator(RenderingButton.bl_idname, text="Start", icon="PLAY")
```

[3.1節](01_Sample_7_Delete_face_by_mouse_click.md)と同様、 ```bpy.types.Panel``` を継承したクラスの中でUIを構築していきます。

最初に描画中か否かの判定を行った後、描画中であればStopボタンを、そうでない場合はStartボタンを配置しています。
また、描画中であれば描画する図形や頂点の座標を指定できるようにするため、 ```layout.prop()``` 関数を用いてこれらのUIパーツを配置しています。
```layout.prop()``` の引数を以下に示します。

|引数|意味|
|---|---|
|第1引数|プロパティを持つオブジェクト|
|第2引数|プロパティ変数名|
|第3引数|表示文字列|

今回は ```bpy.types.Scene``` にプロパティを登録しているため、 ```context.scene``` を第1引数にしています。
第2引数には、 ```bpy.types.Scene``` に登録したプロパティ変数名を文字列で指定しています。

四角形を描画する場合は4つの頂点を指定可能とするため、描画する図形が四角形である場合に4つ目の頂点を指定するUIパーツを配置するようにします。


## まとめ


### ポイント

* Blenderが提供している、OpenGLへアクセスするためのAPIをアドオンから利用するためには、 ```bgl``` モジュールをインポートする必要がある
