---
pagetitle: 2-5. ショートカットキーを割り当てる
subtitle: 2-5. ショートカットキーを割り当てる
---

Blender本体の機能には、ショートカットキーを使って特定の操作を素早く実行できるものがあります。
例えば、*[3Dビューポート]* スペースのメニュー *[オブジェクト]* > *[トランスフォーム]* > *[移動]* で実行される機能には *[G]* キーが割り当てられてます。

Blenderの機能と同様、個人で作成したアドオンの機能にもショートカットキーを割り当てることができます。
本節では、[2-3節](03_Use_Operator_Property.html) で紹介したサンプルアドオンを改良し、アドオンの機能にショートカットキーを割り当てる方法を紹介します。


# 作成するアドオンの仕様

* [2-3節](03_Use_Operator_Property.html) で作成したサンプルアドオンを改良し、*[3Dビューポート]* スペースのメニュー *[オブジェクト]* > *[並進移動]* にショートカットキー（*[Ctrl]* + *[Alt]* + *[T]*）を割り当てる


# アドオンを作成する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして次のソースコードを入力し、ファイル名を `sample_2-5.py` として保存してください。

[@include-source pattern="full" filepath="chapter_02/sample_2-5.py"]


# アドオンを使用する

## アドオンを有効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考に作成したアドオンを有効化すると、コンソールウィンドウに次の文字列が出力されます。

```
サンプル 2-5: アドオン『サンプル 2-5』が有効化されました。
```


## アドオンの機能を使用する

*[3Dビューポート]* スペース上でオブジェクトを選択し、*[Ctrl]* + *[Alt]* + *[T]* キーを押すと、*[3Dビューポート]* スペースのメニュー *[オブジェクト]* > *[並進移動]* を実行したときと同じく、アクティブなオブジェクトが並進移動します。


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にアドオンを無効化すると、コンソールウィンドウに次の文字列が出力されます。

```
サンプル 2-5: アドオン『サンプル 2-5』が無効化されました。
```


# ソースコードの解説

## ショートカットキーの割り当て

ショートカットキーの割り当ては、`register_shortcut` 関数で行っています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-5.py" block="register_shortcut", unindent="True"]

`bpy.context.window_manager.keyconfigs.addon.keymaps` は、アドオンに割り当てられているキーマップです。

`keymaps.new` メソッドを実行することで、新たにキーマップを割り当てることができます。
本節のサンプルアドオンでは、次に示す引数を `keymaps.new` メソッドに指定して呼び出し、キーマップを割り当てています。

|引数|型|値の意味|
|---|---|---|
|`name`|`str`|キーマップ名|
|`space_type`|`str`|キーマップを割り当てるスペース名|

次に、`km.keymap_items.new` メソッドを使い、新しく割り当てたキーマップにショートカットキーを登録します。
`km.keymap_items.new` メソッドに指定する引数を、次に示します。

|引数|型|値の意味|
|---|---|---|
|`idname`|`str`|イベント発生時に実行するオペレータの処理を記述した、オペレータクラスの `bl_idname`|
|`type`|`str`|イベントを発生させるキーボードのキー|
|`value`|`str`|イベントを発生させるための条件値|
|`shift`|`bool`|イベントを発生させるために、*[Shift]* キーが押されている必要がある場合は `True`|
|`ctrl`|`bool`|イベントを発生させるために、*[Ctrl]* キーが押されている必要がある場合は `True`|
|`alt`|`bool`|イベントを発生させるために、*[Alt]* キーが押されている必要がある場合は `True`|

本節のサンプルアドオンは、*[Shift]* + *[Ctrl]* + *[T]* キーが押されたときにイベントを発生させ、オブジェクトを並進移動するオペレータを実行するように、引数を指定しています。
イベント発生時に、引数 `idname` に指定した処理を実行しますが、引数 `value` には、例えば次のようなイベント発生の条件値を指定できます。

|イベント値|値の意味|
|---|---|
|`'PRESS'`|ボタンを押したときに、イベントを発生させる|
|`'RELEASE'`|ボタンを離したときに、イベントを発生させる|
|`'ANY'`|ボタンの状態に何かしら変更があったときに、イベントを発生させる|
|`'NOTHING'`|イベントを発生させない|

最後に、割り当てたキーマップとショートカットキーのペアを、グローバル変数 `addon_keymaps` に保存します。
この変数は、アドオン無効化時に、割り当てたショートカットキーの割り当てを解除するために必要になります。


## ショートカットキーの割り当て解除

登録したショートカットキーは、アドオン無効化時に割り当てを解除する必要があります。

ショートカットキーの割り当てを解除する処理は、`unregister_shortcut` 関数に定義されています。

[@include-source pattern="partial" filepath="chapter_02/sample_2-5.py" block="unregister_shortcut", unindent="True"]

アドオン有効化時に、グローバル変数 `addon_keymaps` に保存したキーマップを、`keymap_items.remove` メソッドの引数に指定して実行することで、ショートカットキーの割り当てを解除できます。

最後に、キーマップとショートカットキーのペアを保存したグローバル変数 `addon_keymaps` をクリアします。


## 割り当てるショートカットキー

Blenderでは、すでに多くの機能にショートカットキーが割り当てられているため、ショートカットキーとして何も割り当てられていないキーを、単一のキーの中から探すのは意外と大変です。
このため、*[Ctrl]* キーや *[Shift]* キー、*[Alt]* キーと組み合わせたショートカットキーを割り当てることも検討しましょう。
これらのキーと組み合わせることで、すでに割り当てられているキーと被る可能性を低くでき、より簡単に空いているキーを見つけることができると思います。
本節のサンプルアドオンでも、*[Ctrl]* キーや *[Alt]* キーを組み合わせたショートカットキーを登録しています。

割り当てるショートカットキーは、ショートカットキーに割り当てた機能を簡単に推測できるようなものにしましょう。
ショートカットキーを割り当てる機能であるオブジェクトの並進移動は、英訳するとTranslate Objectになるため、本節のサンプルアドオンでは英訳の頭文字を取って *[T]* キーを割り当てています。


# まとめ

[2-3節](03_Use_Operator_Property.html) を改造し、*[3Dビューポート]* スペースのメニュー *[オブジェクト]* > *[並進移動]* にショートカットキーを割り当て、ショートカットキーからオペレータを実行できるようにしました。

ショートカットキーをオペレータに割り当てることで、ユーザがオペレータをより素早く実行できるようになります。
頻繁に使う機能に対してショートカットキーを割り当てることは、アドオンの利便性の改善につながる可能性があります。
一方、ショートカットキーに設定できるキーの組み合わせには限りがあるため、ショートカットキーを乱用してユーザが利用可能なショートカットキーを減らしてしまうのは、よいとは言えません。

アドオンをさまざまな人に使ってもらうことを考えている場合は、ショートカットキーによってユーザの利便性が本当に向上するのかを検討してから設定すべきです。
個人的に利用するアドオンではない限り、試しにショートカットキーを割り当ててみたとか、とりあえず割り当てとけばよいという程度の判断で、ショートカットキーを設定すべきではありません。


## ポイント

* スペースごとのキーマップを割り当てたあとに、キーマップに対してショートカットキーを割り当てることで、オペレータにショートカットキーを割り当てることができる
* キーマップは、`bpy.context.window_manager.keyconfigs.addon.keymaps.new` メソッドを実行することで、割り当てることができる
* ショートカットキーは、 キーマップ `km` に対して `km.keymap_items.new` メソッドを実行することで、割り当てることができる
* アドオン有効化時に割り当てたショートカットキーは、アドオン無効化時に割り当てを解除する必要がある
