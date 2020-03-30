---
pagetitle: おわりに
subtitle: おわりに
---


Blenderやアドオンそのものの説明からはじめ、Blenderが提供するAPIを使ったアドオンの作り方を説明しました。
そして、アドオン開発時に役立つtipsを紹介しながら、最後はアドオンをBlender本体に取り込んでもらうための方法を説明しました。
ここまでとても長かったと思います。

本書を読み終えた人であれば、独自のアドオンを作ることができるようになっているでしょうし、初めて見るAPIを調査することもできるはずです。
アドオンの開発に慣れるためには、情報を集めるだけでなく実際に手を動かしてみることが大切です。
本書のサンプルアドオンをそのまま動作させてもよいですし、改造してみてどのように動きが変わるのかを見てもよいです。
すでに作りたいアドオンが決まっているのであれば、本書を見ながらアドオンを作り始めてしまってもよいかもしれません。
ぜひ、積極的に手を動かしてアドオンの開発に慣れていきましょう。

筆者も何度か見直していますが、本書には間違いや誤字・脱字などの問題があるかもしれません。
もしこれらの問題を発見された場合、連絡をいただけると大変助かります。
最後に、今までアドオン開発に踏み出せなかった人が、本書をきっかけとしてアドオン開発に挑戦してもらえれば幸いです。

return {'FINISHED'}

## 宣伝: 電子書籍版『はじめてのBlenderアドオン開発 v3』

より深くBlenderのアドオン開発について学びたい人は、[BOOTH](https://colorful-pico.booth.pm/items/1678181) で販売中の電子書籍版『はじめてのBlenderアドオン開発 v3』をぜひお買い求めください。
電子書籍版では、Web版では紹介していなかったAPIの解説に加え、数多くの異なるサンプルアドオンも含まれていますので、新たな発見があるかと思います。


# 謝辞

Twitteで宣伝したときにリツイートやいいねしてくださった方、感想をくださった方、ホームページで紹介してくださった方、メールなどで意見を送ってくださった方など、本書を執筆するときにはいろいろな人に協力いただきました。
みなさまのフィードバックがあったからこそ、最後まで諦めずに執筆完了できたと思います。
あらためてここでお礼を申し上げます。
本当にありがとうございました。

協力いただいた全ての方をここに掲載してしまうと数ページにもなるので、協力いただいた方の中でとくに感謝したい方を掲載させていただくことにします。
なお、掲載にあたっては本人に掲載の許可をいただいております。


## 宣伝スペースを用意してくださった方

Webサイトの一部をお借りして、本書の宣伝にご協力いただいた方です。

* BLUG.jp 様
    * [BlenderのWiki](https://wiki3.jp/blugjp/page/12)、[blugjpまとめサイト](https://sites.google.com/site/blugjp/blenderpython) にて、本書をご紹介していただきました
* 3D人 様
    * [3D人-3dnchu-](https://3dnchu.com/) にて、本書の [Blender 2.7版](https://3dnchu.com/archives/introduction-to-add-on-development-in-blender/) と [Blender 2.8版](https://3dnchu.com/archives/introduction-addon-dev-book-blender-28/) をご紹介していただきました


## 本書執筆にご協力いただいた方

誤字・脱字の指摘、修正や改善要望していただいた方です。

conchan-akita 様, sariew 様, AWA 様, うにっこ 様, itashin0501 様, N(Natukikazemizo) 様, hzuika 様


## ホームページや連絡先

|||
|---|---|
|Mail|nutti.metro@gmail.com |
|Homepage|[https://colorful-pico.net](https://colorful-pico.net)|
|Twitter|@nutti\_\_（[https://twitter.com/nutti__](https://twitter.com/nutti__)）|
|GitHub|[https://github.com/nutti](https://github.com/nutti)|
|Qiita|[http://qiita.com/nutti](http://qiita.com/nutti)|


## 筆者がこれまで作成したアドオンなど

|アドオン名|URL|リリースレベル|概要|
|---|---|---|---|
|Magic UV|[https://github.com/nutti/Magic-UV](https://github.com/nutti/Magic-UV)|Release（2.79以降）<br>Contrib（2.78以前）|UV座標のコピー＆ペーストをはじめとした、UV編集に役立つ機能を集めたアドオン<br>バージョン2.79よりBlenderの公式アドオンとして登録される|
|fake-bpy-module|[https://github.com/nutti/fake-bpy-module](https://github.com/nutti/fake-bpy-module)|-|Blenderが提供するPython APIについて、テキストエディタでコード補完するためのモジュール|
|Screencast-Keys|[https://github.com/nutti/Screencast-Keys](https://github.com/nutti/Screencast-Keys)|External|入力したキーボードやマウスのキーを、Blender内に表示するアドオン|
|Blender Add-on Manager|[https://github.com/nutti/Blender-Add-on-Manager](https://github.com/nutti/Blender-Add-on-Manager)|-|GitHubに登録されたアドオンのインストール・アンインストール・アップデートを行うことができるツール<br>Windows/MacOS/Linuxに対応|
