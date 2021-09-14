---
pagetitle: 3-8. 座標変換を活用する
subtitle: 3-8. 座標変換を活用する
---

[3-1節](01_Handle_Mouse_Event.html) から [3-5節](05_Draw_Texts.html) では、Blenderが提供するUIのフレームワークを超えて独自のUIを構築する方法について説明しました。
しかしこれらのUIは、基本的に2D座標で表現されるため、*[3Dビューポート]* スペースにおいてリージョン座標から3D空間の座標、またはその逆のように座標変換する必要が出てきます。
このため本節では、Blenderが提供するAPIを使って座標変換する方法を説明します。


# 作成するアドオンの仕様

本節では、リージョン座標から *[3Dビューポート]* スペース上の3D空間の座標へ変換できることを示すため、次のような機能を備えるサンプルアドオンを作成します。
なお、本節のサンプルアドオンを理解することで、*[3Dビューポート]* スペース上のオブジェクトと直線との交差判定方法についても、理解できます。

* マウスカーソルの位置に向けて放った、直線（レイ）と交差するメッシュ型オブジェクトの面を選択状態にし、交差していない面は非選択状態にする


# アドオンを作成する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして次に示すソースコードを入力し、ファイル名 `sample_3-8.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3-8.py"]


# アドオンを使用する

## アドオンを有効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに次に示す文字列が出力されます。

```
サンプル 3-8: アドオン『サンプル 3-8』が有効化されました。
```

*[3Dビューポート]* スペースのSidebarを表示し、メッシュ型オブジェクトを選択した状態で *[編集モード]* にすると、パネル *[サンプル 3-8]* > *[メッシュの面選択]* が追加されます。

![](../../images/chapter_03/08_Use_Coordinate_Transformation/enable_add-on.png "サンプルアドオン3-8 有効化")


## アドオンの機能を使用する

有効化したアドオンの機能を使い、動作を確認します。


<div class="work"></div>

|||
|---|---|
|1|メッシュ型オブジェクトを選択した状態で、*[編集モード]* に変更します。|
|2|*[3Dビューポート]* スペースのSidebarにおいて、パネル *[サンプル 3-8]* > *[メッシュの面選択]* に配置されている *[開始]* ボタンをクリックします。<br>![](../../images/chapter_03/08_Use_Coordinate_Transformation/use_add-on_2.png "サンプルアドオン3-8 手順2")|
|3|マウスカーソルが重なったメッシュの面が、選択状態になります。マウスカーソルが面から離れると、選択状態が解除されます。<br>![](../../images/chapter_03/08_Use_Coordinate_Transformation/use_add-on_3.png "サンプルアドオン3-8 手順3")|
|4|パネル *[サンプル 3-8]* > *[メッシュの面選択]* に配置されている *[終了]* ボタンをクリックすると、マウスカーソルがメッシュの面に重なっても、自動的に選択されないようになります。<br>![](../../images/chapter_03/08_Use_Coordinate_Transformation/use_add-on_4.png "サンプルアドオン3-8 手順4")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして有効化したアドオンを無効化すると、コンソールウィンドウに文字列が出力されます。

```
サンプル 3-8: アドオン『サンプル 3-8』が無効化されました。
```


# ソースコードの解説

本節では、座標変換に関する部分についてのみ説明します。
サンプルアドオンでは `invoke` メソッドや `modal` メソッドを使っていますが、本節では説明を省略します。
なお、これらのメソッドについては、[3-1節](01_Handle_Mouse_Event.html) で説明しています。


## マウスカーソルの位置に向けて発したレイと交差するメッシュの面を選択する

マウスカーソルの位置に向けて発した、レイと交差するメッシュの面を選択するための手順を次に示します。

1. マウスカーソルのリージョン座標を取得する
2. リージョン座標から、レイの向きとレイの始点の座標（*[3Dビューポート]* スペースの3D空間座標）を求める
3. オブジェクトのローカル座標における、レイの始点の座標とレイの向きを求める
4. オブジェクトの面選択状態を解除する
5. bmeshオブジェクトとBVHツリーを構築する
6. オブジェクトとレイの交差判定を行う
7. レイと交差したメッシュの面を選択する

これらの処理は全て、`SAMPLE38_OT_SelectMouseOveredMesh` クラスの `modal` メソッドで行います。


### 1. マウスカーソルのリージョン座標を取得する

最初に、マウスカーソルのリージョン座標を取得します。
マウスカーソルのリージョン座標を取得するためのコードを次に示します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="get_mouse_region_coord", unindent="True"]

