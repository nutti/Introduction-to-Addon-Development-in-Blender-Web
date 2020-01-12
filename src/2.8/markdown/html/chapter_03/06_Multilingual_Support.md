---
pagetitle: 3-6. アドオンのUIを複数の言語に対応する
subtitle: 3-6. アドオンのUIを複数の言語に対応する
---

BlenderのUIは英語がデフォルトであることから、海外でも多くの3DCGデザイナーがBlenderを使ってCGを作成しています。
このため、アドオンのUIも英語ベースで構築するほうが、アドオンを使ってくれる人が多くなります。
しかし一方で、英語が苦手な方が困らないように、日本語などの英語以外の言語をサポートしたいと思う人もいると思います。
そこで本節では、アドオンのUIを複数の言語に対応する方法を説明します。


# 作成するアドオンの仕様

本節ではアドオンのUIを複数の言語に対応させる方法について説明するため、新たな機能は作らずに前に紹介したサンプルを改造します。
このため、本節では次のような仕様のアドオンを作成します。

* [2-5節](05_Allocate_Shortcut_Keys.html) のサンプルを改造し、英語と日本語のUIに対応する


# アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にして次のソースコードを入力し、ファイル名 `sample_3-6.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3-6.py"]


# アドオンを使用する


## アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考に作成したアドオンを有効化すると、コンソールウィンドウに文字列が出力されます。
言語を日本語にした場合には、以下の文字列が出力されます。

```
サンプル 3-6: アドオン『サンプル 3-6』が有効化されました。
```

一方、言語を英語にした場合は以下の文字列が出力されます。

```
Sample 3-6: Add-on 'Sample 3-6' is enabled
```


## アドオンの機能を使用する

有効化したアドオンの機能を使い、動作を確認します。
[2-5節](05_Allocate_Shortcut_Keys.html) と同じ機能を持つアドオンであるため、本節ではUIの言語を変えたときの動作確認方法の手順のみ説明します。

<div class="work"></div>

|||
|---|---|
|1|トップバーから *[編集]* > *[プリファレンス...]* を実行して表示された *[Blenderプリファレンス]* ウィンドウより、*[インターフェース]* ボタンをクリックします。<br>![](../../images/chapter_03/06_Multilingual_Support/use_add-on_1.png "サンプルアドオン3-7 手順1")|
|2|*[翻訳]* のチェックボックスにチェックが入っていることを確認し、言語を *[日本語 (Japanese)]* に設定します。また、配置されている3つのチェックボックスにチェックが入っていることを確認します。<br>![](../../images/chapter_03/06_Multilingual_Support/use_add-on_2.png "サンプルアドオン3-7 手順2")|
|3|[2-5節](05_Allocate_Shortcut_Keys.html) にしたがってアドオンを使用し、UIやコンソールウィンドウなどに表示されるメッセージが、日本語になっていることを確認します。<br>![](../../images/chapter_03/06_Multilingual_Support/use_add-on_3.png "サンプルアドオン3-7 手順3")|
|4|手順1を行った後、*[翻訳]* のチェックボックスにチェックが入っていることを確認し、言語を *[英語 (English)]* に設定します。また、配置されている3つのチェックボックスにチェックが入っていることを確認します。<br>![](../../images/chapter_03/06_Multilingual_Support/use_add-on_4.png "サンプルアドオン3-7 手順4")|
|5|[2-5節](05_Allocate_Shortcut_Keys.html) にしたがってアドオンを使用し、UIやコンソールウィンドウなどに表示されるメッセージが英語になっていることを確認します。<br>![](../../images/chapter_03/06_Multilingual_Support/use_add-on_5.png "サンプルアドオン3-7 手順5")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.html) を参考にしてアドオンを無効化すると、コンソールウィンドウに文字列が出力されます。
言語を日本語にした場合には、以下の文字列が出力されます。

```
サンプル 3-6: アドオン『サンプル 3-6』が無効化されました。
```

一方、言語を英語にした場合には以下の文字列が出力されます。

```
Sample 3-6: Add-on 'Sample 3-6' is disabled
```


# ソースコードの解説

本節のサンプルアドオンは、[2-5節](05_Allocate_Shortcut_Keys.html) のサンプルを改造したものであるため、[2-5節](05_Allocate_Shortcut_Keys.html) で説明した処理については説明せず、複数の言語に対応する方法についてのみ説明します。


## 複数言語への対応方法

本書を読みはじめたときに、「Blender自体が公式で日本語に対応しているため、アドオン側で何もしなくても自動的に翻訳してくれるのでは？」と思う人がいるかもしれません。
しかし、Blenderが日本語に対応しているのはあくまで公式の機能のみであり、個人で作成したアドオンなどは、日本語を選んだとしても日本語に変換されずに英語のまま表示されます。
このため、アドオンのUIを日本語に対応するためには、アドオン側で対応が必要になります。
具体的には、次に示す手順でアドオンを複数の言語に対応させます。

