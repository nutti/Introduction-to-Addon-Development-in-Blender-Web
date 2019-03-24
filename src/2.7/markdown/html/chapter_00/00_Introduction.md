---
pagetitle: はじめに
subtitle: はじめに
---

# 本書について

def execute(self, context):

本書は、3DCGソフト「Blender」のアドオンを初めて開発する方を対象とした、アドオン開発の入門書です。
本書を最後まで読むことで、アドオンを開発する際に最低限必要な知識が得られ、読者が独自のアドオンを開発することができるようになります。

本書はアドオン開発の経験がない方が対象としていますが、すでにアドオンの開発を経験されている方でも参考になる情報があると考えています。
特に4章では、アドオンの公開方法やデバッグ方法、作ったアドオンをBlender本体に取り込んでもらう方法など、アドオンに関連する周辺の話題も取り上げています。
知っておくと後々役立つと思われる情報を載せていますので、余力があればぜひ一読ください。


## Blenderのアドオン開発って面白いの？

筆者は、3DモデルをBlenderで作成していた知人から、Blenderへの新規機能の追加を頼まれたことがきっかけでアドオン開発の世界に入りました。

筆者が初めて作成したアドオンは、3Dビューエリア上で選択したメッシュの面間でUVをコピー＆ペーストする機能を持つものでした。
知人から、BlenderにUVをコピーする機能がなくて困ってるという話を聞いたことが、このアドオンを作ったきっかけでした。
Blenderで作成した3Dモデルにテクスチャを設定する時、最近は直接ペイントしたり自動的にUV展開することが多くなってきていますが、頂点数を少なくして応答性を高めるゲーム分野では、いまだにUVを意識する必要があります。

初めてのアドオン開発ということもあり苦労しましたが、無事に記念すべき第1弾となるアドオンが完成しました。
作ったアドオンを使った知人から便利だと感想をもらった時は、完成までに苦労したこともあり、嬉しかったです。
自分で作成したアドオンを使ったユーザから感想をもらえるのは嬉しく、楽しいものです。

最初に作成したアドオンは、細かい修正を行ってWeb上で公開しました。
そして、Web上で様々な意見を取り入れることで改善が進み、UVのコピー・ペースト機能をベースに様々な機能が追加され、複数のUV編集機能を持つアドオンになりました。
公開から数年が経った今でも、アドオンに対する要望があります。
アドオンを公開することで、自分で開発したアドオンがより高機能になっていくのは、非常におもしろいことです。
そしてこれはアドオンの開発を続けてきて言えることですが、アドオン開発を通して他のアドオン開発者やアドオン利用者と交流できるのも、アドオン開発の醍醐味の一つだと思います。


## 本書をなぜ執筆したの？

アドオン開発を始めた当時は、Blenderの標準の機能ですら使い慣れていない状態でした（今もですが）。
このため、初めてアドオンを開発した時はどこから手をつけたらよいかわからず、手探りで開発を進めるしかありませんでした。
そして当時はアドオン開発の情報源が今以上に少なく、さらに日本語をサポートしているとなると数を数えられるくらいの情報源しかありませんでした。
結局他のアドオンのソースコードを読んで改造してデバッグしながらなんとか完成させたのですが、想像していたよりも開発に時間がかかってしまいました。
このような背景もあり、アドオンを開発しようと考えている人が同じ苦労をして欲しくないと思い、本書の執筆を決めたのです。

さらに、これまでBlenderを3DCGを作るためのツールとしてのみ使ってきた方にも、本書を読んでアドオンの開発に挑戦してもらいたいという期待を持っています。
実際、3DCGを作るためにBlenderを利用するユーザは、開発者が意識していないような改善案や問題意識をBlenderに対して持っていることが多いと筆者は考えています。
本書を読むことで、これまでBlenderを使う立場であった方が、アドオン開発に一歩踏み出せたら嬉しいなと思います。


# 本書の読み方

