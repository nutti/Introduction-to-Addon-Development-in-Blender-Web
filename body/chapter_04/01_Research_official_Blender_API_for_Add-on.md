# 4-1. Blenderが提供するアドオン向けのAPIを調べる

これまで紹介したサンプルでは、Blenderが提供する様々なAPIを使ってきました。
ここで1つ疑問が生じます。サンプルで用いたAPIはどこで知ることができたのでしょうか？
こんな疑問に答えるのが本節となります。

## Blenderが提供するAPIの情報源

Blenderが提供するAPIの情報を収集する方法としては以下のようなものがあります。

* Blender公式のAPIリファレンスを読む
* *Pythonコンソール* でAPIを検索・実行する
* *テキストエディター* のテンプレートを読む
* Blenderアドオン開発の参考サイトを読む
* 他者が作成したアドオンのソースコードを読む
* Blenderのコミュニティサイトで質問する

### Blender公式のAPIドキュメントを読む

Blenderが提供しているAPI一覧は、Blender公式が公開しているドキュメントから確認することができます。

* API documentation - http://www.blender.org/api/

＠＠＠図を入れる＠＠＠

過去のBlenderのバージョンのドキュメントも参照できますが、Blenderのバージョンに応じて提供されているAPIは変わるため、開発に利用しているBlenderのバージョンのドキュメントを参照するようにしましょう。
本書のサンプルはBlenderのバージョンが2.75aであるため、バージョンが2.75aであるドキュメントを見てみましょう。

* API documentation (Blender 2.75a) - http://www.blender.org/api/blender_python_api_2_75a_release/

＠＠＠図を入れる＠＠＠

この中から、 *3Dビュー* ウィンドウのアクティブ状態のオブジェクトを取得するAPIを調べてみましょう。
右側のページには、提供するAPIに対してモジュールごとにメニュー化されています。
モジュールは大きく分けて以下の3つにグループ化されています。

|||
|---|---|
|Application Modules|基本モジュール（bpyモジュール）。Blender本体のデータにアクセスするために最低限必要なモジュール|
|Standalone Modules|拡張モジュール。Application Modulesを簡単に利用したり、アドオン開発を便利にするためのモジュール|
|Game Engine Modules|Blender Game Engine向けモジュール|

最後の *Game Engine Modules* は、Blenderが提供するゲームエンジン *Blender Game Engine(BGE)* 向けのモジュールあるため、アドオンの開発では基本的に利用しません。
アドオン開発に限るのであれば、 *Application Modules* と *Standalone Modules* のみを確認すればよいでしょう。

*Application Modules* である ```bpy``` モジュールは非常に大きなモジュールであるため、複数のサブモジュールから構成されています。
以下にアドオン開発時によく利用するモジュールをまとめました。
アドオンを開発する時に必ず必要になるモジュールであるため、どのようなモジュールが提供されているか一度目を通しておくとよいでしょう。

|モジュール名|概要|
|---|---|
|```bpy.context```|現在のBlenderの実行状態（コンテキスト）を取得するためのAPI群|
|```bpy.data```|メッシュや画像データなど、Blenderで利用されているデータへアクセスするためのAPI群|
|```bpy.ops```|Blenderのデータに対する操作や、アドオンで登録した操作|
|```bpy.types```|Blenderで提供している型|
|```bpy.utils```|アドオンで利用するクラスの登録など、アドオンへ提供する便利関数群|
|```bpy.path```|Blender内でパスを簡単に扱うための関数群|
|```bpy.app```|Blenderのバージョンなど、Blender本体の情報など|
|```bpy.props```|アドオン内部で扱うプロパティ|

*Standalone Modules* は、 ```bpy``` モジュールを拡張するモジュールです。
*Application Modules* だけでは実装が大変な操作を簡単に扱えたり、 UIを構築する関数が揃っていたりとアドオン開発で役立つモジュールばかりですので、こちらも必見です。

|モジュール名|概要|
|---|---|
|```mathutils```|行列やベクトルなどのクラスや演算関数群。また、 ```geometry``` や ```kdtree``` サブモジュールを用いることで、図形の交差判定や3D空間内の探索を高速に行うことができます|
|```bgl```|OpenGLのラッパー関数群|
|```blf```|文字列描画を容易に行うための関数群|
|```gpu```|GLSLを扱うための関数群|
|```aud```|サウンドの読み込みや再生を行うための関数群|
|```bpy_extras```|```bpy``` モジュールに含まれない ```bpy``` 関連の便利関数群|
|```bmesh```|メッシュデータを容易に扱うための関数群|

ここでは、 *3Dビュー* でアクティブ状態のオブジェクトを取得するためのAPI  ```bpy.props.EnumProperty``` を調べてみましょう。

*Application Modules* > *Property Definitions (bpy.props)* をクリックし、 ```bpy.props.EnumProperty``` を探してみましょう。
以下のように、APIの説明に加えて引数に指定できる値や各引数の説明を参照することができます。

＠＠＠図を追加する＠＠＠

### PythonコンソールでAPIを検索・実行する

[1.2節]("../chapter_02/02_Sample_2_Scaling_object_1.md")においても説明しましたが、 *Pythonコンソール* を用いることでBlenderが提供しているAPIを検索・実行することができます。

例えば、Blender内のオブジェクト一覧を保持している ```bpy.data.objects``` を *Pythonコンソール* に入力し、 ```ctrl + space``` をキーを押して（補完して）みましょう。

＠＠＠図を追加＠＠＠

すると現在 *3Dビュー* 上にあるオブジェクト名が候補として表示されますので、適当なオブジェクト名を選んで再び補完してみましょう。

＠＠＠図を追加＠＠＠

また様々な候補が出てきます。
これら候補の中にあった ```select``` を入力し、実行してみましょう。
選んだオブジェクトが選択状態である場合は ```True``` 、選択状態でない場合は ```False``` が表示されます。

どうやら ```select``` は、オブジェクトが選択状態であるか否かを調べるAPIのようです。
実際にBlender公式のAPIドキュメントでも調べてみると、以下のようになっています。
> Object selection state

http://www.blender.org/api/blender_python_api_2_75a_release/bpy.types.Object.html#bpy.types.Object.select

また ```select``` に ```True``` を代入することでオブジェクトを選択状態に、  ```False``` を代入することでオブジェクトを非選択状態に変更することもできます。

＠＠＠図を追加＠＠＠

このように、 *Pythonコンソール* を利用することで実際のAPIを動作確認できるため、APIの効果がわかりづらい場合は、実際に動作させてAPIの効果を確認してみましょう。


## まとめ

### ポイント

*