1. 対応する言語に対する翻訳辞書を作成する
2. 翻訳辞書を登録する
3. 翻訳箇所の文字列を自動翻訳関数に置き換える


## 1. 対応する言語に対する翻訳辞書を作成する

前述したように、日本語に対応しているのはBlender公式の機能のみです。
アドオン開発者が何も対応することなく、Blenderが自動的にアドオンのUIを日本語に翻訳してくれる部分は、ほとんどないと思ったほうがよいでしょう。
このため、Blenderが翻訳できないところは、アドオン開発者が翻訳後（日本語）のテキストをBlenderに教えてあげる必要があります。
このとき必要になってくるのが、翻訳後のテキストと翻訳前（英語）のテキストを結びつける **翻訳辞書** と呼ばれるものです。
人間がわからない単語を辞書で調べて翻訳後の単語を知るのと同じように、わからない単語（テキスト）をBlenderが翻訳辞書で調べることで、翻訳後の単語（テキスト）を知ることができます。
ここで単語（テキスト）と書いたのは、単語だけでなくテキスト（文字列）も、翻訳辞書に登録することができるからです。

登録する翻訳辞書はdict型の変数で、次に示す形式で指定する必要があります。
基本的には、ロケールごとにキーと翻訳語のテキストのペアを指定して、辞書を作っていきます。
このため、翻訳辞書は2段のdict型から構成されることになります。

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

上記のdict型に指定するそれぞれの値の意味を次に示します。

|値|意味|
|---|---|
|`locale`|翻訳対象のロケールを指定します。日本語なら `"jp_JP"` 、英語なら `"en_US"` を指定します。ロケールの調べ方は後述します。|
|`context`|コンテキストを指定します。基本的には `"*"` を指定します。|
|`key`|自動翻訳関数（後述）に指定するキー文字列を指定します。同じ `key` に対して指定した、いずれかの `locale` に属する `translated_str` の文字列を指定するとよいと思います。もし作成したアドオンが英語をサポートするのであれば、文字化けしない英語を指定するのがおすすめです。|
|`translated_str`|翻訳後の文字列を指定します。現在のBlenderのロケールが `locale` と同じ、かつ自動翻訳関数に`key` が指定されたとき、本パラメータに指定した文字列が表示されます。現在のBlenderのロケールがいずれの `locale` にも存在しない場合は、`key` に指定した文字列が表示されます。|


<div class="column">
パラメータ `context` には `"*"` 以外の値も設定できるようですが、指定できる具体的な値はよくわかっていません。
本パラメータを指定する意味がわからない状態で、APIを使用するのはあまりよいとは言えませんが、とりあえず `"*"` を指定しておけば正しく翻訳処理が行われるようです。
</div>


本節のサンプルでは、翻訳辞書としてグローバル変数 `translation_dict` を定義しています。
辞書の登録により、それぞれのロケールで次のように翻訳されます。
なお、`key` にロケールが英語のときの翻訳語の文字列を指定することで、日本語や英語以外のロケールが指定されたときに英語の文字列が表示されるようにしました。

|日本語|英語|その他（keyに指定する文字列）|
|---|---|---|
|並進移動|Translate object|Translate object|
|アクティブなオブジェクトを並進移動します|Translate active object|Translate active object|
|移動軸|Translation axis|Translation axis|
|移動軸を設定します|Set translation axis|Set translation axis|
|X軸|X-axis|X-axis|
|X軸に沿って並進移動します|Translate along X-axis|Translate along X-axis|
|Y軸|Y-axis|Y-axis|
|Y軸に沿って並進移動します|Translate along Y-axis|Translate along Y-axis|
|Z軸|Z-axis|Z-axis|
|Z軸に沿って並進移動します|Translate along Z-axis|Translate along Z-axis|
|移動量|Translation amount|Translation amount|
|移動量を設定します|Set translation amount|Set translation amount|
|サンプル 3-6: 『%s』を%s軸方向へ %f 並進移動しました。|Sample 3-6: Translated object '%s' (Axis: %s, Amount: %f)|Sample 3-6: Translated object '%s' (Axis: %s, Amount: %f)|
|サンプル 3-6: オペレータ『%s』が実行されました。|Sample 3-6: Executed operator '%s'|Sample 3-6: Executed operator '%s'|
|サンプル 3-6: アドオン『サンプル 3-6』が有効化されました。|Sample 3-6: Add-on 'Sample 3-6' is enabled|Sample 3-6: Add-on 'Sample 3-6' is enabled|
|サンプル 3-6: アドオン『サンプル 3-6』が無効化されました。|Sample 3-6: Add-on 'Sample 3-6' is disabled|Sample 3-6: Add-on 'Sample 3-6' is disabled|


### Blenderに設定されたロケールを調べる方法

