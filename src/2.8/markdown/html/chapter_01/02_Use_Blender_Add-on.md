---
pagetitle: 1-2. Blenderアドオンを使う
subtitle: 1-2. Blenderアドオンを使う
---

Blenderアドオンの開発の説明に入る前に、他者が作成したアドオンを使って、アドオンのインストール・有効/無効化の手順を説明します。
ここで紹介する手順は、今後アドオンを開発するときに何度も行うことになりますので、必ず覚えておきましょう。


# Blenderの日本語化

Blenderは海外で開発されたソフトであるため、Blenderを初めて起動したときのUIは全て英語です。
このため、Blenderを利用する敷居が高いと感じる人もいると思いますが、幸いなことにBlenderは公式で日本語のUIをサポートしています。

ここでは、Blenderを日本語化する方法を紹介します。
なお、Blenderに関しては英語のほうが圧倒的に情報量が多いため、英語でも難なく使える人であれば、そのまま使用するようにしてください。
また、今回は日本語化して使っている人も、いずれは英語のままBlenderを使うことにも挑戦してみてください。
本書は入門者向けということもあり、Blenderが日本語化されていることを前提として解説します。


<div class="work"></div>

|||
|---|---|
|1|トップバーから *[Edit]* > *[Preferences...]* を実行します。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/localizing_into_japanese_1.png "Blenderの日本語化 手順1")|
|2|*[Blender Preferences]* ウィンドウが立ち上がるため、*[Interface]* タブを選択します。|
|3|*[Translation]* にチェックを入れると、UIの言語を変更できるようになります。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/localizing_into_japanese_3.png "Blenderの日本語化 手順3")|
|4|*[Language]* を *[Japanese (日本語)]* に変更し、日本語化する項目を選択すると、選択した項目のUIに関して日本語化されます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/localizing_into_japanese_4.png "Blenderの日本語化 手順4")|


# アドオンの種類

アドオンを使用する前に、アドオンのリリースレベルについて理解しましょう。

アドオンの **リリースレベル** は、アドオンの品質やメンテナンスなどの将来性を示します。
リリースレベルが高ければ、よくメンテナンスされていて品質が高い傾向があります。
一方、リリースレベルが低いアドオンの中には、メンテナンスがおろそかなアドオンもあり、正しく動作しないまま放置されているアドオンもあります。

しかし、リリースレベルだけでアドオンの品質を判断するのは正しくありません。
リリースレベルが低くても、非常に有用なアドオンはたくさんあります。
問題が起きても気にせず様々なアドオンを使いたい人は、リリースレベルを使えばよく、安定した動作をするアドオンのみを使いたい人であれば、リリースレベルが高いアドオンだけを使用するのがよいと思います。

リリースレベルは、3段階から構成されます。

|リリースレベル|説明|
|---|---|
|Release|Blenderが公式にサポートするアドオンで、正式版のBlender本体と一緒に提供されます。アドオンの公開や更新のたびに、Blenderの開発者による厳密なレビュー（審査）があるため、不具合が少なく安定しています。|
|Contrib|Blender本体には含まれませんが、テストビルドされたBlender本体と共に提供されます。サポートは各アドオン開発者が行うため、リリースレベルがReleaseであるアドオンに比べて品質が落ちます。Contribとして登録されるためには、Blenderの開発者のレビューで一定の評価を得る必要があるため、一定の品質が保証されています。|
|External|リリースレベルがReleaseおよびContrib以外のアドオンで、ユーザが自らアドオンをインストールする必要があります。Blenderの開発者によるレビューが行われていないため、本リリースレベルのアドオンの利用は基本的に自己責任となります。リリースレベルがReleaseやContribよりも、優れた機能を持つアドオンも存在します。|


# アドオンのインストール

リリースレベルがReleaseであるアドオンは、正式版のBlender本体とともに提供されるため、インストール作業は不要です。
また、テストビルドのBlenderを利用する人は、リリースレベルがContribのアドオンについても、インストールすることなく利用可能です。

ここでは、正式版のBlender本体を利用している人が、リリースレベルがContribのアドオンをインストールする場合や、リリースレベルがExternalであるアドオンをインストールする場合について説明します。
本節では、数あるインストール方法のうちの1つを紹介しています。詳しくは、 [1-4節](04_Understand_Install_Uninstall_Update_Add-on.html) を参照ください。

