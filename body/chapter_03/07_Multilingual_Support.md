<div id="sect_title_img_3_7"></div>

<div id="sect_title_text"></div>

# アドオンを多言語に対応する

<div id="preface"></div>

###### Blenderは英語のUIがデフォルトとなっていることから、海外でも多くのCGデザイナーの方がBlenderを使っています。このため、アドオンも英語ベースのUIで構築した方がユーザ数が多くなるように思います。しかし一方で、日本語や他の言語のUIもサポートして英語が苦手な方が困らないようにしたいと考える人もいるはずです。そこで本節では、アドオンのUIを多言語対応させる方法を説明します。


## 作成するアドオンの仕様

* [3-1節](01_Handle_Mouse_Click_Event.md) のサンプルを改造し、英語と日本語のUIに対応する

## アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考にして以下のソースコードをテキスト・エディタに入力し、ファイル名 ```sample_3-7.py``` として保存してください。

[import](../../sample/src/chapter_03/sample_3-7.py)

## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に作成したアドオンを有効化すると、コンソールウィンドウに文字列が出力されます。言語を日本語にした場合には、以下の文字列が出力されます。

```sh
サンプル3-7: アドオン「サンプル3-7」が有効化されました。
```

一方、言語を英語にした場合は以下の文字列が出力されます。

```sh
Sample3-7: Enabled add-on 'Sample3-7'
```


### アドオンの機能を使用する