ロケールはIT用語であり、言語や国・地域ごとに異なる表記方法の集合のことを指します。
ロケールを変えると、表示方法が指定したロケールの表記方法に従って、表示されるようになります。
ロケールを日本語に設定した場合は、UInなどの表示が日本語になりますし、ロケールを英語にすれば英語で表示されるようになります。
Blenderもこのロケールに従って、UIやメッセージなどの表示内容を決定します。

Blenderに設定されているロケールを調べるためには、*[Pythonコンソール]* スペースから次のコードを実行します。
コードを実行すると、現在設定されているロケールが文字列で表示されます。
ここで表示された文字列は、翻訳辞書の `locale` に指定する文字列に対応します。
アドオンでサポートする全ての言語について、ロケールを一通り確認しておくとよいでしょう。

```python
>>> bpy.app.translations.locale
'ja_JP'
```

## 2. 翻訳辞書を登録する

作成した翻訳辞書をBlenderに登録します。
サンプルアドオンでは、`register` 関数において `bpy.app.translations.register` 関数を呼び出すことで翻訳辞書を登録します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-6.py" block="register_dict"]

`bpy.app.translations.register` 関数の第1引数には、翻訳辞書の登録先モジュールを指定します。
引数に `__name__` を指定することで、自身のモジュールに対して翻訳辞書を登録できます。
`bpy.app.translations.register` 関数の第2引数には、翻訳辞書を定義した変数を指定します。

なお、登録した翻訳辞書は、不要になった時点で `bpy.app.translations.unregister` 関数を呼び出して登録を解除する必要があります。
サンプルアドオンでは、アドオンを無効化したときに翻訳辞書を登録解除するため、`unregister` 関数の処理内で `bpy.app.translations.unregister` 関数を呼び出します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-6.py" block="unregister_dict"]


## 3. 翻訳箇所の文字列を自動翻訳関数に置き換える

翻訳辞書を登録すると、Blenderの現在の言語設定（ロケール）に従って、**自動翻訳関数**で指定したキーに対応した文字列が表示されるようになります。
このため、翻訳を行いたい箇所を自動翻訳関数 `bpy.app.translations.pgettext` 関数で置き換えます。

本節のサンプルアドオンでは、複数の箇所で自動翻訳関数を呼び出していますが、ここではアドオン有効化時にコンソールウィンドウへ文字列を表示する部分について見てみましょう。

[@include-source pattern="partial" filepath="chapter_03/sample_3-6.py" block="translation_func"]

自動翻訳関数 `bpy.app.translations.pgettext` 関数の引数には、翻訳辞書に登録した表示したい翻訳後の文字列 `translated_str` に対応する `key` に指定した文字列を指定します。
上記の例では、引数に `"Sample 3-6: Add-on 'Sample 3-6' is enabled"` を指定することで、ロケールが英語（`"en_US"`）の場合は `"Sample 3-6: Add-on 'Sample 3-6' is enabled"` が、ロケールが日本語（`"ja_JP"`）の場合は `"サンプル 3-6: アドオン『サンプル 3-6』が有効化されました。"` が、`bpy.app.translations.pgettext` 関数の戻り値として返ります。
関数の戻り値を `print` 関数で表示することで、ロケールに応じてコンソールウィンドウに出力される文字列が変わるため、ユーザがBlenderの言語設定を変えたときに、あたかも自動的に翻訳されているようにみえます。

なお、`bpy.app.translations.pgettext` 関数を用いることで文字列を翻訳できますが、次に示す処理のように、文字列フォーマットを用いた文字列を翻訳する場合は、 `bpy.app.translations.pgettext_iface` 関数を用いる必要があることに注意が必要です。

[@include-source pattern="partial" filepath="chapter_03/sample_3-6.py" block="translation_func_with_format"]


# まとめ

本節では、Blenderの言語設定を変更したときに、アドオンが表示するテキストを自動的に変更する方法を説明しました。
アドオンのUIを多言語化するうえで必要な処理はそれほど多くないことから、翻訳辞書を作るところが一番大変かもしれません。
特に翻訳量が多い場合は、翻訳に多くの時間を使ってしまい、アドオンの開発どころではなくなってしまうかもしれません。
このため、正確さに少し難がありますが、Python向けに用意されている自動翻訳APIを利用して自動翻訳に頼ってしまう方法もあります。

海外に向けてアドオンを提供することを考えている人は、ぜひこの機会にアドオンのUIの多言語化に挑戦してみてください。
世界共通語といってもよい英語をサポートするだけで、アドオンを使ってくれるユーザは多くなりますし、海外ユーザからフィードバックを得られる機会も多くなります。
このフィードバックがきっかけで、海外のBlenderユーザと知り合いになれるかもしれません。


## ポイント

* アドオンのUIを複数の言語に対応させるためには、開発者が作成した翻訳辞書を `bpy.app.translations.register` 関数で登録し、翻訳する文字列を `bpy.app.translations.pgettext` 関数で置き換える必要がある
* Blenderがサポートするすべての言語について辞書を作成するのは時間がかかるため、最初は英語をサポートすることからはじめよう