---
pagetitle: おわりに
subtitle: おわりに
---


アドオンについての説明から始め、Blenderが提供するAPIを使ったアドオンの作り方を説明しました。
そして最後は、アドオンをBlender本体に取り込んでもらうための方法を説明しました。
ここまでとても長かったと思います。
特に飛ばさずに最初から最後まで飛ばさずに全て読まれた方、お疲れ様でした。

本来はよりコンパクトな解説書を考えていたのですが、予定よりも規模が大きくなってしまいました。
しかし、Blenderが提供するPython向けのAPIは非常に多く、本書はその数%をカバーしただけに過ぎません。
Blenderが提供する膨大なAPIをここで全て紹介していては、ページと執筆時間がいくらあっても足りなくなってしまいますので、本書ではアドオン開発のために必要となる本質的な内容に絞って説明しました。
本書を読み終えた方であれば、独自のアドオンを作ることができるようになっているでしょうし、初めて見るAPIを調査することもできるはずです。
筆者も何度か見直していますが、本書には間違いや誤字・脱字などの多くの問題があると思います。
もしこれらの問題を発見された場合、連絡をいただけると大変助かります。

本書でも何度か書きましたが、アドオンの開発に慣れるためには、情報を集めるだけでなく実際に手を動かしてみることが大切です。
本書のサンプルをそのまま動作させても良いですし、改造してみてどのように動きが変わるのかを見ても良いです。
すでに作りたいアドオンが決まっているのであれば、本書を見ながらアドオンを作り始めてしまっても良いかもしれません。
ぜひ、積極的に手を動かしてアドオンの開発に慣れていきましょう。

最後に、今までアドオン開発に踏み出せなかった方が本書を読んでアドオンの開発に挑戦するためのきっかけになれば、本書の役目は十分果たせたのかなと思います。
本書が全てのアドオン開発者の手助けになり、読者の中から独自のアドオンを作成し公開された方が1人でも出てくれば、本書の執筆者としてこれ以上嬉しいことはありません。

return {'FINISHED'}


# 謝辞

執筆を終えてから改めて執筆していたときを振り返ってみると、Twitteで宣伝した時にリツイートやふぁぼ（いいね）してくださった方、感想をくださった方、ホームページで紹介しててくださった方、メールなどで意見を言ってくださった方など、いろいろな方に協力いただきました。
皆様のフィードバックがあったからこそ、最後まで諦めずに執筆完了できたと思います。
改めてここでお礼を申し上げます。
本当にありがとうございました。

協力いただいた全ての方をここに掲載してしまうと数ページにもなってしまうので、協力いただいた方の中で特に感謝したい方を掲載させていただくことにします。
なお、掲載にあたっては本人に掲載の許可をいただいております。


## 宣伝スペースを用意していただいた方

Webサイトの一部をお借りして本書の宣伝にご協力いただいた方です。

BLUG.jp 様


## 本書執筆にご協力いただいた方

誤字・脱字の指摘、修正や改善要望していただいた方です。

conchan-akita 様, sariew 様, AWA 様, うにっこ 様, itashin0501 様, N(Natukikazemizo) 様


# 筆者について

2014年より同人サークル『COLORFUL PICO』の代表として活動中。
『COLORFUL PICO』はゲームやアプリの開発を行うサークルであるが、開発で得たノウハウをWeb上で公開しつつ、同人誌として頒布する活動も行っている。
3年近くBlenderのアドオン開発を中心に活動してきたが、最近はサークル本来の目的である3Dアクションゲームの開発へ活動をシフトしている。
アドオン開発に一区切りついた今、Blenderとの今後の付き合い方について模索中。
Blender本体のソースコードリーディング、Release Notesの翻訳（英語から日本語）などおもしろそうなことはたくさんあるのだが・・・


## ホームページや連絡先

|||
|---|---|
|Mail|nutti.metro@gmail.com |
|Homepage|[http://colorful-pico.net/](http://colorful-pico.net/)|
|Blog|[http://colorful-pico.hatenablog.jp](http://colorful-pico.hatenablog.jp)|
|Twitter|@nutti\_\_（[https://twitter.com/nutti__](https://twitter.com/nutti__)）|
|GitHub|[https://github.com/nutti](https://github.com/nutti)|
|Qiita|[http://qiita.com/nutti](http://qiita.com/nutti)|


## 筆者がこれまで作成したアドオン

|アドオン名|URL|サポート<br>レベル|概要|
|---|---|---|---|
|Magic UV|[https://github.com/nutti/Magic-UV](https://github.com/nutti/Magic-UV)|Release（2.79以降）<br>Contrib（2.78以前）|UV座標のコピー・ペーストをはじめとした、UV編集に役立つ機能を集めたアドオン<br>バージョン2.79よりBlenderの公式アドオンとして登録される|
|Paint Tools|[https://github.com/nutti/Paint-Tools](https://github.com/nutti/Paint-Tools)|External|UV/Image Editorにおける矩形選択ツール。選択した範囲に対して、簡単な画像処理（塗りつぶしや2値化など）を適用することができるアドオン|
|Mouse Click Merge|[https://github.com/nutti/Mouse-Click-Merge](https://github.com/nutti/Mouse-Click-Merge)|External|3DCGソフト「メタセコイア」のように、マウスクリックによる隣接頂点結合や、面の対角線を反転させることができるアドオン|
|Index Visualizer|[https://github.com/nutti/Index-Visualizer](https://github.com/nutti/Index-Visualizer)|External|View3Dエリアのオブジェクトの頂点・辺・面のインデックス番号を表示するアドオン|
|Face To Transform Orientation|[https://github.com/nutti/Face-To-Transform-Orientation](https://github.com/nutti/Face-To-Transform-Orientation)|External|View3Dエリアのオブジェクトを、Transform Orientationの方向に向かせるアドオン|
|Blender Add-on Manager|[https://github.com/nutti/Blender-Add-on-Manager](https://github.com/nutti/Blender-Add-on-Manager)|-|GitHubに登録されたアドオンのインストール・アンインストール・アップデートを行うことができるツール（正確にはアドオンではない）<br>Windows/Mac OSX/Linuxに対応|