以下の手順に従って、作成したアドオンの機能を使ってみます。[3-1節](01_Handle_Mouse_Click_Event.md) と同じ機能を持つアドオンであるため、本節ではUIの言語を変えた時の動作確認のみ行います。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*情報* エリアのメニュー *ファイル* > *ユーザー設定...* を実行し、*システム* タブをクリックします。|![3-7節 アドオンの使用 手順1](https://dl.dropboxusercontent.com/s/1jj5f7p6r9d3fc6/use_add-on_1.png "3-7節 アドオンの使用 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*ローカライズ* のチェックボックスにチェックが入っていることを確認し、言語を *日本語 (Japanese)* に設定します。*翻訳* に配置されているボタンが3つとも選択状態であることを確認します。|![3-7節 アドオンの使用 手順2](https://dl.dropboxusercontent.com/s/cttcw6r6izqepjt/use_add-on_2.png "3-7節 アドオンの使用 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|[3-1節](01_Handle_Mouse_Click_Event.md) に従ってアドオンを使用し、コンソールウィンドウなどのメッセージやUIが日本語になっていることを確認します。|![3-7節 アドオンの使用 手順3](https://dl.dropboxusercontent.com/s/5e7rxv7fgivsilb/use_add-on_3.png "3-7節 アドオンの使用 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|手順1を行った後、*ローカライズ* のチェックボックスにチェックが入っていることを確認し、言語を *英語 (English)* に設定します。*翻訳* に配置されているボタンが3つとも選択状態であることを確認します。|![3-7節 アドオンの使用 手順4](https://dl.dropboxusercontent.com/s/7whxog1nqxo1bw5/use_add-on_4.png "3-7節 アドオンの使用 手順4")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">5</div>|[3-1節](01_Handle_Mouse_Click_Event.md) に従ってアドオンを使用し、コンソールウィンドウなどのメッセージやUIが英語になっていることを確認します。|![3-7節 アドオンの使用 手順5](https://dl.dropboxusercontent.com/s/gwha06blmyocize/use_add-on_5.png "3-7節 アドオンの使用 手順5")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に有効化したアドオンを無効化すると、コンソールウィンドウに文字列が出力されます。言語を日本語にした場合には、以下の文字列が出力されます。

```sh
サンプル3-7: アドオン「サンプル3-7」が無効化されました。
```

一方、言語を英語にした場合には以下の文字列が出力されます。

```sh
Sample3-7: Disabled add-on 'Sample3-7'
```


## ソースコードの解説

### 多言語化対応の流れ

アドオンを多言語化する流れを以下に示します。

1. 対応する言語に対する翻訳辞書を作成する
2. 翻訳辞書を登録する
3. 翻訳する箇所の文字列を、自動翻訳関数に置き換える

### 翻訳辞書の作成

Blenderは一部日本語をサポートしていますが、すべてサポートしているわけではありません。特に、公式でサポートしているのではなく自分で作成したアドオンであれば、Blenderの翻訳サポートの恩恵はほとんど受けられないと考えた方が良いです。このため対応する言語について、翻訳用の辞書をアドオン開発者が作成する必要があります。

翻訳辞書は辞書型の変数で、以下の形式で指定する必要があります。ロケールと翻訳内容で辞書を作り、翻訳内容はキーと翻訳文字列で辞書を作成するため、2重の辞書で構成されることになります。

```python
{
    locale: {
        (context, key) : translated_str,
        (context, key) : translated_str,
        ...
    },
    locale: {
        (context, key) : translated_str,
        ...
    }
    ...
}
```

上記形式における、各パラメータの意味を以下に示します。

|パラメータ|意味|
|---|---|
|```locale```|翻訳対象のロケールを指定します。日本語なら ```"jp_JP"``` 、英語なら ```"en_US"``` を指定します。ロケールの調べ方は後述します。|
|```context```|コンテキスト。基本的には ```"*"``` を指定します。|
|```key```|自動翻訳関数に指定するキー文字列を指定します。```translated_str``` に指定する文字列を指定すると良いと思います。筆者としては、文字化けしない英語がお勧めです。|
|```translated_str```|翻訳後の文字列を指定します。現在のBlenderのロケールが ```locale``` と同じで、自動翻訳関数に```key``` が指定された時に表示されます。現在のBlenderのロケールが ```locale``` に存在しない場合は、 ```key``` に指定した文字列が表示されます。|

<div id="tips"></div>

パラメータ ```context``` には ```"*"``` 以外の値も設定できるようですが、具体的に指定できる値はよくわかっていません。本パラメータ自体何を意味しているのか不明ですが、とりあえず ```"*"``` を指定しておけば正しく翻訳処理が行われます。


本節のサンプルでは、翻訳辞書として変数 ```translation_dict``` を定義しています。辞書の定義は以下の通りです。

|日本語|英語|その他|
|---|---|---|
|マウスの右クリックで面を削除|Delete Face By Right Click|Delete Face By Right Click|
|サンプル3-7: 選択範囲外です。|Sample3-7: Out of range|Sample3-7: Out of range|
|サンプル3-7: 面以外を選択しました。|Sample3-7: No face is selected|Sample3-7: No face is selected|
|サンプル3-7: 面を削除しました。|Sample3-7: Deleted Face|Sample3-7: Deleted Face|
|サンプル3-7: 削除処理を開始しました。|Sample3-7: Start deleting faces|Sample3-7: Start deleting faces|
|サンプル3-7: %d個の面を削除しました。|Sample3-7: %d face(s) are deleted|Sample3-7: %d face(s) are deleted|
|開始|Start|Start|
|終了|End|End|
|サンプル3-7: アドオン「サンプル3-7」が有効化されました。|Sample3-7: Enabled add-on 'Sample3-7'|Sample3-7: Enabled add-on 'Sample3-7'|
|サンプル3-7: アドオン「サンプル3-7」が無効化されました。|Sample3-7: Disabled add-on 'Sample3-7'|Sample3-7: Disabled add-on 'Sample3-7'|


#### Blenderに設定されたロケールを調べる方法

IT用語でロケールとは、言語や国・地域ごとに異なる表記方法の集合のことを指します。Blenderは設定されたロケールに基づいて、UIやメッセージなどの表示内容を決定します。

現在、Blenderに設定されているロケールを調べるためには、*Pythonコンソール* エリアから以下のコードを実行します。実行すると現在のロケールが文字列で表示されるため、翻訳辞書の ```locale``` に指定する文字列を確認できます。サポートする言語について、一通り確認しておくとよいでしょう。

```python
>>> bpy.app.translations.locale
'en_US'
```


### 翻訳辞書の登録

作成した翻訳辞書を登録します。翻訳辞書の登録は、```register()``` 関数の ```bpy.app.translations.register()``` 関数で行っています。

[import:"register_dict", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-7.py)

第1引数には翻訳辞書の登録先モジュールを指定しますが、```bpy.utils.register_module()``` の引数に指定した時と同様に ```__name__``` を指定することで、自身のモジュールに対して登録するようにします。第2引数には、翻訳辞書である変数を指定します。

なお登録した翻訳辞書は、```bpy.app.translations.unregister()``` 関数を用いて登録を解除する必要があります。本節のサンプルでは、```unregister()``` 関数で翻訳辞書を登録解除しています。


### 自動翻訳関数の追加

翻訳辞書の登録を行うと、Blenderの言語設定に応じて自動翻訳関数で指定したキーに対応した文字列が表示されるようになります。このため、翻訳を行いたい箇所を自動翻訳関数 ```bpy.app.translations.pgettext()``` で置き換える必要があります。

本節のサンプルでは複数の箇所に自動翻訳関数を追加していますが、ここではアドオン有効化時に表示する文字列について取り上げます。

[import:"translation_func", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-7.py)

自動翻訳関数 ```bpy.app.translations.pgettext()``` の引数には、翻訳辞書に登録されている表示したい文字列のキー文字列を指定します。上記の例では、キーに ```"Sample3-7: Enabled add-on 'Sample3-7'"``` を指定することで、ロケールが ```"en_US"``` の場合は ```"Sample3-7: Enabled add-on 'Sample3-7'"``` が、```"ja_JP"``` の場合は ```"サンプル3-7: アドオン「サンプル3-7」が有効化されました。"``` が戻り値として返ってきます。このため、ロケールが変更された時に自動的に文字列が切り替えられるようになり、翻訳が完了します。

基本的には ```bpy.app.translations.pgettext()``` を用いることで文字列の翻訳が完了しますが、本節のサンプルの以下のコードのように文字列フォーマットによる文字列を翻訳する場合は、代わりに ```bpy.app.translations.pgettext_iface()``` を用いる必要があります。

[import:"translation_func_with_format", unindent:"true"](../../sample_raw/src/chapter_03/sample_3-7.py)


## まとめ

本節ではBlenderのUIの言語を変更した時に、アドオンのUIを対応する言語へ自動的に変更する方法を説明しました。多言語化する上で必要な処理自体は多くなく、翻訳用の辞書を作成することが一番大変なところであると思います。特に翻訳する量が多い場合は、翻訳に時間を使ってしまってアドオン開発どころではなくなってしまうかもしれません。このため、正確さに少し難がありますが、Python向けに用意されている翻訳APIを利用して自動翻訳に頼ってしまう方法もあります。翻訳量と相談して利用することを検討してみてください。

特に海外に向けてアドオンを提供することを考えている方であれば、ぜひこの機会にアドオンの多言語化対応に挑戦してみてください。世界共通語といっても良い英語をサポートするだけでもアドオンを使ってくれるユーザは非常に多くなりますし、海外の方からのフィードバックを得られる機会も多くなります。フィードバックがきっかけとなり、海外のBlenderユーザと知り合いになれるかもしれません。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* アドオンの多言語対応は、開発者が作成した翻訳辞書を ```bpy.app.translations.register()``` 関数で登録し、翻訳する文字列を ```bpy.app.translations.pgettext()``` で置き換える必要がある
* Blenderがサポートする言語すべての辞書を作成するのは大変であるため、最初は英語をサポートすることから検討しよう
