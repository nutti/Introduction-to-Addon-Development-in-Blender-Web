---
pagetitle: 3-4. gpuモジュールを使って図形描画する
subtitle: 3-4. gpuモジュールを使って図形描画する
---


[2-7節](../chapter_02/07_Control_Blender_UI.html) では、Blenderが提供するフレームワークの中で、ボタンやメニューなどのUIを構築する方法を説明しました。
しかし、アドオンの機能によっては、独自のUIを構築したほうがよい場合があります。
例えば、押したキーボードのキーやマウスのボタンを表示するアドオン『Screencast Keys』は、独自のUIを構築しているアドオンの1つです。
押したキーボードのキーをメニューなどに表示しても見づらいため、Blenderが提供している描画APIを使って、よりよいUIを構築しています。


# 作成するアドオンの仕様

本節のサンプルアドオンは、次のような機能を備えています。

* *[3Dビューポート]* スペースのSidebarに、パネル *[サンプル 3-4]* > *[星型の図形を表示]* を配置し、そのパネルに星型の図形を表示するためのボタンを配置する
* 同パネルから、星型図形の中心座標とサイズを変更できる


## アドオンを作成する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして次に示すソースコードを入力し、ファイル名 `sample_3-4.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3-4.py"]


# アドオンを使用する

## アドオンを有効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに次に示す文字列が出力されます。

```
サンプル 3-4: アドオン『サンプル 3-4』が有効化されました。
```

Sidebarを表示し、パネル *[サンプル 3-4]* > *[星型の図形を表示]* が追加されていることを確認します。

![](../../images/chapter_03/04_Draw_Figures/enable_addon.png "サンプルアドオン3-4 有効化")


## アドオンの機能を使用する

有効化したアドオンの機能を使い、動作を確認します。


<div class="work"></div>

|||
|---|---|
|1|*[3Dビューポート]* スペースのSidebarから、パネル *[サンプル 3-4]* > *[星型の図形を表示]* に配置されている *[開始]* ボタンをクリックします。<br>![](../../images/chapter_03/04_Draw_Figures/use_addon_1.png "サンプルアドオン3-4 手順1")|
|2|*[3Dビューポート]* スペース上に三角形が表示されます。また、パネルには表示する図形の中心座標とサイズを変更するためのUIが表示されます。<br>![](../../images/chapter_03/04_Draw_Figures/use_addon_2.png "サンプルアドオン3-4 手順2")|
|3|図形の中心座標やサイズを変更すると、*[3Dビューポート]* スペース上に表示されている三角形も変形されます。<br>![](../../images/chapter_03/04_Draw_Figures/use_addon_3.png "サンプルアドオン3-4 手順3")|
|4|パネル *[サンプル 3-4]* > *[星型の図形を表示]* に配置されている *[終了]* ボタンをクリックすると、図形が描画されなくなります。<br>![](../../images/chapter_03/04_Draw_Figures/use_addon_4.png "サンプルアドオン3-4 手順4")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして有効化したアドオンを無効化すると、コンソールウィンドウに次の文字列が出力されます。

```
サンプル 3-4: アドオン『サンプル 3-4』が無効化されました。
```


# ソースコードの解説

本節では、Blenderが提供する図形描画のためのAPIについて説明します。


## 図形描画に必要なgpuモジュールのインポート

本節のサンプルアドオンは、図形を描画するために、gpuモジュールで提供されるAPIを利用しています。
このため、gpuモジュールをインポートする必要があります。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="import_gpu", unindent="True"]


## アドオン内で利用するプロパティクラスの変数を定義する

本節のサンプルアドオンでは、複数のクラス間（`SAMPLE34_OT_DrawStar` と `SAMPLE34_PT_DrawStar`）で、プロパティクラスの変数を共有しています。
共有するプロパティクラスの変数を、次に示します。

|変数|意味|
|---|---|
|`sample34_center`|星の中心座標|
|`sample34_size`|星の大きさ|

プロパティクラスの変数は、それぞれ `bpy.types.Scene` のメンバ変数として定義します。
以降、各変数には `bpy.types.Scene` を通してアクセスできます。
例えば、プロパティ `sample34_center` にアクセスする場合は、`bpy.types.Scene.sample34_center` とします。
プロパティクラスの変数は、`register` 関数で呼ばれる `init_props` 関数で作成し、`unregister` 関数で呼ばれる `clear_props` 関数で削除しています。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="init_clear_props", unindent="True"]


## 描画関数を登録する

単純にgpuモジュールのAPIを呼び出しただけでは、図形を表示することはできません。
図形を描画するためには、**描画関数** を登録し、描画関数内でgpuモジュールのAPIを呼び出す必要があります。

サンプルアドオンでは、*[3Dビューポート]* スペースに対して描画関数を登録する処理をクラスメソッド `__handle_add` に定義し、`invoke` メソッドの *[開始]* ボタンが押されたときに呼び出します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="handle_add", unindent="True"]

