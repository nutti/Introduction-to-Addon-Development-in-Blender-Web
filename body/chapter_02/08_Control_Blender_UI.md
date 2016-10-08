<div id="sect_title_img_2_8"></div>

<div id="sect_title_text"></div>

# Blender の UI を制御する

<div id="preface"></div>

###### Blender の UI を個人の好みに合わせて修正したいと思ったことはありませんか？ Blender の UI の大半は Python で記載されているため、 Python を理解し修正できるのであれば、個人の好みで Blender の UI を変更することができます。<br>本節はアドオンを開発しないけど自分の好みで UI を変更したい、という方にも参考になると思います。

## Blender の UI は Python で制御できる

Blender の UI の大半は Python のソースコードで記載されています。
このことを確認するために、 *3Dビュー* エリアのメニューを変更してみましょう。

以下の手順で、 *3Dビュー* エリアのメニューを制御するソースコードを修正します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*3Dビュー* エリアのメニューにある、*現在の視点を OpenGL レンダリング* ボタンにマウスカーソルを置いて右クリックします。|![3Dビューエリアのメニューを修正する1](https://dl.dropboxusercontent.com/s/aas9w46b84us2oi/control_UI_on_View3D_1.png "3Dビューエリアのメニューを修正する1")|
|---|---|---|

<div id="process_sep"></div>

---
<div id="process"></div>

|<div id="box">2</div>|*ソース編集* をクリックします。|![3Dビューエリアのメニューを修正する2](https://dl.dropboxusercontent.com/s/jcn6stvh67cg2bx/control_UI_on_View3D_2.png "3Dビューエリアのメニューを修正する2")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">3</div>|*テキストエディタ* エリアにソースコードが表示されます。また、 *現在の視点を OpenGL レンダリング* ボタンを表示するための処理にマウスカーソルが自動的に移動しています。|![3Dビューエリアのメニューを修正する3](https://dl.dropboxusercontent.com/s/f4j1ny6sxio3hmm/control_UI_on_View3D_3.png "3Dビューエリアのメニューを修正する3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|マウスカーソルの行をコメントアウトしましょう。|![3Dビューエリアのメニューを修正する4](https://dl.dropboxusercontent.com/s/h9l4jjzpqm2uu0t/control_UI_on_View3D_4.png "3Dビューエリアのメニューを修正する4")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|*テキストエディタ* エリアのメニュー *テキスト* から *保存* を実行し、上書き保存します。|![3Dビューエリアのメニューを修正する5](https://dl.dropboxusercontent.com/s/8ubgqqmhlunz3oh/control_UI_on_View3D_5.png "3Dビューエリアのメニューを修正する5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|[1-4節](04_Understand_Install_Uninstall_Update_Add-on.md) で紹介した *Reload Scripts* 機能を用いてアップデートすると、 *3Dビュー* エリアのメニューから *現在の視点を OpenGL レンダリング* ボタンが消えます。|![3Dビューエリアのメニューを修正する6](https://dl.dropboxusercontent.com/s/tuq7juvk8ya4xbh/control_UI_on_View3D_6.png "3Dビューエリアのメニューを修正する6")|
|---|---|---|

<div id="process_start_end"></div>

---

元の *3Dビュー* エリアのメニューに戻すためには先ほどコメントアウトした行のコメントを外して保存し、アップデートすることで元に戻すことができます。

ここまでの説明で、 Blender の UI は Python で制御されていることが理解できたのではないでしょうか。
以降の説明では、 Blender の UI を Python から構築する時に知っておくと良いことなどをサンプルを用いて説明します。

## 作成するアドオンの仕様

* 以下のようなタブを *3Dビュー* エリアの *ツール・シェルフ* に追加する

![アドオンの仕様](https://dl.dropboxusercontent.com/s/ial27tu1ousllmx/specification.png "アドオンの仕様")


* 追加したタブは、 *オブジェクトモード* 時かつオブジェクトが選択されている時のみ表示される

## アドオンを作成する

[1-2節](../chapter_01/02_Use_Blender_What_is_Add-on.md) のBlenderアドオン用フォルダにディレクトリ名 ```sample_2-2``` のディレクトリを作成します。
[1-4節](../chapter_01/04_Install_own_Add-on.md) を参考にして以下のソースコードをテキスト・エディタに入力し、作成したディレクトリの下にファイル名をそれぞれ ```__init__.py``` , ```enlarge_object.py``` , ```reduce_object.py``` として保存してください。

[import](../../sample/src/chapter_02/sample_2-8.py)


## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に作成したアドオンを有効化すると、コンソールに以下の文字列が出力されます。

```sh
サンプル2-8: アドオン「サンプル2-8」が有効化されました。
```

そして、 *3Dビュー* エリアの *ツール・シェルフ* にタブ *カスタムメニュー* が追加されます。
タブは *オブジェクトモード* 時かつオブジェクトが 1 つでも選択されている時のみ表示されます。
*エディットモード* または、*オブジェクトモード* でもオブジェクトが 1 つも選択されていない場合は表示されません。

また、 *3Dビュー* エリアのメニュー *オブジェクト* に *項目 1* と *項目2* が追加されます。

### アドオンの機能を使用する

*3Dビュー* エリアの *ツール・シェルフ* にタブ *カスタムメニュー* をクリックすると、カスタムメニューのメニューが表示されます。

カスタムメニューに表示されたボタンやメニューなどをクリックしたり選択したりできますが、基本的に何も起こりません。
ただし、 *ポップアップメッセージ* ボタンと *ダイアログメニュー* ボタン、 *ファイルブラウザ* ボタン、 *確認ポップアップ* ボタン、 *プロパティ付きポップアップ* ボタン、 *検索ウィンドウ付きポップアップ* ボタン、 *利用可能なアイコンをすべて表示* ボタンはこれから説明するように少なからず変化が起きますので実際に動かして確認してみてください。

#### ポップアップメッセージボタン

*ポップアップメッセージ* ボタンを押すと、ポップアップメッセージが表示されます。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *ポップアップメッセージ* ボタンをクリックします。|![ポップアップメッセージボタン1](https://dl.dropboxusercontent.com/s/os3tka7asic48ai/popup_message_1.png "ポップアップメッセージボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|クリックした場所にポップメッセージが表示されます。|![ポップアップメッセージボタン2](https://dl.dropboxusercontent.com/s/uf3j7u0ezi92uqd/popup_message_2.png "ポップアップメッセージボタン2")|
|---|---|---|

<div id="process_start_end"></div>

---


#### ダイアログメニューボタン

*ダイアログメニュー* ボタンを押すと、4つのプロパティと *OK* ボタン付きのダイアログメニューが表示されます。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *ダイアログメニュー* ボタンをクリックします。|![ダイアログメニューボタン1](https://dl.dropboxusercontent.com/s/p63yfu6yh8ddnrt/dialog_menu_1.png "ダイアログメニューボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|クリックした場所にダイアログメニューが開きます。|![ダイアログメニューボタン2](https://dl.dropboxusercontent.com/s/jjf8bfxa4x77dqv/dialog_menu_2.png "ダイアログメニューボタン2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|ダイアログメニュー上のプロパティは変更することができます。|![ダイアログメニューボタン3](https://dl.dropboxusercontent.com/s/wujq9rb6rp2k0vx/dialog_menu_3.png "ダイアログメニューボタン3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*OK* ボタンを押すと *情報* エリアにプロパティで指定した値が表示されます。|![ダイアログメニューボタン4](https://dl.dropboxusercontent.com/s/voqatxxy1ht4coi/dialog_menu_4.png "ダイアログメニューボタン4")|
|---|---|---|

<div id="process_start_end"></div>

---


#### ファイルブラウザボタン

*ファイルブラウザ* ボタンを押すと、ファイルブラウザが表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *ファイルブラウザ* ボタンをクリックします。|![ファイルブラウザボタン1](https://dl.dropboxusercontent.com/s/xi29nw88hvy9k6w/file_browser_1.png "ファイルブラウザボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|ファイルブラウザが開きます。|![ファイルブラウザボタン2](https://dl.dropboxusercontent.com/s/o2xy1e08aiu6xj8/file_browser_2.png "ファイルブラウザボタン2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|適当にファイルを開くと、*情報* エリアに開いたファイルのファイルパス・ファイル名・ファイルが置かれたディレクトリが表示されます。|![ファイルブラウザボタン3](https://dl.dropboxusercontent.com/s/qbtvg81av8jprc0/file_browser_3.png "ファイルブラウザボタン3")|
|---|---|---|


<div id="process_start_end"></div>

---


#### 確認ポップアップボタン

*確認ポップアップ* ボタンを押すと、操作を実行するか否かを問うポップアップが表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *確認ポップアップ* ボタンをクリックします。|![確認ポップアップボタン1](https://dl.dropboxusercontent.com/s/2apytkkmilgjlpv/confirm_popup_1.png "確認ポップアップボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|操作を実行するか否かを問うポップアップが表示されますので、 *確認ポップアップ* をクリックします。|![確認ポップアップボタン2](https://dl.dropboxusercontent.com/s/s5vaxp8zoip01aq/confirm_popup_2.png "確認ポップアップボタン2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*情報* エリアに以下のメッセージが表示されます。|![確認ポップアップボタン3](https://dl.dropboxusercontent.com/s/w0nwr4rkht11e1t/confirm_popup_3.png "確認ポップアップボタン3")|
|---|---|---|

```
確認ポップアップボタンをクリックしました
```

<div id="process_start_end"></div>

---


#### プロパティ付きポップアップボタン

*プロパティ付きポップアップ* ボタンを押すと、4つのプロパティがポップアップで表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *プロパティ付きポップアップ* ボタンをクリックします。|![プロパティ付きポップアップボタン1](https://dl.dropboxusercontent.com/s/4nh5dtfsg597bwf/prop_popup_1.png "プロパティ付きポップアップボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|プロパティを変更するたびに、 *情報* エリアに現在のプロパティ値が表示されます。|![プロパティ付きポップアップボタン2](https://dl.dropboxusercontent.com/s/lpn7vxq04xyxmna/prop_popup_2.png "プロパティ付きポップアップボタン2")|
|---|---|---|

<div id="process_start_end"></div>

---


#### 検索ウィンドウ付きポップアップボタン


*検索ウィンドウ付きポップアップ* ボタンを押すと、検索ウィンドウがポップアップで表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *検索ウィンドウ付きポップアップ* ボタンをクリックします。|![検索ウィンドウ付きポップアップボタン1](https://dl.dropboxusercontent.com/s/6cx6smtn2gz44qo/search_popup_1.png "検索ウィンドウ付きポップアップボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|検索ウィンドウ付きポップアップが表示されます。|![検索ウィンドウ付きポップアップボタン2](https://dl.dropboxusercontent.com/s/twu5ds60i0ptgi0/search_popup_2.png "検索ウィンドウ付きポップアップボタン2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|項目1・項目2・項目3の中から検索することができます。|![検索ウィンドウ付きポップアップボタン3](https://dl.dropboxusercontent.com/s/jpgbjzre6sodj35/search_popup_3.png "検索ウィンドウ付きポップアップボタン3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|項目を確定すると確定した項目の識別子が、 *情報* エリアに表示されます。|![検索ウィンドウ付きポップアップボタン4](https://dl.dropboxusercontent.com/s/j0krszjrtsz1r50/search_popup_4.png "検索ウィンドウ付きポップアップボタン4")|
|---|---|---|

<div id="process_start_end"></div>

---


#### 利用可能なアイコンをすべて表示ボタン

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *利用可能なアイコンをすべて表示* ボタンをクリックします。|![利用可能なアイコンをすべて表示ボタン1](https://dl.dropboxusercontent.com/s/ru4ckm8y65wyzsz/icon_list_1.png "利用可能なアイコンをすべて表示ボタン1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*ツール・シェルフ* のオプションに、アドオンから利用することのできるアイコン一覧と、それぞれのアイコンを表示するためのアイコンのキーコードが表示されます。|![利用可能なアイコンをすべて表示ボタン2](https://dl.dropboxusercontent.com/s/8tddbytmq5j8ghr/icon_list_2.png "利用可能なアイコンをすべて表示ボタン2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*一行に表示するアイコン数* から一行に表示するアイコンの数を変更することができます。|![利用可能なアイコンをすべて表示ボタン3](https://dl.dropboxusercontent.com/s/fzv6foiqzln3dyg/icon_list_3.png "利用可能なアイコンをすべて表示ボタン3")|
|---|---|---|


<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に有効化したアドオンを無効化すると、コンソールに以下の文字列が出力されます。

```sh
サンプル2-8: アドオン「サンプル2-8」が無効化されました。
```


## ソースコードの解説

本節のサンプルプログラムは UI の種類が多いためソースコードの分量が多いですが、それぞれの UI を構築するソースコードは短いので UI ごとに説明していきます。

### ツール・シェルフのタブを追加する

本節のサンプルでは、ツール・シェルフのタブを追加しています。
アドオンの機能をタブとしてまとめることで、ユーザはそのアドオンがどのような機能を持っているかが一目でわかるようになります。

また、普段よく使う機能をタブにまとめ、独自の UI を構築して Blender の利便性良いかもしれません。

ツール・シェルフのタブに追加するためには、以下に示すような ```bpy.types.Panel``` クラスを継承したパネルクラスを作成する必要があります。

```python
# ツール・シェルフに「カスタムメニュー」タブを追加
class VIEW3D_PT_CustomMenu(bpy.types.Panel):
    bl_label = "カスタムメニュー"       # タブに表示される文字列
    bl_space_type = 'VIEW_3D'           # メニューを表示するエリア
    bl_region_type = 'TOOLS'            # メニューを表示するリージョン
    bl_category = "カスタムメニュー"    # タブを開いたメニューのヘッダーに表示される文字列
```

本節のサンプルでは、 ```bpy.types.Panel``` クラスを継承した ```VIEW3D_PT_CustomMenu``` クラスを作成しています。
基本的に自由にクラス名をつけることができますが、 Blender では ```<エリア名>_<タイプ>_<クラスを表す適切な名前>``` のように命名されていることが多いようなので、本節のサンプルではそれに合わせてみました。
ここで ```<タイプ>``` には、継承する型に応じて以下のような文字列が対応します。


|文字列|型|
|---|---|
|```MT```|```bpy.types.Menu```|
|```PT```|```bpy.types.Panel```|

クラス ```VIEW3D_PT_CustomMenu``` には、メンバ変数が4つ定義されています。

```bl_label``` は、ツール・シェルフのタブに表示される文字列を指定します。

|メンバ変数|値の意味|
|---|---|
|```bl_label```|パネルに登録時に、タイトルとして表示される文字列。ツール・シェルフに登録する場合はタブに表示される文字列となる|
|```bl_space_type```|登録先のエリア|
|```bl_region_type```|登録先のリージョン|
|```bl_category```|ツール・シェルフのタブを開いたときに表示されるメニューのヘッダーに表示される文字列|

メンバ変数 ```bl_space_type``` には登録先のエリアを指定します。今回は3Dビューエリアに登録することを考えて ```VIEW_3D``` を指定しています。

メンバ変数 ```bl_space_type``` には、他にも以下のような値を指定することができます。

|設定値|値の意味|
|---|---|
|```VIEW_3D```|*3Dビュー*|
|```IMAGE_EDITOR```|*UV/画像エディター*|
|```NLA_EDITOR```|*NLAエディター*|
|```NODE_EDITOR```|*ノードエディター*|
|```LOGIC_EDITOR```|*ロジックエディター*|
|```SEQUENCE_EDITOR```|*ビデオシーケンスエディター*|
|```GRAPH_EDITOR```|*グラフエディター*|

メンバ変数 ```bl_region_type``` には登録先のリージョンを指定します。今回はツール・シェルフに登録するため、　```TOOLS``` を指定しています。

メンバ変数 ```bl_region_type``` には、他にも以下のような値を設定することが可能です。

|設定値|値の意味|
|---|---|
|```UI```|*プロパティパネル*|
|```TOOLS```|*ツール・シェルフ*|
|```TOOL_PROPS```|*ツール・シェルフ* のプロパティ|


```VIEW3D_PT_CustomMenu``` クラスには、 ```poll()``` メソッド・ ```draw_header()``` メソッド・ ```draw()``` メソッドが定義されています。
それぞれのメソッドは以下の処理を行います。
定義したメソッドの詳細については後ほど説明します。

|メソッド|処理|
|---|---|
|```poll()```|本メソッドが定義されたクラスの処理が実行可能な状態にあるかを判定するメソッド。```True``` を返すと実行可能と判断し、 ```False``` を実行不可能であると判断する。実行不可能と判断されると、本メソッドが定義されたクラスはいかなる処理も無効化される|
|```draw_header()```|ヘッダーを描画するメソッド|
|```draw()```|メニューを描画するメソッド。本メソッドでは、ヘッダー部の UI を変更することはできない|


### タブが表示される条件を設定する

本節のサンプルでは、 *オブジェクトモード* 時かつオブジェクトが選択されている時のみタブが表示される仕様としていました。
特定の状況下でのみメニューを表示したり、処理を実行させるようにしたりするためには ```poll()``` メソッドとメンバ変数 ```bl_context``` 活用します。

```bl_context``` は、パネルクラス時に指定することが可能なメンバ変数で、指定したコンテキストである時にパネルの描画処理を実行します。
```bl_context``` には以下のような値を設定することができます。

|値|説明|
|---|---|
|```objectmode```|オブジェクトモード時のみ描画する|
|```mesh_edit```|エディットモード時のみ描画する|

本節のサンプルではタブをオブジェクトモード時のみ描画するため、```bl_context = "objectmode"``` としています。

また、```poll()``` メソッドではオブジェクトが選択されている時に描画する処理を追加しています。

```python
# 本クラスの処理が実行可能かを判定する
@classmethod
def poll(cls, context):
    # オブジェクトが選択されている時のみメニューを表示させる
    for o in bpy.data.objects:
        if o.select:
            return True
    return False
```

```poll()``` メソッドはクラス単位の処理となるため、クラスメソッドとして定義する必要があります。
このため、メソッドの前にデコレータ ```@classmethod``` をつける必要があります。
```poll()``` メソッドに渡されてくる引数は以下の通りです。

|引数|型|意味|
|---|---|
|```cls```|```bpy.types.RNAMeta```|```poll()``` メソッドを実装したクラス|
|```context```|```bpy_types.Context```|```poll()``` メソッド実行時のコンテキスト|

```poll()``` メソッド内では、 ```bpy.data.objects``` からオブジェクトを全て取得して、選択されているオブジェクトが存在する場合は ```True``` を返しています。
これにより、選択されているオブジェクトが 1 つでもあればタブが表示されます。


### ヘッダーの UI を変更する

タブに追加したメニューのヘッダーの UI を変更するためには、パネルクラスの ```draw_header()``` メソッドを定義します。

```python
# ヘッダーのカスタマイズ
def draw_header(self, context):
    layout = self.layout
    layout.label(text="", icon='PLUGIN')
```

```draw_header()``` メソッドの引数は、以下の通りです。

|引数|型|値の説明|
|---|---|---|
|```self```|呼ばれた ```draw_header()``` メソッドを定義しているクラス|オペレータクラスのインスタンス|
|```context```|```bpy_types.Context```|```draw_header()``` メソッド実行時のコンテキスト|

```draw_header()``` メソッドでは、メニューのヘッダーに表示される文字列の左にアイコンを追加する処理を行っています。

```layout.label()``` の引数を以下に示します。

|引数|値の意味|
|---|---|
|```text```|表示する文字列|
|```icon```|表示するアイコン|

本節のサンプルでは文字列を追加したくはないので、引数 ```text``` に空の文字列、引数 ```icon``` にプラグインのアイコン ID を指定しています。


### メニューを構築する

タブに追加するメニューを構築するためには、 ```draw()``` メソッドを定義する必要があります。
```draw()``` メソッドの引数などの詳細については、 [2-5節](05_Create_Sub-menu.md) を参考にしてください。
本節のサンプルの ```draw()``` メソッドは非常に長いメソッドですので、それぞれの UI ごとに説明していきます。


#### ボタンを追加する

本節のサンプルでは以下の処理により、2種類のボタン（標準のボタンと文字列の周りの装飾が消えたボタン）を追加しています。

```python
# ボタンを追加
layout.label(text="ボタンを追加する:")
layout.operator(NullOperation.bl_idname, text="ボタン1")
layout.operator(NullOperation.bl_idname, text="ボタン2", emboss=False)
```

ボタンは ```layout.operator()``` 関数で追加することができ、以下の引数を指定します。
ボタンを押すと、第1引数に指定したオペレータクラスの ```bl_idname``` を持つオペレータクラスの処理が実行されます。

|引数|値の意味|
|---|---|
|第1引数|オペレータクラスの ```bl_idname```|
|```text```|ボタンに表示する文字列|
|```icon```|ボタンに表示するアイコン|
|```emboss```|```False``` の場合、文字列の周りの装飾が消える|


#### メニューを追加する

メニューを追加する処理の前に ```layout.separator()``` 関数を呼ぶことで、上下のスペースを空けることができます。
メニュー時の ```layout.separator()``` の動作については、 [2-1節](01_Basic_of_Add-on_Development.md) を参考にしてください。

本節のサンプルでは以下の処理により、メニューを追加しています。

```python
layout.label(text="メニューを追加する:")
layout.menu(NullOperationMenu.bl_idname, text="メニュー")
```

[2-5節](05_Create_Sub-menu.md) で説明したサブメニューを追加するための関数 ```layout.menu()``` により、メニューを追加しています。
追加されたメニューは、セレクトボックスの UI となります。
表示されるメニュー名はデフォルトで、第1引数に指定したメニュークラスの ```bl_label``` が表示されますが、 ```text``` 引数により変更することができます。


#### プロパティを追加する

処理のパラメータなどをユーザ指定するためのプロパティを追加します。

##### プロパティを定義する

プロパティを追加するためには、プロパティの定義を行う必要があります。

プロパティの定義は、アドオン有効化時に ```register()``` 関数から呼び出される ```init_props()``` 関数で行います。
プロパティは、 ```bpy.types.Scene``` に変数を追加することで定義できます。

```python
# プロパティの初期化
def init_props():
    scene = bpy.types.Scene
    scene.cm_prop_int = IntProperty(
        name="Prop 1",
        description="Integer Property",
        default=100,
        min=0,
        max=255)
    scene.cm_prop_float = FloatProperty(
        name="Prop 2",
        description="Float Property",
        default=0.75,
        min=0.0,
        max=1.0)
    scene.cm_prop_enum = EnumProperty(
        name="Prop 3",
        description="Enum Property",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")],
        default='ITEM_1')
    scene.cm_prop_floatv = FloatVectorProperty(
        name="Prop 4",
        description="Float Vector Property",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0)
```

##### プロパティを削除する

アドオン無効時には、```bpy.types.Scene``` に追加したプロパティのグループを削除する必要があります。削除しないとアドオン無効化時にもプロパティのデータが残ることになり無駄にメモリを消費するため、忘れずに削除するようにしましょう。
本節のサンプルでは、 ```unregister()``` 関数から呼び出される ```clear_props()``` 関数により、定義したプロパティの削除処理を行っています。

```python
# プロパティを削除
def clear_props():
    scene = bpy.types.Scene
    del scene.cm_prop_int
    del scene.cm_prop_float
    del scene.cm_prop_enum
    del scene.cm_prop_floatv
```

##### プロパティを変更するための UI を構築する

定義したプロパティをユーザが変更するための UI を表示するためには ```layout.prop()``` 関数を使います。```layout.prop()``` 関数の引数を以下に示します。

|引数|意味|
|---|---|
|第1引数|プロパティを持つオブジェクト|
|第2引数|プロパティ変数名|
|第3引数(```text```)|表示文字列|

本節のサンプルは ```bpy.types.Scene``` にプロパティを登録したため、 ```context.scene``` を第1引数に指定します。第2引数には、 ```bpy.types.Scene``` に登録したプロパティ変数名を文字列で指定します。

```python
scene = context.scene
# ・・・（略）・・・
# プロパティを追加
layout.label(text="プロパティを追加する:")
layout.prop(scene, "cm_prop_int", text="プロパティ 1")
layout.prop(scene, "cm_prop_float", text="プロパティ 2")
layout.prop(scene, "cm_prop_enum", text="プロパティ 3")
layout.prop(scene, "cm_prop_floatv", text="プロパティ 4")
```

#### ボタンを一行に並べる

```layout.operator()``` 関数を用いると、横幅が 100% のボタンが配置されます。
このため単純に ```layout.operator()``` を複数回実行すると実行した回数分、縦方向にボタンが配置されてしまいます。

ボタンを横に並べるためには ```layout.row()``` 関数を使って行成分を取得し、取得した行成分に対して ```operator()``` 関数を使ってボタンを配置する必要があります。
本節のサンプルでは、以下のようにして3つのボタンを一行に並べています。

```python
# 一行に並べる（アライメント無）
layout.label(text="一行に並べる（アライメント無）:")
row = layout.row(align=False)
for i in range(3):
    row.operator(NullOperation.bl_idname, text=("列 %d" % (i)))
```

なお、 ```layout.row()``` 関数の引数に ```align=False``` を指定すると、ボタンとボタンの間に隙間が空くようにして配置されるようになります。以下のように、 ```align=True``` を指定すると、この隙間がなくなります。

```python
# 一行に並べる（アライメント有）
layout.label(text="一行に並べる（アライメント有）:")
row = layout.row(align=True)
for i in range(3):
    row.operator(NullOperation.bl_idname, text=("列 %d" % (i)))
```

なお、 ```operator()``` の代わりに ```label()``` 、 ```prop()``` や ```menu()``` 関数を使うことによって、ラベル、プロパティやメニューを一行に並べて配置することができます。

#### ボタンを一列に並べる

```layout.operator()``` 関数を複数回実行することでボタンを一列に配置することができますが、隙間が広いのが難点です。
隙間を縮めた状態でボタンを縦に並べるためには ```layout.column()``` 関数を使って列成分を取得し、取得した列成分に対して ```operator()``` 関数を使ってボタンを配置します。
本節のサンプルでは、以下のように3つのボタンを一列に並べています。

```python
layout.label(text="一列に並べる（アライメント無）:")
column = layout.column(align=False)
for i in range(3):
    column.operator(NullOperation.bl_idname, text=("行 %d" % (i)))
```

ボタン間の隙間を無くすためには、 ```align=True``` を指定するところは ```layout.row()``` 関数と同様です。

```python
layout.label(text="一列に並べる（アライメント有）:")
column = layout.column(align=True)
for i in range(3):
    column.operator(NullOperation.bl_idname, text=("行 %d" % (i)))
```

なお、 ```operator()``` の代わりに ```label()``` 、 ```prop()``` や ```menu()``` 関数を使うことによって、ラベル、プロパティやメニューを一列に並べて配置することができます。

#### ボタンを複数列に配置する

```layout.column()``` 関数や  ```layout.row()``` 関数で取得した行成分や列成分に対してさらに行成分や列成分を取得することで、より複雑なボタンの配置を実現することができます。

本節のサンプルでは、以下のようにして2行2列にボタンを配置しています。

```python
# 複数列に配置する
layout.label(text="複数列に配置する:")
column = layout.column(align=True)
row = column.row(align=True)
row.operator(NullOperation.bl_idname, text="列 1, 行 1")
row.operator(NullOperation.bl_idname, text="列 2, 行 1")
row = column.row(align=True)
row.operator(NullOperation.bl_idname, text="列 1, 行 2")
row.operator(NullOperation.bl_idname, text="列 2, 行 2")
```


#### 領域を分割する

```layout.row()``` 関数を用いて行成分を取得することで一行にボタンを配置することができましたが、ボタンはすべて等幅になっていました。
ボタンの横幅を変えたいときは、 ```layout.split()``` 関数を用いて領域を分割します。

```layout.split()``` 関数の引数 ```percentage``` に値を指定することで、領域の横幅を決めることができます。
引数 ```percentage``` の値は浮動小数点数で指定し、 ```1``` で横幅 ```100%``` 、 ```0``` で横幅 ```0%``` となります。
例えば、ツール・シェルフの横幅に対して ```70%``` の横幅を持つ領域を分割する場合、 ```layout.split(percentage=0.7)``` とします。

本節のサンプルでは、以下のような処理で領域を3分割しています。

```python
# 領域を分割する
layout.label(text="領域を分割する:")
split = layout.split(percentage=0.3)
column = split.column(align=True)
column.label(text="領域1:")
column.operator(NullOperation.bl_idname, text="行 1")
column.operator(NullOperation.bl_idname, text="行 2")
split = split.split(percentage=0.7)
column = split.column()
column.label(text="領域2:")
column.operator(NullOperation.bl_idname, text="行 1")
column.operator(NullOperation.bl_idname, text="行 2")
split = split.split(percentage=1.0)
column = split.column(align=False)
column.label(text="領域3:")
column.operator(NullOperation.bl_idname, text="行 1")
column.operator(NullOperation.bl_idname, text="行 2")
```

各領域では、縦並びにボタンを2つ表示しています。

```layout.split()``` により分割した領域の変数 ```split``` に対して ```split.split()``` を実行することで、2つ以上の領域に分割することができます。
なお、ここで ```split.split()``` 関数に指定する引数 ```percentage``` について注意が必要です。
最初の領域分割 ```layout.split()``` の場合、 引数に指定した ```percentage``` はツール・シェルフの横幅に対する割合を示しますが、2回目の領域分割 ```split.split()``` は ```layout.split()``` で分割した残りの領域、つまり本節のサンプルではツール・シェルフの横幅 70% の領域に対する割合を指定します。
同様に3回目の領域分割では、2回目に分割した残りの領域に対する割合を指定します。
従って、ツール・シェルフに対する横幅はそれぞれ、領域1で 30% 、領域2で 70% × 0.7 = 49% 、領域3で 70% × 0.3 = 21% となります。


#### ボタンの横幅を自動的に拡大する

```layout.operator()``` ボタンを配置すると、自動的にボタンの横幅が領域全体に拡大されます。
ボタンの横幅を、明示的に領域全体に拡大する方法もあります。

本節のサンプルでは、以下のように ```row.alignment``` へ ```EXPAND``` を設定してボタンの横幅を自動的に拡大しています。

```python
# 横幅を自動的に拡大する
layout.label(text="横幅を自動的に拡大する:")
row = layout.row()
row.alignment = 'EXPAND'
row.operator(NullOperation.bl_idname, text="列 1")
row.operator(NullOperation.bl_idname, text="列 2")
```


#### ボタンを右寄せ・左寄せ配置にする

ボタンの横幅を自動的に拡大せず、右や左に寄せて配置することもできます。

本節のサンプルでは、以下のように ```row.alignment``` へ ```LEFT``` を設定してボタンを左寄せ配置しています。

```python
# 左寄せする
layout.label(text="左寄せする:")
row = layout.row()
row.alignment = 'LEFT'
row.operator(NullOperation.bl_idname, text="列 1")
row.operator(NullOperation.bl_idname, text="列 2")
```

また、 ```row.alignment``` へ ```RIGHT``` を設定することで右寄せ配置も可能です。

```python
# 右寄せする
layout.label(text="右寄せする:")
row = layout.row()
row.alignment = 'RIGHT'
row.operator(NullOperation.bl_idname, text="列 1")
row.operator(NullOperation.bl_idname, text="列 2")
```


#### グループ化する

複数の UI パーツをグループ化することもできます。
```layout.box()``` 関数の戻り値に対して ```operator()``` や ```menu()``` などを実行して作成した UI がグループ化されます。

本節のサンプルでは、以下のように4つのボタンをグループ化しています。

```python
# グループ化する
layout.label(text="グループ化する:")
row = layout.row()
box = row.box()
box_row = box.row()
box_column = box_row.column()
box_column.operator(NullOperation.bl_idname, text="行 1, 列 1")
box_column.separator()
box_column.operator(NullOperation.bl_idname, text="行 2, 列 1")
box_row.separator()
box_column = box_row.column()
box_column.operator(NullOperation.bl_idname, text="行 1, 列 2")
box_column.separator()
box_column.operator(NullOperation.bl_idname, text="行 2, 列 2")
```

上記の例から、グループ化した内部の UI は通常の UI と同じような処理で構築することができます。


#### ポップアップメッセージを表示する

アドオンからBlender内で、ポップアップメッセージを表示することもできます。

以下は、ポップアップメッセージを表示するオペレータクラスです。

```python
class ShowPopupMessage(bpy.types.Operator):
    bl_idname = "object.show_popup_message"
    bl_label = "ポップアップメッセージ"
    bl_description = "ポップアップメッセージ"
    bl_options = {'REGISTER', 'UNDO'}

    # execute() メソッドがないと、やり直し未対応の文字が出力される
    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # ポップアップメッセージ表示
        return wm.invoke_popup(self, width=200, height=100)

    # ポップアップメッセージに表示する内容
    def draw(self, context):
        layout = self.layout
        layout.label("メッセージ")
```

ポップアップメッセージの表示はボタンを押したときに呼ばれる ```invoke()``` メソッドの ```wm.invoke_popup()``` 関数で行っています。

```invoke()``` メソッドは、処理が実行された時に呼ばれるメソッドです。これまで使ってきた ```execute()``` メソッドも処理が実行された時に呼ばれますが、 ```execute()``` メソッドの前に ```invoke()``` メソッドが呼ばれる点が異なります。このため、 ```execute()``` メソッドの実行前に行いたい処理がある場合は、 ```invoke()``` メソッドを使用します。

```wm.invoke_popup()``` 関数の引数を以下に示します。

|引数|型|意味|
|---|---|
|第1引数|オペレータクラスのインスタンス||
|```width```|整数|ポップアップメッセージの横幅|
|```height```|整数|ポップアップメッセージの縦幅(UI に応じて自動的に調整されるため効果なし)|

```wm.invoke_popup()``` 関数により表示されるポップアップの UI は、 ```draw()``` メソッドで定義します。
本節のサンプルでは、 ```メッセージ``` と書かれたラベルを表示しています。

```wm.invoke_popup()``` 関数の戻り値は ```{'RUNNING_MODAL'}``` ですが、ここでは説明を省略します。
ポップアップメッセージを表示する時には ```wm.invoke_popup()``` 関数を ```invoke()``` メソッドの戻り値に指定すればよいということだけを覚えておきましょう。

ポップアップメッセージを表示するためのボタンの配置は、以下の処理で行います。

```python
# ポップアップメッセージを表示する
layout.label(text="ポップアップメッセージを表示する:")
layout.operator(ShowPopupMessage.bl_idname)
```


#### ダイアログメニューを表示する

ポップアップメッセージの応用として、プロパティをポップアップから入力することのできるダイアログメニューを表示することもできます。

以下は、ダイアログメニューを表示するオペレータクラスです。

```python
class ShowDialogMenu(bpy.types.Operator):
    bl_idname = "object.show_dialog_menu"
    bl_label = "ダイアログメニュー"
    bl_description = "ダイアログメニュー"
    bl_options = {'REGISTER', 'UNDO'}

    prop_int = IntProperty(
        name="ダイアログプロパティ 1",
        description="ダイアログプロパティ 1",
        default=100,
        min=0,
        max=255)
    prop_float = FloatProperty(
        name="ダイアログプロパティ 2",
        description="ダイアログプロパティ 2",
        default=0.75,
        min=0.0,
        max=1.0)
    prop_enum = EnumProperty(
        name="ダイアログプロパティ 3",
        description="ダイアログプロパティ 3",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")],
        default='ITEM_1')
    prop_floatv = FloatVectorProperty(
        name="ダイアログプロパティ 4",
        description="ダイアログプロパティ 4",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0)

    def execute(self, context):
        self.report({'INFO'}, "1: %d, 2: %f, 3: %s, 4: (%f, %f, %f)"
            % (self.prop_int, self.prop_float, self.prop_enum, self.prop_floatv[0], self.prop_floatv[1], self.prop_floatv[2]))

        return {'FINISHED'}

    def invoke(self, context, event):
        scene = context.scene

        self.prop_int = scene.cm_prop_int
        self.prop_float = scene.cm_prop_float
        self.prop_enum = scene.cm_prop_enum
        self.prop_floatv = scene.cm_prop_floatv

        # ダイアログメニュー呼び出し
        return context.window_manager.invoke_props_dialog(self)
```

```ShowDialogMenu``` クラスには4つのプロパティクラスの変数が宣言されていて、ダイアログメニューではこれらのプロパティを表示します。
ダイアログメニューの表示は ```context.window_manager.invoke_props_dialog()``` 関数で行います。
引数には、ダイアログメニューに表示するプロパティクラスの変数を持つオペレータクラスのインスタンスを渡します。

```context.window_manager.invoke_props_dialog()``` 関数の引数を以下に示します。

|引数|型|意味|
|---|---|
|第1引数|オペレータクラスのインスタンス|OK ボタンを押したときに、引数に指定したインスタンスの ```execute()``` メソッドが実行される。<br>また、ダイアログメニューのプロパティは本引数に指定したインスタンスに定義したプロパティクラスの変数が表示される|
|```width```|整数|ポップアップメッセージの横幅|
|```height```|整数|ポップアップメッセージの縦幅(UI に応じて自動的に調整されるため効果なし)|

```context.window_manager.invoke_props_dialog()``` 関数の戻り値はポップアップメッセージと同様、```{'RUNNING_MODAL'}``` ですが、ここでは説明を省略します。
ダイアログメニューを表示する時には ```wm.invoke_popup()``` 関数を ```invoke()``` メソッドの戻り値に指定すればよいということだけを覚えておきましょう。

ダイアログメニューに表示された OK ボタンを押すと、 ```execute()``` メソッドが実行されます。
```execute()``` メソッドでは、ダイアログメニューのプロパティに指定した値をコンソール・ウィンドウに出力します。
ダイアログメニューで指定したプロパティの値でアドオンの処理を実行したいときに活用しましょう。

ダイアログメニューを表示するためのボタンの配置は、以下の処理で行います。

```python
# ダイアログメニューを表示する
layout.label(text="ダイアログメニューを表示する:")
layout.operator(ShowDialogMenu.bl_idname)
```


#### ファイルブラウザを表示する

ファイルを開いたり保存したりする時などの Blender 標準の機能を使用した場合でも、ファイルを選択するためのファイルブラウザを表示する処理が存在します。
```context.window_manager.fileselect_add()``` を用いることで、アドオンからファイルブラウザを表示することができます。

本節のサンプルでは、以下のようにしてファイルブラウザを表示しています。

```python
class ShowFileBrowser(bpy.types.Operator):
    bl_idname = "object.show_file_browser"
    bl_label = "ファイルブラウザ"
    bl_description = "ファイルブラウザ"
    bl_options = {'REGISTER', 'UNDO'}

    filepath = StringProperty(subtype="FILE_PATH")
    filename = StringProperty()
    directory = StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        self.report({'INFO'}, "FilePath: %s, FileName: %s, Directory: %s" % (self.filepath, self.filename, self.directory))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # ファイルブラウザ表示
        wm.fileselect_add(self)

        return {'RUNNING_MODAL'}
```

ファイルブラウザを表示させるためには、 ```invoke()``` メソッド内で ```wm.fileselect_add()``` 関数を呼ぶ必要があります。
引数には、ファイルブラウザ内でファイルを確定した時に実行される、 ```execute()``` メソッドが定義されたオペレータクラスのインスタンスを指定します。
```invoke()``` メソッドの戻り値は、 ```{'RUNNING_MODAL'}``` にする必要があります。

またファイルブラウザで確定したファイルの情報を保存するために、メンバ変数 ```filepath``` ・ ```filename``` ・ ```directory``` を宣言しています。
ファイルブラウザからファイルの情報を受け取るためには、これらの変数名でなくてはならないことに注意が必要です。
なお、 ```filepath``` や ```directory``` は、 プロパティクラス ```StringProperty``` の引数 ```subtype``` にファイルパスを格納するプロパティであることを示す ```FILE_PATH``` を指定する必要があります。

ファイルブラウザでファイルを確定すると ```execute()``` メソッドが呼ばれ、確定したファイルパス・ファイル名・ファイルが置かれたディレクトリをコンソール・ウィンドウに表示します。

ファイルブラウザを表示するボタンを表示する処理は、以下の通りです。

```python
# ファイルブラウザを表示する
layout.label(text="ファイルブラウザを表示する:")
layout.operator(ShowFileBrowser.bl_idname)
```


#### 実行確認のポップアップを表示する

Blender の機能の中には、実行する前に本当にその処理を実行するか確認するためのポップアップを表示するものがあります。
例えば、 *情報* エリアのメニュー *ファイル* > *スタートアップファイルを保存* が実行確認のポップアップを表示する例です。

実行確認のポップアップは、 ```context.window_manager.invoke_confirm()``` 関数により表示することができます。

本節のサンプルでは、以下のようにして実行確認のポップアップを表示しています。

```python
class ShowConfirmPopup(bpy.types.Operator):
    bl_idname = "object.show_confirm_popup"
    bl_label = "確認ポップアップ"
    bl_description = "確認ポップアップ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "確認ポップアップボタンをクリックしました")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # 確認メッセージ表示
        return wm.invoke_confirm(self, event)
```

実行確認のポップアップは、 ```invoke()``` メソッド内から ```wm.invoke_confirm()``` 関数を呼び出して表示しています。

```vm.invoke_confirm()``` 関数の引数を以下に示します。

|引数|意味|
|---|---|
|第1引数|実行確認ポップアップで実行を決定したときに呼び出される ```execute()``` メソッドが定義されたオペレータクラスのインスタンス|
|第2引数|```invoke()``` メソッドの引数 ```event``` を指定|

クリック時に実行確認のポップアップを表示するボタンを表示する処理は、以下の通りです。

```python
# 確認ポップアップを表示する
layout.label(text="確認ポップアップを表示する:")
layout.operator(ShowConfirmPopup.bl_idname)
```


#### プロパティ付きポップアップを表示する

プロパティを変更することができる、プロパティ付きポップアップを作ることもできます。
実行結果を見るとダイアログメニューと同じ動作のように見えますが、ダイアログメニューは ```OK``` ボタンを押すまで処理が実行されないのに対し、プロパティ付きポップアップではプロパティを変更するたびに処理が実行されます。

本節のサンプルでは、以下のようにしてプロパティ付きポップアップを表示しています。

```python
class ShowPropertyPopup(bpy.types.Operator):
    bl_idname = "object.show_property_popup"
    bl_label = "プロパティ付きポップアップ"
    bl_description = "プロパティ付きポップアップ"
    bl_options = {'REGISTER', 'UNDO'}

    prop_int = IntProperty(
        name="プロパティ 1",
        description="プロパティ 1",
        default=100,
        min=0,
        max=255)
    prop_float = FloatProperty(
        name="プロパティ 2",
        description="プロパティ 2",
        default=0.75,
        min=0.0,
        max=1.0)
    prop_enum = EnumProperty(
        name="プロパティ 3",
        description="プロパティ 3",
        items=[
            ('ITEM_1', "項目 1", "項目 1"),
            ('ITEM_2', "項目 2", "項目 2"),
            ('ITEM_3', "項目 3", "項目 3")],
        default='ITEM_1')
    prop_floatv = FloatVectorProperty(
        name="プロパティ 4",
        description="プロパティ 4",
        subtype='COLOR_GAMMA',
        default=(1.0, 1.0, 1.0),
        min=0.0,
        max=1.0)

    def execute(self, context):
        self.report({'INFO'}, "1: %d, 2: %f, 3: %s, 4: (%f, %f, %f)"
            % (self.prop_int, self.prop_float, self.prop_enum, self.prop_floatv[0], self.prop_floatv[1], self.prop_floatv[2]))
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # プロパティ付きポップアップ表示
        return wm.invoke_props_popup(self, event)
```

プロパティ付きポップアップは、```invoke()``` メソッド内から ```wm.invoke_props_popup()``` 関数を実行することで表示することができます。
プロパティを変更すると ```execute()``` メソッドが実行され、 現在のプロパティの値が *コンソール・ウィンドウ* に表示されます。

```wm.invoke_props_popup()``` 関数には、以下のような引数を指定します。

|引数|意味|
|---|---|
|第1引数|プロパティを変えた時に呼び出される ```execute()``` メソッドが定義されたオペレータクラスのインスタンス|
|第2引数|```invoke()``` メソッドの引数 ```event``` を指定|

なお、プロパティ付きポップアップで表示されたプロパティは、 *ツール・シェルフ* の *オプション* にも表示されているため、ポップアップが閉じてしまった場合でも他の操作を行わなわない限り変更することができます。

クリック時にプロパティ付きポップアップを表示するボタンを表示する処理は、以下に示します。

```python
# プロパティ付きポップアップを表示する
layout.label(text="プロパティ付きポップアップを表示する:")
layout.operator(ShowPropertyPopup.bl_idname)
```


#### 検索ウィンドウ付きポップアップを表示する

あらかじめ登録した項目について検索することができる、検索ウィンドウ付きのポップアップを表示することができます。
実際この UI がどのように役立つのかよくわかっていませんが、 Blender の API として用意されていましたので紹介します。

本節のサンプルでは、検索ウィンドウ付きポップアップを以下のようにして表示しています。

```python
class ShowSearchPopup(bpy.types.Operator):
    bl_idname = "object.show_search_popup"
    bl_label = "検索ウィンドウ付きポップアップ"
    bl_description = "検索ウィンドウ付きポップアップ"
    bl_options = {'REGISTER', 'UNDO'}
    bl_property = "item"

    item = EnumProperty(
        name="配置位置",
        description="複製したオブジェクトの配置位置",
        items=[
            ('ITEM_1', '項目1', '項目1'),
            ('ITEM_2', '項目2', '項目2'),
            ('ITEM_3', '項目3', '項目3')
        ],
        default='ITEM_1'
    )

    def execute(self, context):
        self.report({'INFO'}, "%s を選択しました" % self.item)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        # 検索ウィンドウ付きポップアップ表示
        wm.invoke_search_popup(self)

        # {'FINISHED'} を返す必要がある
        return {'FINISHED'}
```

検索ウィンドウ付きのポップアップを表示するためには、 ```invoke()``` メソッド内で ```wm.invoke_search_popup()``` 関数を使います。
引数には、項目確定時に呼び出される ```execute()``` メソッドが定義されたクラスのインスタンスを指定します。
なお ```invoke()``` メソッドは ```{'FINISHED'}``` を返す必要があります。

項目を確定すると ```execute()``` メソッドが呼び出され、選択した項目の識別子が *コンソール・ウィンドウ* に表示されます。

検索ウィンドウで検索できる項目は、アドオン開発者が追加する必要があります。
検索ウィンドウへ追加する項目リストを持つ変数は ```EnumProperty``` プロパティクラスの型である必要があり、 メンバ変数 ```bl_property``` にその変数名を記載する必要があります。
本節のサンプルでは、メンバ変数 ```item``` が項目リストであるため、 ```bl_property="item"``` としています。

クリック時に検索ウィンドウ付きポップアップを表示するボタンを表示する処理は、以下に示します。

```python
# 検索ポップアップを表示する
layout.label(text="検索ポップアップを表示する:")
layout.operator(ShowSearchPopup.bl_idname)
```


#### オプションの UI をカスタマイズする

[2-3節](../chapter_02/03_Use_Property_on_Tool_Shelf_1.md) で説明した、ツール・シェルフのオプションの UI もカスタマイズできます。

オプションの UI をカスタマイズするために、本節のサンプルでは ```ShowAllIcons``` というオペレータクラスを作成しています。
このクラスは、 Python から利用できるすべてのアイコンをツール・シェルフのオプションに表示する処理を定義しています。

オプションの UI をカスタマイズする処理を以下に示します。


```python
# オプションのUI
def draw(self, context):
    layout = self.layout

    layout.prop(self, "num_column")

    layout.separator()

    # 利用可能なアイコンをすべて表示
    layout.label(text="利用可能なアイコン一覧:")
    for i, key in enumerate(bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items.keys()):
        if i %self.num_column == 0:
            row = layout.row()
        row.label(text=key, icon=key)
```

オプションの UI は、オペレータクラスの ```draw()``` メソッドで行います。
メソッドで定義している処理は、メニュークラスやパネルクラスで定義する ```draw()``` メソッドと同じように、 ```self.layout``` を通して行います。

利用可能なアイコンの識別子一覧は、 ```bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].enum_items.keys()``` により取得することが可能です。
取得したアイコンの識別子を、 ```row.label()``` 関数の引数 ```icon``` に指定することで、アイコンを表示することができます。
また本節のサンプルは今後アドオンを作る人のために、アイコンと識別子がどのように対応しているかわかるように、引数 ```text``` に識別子を代入してアイコンと一緒に表示しています。
見やすさを考慮して、一行に表示可能なアイコンの数をオプションから指定することができるようにしています。ぜひ活用してください。

最後に、 ```ShowAllIcons``` のボタンを配置する処理は、以下のようになります。

```python
# プロパティのUIをカスタマイズする＋アイコン一覧を表示する
layout.label(text="プロパティのUIをカスタマイズする")
layout.operator(ShowAllIcons.bl_idname)
```

### メニューへ項目を追加する順番を制御する

[2-1節](01_Basic_of_Add-on_Development.md) では、 ```bpy.types.INFO_MT_mesh_add.append()``` 関数を用いてメニューの末尾へ項目を追加していました。

本節のサンプルでは、 ```bpy.types.VIEW3D_MT_object.prepend()``` 関数を用いてメニューの先頭へ項目を追加しています。

```python
# 項目をメニューの先頭に追加
bpy.types.VIEW3D_MT_object.append(menu_fn_1)
# 項目をメニューの末尾に追加
bpy.types.VIEW3D_MT_object.prepend(menu_fn_2)
```


## まとめ

Blender に限らず UI は、ボタンやメニューなど数多くの部品により構成されるため、説明が長くなってしまいました。
分量が多いため、本節の内容をすべて理解するというよりも、必要な時に本節を参照すると良いと思います。
個々の部品を制御するためのソースコードは数行～数十行の規模ですし、ソースコード自体も似たようなパターンのため、ここまで読み進められた方であれば難なく理解できると思います。
UIの部品 と部品を追加するための API の対応関係を以下にまとめておきます。

|UI|API|
|---|---|
|間隔をあける|```layout.separator()```|
|ラベル|```layout.label()```|
|ボタン|```layout.operator()```|
|メニュー（セレクトボックス）|```layout.menu()```|
|プロパティ|```layout.prop()```|
|行成分取得(アライメント無)|```layout.row()``` <br> ```layout.row(align=False)```|
|行成分取得(アライメント有)|```layout.row(align=True)```|
|列成分取得(アライメント無)|```layout.column()``` <br> ```layout.column(align=False)```|
|列成分取得(アライメント有)|```layout.column(align=True)```|
|UI 部品の横幅を自動的に拡大|```row.alignment = 'EXPAND'```|
|UI 部品を左寄せ|```row.alignment = 'LEFT'```|
|UI 部品を右寄せ|```row.alignment = 'RIGHT'```|
|領域を分割|```layout.split()```|
|グループ化|```layout.box()```|
|ポップアップメッセージ|```context.window_manager.invoke_popup()```|
|ダイアログメニュー|```context.window_manager.invoke_props_dialog()```|
|ファイルブラウザ|```context.window_manager.fileselect_add()```|
|確認ポップアップ|```context.window_manager.invoke_confirm()```|
|プロパティ付きポップアップ|```context.window_manager.invoke_props_popup()```|
|検索ウィンドウ付きポップアップ|```context.window_manager.invoke_search_popup()```|
|メニューへの項目追加(末尾)|```append()```|
|メニューへの項目追加(先頭)|```prepend()```|

本節では Blender の UI を構築する方法を説明しましたが、わかりやすい UI を構築するためのポイントについては説明していません。
わかりやすい UI を構築するのはアドオンの開発と異なり、はっきりとした答えがないため非常に難しいです。
他の Blender の アドオンの UI を参考にするだけでなく、他の人が作成した Web ページやアプリの画面などにもアンテナを常に張り巡らせ、自分で良いと思ったデザインを真似して吸収していくのが、わかりやすい UI を構築する最も早い道であると思います。

本節で本書の前編は終了です。
ここまで読まれた方であれば、アドオンを作るだけでなく Python で書かれている Blender の UI も自由に変更することができるようになるでしょう。
本書の後半では、より高度なアドオンを作りたい人向けの説明を行います。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blender はボタンやメニューなどの UI 部品を追加するための API を用意しているため、 API を活用することで独自の UI を構築できる
* ツール・シェルフのタブを追加するためには、 ```bpy.types.Panel``` クラスを継承したパネルクラスを作成し、メンバ変数 ```bl_region_type``` に ```TOOLS``` を指定する必要がある
* 特定の状況下でのみメニューを表示したり、処理を実行させたりするように制限をかける場合は ```poll()``` メソッドを使用する
* パネルクラスのメンバ変数 ```bl_context``` を宣言することで、描画するコンテキストを指定することができる
* ツール・シェルフに追加したタブのヘッダーの UI を変更するためには、パネルクラスに ```draw_header()``` メソッドを定義する
* ツール・シェルフに追加したタブのメニューの UI を変更するためには、パネルクラスに ```draw()``` メソッドを定義する
* オペレータクラスに定義する ```invoke()``` メソッドは、オペレータクラスが実行された時に呼ばれるメソッドで、 ```execute()``` メソッドより前に呼ばれる
* 本節のサンプルは、アドオンから利用可能なアイコンの一覧を確認できる
* UI の構築方法を知ることとわかりやすい UI の構築することは別物である。わかりやすい UI を構築するために他人が作成した UI を参考にしよう