本書は、はじめてBlenderのアドオンを開発する方を対象としているため、Blenderやアドオンに関する説明から始めています。
すでにBlenderを使ったことがある方にとって、前半の解説は当たり前の内容で物足りないかもしれません。
このため、本書は前から後ろに進んでいくにつれて、基本的な内容から発展的な内容になるような構成を意識して執筆しています。
すでに理解していて読む必要がないと感じた部分は、必要に応じて読み飛ばしてください。
また、本書は節ごとにテーマを決めて説明する構成を取っているため、知りたい内容だけに絞って読んでも問題ありません。

本書は、読者の方が実際に手を動かして作業する場面が数多くあります。
本を読んだだけで理解することはなかなか難しいので、積極的に手を動かして理解するようにしましょう。
特にアドオンのサンプルを用いて説明している節では、必ず読者の環境で動作させて確認してください。
サンプルをそのまま動かすだけでも、いろいろ学べることはあります。

それでは、楽しいBlenderアドオン開発の世界を満喫してください！

# 本書で紹介するサンプルのソースコードについて

本書で紹介するアドオンのサンプルのソースコードは、以下のURLからダウンロードすることができます。

https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/releases/download/v2/sample_v2.zip


# 前提知識

本書を読むための必須知識と、より高度なアドオンを開発するために知っておくと役立つ推奨知識を示します。


## 必須知識

本書を読むために必要となる必須知識を次に示します。

* Blenderの基礎知識
  * 基本操作
* Pythonの基礎知識
  * 変数（変数宣言、値の代入、型）
  * 四則演算
  * オブジェクト（タプル、リスト、辞書）
  * 関数（関数定義、呼び出し、戻り値）
  * クラス（クラス定義、メンバ変数、メソッド、継承）
  * モジュールのインポート
* 3DCGの知識
  * 基本用語（メッシュ、UV座標、面、法線など）


## 推奨知識

必須知識に加えて次のような知識があると、本書で紹介している以上の高度なアドオンを作成することができます。
なお本書を読むだけであれば、必ずしも必要ではない知識です。

* 数学
  * 三角関数
  * ベクトル演算
  * 行列演算
* 物理
  * 古典力学
  * 流体力学
* 英語
  * 3DCG関連の英語
  * 日常会話で利用する英語(チャット)


# 本書の著作権（ライセンス）について

## 本文（ソースコードを除く）

本書は本書内に記載しているソースコードを除き、クリエイティブ・コモンズ・ライセンス **CC BY** が適用されています。

<a rel="license" href="http://creativecommons.org/licenses/by/2.1/jp/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by/2.1/jp/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by/2.1/jp/">クリエイティブ・コモンズ 表示 2.1 日本 ライセンスの下に提供されています。</a>

## 本書内のソースコードについて

本書内で記載しているソースコードには、クリエイティブ・コモンズ・ライセンス **CC0** が適用されています。

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://www.gitbook.com/book/nutti/introduction-to-add-on-development-in-blender/details">
    <span property="dct:title">ぬっち</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">はじめてのBlender開発（ソースコード）</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="JP" about="https://www.gitbook.com/book/nutti/introduction-to-add-on-development-in-blender/details">
  日本</span>.
</p>



# 誤字・脱字を報告いただける方について

本書内の誤字・脱字を見つけた方は、以下のサポートページや [おわりに](../chapter_99/01_Conclusion.html) に記載している連絡先よりご連絡ください。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues)

また、本書の原本が置かれているGitHubページからPull Requestを出すことにより、各自修正した内容について反映依頼を出すことができます。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/pulls](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/pulls)

なお本書の執筆に貢献いただいた方は、許可を取った上で [おわりに](../chapter_99/01_Conclusion.html) の謝辞に名前（またはニックネーム）を掲載させていただきます。

# 本書へのリクエストについて

本書に執筆内容の追加等を希望される方は、以下のサポートページや [おわりに](../chapter_99/01_Conclusion.html) に記載している連絡先より、リクエストを出すことができます。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues)


# 本書の内容に関するお問い合わせについて

本書の内容に関する問い合わせについては、以下のサポートページや [おわりに](../chapter_99/01_Conclusion.html) に記載している連絡先から問い合わせください。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender/issues)
