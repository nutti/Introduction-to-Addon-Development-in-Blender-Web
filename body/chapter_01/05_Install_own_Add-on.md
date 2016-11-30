<div id="sect_title_img_1_5"></div>

<div id="sect_title_text"></div>

# 自作のアドオンをインストールする

<div id="preface"></div>

###### ここまでアドオン開発の準備ばかりで飽きてしまった方も多いと思いますが、本節ではいよいよアドオンを作成します。本節では具体的なアドオンのソースコードの解説はせずにアドオンを作成し、作成したアドオンをインストールして使うまでの手順を紹介します。具体的なソースコードの解説は、次章以降からです。

## アドオンを作成する

本節では、インストールやアンインストールのみ行うことのできるアドオンを作成します。以下の手順に従ってアドオンを作成してください。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|[1-3節](03_Prepare_Add-on_development_environment.md) を参考にしてコンソールウィンドウからBlenderを起動します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*テキストエディター* エリアのメニューから*新規* をクリックして空のテキストを作成します。|![アドオン作成 手順2](https://dl.dropboxusercontent.com/s/6x7jkbaadtehb2e/blender_make_add-on_2.png "アドオン作成 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>| 以下に示すソースコード全文を入力します。**空白は全て半角スペースで入力し、タブや全角スペースが含まれない** ように注意してください。|![アドオン作成 手順3](https://dl.dropboxusercontent.com/s/yv4zxwqlzljnm10/blender_make_add-on_3.png "アドオン作成 手順3")|
|---|---|---|

[import](../../sample/src/chapter_01/sample_1-5.py)

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|入力が完了したら、 *テキストエディター* エリアのメニューから *テキスト* > *名前をつけて保存* を実行します。|![アドオン作成 手順4](https://dl.dropboxusercontent.com/s/cbwyg0yebb8loww/blender_make_add-on_4.png "アドオン作成 手順4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|ファイル名 *sample_1-5.py* として保存します。保存先はOSごとに異なりますので注意してください。|![アドオン作成 手順5](https://dl.dropboxusercontent.com/s/z9ibf7qz2t1jlj7/blender_make_add-on_5.png "アドオン作成 手順5")|
|---|---|---|

|OS|保存先|
|---|---|
|Windows|```C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons```|
|Mac|```/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons```|
|Linux|```/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons```|

<div id="process_start_end"></div>

---


## アドオンを有効化する

以下の手順に従い、作成したアドオンを有効化します。


<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*情報* エリアの *ファイル* > *ユーザー設定...* を選択します。|
|---|---|


<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*アドオン* タブを選択し、サポートレベルを *テスト中* に変更すると、今回作成したアドオンが表示されます。|![アドオン有効化 手順2](https://dl.dropboxusercontent.com/s/7p3apgnyvjj8dl0/blender_enable_add-on_2.png "アドオン有効化 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|チェックボックスをクリックし、アドオンを有効化します。|![アドオン有効化 手順3](https://dl.dropboxusercontent.com/s/d5wd9q0xfdbpvqd/blender_enable_add-on_3.png "アドオン有効化 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|アドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。|
|---|---|

```sh
サンプル1-5: アドオン「サンプル1-5」が有効化されました。
```

ここまでの手順で本節で作成したアドオンが有効化され、アドオンを使用する準備が整いました。

<div id="process_start_end"></div>

---



## アドオンを無効化する

本節で作成したアドオンは機能を持たない単純なアドオンですので、有効化・無効化以外にできることはありません。

<div id="sidebyside"></div>

|右図のように、アドオン有効化時にクリックしたチェックボックスを再度クリックしてチェックを外すことで、アドオンを無効化できます。|![アドオン無効化](https://dl.dropboxusercontent.com/s/73xlppzkxu21u5w/blender_disable_add-on.png "アドオン無効化")|
|---|---|


アドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル1-5: アドオン「サンプル1-5」が無効化されました。
```

<div id="column"></div>

ここまで期待した動作をしているでしょうか。もし期待した動作にならずにエラーが出る場合は、ソースコードに入力した内容が正しいかを再度確認してください。Pythonではスペースやタブが混ざっていたり、スペースやタブの数が合っていなかったりする場合にエラーになることが多いので、特に空白には注意してください。

## まとめ

本節ではアドオンを作成し、作成したアドオンをインストールしてアドオンの有効化/無効化しました。実際にソースコードを入力してアドオンを作成しましたが、ソースコードの解説が無いため具体的に何をしているかよくわからなかったと思います。

次節からはより実用的なサンプルを紹介し、もう少し踏み込んだソースコードの解説をしながらアドオンの作り方を紹介します。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* アドオンのソースコードは、Blender本体に備わっている *テキストエディター* を用いて作成・編集できる
* アドオンの有効化/無効化は、*情報* エリアのメニューから *ファイル* > *ユーザ設定* で表示される *Blenderユーザ設定* ウィンドウの *アドオン* タブから行う
