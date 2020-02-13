---
pagetitle: はじめに
subtitle: はじめに
---

# 本書について

def execute(self, context):

本書は、3DCGソフト「Blender」のアドオンを初めて開発する人を対象とした、アドオン開発の入門書です。
本書を最後まで読むことで、アドオンを開発する際に最低限必要な知識が得られ、読者が独自のアドオンを開発できるようになります。

本書はアドオン開発の経験がない人を対象としていますが、すでにアドオンの開発を経験されている人でも参考になる情報があると考えています。
特に4章では、アドオンの公開方法やデバッグ方法など、アドオンに関連する周辺の話題も取り上げています。
知っておくとのちのち役立つと思われる情報を載せていますので、余力があればぜひ一読ください。


## Blender 2.79以前のアドオン開発

Blender 2.79以前とBlender 2.80以降とではPython APIに大きな変更があり、アドオン開発に必要な知識も異なります。
Blender 2.79以前のアドオン開発に関しては、[はじめてのBlenderアドオン開発 (Blender 2.7版)](https://colorful-pico.net/introduction-to-addon-development-in-blender/2.7/) を参照してください。


## 電子書籍版『はじめてのBlenderアドオン開発 v3』

より内容を充実させた電子書籍版『はじめてのBlenderアドオン開発 v3』を [BOOTH](https://colorful-pico.booth.pm/items/1678181) で販売しています。
電子書籍版では、Web版とは異なるサンプルアドオンも数多く紹介していますので、興味がありましたら、こちらもぜひ手に取っていただけると幸いです。


## Blenderのアドオン開発って面白いの？

筆者は、3DモデルをBlenderで作成していた知人から、Blenderへの新規機能の追加を頼まれたことがきっかけでアドオン開発の世界に入りました。
はじめてのアドオン開発ということもあり、当時はとても苦労しました。
しかし、開発したアドオンをWeb上で公開して5年以上経った今でもアドオンに対する要望があるなど、アドオン開発を通してほかのアドオン開発者やユーザと交流できるのは、アドオン開発の楽しいところの1つです。


## 本書をなぜ執筆したの？

筆者がはじめてアドオンを開発したときは、アドオン開発に関する情報が今以上に少なく、さらに日本語となると数を数えられるくらいの情報しかありませんでした。
このため、想像していたよりもアドオンの開発に時間がかかってしまいました。
このような背景もあり、今後アドオンを開発しようと考えている人が同じ苦労をして欲しくないと思い、本書の執筆を決めました。

さらに、これまでBlenderを3DCGを作るためのツールとしてのみ使ってきた人にも、本書を読んでアドオンの開発に挑戦してもらいたいということも、モチベーションの1つとしてありました。
実際、3DCGを作るためにBlenderを利用するユーザは、開発者が意識していないような改善案や問題意識をBlenderに対して持っていることが多いと筆者は考えています。
本書を読むことで、これまでBlenderを使う立場であった人が、アドオン開発に一歩踏み出せたら嬉しいです。


# 本書の読み方

本書は、はじめてBlenderのアドオンを開発する人を対象としています。
すでにBlenderを使ったことがある人にとって、前半の解説は当たり前の内容で物足りないかもしれません。
本書は前から後ろに進んでいくにつれて、基本的な内容から発展的な内容になるような構成を意識して執筆しています。
すでに理解していて読む必要がないと感じた部分は、必要に応じて読み飛ばしてください。
また本書は、節ごとにテーマを決めているため、知りたい内容だけに絞って読んでも問題ありません。

本書は、読者が実際に手を動かして作業する場面が数多くあります。
本を読んだだけで理解することはなかなか難しいため、積極的に手を動かして理解するようにしましょう。
特にサンプルアドオンを用いて説明している節では、必ず各自の環境で動作させて確認してください。
アドオンをそのまま動かすだけでも、いろいろ学べることはあります。

それでは、楽しいBlenderアドオン開発の世界を満喫してください！


# 本書で紹介するサンプルアドオンのソースコードについて

本書で紹介するサンプルアドオンのソースコードは、各節の最初に記載されています。
必要に応じてコピペするなどして、ご利用ください。
なお、サンプルアドオンのライセンスに関しては後述します。


# 前提知識

本書を読むための必須知識と、より高度なアドオンを開発するために知っておくとよい推奨知識を次に示します。


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

必須知識に加えて次のような知識があると、本書で紹介している以上の高度なアドオンを作成できます。
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
  * 日常会話で利用する英語


# 本書の著作権（ライセンス）について

## 本文（ソースコードを除く）

本書は、本書内に記載しているソースコードを除き、クリエイティブ・コモンズ・ライセンス「CC BY」が適用されています。

<a rel="license" href="http://creativecommons.org/licenses/by/2.1/jp/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by/2.1/jp/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by/2.1/jp/">クリエイティブ・コモンズ 表示 2.1 日本 ライセンスの下に提供されています。</a>


## 本書内のソースコードについて

本書内で記載しているソースコードには、クリエイティブ・コモンズ・ライセンス「CC0」が適用されています。

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


# 誤字・脱字を報告いただける人について

本書内の誤字・脱字を見つけられた人は、次に示すサポートページや [おわりに](../chapter_99/01_Conclusion.html) に記載している連絡先よりご連絡ください。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/issues)

また、本書の原本が置かれているGitHubページからPull Requestを出すことにより、各自修正した内容について反映依頼を出すことができます。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/pulls](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/pulls)

なお本書の執筆に貢献いただいた人は、許可を取った上で [おわりに](../chapter_99/01_Conclusion.html) の謝辞に名前（またはニックネーム）を掲載させていただきます。


# 本書へのリクエストについて

本書に執筆内容の追加等を希望される人は、次に示すサポートページや [おわりに](../chapter_99/01_Conclusion.html) に記載している連絡先より、リクエストを出すことができます。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/issues)


# 本書の内容に関するお問い合わせについて

本書の内容に関する問い合わせについては、次に示すサポートページや [おわりに](../chapter_99/01_Conclusion.html) に記載されている連絡先から問い合わせください。

[https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/issues](https://github.com/nutti/Introduction-to-Addon-Development-in-Blender-Web/issues)