描画関数の登録は、スペース単位で行います。
例えば、*[3Dビューポート]* スペースに描画関数を登録したい場合は、`bpy.types.SpaceView3D.draw_handler_add` メソッドを使って登録します。
ここで `bpy.types.SpaceView3D` は、*[3Dビューポート]* スペースのスペース情報ですが、描画先のスペースによってこの部分の記述が変わります。
描画先のスペースの候補一覧を次に示します。
なお、同じスペースを持つエリアがウィンドウ内に複数存在した場合は、該当するエリアすべてに描画されます。

|クラス|スペース|
|---|---|
|`SpaceView3D`|*[3Dビューポート]* スペース|
|`SpaceImageEditor`|*[画像エディター]* スペース、*[UVエディター]* スペース|
|`SpaceNodeEditor`|*[シェーダーエディター]* スペース、*[コンポジター]* スペース、*[テクスチャノードエディター]* スペース|
|`SpaceSequenceEditor`|*[ビデオシーケンサー]* スペース|
|`SpaceClipEditor`|*[動画クリップエディター]* スペース|
|`SpaceDopeSheetEditor`|*[ドープシート]* スペース、*[タイムライン]* スペース|
|`SpaceGraphEditor`|*[グラフエディター]* スペース、*[ドライバー]* スペース|
|`SpaceNLA`|*[ノンリニアアニメーション]* スペース|
|`SpaceTextEditor`|*[テキストエディター]* スペース|
|`SpaceConsole`|*[Pythonコンソール]* スペース|
|`SpaceInfo`|*[情報]* スペース|
|`SpaceOutliner`|*[アウトライナー]* スペース|
|`SpaceProperties`|*[プロパティ]* スペース|
|`SpaceFileBrowser`|*[ファイルブラウザー]* スペース|
|`SpacePreferences`|*[プリファレンス]* スペース|

`bpy.types.SpaceView3D.draw_handler_add` メソッドの引数には、次に示す引数を指定します。

|引数|型|意味|
|---|---|---|
|第1引数||描画関数（描画関数は、関数、クラスメソッド、またはスタティックメソッドのいずれか）|
|第2引数|`tuple`|描画関数で受け取る引数（タプル型）|
|第3引数|`str`|描画先のリージョン|
|第4引数|`str`|描画モード（深度バッファの扱いを指定。基本は `POST_PIXEL` を指定する）|

本節のサンプルアドオンでは、第1引数に `SAMPLE34_OT_DrawStar.__draw` 、第3引数に `WINDOW` を指定します。
第2引数にはコンテキスト情報を渡し、描画関数内でこれらの値を利用します。

<div class="column">
第2引数に `(context, )` を渡しているところに、違和感を感じるかもしれません。
単純に考えると、ここには `context` のみを渡せばよさそうです。
しかし、実際に試した人はわかると思いますが、仮にここで第2引数に `context` を指定すると、「Contextではなくタプル型の値を指定する必要があります」というエラーメッセージが表示されて、エラー終了してしまいます。
このため、サンプルアドオンでは、タプル型であることを明示するために `(context, )` を指定しています。
なお、要素が1つの場合にタプル型であることを認識させるために、要素のあとにカンマ（,）を追加していることに注意してください。
`(context)` のようにカンマがないと、`context` と同じであると判断されてしまいます。
</div>

`bpy.types.SpaceView3D.draw_handler_add` メソッドは、戻り値としてハンドルを返します。
ハンドルは、クラス変数 `SAMPLE34_OT_DrawStar.__handle` に保存し、描画関数の登録解除時に利用します。

<div class="column">
登録した描画関数は、描画先のリージョンが更新されたときに呼ばれます。
したがって、*[開始]* ボタンをクリックしたあとに、何かしらの更新処理（オブジェクトの移動など）を行わないと描画関数が呼ばれないため、ボタンを押した直後は表示されません。
この問題を解決するため、本節のサンプルアドオンでは *[開始]* ボタンや *[終了]* ボタンをクリックしたときに描画先のリージョンが更新されるように、`context.area.tag_redraw` メソッドを実行しています。
</div>


## 描画関数を定義する

描画関数は、クラスメソッド `SAMPLE34_OT_DrawStar.__draw` として定義します。
クラスメソッド `SAMPLE34_OT_DrawStar.__draw` は、次の手順で星型の図形を描画します。

1. ビルトインシェーダの取得
2. 頂点データ、インデックスデータ作成
3. バッチ作成
4. シェーダパラメータ指定
5. 描画

なお、サンプルアドオンでは、gpu_extrasモジュールを使って描画処理を簡略化しています。
次のようにして、gpu_extrasモジュールの `batch.batch_for_shader` 関数をインポートしていることに注意してください。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="import_gpu_extras", unindent="True"]


### 1. ビルトインシェーダの取得

