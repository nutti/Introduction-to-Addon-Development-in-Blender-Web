<div id="sect_title_img_2_10"></div>

<div id="sect_title_text"></div>

# BlenderのUIを制御する③

<div id="preface"></div>

###### [2-8節](08_Control_Blender_UI_1.md) から続けてきたBlenderのUI制御の解説ですが、本節ではその締めくくりとしてBlenderが提供する特殊なUIをアドオンから呼び出す方法について説明します。本節では、ファイルブラウザなどの利用頻度の高いUIから検索ボックスなどのあまり使われないUIまで一通り説明します。


## 作成するアドオンの仕様

* 以下のようなタブを *3Dビュー* エリアのツール・シェルフに追加する

<div id="centerize_img"></div>

![アドオンの仕様](https://dl.dropboxusercontent.com/s/b4pvtpef8rjog0a/add-on_spec.png "アドオンの仕様")

* *ポップアップメッセージ* ボタンをクリックすると、ポップアップメッセージを表示する
* *ダイアログメニュー* ボタンをクリックすると、プロパティを設定するためのダイアログメニューを表示する
* *ファイルブラウザ* ボタンをクリックすると、Blenderが提供するファイルブラウザを表示する
* *確認ポップアップ* ボタンをクリックすると、処理の実行を確定するか中断するかを確認するためのポップアップを表示する
* *プロパティ付きポップアップ* ボタンをクリックすると、プロパティを変更するためのポップアップを表示する
* *検索ウィンドウ付きポップアップ* ボタンをクリックすると、検索ウィンドウの付いたポップアップを表示する


## アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考にして以下のソースコードを入力し、ファイル名を ```sample_2-10.py``` として保存してください。

[import](../../sample/src/chapter_02/sample_2-10.py)


## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に作成したアドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル2-10: アドオン「サンプル2-10」が有効化されました。
```

そして、*3Dビュー* エリアのツール・シェルフにタブ *カスタムメニュー* が追加されます。

### アドオンの機能を使用する

*3Dビュー* エリアのツール・シェルフのタブ *カスタムメニュー* をクリックすると、カスタムメニューのメニューが表示されます。

*カスタムメニュー* タブに設置されたボタンをクリックし、動作を確認します。

#### ポップアップメッセージボタン

*ポップアップメッセージ* ボタンを押すと、ポップアップメッセージが表示されます。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *ポップアップメッセージ* ボタンをクリックします。|![ポップアップメッセージボタン 手順1](https://dl.dropboxusercontent.com/s/os3tka7asic48ai/popup_message_1.png "ポップアップメッセージボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|クリックした場所にポップメッセージが表示されます。|![ポップアップメッセージボタン 手順2](https://dl.dropboxusercontent.com/s/uf3j7u0ezi92uqd/popup_message_2.png "ポップアップメッセージボタン 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---


#### ダイアログメニューボタン

*ダイアログメニュー* ボタンを押すと、4つのプロパティと *OK* ボタン付きのダイアログメニューが表示されます。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *ダイアログメニュー* ボタンをクリックします。|![ダイアログメニューボタン 手順1](https://dl.dropboxusercontent.com/s/p63yfu6yh8ddnrt/dialog_menu_1.png "ダイアログメニューボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|クリックした場所にダイアログメニューが開きます。|![ダイアログメニューボタン 手順2](https://dl.dropboxusercontent.com/s/jjf8bfxa4x77dqv/dialog_menu_2.png "ダイアログメニューボタン 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|ダイアログメニュー上のプロパティは変更することができます。|![ダイアログメニューボタン 手順3](https://dl.dropboxusercontent.com/s/wujq9rb6rp2k0vx/dialog_menu_3.png "ダイアログメニューボタン 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*OK* ボタンを押すとスクリプト実行ログに以下のメッセージが表示されます。|![ダイアログメニューボタン 手順4](https://dl.dropboxusercontent.com/s/voqatxxy1ht4coi/dialog_menu_4.png "ダイアログメニューボタン 手順4")|
|---|---|---|

```sh
サンプル2-10: [1] (ダイアログプロパティ 1の値), [2] (ダイアログプロパティ 2の値), [3] (ダイアログプロパティ 3の識別子),
[4] (ダイアログプロパティ 4の値)
```


<div id="process_start_end"></div>

---


#### ファイルブラウザボタン

*ファイルブラウザ* ボタンを押すと、ファイルブラウザが表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *ファイルブラウザ* ボタンをクリックします。|![ファイルブラウザボタン 手順1](https://dl.dropboxusercontent.com/s/xi29nw88hvy9k6w/file_browser_1.png "ファイルブラウザボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|ファイルブラウザが開きます。|![ファイルブラウザボタン 手順2](https://dl.dropboxusercontent.com/s/o2xy1e08aiu6xj8/file_browser_2.png "ファイルブラウザボタン 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|適当にファイルを開くと、スクリプト実行ログに以下のメッセージが表示されます。|
|---|---|


```sh
サンプル2-10: [FilePath] (開いたファイルのファイルパス), [FileName] (開いたファイルのファイル名),
[Directory] (開いたファイルが置かれたディレクトリ)
```


<div id="process_start_end"></div>

---


#### 確認ポップアップボタン

*確認ポップアップ* ボタンを押すと、操作を実行するか中断するかを問うポップアップが表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *確認ポップアップ* ボタンをクリックします。|![確認ポップアップボタン 手順1](https://dl.dropboxusercontent.com/s/2apytkkmilgjlpv/confirm_popup_1.png "確認ポップアップボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|操作を実行するか中断するかを問うポップアップが表示されるので、*確認ポップアップ* をクリックします。|![確認ポップアップボタン 手順2](https://dl.dropboxusercontent.com/s/s5vaxp8zoip01aq/confirm_popup_2.png "確認ポップアップボタン 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|スクリプト実行ログに以下のメッセージが表示されます。仮に、*確認ポップアップ* をクリックしなかった場合は、処理が中断されます。|
|---|---|

```
サンプル2-10: 確認ポップアップボタンをクリックしました
```

<div id="process_start_end"></div>

---


#### プロパティ付きポップアップボタン

*プロパティ付きポップアップ* ボタンを押すと、4つのプロパティがポップアップで表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *プロパティ付きポップアップ* ボタンをクリックします。|![プロパティ付きポップアップボタン 手順1](https://dl.dropboxusercontent.com/s/4nh5dtfsg597bwf/prop_popup_1.png "プロパティ付きポップアップボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|プロパティを変更するたびに、*スクリプト実行ログ* に以下のメッセージが表示されます。|![プロパティ付きポップアップボタン 手順2](https://dl.dropboxusercontent.com/s/lpn7vxq04xyxmna/prop_popup_2.png "プロパティ付きポップアップボタン 手順2")|
|---|---|---|

```sh
サンプル2-10: [1] (プロパティ 1の値), [2] (プロパティ 2の値), [3] (プロパティ 3の識別子), [4] (プロパティ 4の値)
```

<div id="process_start_end"></div>

---



#### 検索ウィンドウ付きポップアップボタン

*検索ウィンドウ付きポップアップ* ボタンを押すと、検索ウィンドウがポップアップで表示されます。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *検索ウィンドウ付きポップアップ* ボタンをクリックします。|![検索ウィンドウ付きポップアップボタン 手順1](https://dl.dropboxusercontent.com/s/6cx6smtn2gz44qo/search_popup_1.png "検索ウィンドウ付きポップアップボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|検索ウィンドウ付きポップアップが表示されます。|![検索ウィンドウ付きポップアップボタン 手順2](https://dl.dropboxusercontent.com/s/twu5ds60i0ptgi0/search_popup_2.png "検索ウィンドウ付きポップアップボタン 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*項目1*・*項目2*・*項目3*の中から検索することができます。|![検索ウィンドウ付きポップアップボタン 手順3](https://dl.dropboxusercontent.com/s/jpgbjzre6sodj35/search_popup_3.png "検索ウィンドウ付きポップアップボタン 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|項目を確定するとスクリプト実行ログに以下のメッセージが表示されます。|
|---|---|

```sh
サンプル2-10: (確定した項目の識別子) を選択しました
```

<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル2-10: アドオン「サンプル2-10」が無効化されました。
```



## ソースコードの解説


#### ポップアップメッセージを表示する

ポップアップメッセージを表示する方法について説明します。

ポップアップメッセージを表示するためのオペレータクラスを、以下に示します。

[import:"ops_show_popup_message"](../../sample_raw/src/chapter_02/sample_2-10.py)


ポップアップメッセージの表示はボタンを押したときに呼ばれる ```invoke()``` メソッドで行っています。

```invoke()``` メソッドは、処理が実行された時に呼ばれるメソッドです。```execute()``` メソッドも処理が実行された時に呼ばれますが、```execute()``` メソッドの引数にはなかったイベント ```event``` を受け取る点が異なります。[3-1節](../chapter_03/01_Handle_Mouse_Click_Event.md) でも説明しますが、引数 ```event``` には ```invoke()``` メソッドが呼ばれた時のマウスの位置や発生したキーイベントなどの情報が含まれています。また、```invoke()``` と ```execute()``` が2つ定義されていた場合、メニューの項目を選択した時やボタンを押したなどのUIから操作を行うと ```invoke()``` が優先的に呼ばれます。一方、[2-2節](../chapter_02/02_Register_Multiple_Operation_Classes.md) で説明した ```bpy.ops.<オペレーションクラスのbl_idname>``` を実行すると ```execute()``` が呼び出されます。

このようにユーザからの入力を積極的に使いたい場合や、```invoke()``` メソッドで前処理を行った後に ```bpy.ops.<オペレーションクラスのbl_idname>``` を実行じて ```excute()``` を呼び出したい場合に ```invoke()``` メソッドを利用します。

本節のサンプルでは、```invoke()``` メソッド内で ```wm.invoke_popup()``` 関数を次に示す引数を指定して実行しています。

|引数|型|意味|
|---|---|
|第1引数|オペレータクラス|オペレータクラスのインスタンス|
|```width```|整数|ポップアップメッセージの横幅|
|```height```|整数|ポップアップメッセージの縦幅(UIに応じて自動的に調整されるため効果なし)|

```wm.invoke_popup()``` 関数により表示されるポップアップのUIは、```draw()``` メソッドで定義します。本節のサンプルでは、```メッセージ``` と書かれたラベルを表示しています。

```wm.invoke_popup()``` 関数の戻り値は ```{'RUNNING_MODAL'}``` ですが、本節では説明を省略します。ポップアップメッセージを表示する時には、```wm.invoke_popup()``` 関数を ```invoke()``` メソッドの戻り値に指定すればよいということだけを覚えておきましょう。

*ポップアップメッセージ* ボタンを配置する処理を以下に示します。

[import:"show_popup_message", unindent:"true"](../../sample_raw/src/chapter_02/sample_2-10.py)


#### ダイアログメニューを表示する

ポップアップメッセージの応用として、ポップアップからプロパティを入力できるダイアログメニューを表示することもできます。ダイアログメニューを表示するためには、```context.window_manager.invoke_props_dialog()``` 関数を使用します。

ダイアログメニューを表示するオペレータクラスを以下に示します。

[import:"ops_show_dialog_menu"](../../sample_raw/src/chapter_02/sample_2-10.py)

```ShowDialogMenu``` クラスには4つのプロパティクラスの変数が宣言されていて、ダイアログメニューではこれらのプロパティを表示します。ダイアログメニューの表示は ```wm.invoke_props_dialog()``` 関数で行います。引数には、ダイアログメニューに表示するプロパティクラスの変数を持つオペレータクラスのインスタンスを渡します。

```wm.invoke_props_dialog()``` 関数の引数を以下に示します。

|引数|型|意味|
|---|---|
|第1引数|オペレータクラスのインスタンス|*OK* ボタンを押したときに、引数に指定したインスタンスの ```execute()``` メソッドが実行される。また、ダイアログメニューのプロパティは本引数に指定したインスタンスに定義したプロパティクラスの変数が表示される|
|```width```|整数|ポップアップメッセージの横幅|
|```height```|整数|ポップアップメッセージの縦幅(UIに応じて自動的に調整されるため効果なし)|

```wm.invoke_props_dialog()``` 関数の戻り値は、ポップアップメッセージと同様に```{'RUNNING_MODAL'}``` ですが、本節では説明を省略します。ダイアログメニューを表示する時には、```wm.invoke_props_dialog()``` 関数を ```invoke()``` メソッドの戻り値に指定すればよいということだけを覚えておきましょう。

ダイアログメニューに表示された *OK* ボタンを押すと、```execute()``` メソッドが実行されます。
```execute()``` メソッドでは、ダイアログメニューのプロパティに指定した値をスクリプト実行ログに出力します。
ダイアログメニューで指定したプロパティの値でアドオンの処理を実行したいときに活用しましょう。

*ダイアログメニュー* ボタンを配置する処理を以下に示します。

[import:"show_dialog_menu", unindent:"true"](../../sample_raw/src/chapter_02/sample_2-10.py)


#### ファイルブラウザを表示する

ファイルを開いたり保存したりする時など、Blender標準の機能を使用した場合でも、ファイルを選択するためのファイルブラウザを表示する機能が存在します。アドオンからファイルブラウザを表示するためには、```context.window_manager.fileselect_add()``` 関数を利用します。

本節のサンプルでは、以下のコードでファイルブラウザを表示しています。

[import:"ops_show_file_browser"](../../sample_raw/src/chapter_02/sample_2-10.py)

ファイルブラウザを表示するためには、```invoke()``` メソッド内で ```wm.fileselect_add()``` 関数を呼ぶ必要があります。引数には、ファイルブラウザ内でファイルを確定した時に実行される ```execute()``` メソッドが定義されたオペレータクラスのインスタンスを指定します。```invoke()``` メソッドの戻り値は、```{'RUNNING_MODAL'}``` にする必要があります。

ファイルブラウザで確定したファイルの情報を保存するために、クラス変数 ```filepath``` , ```filename``` , ```directory``` を宣言しています。**ファイルブラウザからファイルの情報を受け取るためには、本節のサンプルと同じ変数名にする** 必要があることに注意が必要です。なお、```filepath``` や ```directory``` は、プロパティクラス ```StringProperty``` の引数 ```subtype``` にファイルパスを格納するプロパティであることを示す ```FILE_PATH``` を指定する必要があります。

ファイルブラウザでファイルを確定すると ```execute()``` メソッドが呼ばれ、確定したファイルパス・ファイル名・ファイルが置かれたディレクトリをスクリプト実行ログに表示します。

最後に、*ファイルブラウザ* ボタンを配置する処理を以下に示します。

[import:"show_file_browser", unindent:"true"](../../sample_raw/src/chapter_02/sample_2-10.py)


#### 実行確認のポップアップを表示する

Blenderの機能の中には、実行する前に処理を実行するか中断するかを確認するためのポップアップを表示する機能があります。例えば、*情報* エリアのメニュー *ファイル* > *スタートアップファイルを保存* は、実行確認のポップアップを表示する例の1つです。

実行確認のポップアップは、```context.window_manager.invoke_confirm()``` 関数により表示することができます。

本節のサンプルでは、以下のコードで実行確認のポップアップを表示しています。

[import:"ops_show_confirm_popup"](../../sample_raw/src/chapter_02/sample_2-10.py)


実行確認のポップアップは、```invoke()``` メソッド内から ```wm.invoke_confirm()``` 関数を呼び出して表示しています。

```vm.invoke_confirm()``` 関数の引数を以下に示します。

|引数|意味|
|---|---|
|第1引数|実行確認ポップアップにて処理の実行を決定したときに呼び出される ```execute()``` メソッドが定義されたオペレータクラスのインスタンス|
|第2引数|```invoke()``` メソッドの引数 ```event``` を指定|

*確認ポップアップ* ボタンを配置する処理を以下に示します。

[import:"show_confirm_popup", unindent:"true"](../../sample_raw/src/chapter_02/sample_2-10.py)


#### プロパティ付きポップアップを表示する

値を変更することができる、プロパティ付きポップアップを作ることもできます。実行結果を見るとダイアログメニューと同じ動きに見えますが、ダイアログメニューは *OK* ボタンを押すまで処理が実行されないのに対し、**プロパティ付きポップアップではプロパティを変更するたびに処理が実行されます。**

本節のサンプルでは、以下のようにしてプロパティ付きポップアップを表示しています。

[import:"ops_show_property_popup"](../../sample_raw/src/chapter_02/sample_2-10.py)


プロパティ付きポップアップは、```invoke()``` メソッド内から ```context.window_manager.invoke_props_popup()``` 関数を実行することで表示することができます。プロパティを変更すると ```execute()``` メソッドが実行され、 現在のプロパティの値がスクリプト実行ログに表示されます。

```wm.invoke_props_popup()``` 関数には、以下に示す引数を指定します。

|引数|意味|
|---|---|
|第1引数|プロパティを変えた時に呼び出される ```execute()``` メソッドが定義されたオペレータクラスのインスタンス|
|第2引数|```invoke()``` メソッドの引数 ```event``` を指定|

なお、プロパティ付きポップアップで表示されたプロパティは、ツール・シェルフのオプションにも表示されているため、ポップアップが閉じてしまった場合でも他の操作を行わなわない限り変更することができます。

*プロパティ付きポップアップ* ボタンを配置する処理を以下に示します。

[import:"show_property_popup", unindent:"true"](../../sample_raw/src/chapter_02/sample_2-10.py)


#### 検索ウィンドウ付きポップアップを表示する

あらかじめ登録した項目の中から検索することができる、検索ウィンドウ付きのポップアップを表示することができます。実際このUIがどのように役立つのか、筆者もよくわかっていませんが、BlenderのAPIとして用意されているので紹介します。

本節のサンプルでは、検索ウィンドウ付きポップアップを以下のコードにより表示します。

[import:"ops_show_search_popup"](../../sample_raw/src/chapter_02/sample_2-10.py)


検索ウィンドウ付きのポップアップを表示するためには、```invoke()``` メソッド内で ```context.window_manager.invoke_search_popup()``` 関数を使います。引数には、項目確定時に呼び出される ```execute()``` メソッドが定義されたクラスのインスタンスを指定します。なお ```invoke()``` メソッドは ```{'FINISHED'}``` を返す必要があります。

項目を確定すると ```execute()``` メソッドが呼び出され、選択した項目の識別子がスクリプト実行ログに表示されます。

検索ウィンドウで検索できる項目は、**アドオン開発者が追加する** 必要があります。検索ウィンドウへ追加する項目リストを持つ変数は ```EnumProperty``` クラスの型で定義する必要があり、クラス変数 ```bl_property``` に定義した変数名を代入する必要があります。本節のサンプルではクラス変数 ```item``` が項目リストであるため、 ```bl_property="item"``` とします。

最後に、*検索ウィンドウ付きポップアップ* ボタンを配置する処理を以下に示します。

[import:"show_search_popup", unindent:"true"](../../sample_raw/src/chapter_02/sample_2-10.py)

<div id="space_s"></div>

## まとめ

本節では、Blenderが提供するUIをアドオンから呼び出す方法について説明しました。

[2-9節](09_Control_Blender_UI_2.md) に引き続き本節のサンプルでも様々なAPIが登場しましたので、本節で紹介したUI関連のAPIをまとめておきます。

|UI|API|
|---|---|
|ポップアップメッセージ|```context.window_manager.invoke_popup()```|
|ダイアログメニュー|```context.window_manager.invoke_props_dialog()```|
|ファイルブラウザ|```context.window_manager.fileselect_add()```|
|確認ポップアップ|```context.window_manager.invoke_confirm()```|
|プロパティ付きポップアップ|```context.window_manager.invoke_props_popup()```|
|検索ウィンドウ付きポップアップ|```context.window_manager.invoke_search_popup()```|

[2-8節](08_Control_Blender_UI_1.md) から本節まで3節にわたりBlenderのUIを構築する方法を説明しましたが、わかりやすいUIを構築するためのポイントについては説明していません。わかりやすいUIを構築するのはアドオンの開発とは異なり、明確な答えがありません。他の方が開発されたアドオンのUIを参考にするだけでなく、**世の中に公開されているWebページやアプリの画面などにもアンテナを常に張り巡らせ、自分で良いと思ったデザインを真似して吸収していく** ことが、わかりやすいUIを構築するための早道であると思います。

本節で前編は終わりです。ここまで読まれた方であれば、アドオンを作るだけでなくPythonで書かれているBlenderのUIも自由に変更することができるようになっていることでしょう。後編では、より高度なアドオンを作りたい人向けの話題を取り上げます。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* ポップアップウィンドウやファイルブラウザなど、Blenderが提供する特殊なUIは、実行コンテキストの ```window_manager``` を通して呼び出すことができる
* オペレータクラスに定義する ```invoke()``` メソッドと ```execute()``` メソッドは、引数にイベント情報を受け取らない点で異なる
* メニューやボタンからオペレータクラスの処理を実行する場合は、```invoke()``` メソッドが優先的に実行される
* ```bpy.ops.<オペレーションクラスのbl_idname>``` オペレータクラスの処理を実行した場合は、```execute()``` メソッドが優先的に実行される
* UIの構築方法を知ることと、わかりやすいUIを構築することは別である。わかりやすいUIを構築するために他の方が作成したUIを参考にしよう

<div id="space_page"></div>
