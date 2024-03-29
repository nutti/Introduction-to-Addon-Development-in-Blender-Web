---
pagetitle: 3-4. OpenGLにアクセスするAPIを利用する
subtitle: 3-4. OpenGLにアクセスするAPIを利用する
---


[2-9節](../chapter_02/09_Control_Blender_UI_2.html) では、Blenderが提供するフレームワークの中で、ボタンやメニューなどのUIを構築する方法を説明しました。
しかし、アドオンの機能によっては、独自のUIを構築したほうがよい場合があります。
例えば、押したキーボードのキーやマウスのボタンを表示するアドオン「Screencast Key Status」は独自のUIを構築しているアドオンの1つです。
押したキーボードのキーなどをメニューなどに表示しても見づらいため、Blenderが提供しているOpenGLにアクセスするAPIを使って、わかりやすいUIを構築しています。


# OpenGLとは？

3DCGに何かしら関わっている方であれば知らない人はいないと思いますが、OpenGL向けのAPIの使い方を説明する前にOpenGLについて簡単に説明します。

OpenGLはOpen Graphic Libraryの略で、2D/3DグラフィックAPIの1つです。
OpenGLを利用することで、画像や3Dモデルを比較的簡単に表示することができます。
近年ではゲームエンジンや3DCGツールの発展に伴い、OpenGLを直接触ることはほとんどなくなりましたが、これらのツールの内部でも最終的にOpenGLを使って画像や3Dモデルを表示しているなど、OpenGLはなくてはならないライブラリとなっています。

2D/3D向けグラフィックAPIはOpenGLの他にもDirectXがあり、OpenGLとDirectXとで以下の違いがあります。

|　|DirectX|OpenGL|
|---|---|---|
|開発元|Microsoft|シリコングラフィクス|
|主な用途|ゲームの描画|3DCGソフト、CADソフト|
|レンダリング精度|OpenGLに比べて低精度|精度が求められるCADソフトで利用されるため高精度|
|レンダリング速度|高い応答性が求められるゲームで利用されるため高速|DirectXに比べて低速|
|動作環境|Windows, XBox|Windows, Mac, Linux, iOS, Android, Webアプリなど|

上記の比較からもわかるように、Blenderが3DCGソフトであることと複数のOSでの動作をサポートすることから、BlenderはOpenGLをグラフィックスAPIとして採用しています。

BlenderはPythonからOpenGLへアクセスするためのAPIも用意しているため、ユーザはPythonスクリプトからOpenGLの機能の一部を使うことができます。
本節では、Blenderが提供しているこのAPIを利用し、図形を描画する方法を説明します。


# 作成するアドオンの仕様

OpenGLを使った図形の描画方法を理解するため、次のような機能を持つアドオンを作成します。

* [3Dビュー] エリアに図形を表示
* 表示する図形は、[3Dビュー] エリアのプロパティパネルから選択
  * 表示可能な図形は三角形と四角形


## アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして以下のソースコードを入力し、ファイル名 `sample_3_4.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3_4.py"]


# アドオンを使用する

## アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル3-4: アドオン「サンプル3-4」が有効化されました。
```

プロパティパネルを表示し、項目 [図形を表示] が追加されていることを確認します。

![](../../images/chapter_03/04_Use_API_for_OpenGL/enable_addon.png "図の表示 有効化")


## アドオンの機能を使用する

有効化したアドオンの機能を使い、動作を確認します。


<div class="work"></div>

|||
|---|---|
|1|プロパティパネルの項目 [図形を表示] に配置されている [開始] ボタンをクリックします。<br>![](../../images/chapter_03/04_Use_API_for_OpenGL/use_addon_1.png "図の表示 手順1")|
|2|[3Dビュー] エリア上に三角形が表示されます。また、プロパティパネルには表示する図形と図形の頂点の座標を変更するためのUIが表示されます。<br>![](../../images/chapter_03/04_Use_API_for_OpenGL/use_addon_2.png "図の表示 手順2")|
|3|2で表示されたプロパティから頂点の座標値を変更すると、[3Dビュー] エリア上に表示されている三角形が、頂点の座標値の変更に合わせて変形します。<br>![](../../images/chapter_03/04_Use_API_for_OpenGL/use_addon_3.png "図の表示 手順3")|
|4|[図形] を [三角形] から [四角形] へ変更すると、プロパティパネルで4つの頂点座標値を編集できるようになり、[3Dビュー] エリア上に表示されている図形も四角形に変更されます。<br>![](../../images/chapter_03/04_Use_API_for_OpenGL/use_addon_4.png "図の表示 手順4")|
|5|プロパティパネルの項目 [図形を表示] に配置されている [終了] ボタンをクリックすると、図形が描画されなくなります。<br>![図の表示 手順5](../../images/chapter_03/04_Use_API_for_OpenGL/use_addon_5.png "図の表示 手順5")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```
サンプル3-4: アドオン「サンプル3-4」が無効化されました。
```


# ソースコードの解説

本節では、Blenderが提供するOpenGLへアクセスするためのAPIを利用する方法を中心に説明します。
これまで説明してきた内容ついては、説明を省いています。
サンプルのソースコードに関して、ポイントとなる点を次に示します。

* OpenGLへアクセスするためのAPIを利用する方法
* 図形描画関数の登録
* APIを利用した図形描画


## OpenGLへアクセスするためのAPIを利用する

本節のサンプルでは図形を描画するために、OpenGLへアクセスするためのAPIを利用します。

OpenGLへアクセスするためのAPIをアドオンから利用するためには、`bgl` とよばれるモジュールをインポートする必要があります。

[@include-source pattern="partial" filepath="chapter_03/sample_3_4.py" block="import_bgl", unindent="True"]


## アドオン内で利用するプロパティを定義する

複数のクラス間で共有するプロパティの一覧を次に示します。
本節のサンプルでは、プロパティパネルにプロパティを追加するため、`bpy.types.PropertyGroup` によるプロパティのグループ化は行っていません。

|変数|意味|
|---|---|
|`rf_running`|図形描画中は、`True`|
|`rf_figure`|表示する図形<br>三角形（`TRIANGE`）か四角形（`RECTANGLE`）のいずれかの値|
|`rf_vert_1`|頂点1の座標（2次元）|
|`rf_vert_2`|頂点2の座標（2次元）|
|`rf_vert_3`|頂点3の座標（2次元）|
|`rf_vert_4`|頂点4の座標（2次元）、四角形を表示する場合のみ利用可能|


## 図形を描画する関数を登録する

インポートした `bgl` モジュールを使うことで図形を描画することができますが、単純に `bgl` モジュールの関数を呼び出しただけでは、図形を表示することはできません。
図形を描画するためには、図形を描画する関数を登録し、登録した関数内で `bgl` モジュールの関数を呼び出す必要があります。

本節のサンプルでは、[3Dビュー] エリア上で図形を描画する関数を登録する処理を `__handle_add` メソッドに定義し、`invoke` メソッドの [開始] ボタンが押されたときに呼び出します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_4.py" block="handle_add", unindent="True"]


描画関数の登録はエリア単位で行い、例えば [3Dビュー] エリアに描画関数を登録したい場合は `bpy.types.SpaceView3D.draw_handler_add` 関数を使って登録します。
ここで、`bpy.types.SpaceView3D` は [3Dビュー] エリアを描画対象とした場合のスペース情報ですが、描画先のエリアによってこの部分の記述が変わります。
描画先のエリアの候補一覧を次に示します。
なお、同じスペースがウィンドウ内に複数存在した場合は、当該スペース全てに描画されます。

|クラス|意味|
|---|---|
|`SpaceConsole`|[Pythonコンソール] エリアのスペース情報|
|`SpaceFileBrowser`|[ファイルブラウザー] エリアのスペース情報|
|`SpaceInfo`|[情報] エリアのスペース情報|
|`SpaceUserPreferences`|[ユーザ設定] エリアのスペース情報|
|`SpaceOutliner`|[アウトライナー] エリアのスペース情報|
|`SpaceProperties`|[プロパティ] エリアのスペース情報|
|`SpaceLogicEditor`|[ロジックエディター] エリアのスペース情報|
|`SpaceNodeEditor`|[ノードエディター] エリアのスペース情報|
|`SpaceTextEditor`|[テキストエディター] エリアのスペース情報|
|`SpaceClipEditor`|[動画クリップエディター] エリアのスペース情報|
|`SpaceSequenceEditor`|[ビデオシーケンスエディター] エリアのスペース情報|
|`SpaceImageEditor`|[UV/画像エディター] エリアのスペース情報|
|`SpaceNLA`|[NLAエディター] エリアのスペース情報|
|`SpaceDopeSheetEditor`|[ドープシート] エリアのスペース情報|
|`SpaceGraphEditor`|[グラフエディター] エリアのスペース情報|
|`SpaceTimeline`|[タイムライン] エリアのスペース情報|
|`SpaceView3D`|[3Dビュー] エリアのスペース情報|


`bpy.types.SpaceView3D.draw_handler_add` 関数の引数には、次に示す引数を指定します。

|引数|意味|
|---|---|
|第1引数|描画関数（描画関数は関数、またはスタティックメソッド）|
|第2引数|描画関数で受け取る引数（タプル型）|
|第3引数|描画先のリージョン|
|第4引数|描画モード（深度バッファの扱いを指定、基本は `POST_PIXEL` でよい）|

本節のサンプルでは、`RenderFigure.__render` スタティックメソッドを描画関数、`WINDOW` を描画先のリージョンとして、第1引数に `RenderFigure.__render` 、第3引数に `WINDOW` を指定します。
第2引数にはコンテキスト情報を渡し、描画関数内でこれらの値を利用します。

<div class="column">
第2引数に `(context, )` を渡しているところに違和感があるかもしれません。
単純に考えると、ここにはcontextのみを渡せばよさそうです。
しかし、実際に試した読者はわかると思いますが、仮にここで第2引数に `context` を指定すると「Contextではなくタプル型の値を指定する必要があります」というエラーメッセージが表示されて、エラー終了してしまいます。
このため、サンプルではタプル型であることを明示するために `(context, )` を指定しています。
なお、要素が1つの場合にタプル型であることを認識させるためには、要素の後にカンマ（,）を追加することに注意してください。
`(context)` のようにカンマがないと、`context` と同じであると判断されてしまいます。
</div>

`bpy.types.SpaceView3D.draw_handler_add` 関数は、戻り値としてハンドルを返します。
ハンドルはクラス変数 `RenderFigure.__handle` に保存し、描画関数の登録解除時に利用します。
ここで、`RenderFigure.__handle` はクラス変数でなければ正しく動作しないことに注意が必要です。

<div class="column">
登録した描画関数は、描画先のリージョンが更新された時に呼ばれます。
従って、[開始] ボタンをクリックしたあとに何かしらの更新処理（オブジェクトの移動など）を行わないと描画関数が呼ばれないため、ボタンを押した直後は表示されません。
この問題を解決するため、本節のサンプルでは [開始] ボタンや [終了] ボタンをクリックしたときに描画先のリージョンを更新するよう、`context.area.tag_redraw` 関数を実行しています。
</div>


## 図形を描画する関数を作成する

図形を描画するスタティックメソッド `RenderFigure.__render` を作成します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_4.py" block="render", unindent="True"]

OpenGLのプログラミングに慣れている方は、`RenderFigure.__render` スタティックメソッド内の図形描画処理を見て既視感を感じるのではないでしょうか？
なぜなら、`bgl` が提供するAPIはOpenGLが提供する関数とほぼ同一で、かつ描画手順もほぼ一緒になるようにユーザへAPIを提供しているからです。
このため、以降の説明はOpenGLを使ったことがある方ならばすでに知っている内容かもしれません。

`RenderFigure.__render` スタティックメソッドは、最初に `bgl.glEnable(bgl.GL_BLEND)` を呼び出すことで半透明処理を有効化します。
`bgl.glEnable` 関数は、引数に指定した描画処理を有効化します。
ここでは、半透明処理を有効化するために `bgl.GL_BLEND` を指定します。
この処理がないと透過が無効な状態で図形が描画されるため、期待した結果になりません。

続いて表示する図形の判定を行った後、`bgl.glBegin` 関数により図形の描画を開始します。
`bgl.glBegin` 関数の引数には描画モードを指定します。
`bgl.GL_TRIANGLES` を指定することで三角形の描画を、`bgl.GL_QUADS` を指定することで四角形の描画を開始します。

次に、`bgl.glColor4f` 関数を呼び出して図形の色を指定します。
引数は順に赤(R)、緑(G)、青(B)、アルファ値(A)となります。
今回はやや半透明の白色を描画色として設定しました。
そして `bgl.glVertex2f` 関数を呼び出して図形の頂点の座標値を設定した後に、`bgl.glEnd` 関数を呼び出すことで描画が完了します。

`bgl.glVertex2f` 関数の引数に、X座標、Y座標の順で浮動小数点値で座標値を指定します。
`bgl.glVertex2f` 関数を呼び出した回数だけ、頂点が指定されます。
三角形の場合は3つの頂点を指定するため3回 `bgl.glVertex2f` 関数を呼び、四角形の場合は4つの頂点を指定するため4回 `bgl.glVertex2f` 関数を呼びます。
座標値は、リージョンの左下が (x, y) = (0, 0) となることに注意が必要です。

![](../../images/chapter_03/04_Use_API_for_OpenGL/region_coordinate.png "リージョン座標")

最後に `bgl.glDisable(bgl.GL_BLEND)` 関数を呼び出し、`bgl.glBegin` 関数で有効化したOpenGLの設定を無効化する必要があります。
OpenGLの設定を無効化しないまま描画関数を終えてしまうと、OpenGLの設定がすべてのBlenderのUIに対して適用されてしまいます。
`bgl.GL_BLEND` 以外の他のOpenGLの設定についても同様ですので、覚えておいてください。


## 図形を描画する関数を登録解除する

`bpy.types.SpaceView3D.draw_handler_add` 関数を使って登録した図形を描画する関数は、登録を解除するまで呼ばれ続けます。
このため、不要になった時（本節のサンプルでは、[終了] ボタンが押された時）に登録を解除する必要があります。
図形描画関数を登録解除する処理を次に示します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_4.py" block="handle_remove", unindent="True"]


描画関数の登録解除は、クラス変数 `RenderFigure.__handle` にハンドルが登録したことを確認した後に `bpy.types.SpaceView3D.draw_handler_remove` 関数を呼び出して行います。
`bpy.types.SpaceView3D.draw_handler_remove` 関数に指定する引数を次に示します。
描画関数の登録時に使用した `bpy.types.SpaceView3D.draw_handler_add` 関数と同様、`SpaceView3D` は描画関数を登録解除するエリアによって記述を変える必要があります。

|引数|意味|
|---|---|
|第1引数|ハンドル（`draw_handler_add` 関数の戻り値）|
|第2引数|描画するリージョン|

本節のサンプルでは、クラス変数 `RenderFigure.__handle` にハンドルが保存されているため、クラス変数 `RenderFigure.__handle` を第1引数に指定します。
第2引数は、描画を解除するリージョンを指定しますが、本節のサンプルでは `bpy.types.SpaceView3D.draw_handler_add` 関数の第3引数に指定したリージョン `WINDOW` を指定します。

これで描画関数の登録が解除されました。
解除後には、クラス変数 `RenderFigure.__handle` に `None` を代入してハンドルが無効であることを明示します。
描画関数登録/解除時に、クラス変数 `RenderFigure.__handle` が `None` であるかを確認している部分を含め、本来はこの処理自体不要なものですが、登録解除後の不正なハンドルを利用してしまった場合にBlender内部で異常な状態になることを防ぐため、処理を追加しています。


## UIを構築する

最後に、本アドオンのUIを構築します。

[@include-source pattern="partial" filepath="chapter_03/sample_3_4.py" block="panel_class", unindent="True"]


[3-1節](01_Handle_Mouse_Click_Event.html) と同様、`bpy.types.Panel` を継承したパネルクラスの `draw` メソッドに処理を記述してUIを構築します。

最初に描画中か否かの判定を行ったあと、描画中であれば [終了] ボタンを、描画中でなければ [開始] ボタンを配置します。

図形描画中（`sc.rf_running` が `True`）のときは、図形描画関数の登録を解除して描画を停止するための [終了] ボタンを表示します。
図形描画中は、描画する図形の種類や頂点の座標値をユーザが指定できるようにするため、`layout.prop` 関数を用いてUIパーツを配置します。
`layout.prop` 関数の詳細については、[2-9節](../chapter_02/09_Control_Blender_UI_2.html) を参照してください。
四角形を描画する場合、ユーザが4つの頂点の座標値を指定できる必要があるため、描画する図形が四角形に選択されている場合は三角形が選択されていた場合のUIパーツに加えて、4つ目の頂点の座標値を指定するUIパーツを配置します。

図形描画中でない時（`sc.rf_running` が `False`）のときは、図形描画関数を登録して描画を開始するための [開始] ボタンのみを表示し、描画する図形の種類や頂点の座標値を指定するためのUIパーツは配置しません。


# まとめ

PythonからOpenGLへアクセスするためのAPIを提供する `bgl` モジュールを使って、[3Dビュー] エリアで図形を描画するための方法を説明しました。

本節で紹介した `bgl` モジュールと、[3-1節](01_Handle_Mouse_Click_Event.html) と [3-2節](02_Handle_Keyboard_Key_Event.html) で説明したユーザからのイベントを扱う処理を組み合わせることで、Blenderの枠組みで実現可能なUIとは全く異なる、独自のUIを構築することができます。

なお、`bgl` モジュールを使うとOpenGLのAPIを間接的に利用することができますが、`bgl` モジュールは全てのOpenGLのAPIについて対応していません。
このため、`bgl` モジュールを利用する場合は、[4-1節](../chapter_04/01_Research_official_Blender_API_for_Add-on.html) で説明する方法で、Blenderが提供するAPIを確認する必要があります。


## ポイント


* OpenGLのAPIを利用するためには、`bgl` モジュールをインポートする必要がある
* `bgl` モジュールを用いて、アドオン内でOpenGLを用いて描画するためには、`bpy.types.XXX.draw_handler_add` （XXX：描画するエリアにより変わる）関数を用いて、描画処理を行う関数、またはスタティックメソッドを登録する必要がある
* 登録した描画処理を行う関数、またはスタティックメソッドは、必要がなくなった時に `bpy.types.XXX.draw_handler_remove` 関数を用いて登録を解除する必要がある
* `bgl` モジュールは、オリジナルのOpenGLの使い方と似たような方法で、OpenGLの機能を間接的に利用するための手段を提供する
* `bgl` モジュールは、OpenGLが提供するAPIをすべてサポートしているわけではない。事前に使いたいAPIが用意されているか、確認する必要がある
* `bgl.glEnable` 関数により有効化したOpenGLの設定は、描画関数の処理が終わる前に `bgl.glDisable` を使って無効化する必要がある
