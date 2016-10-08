<div id="sect_title_img_2_10"></div>

<div id="sect_title_text"></div>

# Blender の UI を制御する③

<div id="preface"></div>

###### B



## 作成するアドオンの仕様

* 以下のようなタブを *3Dビュー* エリアの *ツール・シェルフ* に追加する

![アドオンの仕様](https://dl.dropboxusercontent.com/s/ial27tu1ousllmx/specification.png "アドオンの仕様")


## アドオンを作成する

[1-4節](../chapter_01/04_Install_own_Add-on.md) を参考にして以下のソースコードを テキスト・エディタに入力し、ファイル名を ```sample_2-10.py``` として保存してください。

[import](../../sample/src/chapter_02/sample_2-10.py)


## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に作成したアドオンを有効化すると、コンソールに以下の文字列が出力されます。

```sh
サンプル2-10: アドオン「サンプル2-10」が有効化されました。
```

また、 *3Dビュー* エリアのメニュー *オブジェクト* に *項目 1* と *項目2* が追加されます。

### アドオンの機能を使用する

*3Dビュー* エリアの *ツール・シェルフ* にタブ *カスタムメニュー3* をクリックすると、カスタムメニューのメニューが表示されます。



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
サンプル2-10: アドオン「サンプル2-10」が無効化されました。
```


## ソースコードの解説


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


|UI|API|
|---|---|
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

* 本節のサンプルは、アドオンから利用可能なアイコンの一覧を確認できる
* UI の構築方法を知ることとわかりやすい UI の構築することは別物である。わかりやすい UI を構築するために他人が作成した UI を参考にしよう
