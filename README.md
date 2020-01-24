# Web版「はじめてのBlenderアドオン開発」

「はじめてのBlenderアドオン開発」は、これからBlenderのアドオンを開発しようと考えている人向けの入門書です。
本リポジトリでは、Web版「はじめてのBlenderアドオン開発」を構成するソースコード一式を置いています。  
Web版「はじめてのBlenderアドオン開発」は、以下から参照することが可能です。

* [2.7x](https://colorful-pico.net/introduction-to-addon-development-in-blender/2.7/index.html)


# 本書の問い合わせ、修正依頼

本書の内容に関する問い合わせは、[Issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues) から行ってください。

本書を修正する場合は、[Pull requests](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/pulls) から修正依頼を出してください。


# 開発者向け情報

## ビルド方法

#### 1. ソースコード一式を取得

```
$ git clone https://github.com/nutti/Introduction-to-Addon-Development-in-Blender.git
```

#### 2. ビルドスクリプトを使ってビルド

Blender 2.7向けにビルドする場合は、`{version}` は `2.7` とします。

```
$ cd Introduction-to-Addon-Development-in-Blender
$ perl tools/build.pl src/<version> <output>
```

## 独自の拡張

本書のソースコードは、ビルド時に特殊な処理を行うための独自な命令を追加しています。  
本書はこれらの命令をビルド時に解釈し、命令に応じて最終的な結果を出力します。

### HTML

#### `<!-- @include-toc -->`

本命令が記載された箇所に、目次を追加します。

#### `<!-- @replace-own-url -->`

本命令が記載された箇所に、自身のビルド時に指定した `<output>` からの相対パスを挿入します。

#### `<!-- @include-prev-url -->`

目次の並び順で、前のページのあたるページについて、ビルド時に指定した `<output>` からの相対パスを挿入します。

#### `<!-- @include-next-url -->`

目次の並び順で、次のページのあたるページについて、ビルド時に指定した `<output>` からの相対パスを挿入します。


### toc.json

`templates/toc.json` に沿って目次を作成します。  
`templates/toc.json` をsortした順に目次を作成します。

#### `@pre`

`@pre` を指定することで、sortの結果に関わらず目次の先頭であることを強制させることができます。

#### `@post`

`@post` を指定することで、sortの結果に関わらず目次の末尾であることを強制させることができます。

#### `@XX:YY`

`XX` は数値、`YY` は節の題名とします。  
`@XX:YY` を指定することで、`XX` の順番で目次が並びます。  
なお目次を出力する時には、`@XX:` は削除されて `YY` のみが出力されます。

#### `@title`

章にページを割り当てたい場合は、`@title` を利用します。


### Markdown

#### `@include-source`

ソースコードをMarkdownに埋め込みます。  
オプションとして以下を指定できます。

|オプション|意味|
|---|---|
|`pattern`|`full`: 指定したソースコード全てを埋め込みます<br>`partial`: ソースコードの一部を埋め込みます|
|`filepath`|埋め込むソースコードのパス|
|`block`|`pattern` に `partial` を指定した時に、埋め込む場所を指定します|

### Source Code

#### `# @include-source`

Markdownに埋め込むソースコードの部分を `# @include-source start [<block>]` と `# @include-source end [<block>]` で指定します。  
`<block>` には、Markdown拡張 `@include-source` のオプション `block` に指定する、埋め込む場所を示す識別子を指定します。  
なお、`# @include-source` で始まる行は、ソースコードをMarkdownに埋め込む際に削除されます。


## 索引自動生成ツール

以下のコマンドを実行することで、`src/2.8` 以下に存在する `.md` ファイルから、強調表示された単語（`**` で囲われた単語）を抽出し、Markdown形式の索引を自動生成します。

```
$ node tools/gen_word_index.js --src-dir=src/2.8 --dest-file=00_Index.md
```
