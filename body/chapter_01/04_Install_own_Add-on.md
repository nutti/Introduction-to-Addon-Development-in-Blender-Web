<div id="sect_title_img_1_1"></div>

<div id="sect_title_text"></div>

# 自作のアドオンをインストールしてみよう

<div id="preface"></div>

###### これまでアドオン開発の準備ばかりで飽きてしまった方も多いと思いますが、本節ではいよいよアドオンを作成して使ってみます。ここでは具体的なアドオンのソースコードの解説はせずに簡単なアドオンを作成し、作成したアドオンをインストールして使うまでの手順を紹介します。具体的なアドオンのソースコードの解説は、次節以降で行います。

## アドオンを作成する

早速ですが、簡単なアドオンを作成します。
以下の手順に沿ってアドオンを作成してください。

<div id="process"></div>

|　|　|　|
|---|---|---|
|1|コンソールからBlenderを起動します。|　|
|2|*テキストエディター* エリアのメニューバーにある *新規* をクリックして空のテキストを作成します。|![アドオン作成 手順1](https://dl.dropboxusercontent.com/s/6x7jkbaadtehb2e/blender_make_add-on_1.png "アドオン作成 手順1")|
|3| 以下に示すソースコード全文を入力します。空白は全て半角スペースで入力し、タブや全角スペースが含まれないように注意してください。|![アドオン作成 手順2](https://dl.dropboxusercontent.com/s/t6agj2bu859vk1c/blender_make_add-on_2.png "アドオン作成 手順2")|

[import](../../sample/src/chapter_01/sample_0.py)

<div id="process"></div>

|　|　|　|
|---|---|---|
|4|入力が完了したら、 *テキストエディタ* エリアのメニューバーから *テキスト* > *名前つけて保存* を実行します。|![アドオン作成 手順3](https://dl.dropboxusercontent.com/s/cbwyg0yebb8loww/blender_make_add-on_3.png "アドオン作成 手順3")|
|5|*04.py* という名前で保存します。[1.2節](02_Use_Blender_Add-on.md) でも解説しましたが、保存先はOSごとに異なりますので注意してください。|![アドオン作成 手順4](https://dl.dropboxusercontent.com/s/z9ibf7qz2t1jlj7/blender_make_add-on_4.png "アドオン作成 手順4")|

|OS|保存先|
|---|---|
|Windows|```C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons```|
|Mac|```/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons```|
|Linux|```/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons```|


## アドオンを有効化する

以下の手順で、作成したアドオンを有効化します。

<div id="process"></div>

|　|　|　|
|---|---|---|
|1|*情報* エリアの *ファイル* > *ユーザ設定* を選択してください。|　|
|2|*アドオン* タブを選択し、サポートレベルを *テスト中* に変更すると、今回作成したアドオンが表示されていると思います。|![アドオン有効化 手順1](https://dl.dropboxusercontent.com/s/7p3apgnyvjj8dl0/blender_enable_add-on_1.png "アドオン有効化 手順1")|
|3|チェックボックスをクリックし、アドオンを有効化します。|![アドオン有効化 手順2](https://dl.dropboxusercontent.com/s/ghc3rhh2wf3v9zc/blender_enable_add-on_2.png "アドオン有効化 手順2")|
|4| アドオンを有効化したら、コンソールに以下の文字列が出力されているはずです。|　|

```shell-session
アドオンが有効化されました。
```

今回作成したアドオンが有効化され、使用する準備が整ったことになります。

## アドオンを無効化する

今回作成したアドオンは機能を持たない単純なアドオンですので、有効化・無効化以外にできることはありません。
有効化したアドオンを無効化しましょう。

アドオンの無効化は、アドオンを有効化時にクリックしたチェックボックスを再度クリックすることで行えます。

![アドオン無効化](https://dl.dropboxusercontent.com/s/73xlppzkxu21u5w/blender_disable_add-on.png "アドオン無効化")

アドオンを無効化すると、コンソールに以下の文字列が出力されます。

```shell-session
アドオンが無効化されました。
```

## まとめ

本節ではアドオンを作成し、自作したアドオンをインストールしてアドオンの有効化/無効化を行ってみました。
実際にソースコードを入力してアドオンを作成してもらいましたが、解説が無いので何をしているかよくわからなかったと思います。
次節からは新たなサンプルを紹介し、もう少し踏み込んだ解説をしながらアドオンの作り方を紹介していきます。

<div id="point"></div>

### ポイント

* アドオンのソースコードは、Blender本体に備わっている *テキストエディタ* を用いて作成・編集できる
* アドオンの有効化/無効化は、 *情報* エリアのメニューバーから *ファイル* > *ユーザ設定* で表示される *Blenderユーザ設定* ウィンドウの *アドオン* タブから行う
