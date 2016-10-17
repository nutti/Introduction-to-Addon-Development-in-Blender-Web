<div id="sect_title_img_2_10"></div>

<div id="sect_title_text"></div>

# Blender の UI を制御する③

<div id="preface"></div>

###### [2-8節](08_Control_Blender_UI_1.md) から続いてきた Blender の UI 制御の解説の最後として、 Blender が提供する特殊な UI をアドオンから呼び出す方法について説明します。本節では、ファイルブラウザなどの利用頻度の高い UI から、検索ボックスなどあまり使われない UI まで、一通り説明しているため、必ずしも全て理解する必要はありません。



## 作成するアドオンの仕様

* 以下のようなタブを *3Dビュー* エリアの *ツール・シェルフ* に追加する

![アドオンの仕様](https://dl.dropboxusercontent.com/s/b4pvtpef8rjog0a/add-on_spec.png "アドオンの仕様")

* *ポップアップメッセージ* ボタンをクリックすると、ポップアップメッセージを表示する
* *ダイアログメニュー* ボタンをクリックすると、プロパティ設定するためのダイアログメニューを表示する
* *ファイルブラウザ* ボタンをクリックすると、 Blender が提供するファイルブラウザを表示する
* *確認ポップアップ* ボタンをクリックすると、処理の実行を確定するか否かを確認するポップアップを表示する
* *プロパティ付きポップアップ* ボタンをクリックすると、プロパティを変更するためのポップアップを表示する
* *検索ウィンドウ付きポップアップ* ボタンをクリックすると、検索ウィンドウの付いたポップアップを表示する


## アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考にして以下のソースコードを テキスト・エディタに入力し、ファイル名を ```sample_2-10.py``` として保存してください。

[import](../../sample/src/chapter_02/sample_2-10.py)


## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に作成したアドオンを有効化すると、コンソールに以下の文字列が出力されます。

```sh
サンプル2-10: アドオン「サンプル2-10」が有効化されました。
```

そして、 *3Dビュー* エリアの *ツール・シェルフ* にタブ *カスタムメニュー* が追加されます。

### アドオンの機能を使用する

*3Dビュー* エリアの *ツール・シェルフ* のタブ *カスタムメニュー* をクリックすると、カスタムメニューのメニューが表示されます。

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

|<div id="box">4</div>|*OK* ボタンを押すと *コンソール・ウィンドウ* に以下のメッセージが表示されます。|![ダイアログメニューボタン 手順4](https://dl.dropboxusercontent.com/s/voqatxxy1ht4coi/dialog_menu_4.png "ダイアログメニューボタン 手順4")|
|---|---|---|

```sh
サンプル2-10: [1] (ダイアログプロパティ 1 の値), [2] (ダイアログプロパティ 2 の値), [3] (ダイアログプロパティ 3 の識別子), [4] (ダイアログプロパティ 4 の値)
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

<div id="process"></div>

|<div id="box">3</div>|適当にファイルを開くと、*コンソール・ウィンドウ* に以下のメッセージが表示されます。|
|---|---|


```sh
サンプル2-10: [FilePath] (開いたファイルのファイルパス), [FileName] (開いたファイルのファイル名), [Directory] (開いたファイルが置かれたディレクトリ)
```


<div id="process_start_end"></div>

---


#### 確認ポップアップボタン

*確認ポップアップ* ボタンを押すと、操作を実行するか否かを問うポップアップが表示されます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|タブ *カスタムメニュー* の *確認ポップアップ* ボタンをクリックします。|![確認ポップアップボタン 手順1](https://dl.dropboxusercontent.com/s/2apytkkmilgjlpv/confirm_popup_1.png "確認ポップアップボタン 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|操作を実行するか否かを問うポップアップが表示されますので、 *確認ポップアップ* をクリックします。|![確認ポップアップボタン 手順2](https://dl.dropboxusercontent.com/s/s5vaxp8zoip01aq/confirm_popup_2.png "確認ポップアップボタン 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*コンソール・ウィンドウ* に以下のメッセージが表示されます。|
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

|<div id="box">2</div>|プロパティを変更するたびに、 *コンソール・ウィンドウ* に以下のメッセージが表示されます。|![プロパティ付きポップアップボタン 手順2](https://dl.dropboxusercontent.com/s/lpn7vxq04xyxmna/prop_popup_2.png "プロパティ付きポップアップボタン 手順2")|
|---|---|---|

```sh
サンプル2-10: [1] (プロパティ 1 の値), [2] (プロパティ 2 の値), [3] (プロパティ 3 の識別子), [4] (プロパティ 4 の値)
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

|<div id="box">3</div>|項目1・項目2・項目3の中から検索することができます。|![検索ウィンドウ付きポップアップボタン 手順3](https://dl.dropboxusercontent.com/s/jpgbjzre6sodj35/search_popup_3.png "検索ウィンドウ付きポップアップボタン 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|項目を確定すると*コンソール・ウィンドウ* に以下のメッセージが表示されます。|
|---|---|

```sh
サンプル2-10: (確定した項目の識別子) を選択しました
```

<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に有効化したアドオンを無効化すると、コンソールに以下の文字列が出力されます。

```sh
サンプル2-10: アドオン「サンプル2-10」が無効化されました。
```


## ソースコードの解説


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

## まとめ

本節では、Blender が提供する UI をアドオンから呼び出す方法について説明しました。

[2-8節](08_Control_Bnder_UI_1.md) に引き続き、本節のサンプルでも様々な API が登場しましたので、本節で紹介した UI 関連の API をまとめておきます。

|UI|API|
|---|---|
|ポップアップメッセージ|```context.window_manager.invoke_popup()```|
|ダイアログメニュー|```context.window_manager.invoke_props_dialog()```|
|ファイルブラウザ|```context.window_manager.fileselect_add()```|
|確認ポップアップ|```context.window_manager.invoke_confirm()```|
|プロパティ付きポップアップ|```context.window_manager.invoke_props_popup()```|
|検索ウィンドウ付きポップアップ|```context.window_manager.invoke_search_popup()```|

[2-8節](08_Control_Bnder_UI_1.md) から本節まで、3節にわたり Blender の UI を構築する方法を説明しましたが、わかりやすい UI を構築するためのポイントについては説明していません。
わかりやすい UI を構築するのはアドオンの開発と異なり、はっきりとした答えがないため非常に難しいです。
他の Blender の アドオンの UI を参考にするだけでなく、他の人が作成した Web ページやアプリの画面などにもアンテナを常に張り巡らせ、自分で良いと思ったデザインを真似して吸収していくのが、わかりやすい UI を構築する最も早い道であると思います。

本節で本書の前編は終了です。
ここまで読まれた方であれば、アドオンを作るだけでなく Python で書かれている Blender の UI も自由に変更することができるようになるでしょう。
本書の後半では、より高度なアドオンを作りたい人向けの説明を行います。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* ポップアップウィンドウやファイルブラウザなど、Blender が提供する特殊な UI は、実行コンテキストの ```window_manager``` を通して呼び出すことができる
* オペレータクラスに定義する ```invoke()``` メソッドは、オペレータクラスが実行された時に呼ばれるメソッドで、 ```execute()``` メソッドより前に呼ばれる
* UI の構築方法を知ることとわかりやすい UI の構築することは別物である。わかりやすい UI を構築するために他人が作成した UI を参考にしよう