[3-1節](01_Handle_Mouse_Event.html) で説明したように、マウスカーソルのリージョン座標は、`mouse_region_x` （X座標）と `mouse_region_y` （Y座標）で取得できます。


### 2. リージョン座標から、レイの向きとレイの始点の座標を求める

1で取得したマウスカーソルのリージョン座標から、レイの向きとレイの始点の座標を、*[3Dビューポート]* スペースの3D座標で求めます。
リージョン座標からこれらの座標への変換は、bpy_extraモジュールのview3d_utilsサブモジュールを利用すると簡単に実現できます。
事前に、bpy_extraモジュールをインポートしておきましょう。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="import_bpy_extras", unindent="True"]

マウスのリージョン座標から、レイの向きと始点の座標を求めるためのコードを次に示します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="calc_ray_dir_and_orig", unindent="True"]

レイの始点の座標は、*[3Dビューポート]* スペースの3D空間を映し出しているカメラの座標（視点）と同じです。
これは、`view3d_utils.region_2d_to_origin_3d` 関数を使って取得できます。
一方でレイの向きは、マウスカーソルのリージョン座標を、*[3Dビューポート]* スペースの3D空間の座標に座標変換することで求めることができます。
この座標変換は、`view3d_utils.region_2d_to_vector_3d` 関数を使って実現できます。
`view3d_utils.region_2d_to_vector_3d` 関数と `view3d_utils.region_2d_to_origin_3d` 関数の引数は、次に示すようにどちらも同じ引数を受け取ります。

|引数|型|意味|
|---|---|---|
|第1引数|`bpy.types.Region`|座標変換に使用するリージョン|
|第2引数|`bpy.types.RegionView3D`|座標変換に使用する3Dリージョンデータ|
|第3引数|`mathutils.Vector`|座標変換対象のリージョン座標の値|

それぞれの関数に渡す第1引数と第2引数は、`get_region_space` 関数で取得します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="get_region_space", unindent="True"]

`get_region_space` 関数は、[3-5節](05_Draw_Texts.md) で紹介した `get_region` 関数の改良版です。
`get_region_space` 関数は、引数 `area_type` で指定されたエリア上において、`region_type` に指定されたリージョン情報を返すことに加え、引数 `space_type` に指定されたスペース情報も返します。

エリアで表示しているスペースの情報は、`area` のメンバ変数 `spaces` に保存されています。
スペース情報の `type` と、引数 `space_type` を確認し、一致したものが取得対象となるスペース情報です。
サンプルアドオンでは、*[3Dビューポート]* スペースの情報と *[ウィンドウ]* リージョンの情報を取得するため、`region_type` が `'WINDOW'` であるリージョン情報と、`space_type` が `'VIEW_3D'` であるスペース情報を取得します。

`get_region_space` 関数を呼び出して取得した情報を用いて、`view3d_utils.region_2d_to_vector_3d` 関数と `view3d_utils.region_2d_to_origin_3d` 関数を呼び出します。
第1引数にはリージョン情報を、第2引数にはスペース情報のメンバ変数 `region_3d` を、第3引数にはマウスカーソルのリージョン座標を指定して呼び出すことで、レイの向きと始点の座標を *[3Dビューポート]* スペースの3D座標として求めることができます。


### 3. オブジェクトのローカル座標における、レイの始点の座標とレイの向きを求める

6において、レイと *[3Dビューポート]* スペースに配置されている、メッシュ型オブジェクトの面と交差判定を行うために使用する `ray_cast` メソッドは、レイの始点座標とレイの向きを、ローカル座標で引数に指定する必要があります。
しかし、`ray_cast` メソッドによるレイとオブジェクトの交差判定は、オブジェクトのローカル座標で行う必要があります。
このため、2で求めたレイの始点座標と向きを、オブジェクトのローカル座標に座標変換する必要があります。
次のコードは、2で取得したレイの始点の座標とレイの向きから、オブジェクトのローカル座標でのレイの始点座標とレイの向きを求める処理です。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="calc_ray_start_end", unindent="True"]

2で取得したレイの始点の座標とレイの向きから、レイの終点の座標を求めたあと、レイの始点と終点の座標をそれぞれローカル座標に変換している点に注意が必要です。
グローバル座標からローカル座標へは、オブジェクトのグローバル座標変換行列の逆行列である `matrix_world.inverted` をグローバル座標にかけることで変換できます。
最後に、ローカル座標に変換されたレイの始点と終点の座標を使って、ローカル座標でのレイの向きを求めています。


### 4. オブジェクトの面選択状態を解除する