シェーダを自作することも可能ですが、サンプルアドオンではビルトインのシェーダ `'2D_UNIFORM_COLOR'` を利用しています。
シェーダ `'2D_UNIFORM_COLOR'` は、1色で図形を塗りつぶすときに利用します。
ビルトインのシェーダは、`gpu.shader.from_builtin` 関数を呼び出して取得します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="build_shader", unindent="True"]


### 2. 頂点データ、インデックスデータ作成

バッチを作るために必要な、頂点データやインデックスデータを作成します。
星型の図形になるように、頂点データやインデックスデータを作成していますが、星型図形の頂点の求め方に関しては、ここでは詳細を割愛します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="build_vert_and_idx_data", unindent="True"]

なお、クラスメソッド `SAMPLE34_OT_DrawStar.__draw` に渡されてくる引数 `context` はコンテキスト情報であり、`context.scene` は `bpy.types.Scene` と同じものであることに注意してください。
このため、`bpy.types.Scene.sample34_center` として定義したプロパティクラスの変数は、`context.scene.sample34_center` としてアクセスできます。


### 3. バッチ作成

作成した、頂点データやインデックスデータをもとに、バッチを作成します。
バッチは、gpu_extraモジュールの `batch_for_shader` 関数を呼び出して作成します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="build_batch", unindent="True"]

`batch_for_shader` 関数は、次に示す引数を受け取ります。

|引数|型|意味|
|---|---|---|
|第1引数|`gpu.types.Shader`|シェーダ|
|第2引数|`str`|描画図形の型|
|第3引数|`dict`|頂点データ|
|第4引数|`list`|インデックスデータ|

サンプルアドオンでは、第2引数に `'LINES'` を渡して線分を表示しています。


### 4. シェーダパラメータ指定

シェーダにパラメータを渡します。
渡せるパラメータはシェーダによって異なりますが、サンプルアドオンで使用するシェーダには、図形を塗りつぶす色 `"color"` をパラメータとして渡すことができます。
シェーダにパラメータを渡すために、`shader.uniform_float` メソッドを呼び出しています。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="set_shader_parameter", unindent="True"]

サンプルアドオンでは `(赤, 緑, 青, アルファ値) = (0.5, 1.0, 1.0, 1.0)` を渡すことで、描画色を水色に設定しています。


### 5. 描画

最後に、`batch.draw` メソッドを呼び出して、図形を描画します。
引数にシェーダを渡していることに注意してください。


## 描画関数を登録解除する

`bpy.types.SpaceView3D.draw_handler_add` メソッドを使って登録した描画関数は、登録解除するまで呼ばれ続けます。
このため、不要になったとき（本節のサンプルアドオンでは、*[終了]* ボタンが押されたとき）に登録解除する必要があります。
描画関数を登録解除する処理を次に示します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-4.py" block="handle_remove", unindent="True"]

描画関数の登録解除は、`bpy.types.SpaceView3D.draw_handler_remove` メソッドを呼び出して行います。
描画関数を登録したときに使用した `bpy.types.SpaceView3D.draw_handler_add` メソッドと同様、`SpaceView3D` は、描画関数を登録解除する対象のスペースによって変更する必要があります。
`bpy.types.SpaceView3D.draw_handler_remove` メソッドに指定する引数を次に示します。

|引数|型|意味|
|---|---|---|
|第1引数||ハンドル（`draw_handler_add` メソッドの戻り値）|
|第2引数|`str`|描画関数を登録したリージョン|

本節のサンプルアドオンでは、クラス変数 `SAMPLE34_OT_DrawStar.__handle` にハンドルが保存されているため、クラス変数 `SAMPLE34_OT_DrawStar.__handle` を第1引数に指定します。
第2引数は、描画関数の登録を解除するリージョンを指定しますが、本節のサンプルアドオンでは、 `bpy.types.SpaceView3D.draw_handler_add` メソッドの第3引数に指定したリージョン `WINDOW` を指定します。

これで描画関数の登録が解除されました。
登録解除後は、クラス変数 `SAMPLE34_OT_DrawStar.__handle` に `None` を代入してハンドルが無効であることを明示します。


# まとめ

gpuモジュールを使って、*[3Dビューポート]* スペースで図形を描画するための方法を説明しました。

本節で紹介したgpuモジュール、[3-1節](01_Handle_Mouse_Event.html) と [3-2節](02_Handle_Keyboard_Event.html) で説明したユーザからのイベントを扱う処理を組み合わせることで、Blenderの枠組みで実現可能なUIとは全く異なる、独自のUIを構築できます。


## ポイント

* gpuモジュールを利用することで、図形を描画できる
* 図形を描画するためには、`bpy.types.XXX.draw_handler_add` （XXX：描画対象のスペースにより変わる）メソッドを用いて、描画関数を登録する必要がある
* 登録した描画関数は、必要なくなったときに `bpy.types.XXX.draw_handler_remove` メソッドを用いて、登録を解除する必要がある
* gpu_extrasモジュールを利用することで、図形の描画が容易になる
* `gpu.shader.from_builtin` 関数を利用することで、Blenderのビルトインシェーダを取得できる