インストール手順を説明するのにあたり、アドオン開発で筆者がいつもお世話になっているmifth氏のアドオンMira Toolsを例として取り上げます。
Mira Toolsの機能は、[https://github.com/mifth/mifthtools/wiki/Mira-Tools](https://github.com/mifth/mifthtools/wiki/Mira-Tools)から確認できます。
Mira Toolsは日本語をサポートしていないため、アドオンを使う敷居がやや高くなりますが、リリースレベルがExternalのアドオンの中でも非常に高機能なアドオンの1つですので、ぜひ1度使ってみてください。

Mira Toolsのインストール方法は、前述のURLにも記載されていますが、ここでもインストール方法を紹介します。


<div class="work"></div>

|||
|---|---|
|1|[https://github.com/mifth/mifthtools/archive/master.zip](https://github.com/mifth/mifthtools/archive/master.zip) から、mifth氏が作成したアドオン一式をダウンロードします。|
|2|ダウンロードしたファイル `mifthtools-master.zip` を解凍します。|
|3|`mifthtools-master/blender/addons/2.8/mira_tools` がMira Tools本体です。このフォルダ一式を、Blenderアドオン用フォルダへコピーしたらインストール完了です。Blenderアドオン用フォルダは後述するように、OSごとにパスが異なります。インストール先のフォルダがない場合は、新たに作成してください。|


|OS|インストール先|
|---|---|
|Windows|`C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons`|
|Mac|`/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons`|
|Linux|`/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons`|


<div class="column">
コピーしたファイルの中に拡張子が .py であるファイルがあります。 このファイルはアドオンのソースコードと呼ばれ、プログラミング言語Pythonによりアドオンの動作が記述されたテキストファイルです。
</div>


# アドオンの有効化

インストールしたアドオンを有効化し、アドオンの機能を使えるようにします。

次の手順に従い、先ほどインストールしたMira Toolsを有効化します。

<div class="work"></div>

|||
|---|---|
|1|Blenderを起動します。|
|2|トップバーのメニューから、*[編集]* > *[プリファレンス...]* を選択します。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/enable_add-on_2.png "アドオンの有効化 手順2")|
|3|*[プリファレンス]* が別ウィンドウで開くため、*[アドオン]* タブを選択します。|
|4|検索窓に *[mira tools]* と入力します。|
|5|ウィンドウ右側に *[Mira Tools]* が表示され、チェックボックスにチェックを入れるとアドオンが有効化されます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/enable_add-on_5.png "アドオンの有効化 手順5")|
|6|実際にアドオンが有効化されているかは、*[編集モード]* 時に *[3Dビューポート]* スペースの右側のSidebarのタブに *[Mira]* が追加されていることで確認できます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/enable_add-on_6.png "アドオンの有効化 手順6")|


<div class="column">
Mira Toolsの使い方をここで紹介するのは本書の範囲を超えてしまうので、ここでは説明しません。
興味のある人は次のページを参照してください。
[https://github.com/mifth/mifthtools/wiki/Mira-Tools](https://github.com/mifth/mifthtools/wiki/Mira-Tools)
</div>


# アドオンの無効化

次に紹介する手順でMira Toolsを無効化できます。


<div class="work"></div>

|||
|---|---|
|1|アドオンを有効化したときと同様、*[プリファレンス]* を開きます。|
|2|*[アドオン]* タブを選択し、*[Mira Tools]* のチェックボックスのチェックを外すと、アドオンが無効化されます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/disable_add-on_2.png "アドオンの無効化 手順2")|


# アドオンのアンインストール

インストールしたMira Toolsを、アンインストールします。

本節では数あるアンインストール方法のうちの1つを紹介しています。
詳しくは、[1-4節](04_Understand_Install_Uninstall_Update_Add-on.html) を参照ください。


<div class="work"></div>

|||
|---|---|
|1|*[プリファレンス]* の *[アドオン]* タブを選択し、*[Mira Tools]* の左の矢印をクリックして詳細情報を開きます。|
|2|*[削除]* ボタンをクリックすると、アンインストールが完了します。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/uninstall_add-on_2.png "アドオンのアンインストール 手順2")|


# まとめ

アドオンのリリースレベルについて解説し、アドオンのリリースレベルがExternalであるアドオンをインストール・アンインストールする方法を紹介しました。
さらに、インストールしたアドオンが動作していることも確認しました。
ここで紹介した手順は、アドオン開発時に何度も行う操作であるため、必ず覚えておきましょう。

また、本節ではBlenderのUIを日本語化する方法も紹介しました。
本節以降は、BlenderのUIが日本語化されていることを前提に解説しますので、必要に応じて本節を参考にしてください。


## ポイント

* Blenderは標準で日本語のUIをサポートするため、必要に応じてUIを日本語化できる
* Blenderのアドオンは、アドオンの品質やメンテナンス状況を示すリリースレベルで分類できる。
* Blenderのアドオンのソースコードは、プログラミング言語Pythonで書かれた拡張子が.pyのテキストファイルである。