オブジェクトのすべての面の選択を解除するためには、`bpy.ops.mesh.select_all` 関数の引数 `action` に `'DESELECT'` を渡します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="deselect_all", unindent="True"]


### 5. bmeshオブジェクトとBVHツリーを構築する

メッシュデータにアクセスするためには、bmesh用のメッシュデータを構築する必要があります。
bmesh用のメッシュデータを構築するためには、オブジェクトのデータ `activate_obj.data` を `bmesh.from_edit_mesh` 関数に渡す必要があります。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="build_bmesh", unindent="True"]

`bmesh.from_edit_mesh` 関数は、bmeshモジュールに定義されているため、あらかじめbmeshモジュールをインポートしておく必要があります。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="import_bmesh", unindent="True"]

続いて、bmeshオブジェクトからBVHツリーを構築します。
bmeshオブジェクトからBVHツリーを構築するためには、mathutilsモジュールに定義されている `mathutils.bvhtree.BVHTree.FromBMesh` 関数を呼び出す必要があります。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="build_bvhtree", unindent="True"]


### 6. オブジェクトとレイの交差判定を行う

構築したBVHツリーの `ray_cast` メソッドを使って、オブジェクトとレイの交差判定を行います。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="ray_cast", unindent="True"]

`ray_cast` メソッドの引数には、ローカル座標でのレイの始点と向きに加えて、始点からの距離を渡します。
本節では、始点から距離が2000だけ離れたところにレイの終点を設定するため、第3引数に `2000.0` を渡しています。
このため、レイの始点から2000以上距離が離れたオブジェクトの面は、交差判定の対象外となることに注意が必要です。

交差判定結果は、`ray_cast` メソッドの戻り値に保存されています。
`ray_cast` メソッドの戻り値の第3要素に、レイと交差した面のインデックスが保存されています。


### 7. レイと交差したメッシュの面を選択する

6の結果を使って、レイと交差したメッシュの面を選択します。
`bm.faces[fidx]` で、レイと交差したメッシュの面を取得できるため、そのメンバ変数である `select` に `True` を設定することで、該当する面を選択状態に変更できます。

[@include-source pattern="partial" filepath="chapter_03/sample_3-8.py" block="select_intersected_face", unindent="True"]


# まとめ

本節では、bpy_extrasモジュールのview3d_utilsサブモジュールを使って、リージョン座標から *[3Dビューポート]* スペース上の3D空間の座標へ、座標変換する方法を説明しました。
ここで、view3d_utilsサブモジュールが提供する、座標変換のAPIの一覧を紹介します。

|API|概要|
|---|---|
|`view3d_utils.region_2d_to_origin_3d`|リージョンを映すカメラの位置（3D空間の座標）を取得する|
|`view3d_utils.region_2d_to_vector_3d`|リージョンを映すカメラの位置から、指定されたリージョン座標へ発するレイの方向を3Dベクトルで取得する|
|`view3d_utils.region_2d_to_location_3d`|指定されたリージョン座標を、3D空間の座標へ変換する|
|`view3d_utils.location_3d_to_region_2d`|指定した3D空間の座標を、リージョン座標へ変換する|

さらに本節のサンプルアドオンでは、`ray_cast` メソッドを使ったレイとオブジェクトの交差判定も行いました。
`ray_cast` メソッドは非常に便利な関数で、交差した面に加えて交差した位置なども取得できます。
`ray_cast` メソッドを使うことで、例えばマウスでクリックしたときにマウスカーソルの位置に穴を開けたり、マウスカーソルが重なっている面を強調表示といった処理を実装できます。

長くなりましたが、サンプルアドオンを使ってBlenderのAPIを紹介するのは、本節で最後になります。
これまで様々なサンプルアドオンを紹介してきましたが、ここまでで紹介したBlenderのAPIを組み合わせることで、いろいろなことが実現できると思います。
APIを組み合わせて使うことで、よりおもしろく、そして便利な機能を提供できます。
このことを理解してもらえるように、[5章](../chapter_05/index.html) では、これまで紹介してきたAPIを組み合わせて作ったサンプルアドオンをいくつか紹介しますので、アドオンを開発するときの参考にしてみてください。

実質最後の章にあたる [4章](../chapter_04/index.html) では、アドオン開発時や公開時に参考になる情報を紹介します。
ぜひこちらも読んでみてください。


## ポイント

* bmeshモジュールは、オブジェクトのメッシュデータにアクセスするために利用するモジュールである
* bpy_extrasモジュールのview3d_utilsサブモジュールは、座標変換に便利なAPIを提供している
* BVHツリーの `ray_cast` メソッドを使用することで、レイとオブジェクトの交差判定を行うことができる
