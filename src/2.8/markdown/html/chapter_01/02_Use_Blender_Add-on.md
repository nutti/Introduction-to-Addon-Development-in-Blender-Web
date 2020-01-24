---
pagetitle: 1-2. Blenderアドオンを使う
subtitle: 1-2. Blenderアドオンを使う
---

Blenderアドオンの開発の説明に入る前に他の方が開発したアドオンを使い、アドオンのインストール・有効/無効化の手順を説明します。
ここで紹介する手順は今後アドオンを開発する際に何度も行うことになりますので、必ず覚えておきましょう。


# Blenderの日本語化

Blenderは海外で開発されたソフトであるため、Blenderを初めて起動した時のUIは全て英語です。
このため、Blenderを利用する敷居が高いと感じる方もいると思いますが、幸いなことにBlenderは公式で日本語のUIをサポートしています。

英語でも難なく使える方であればそのままでも良いのですが、英語では敷居が高いと言う方のためにBlenderを日本語化する方法を紹介します。

なお本書では、Blenderが日本語化されていることを前提として解説しますので、不安な方はここで日本語化することをお勧めします。

<div class="work"></div>

|||
|---|---|
|1|トップバーから *[Edit]* > *[Preferences...]* を実行します。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/localizing_into_japanese_1.png "アドオンの日本語化 手順1")|
|2|*[Blender Preferences]* ウィンドウが立ち上がるので、*[Interface]* タブを選択します。|
|3|*[Translation]* にチェックを入れると、UIの言語を変更することができるようになります。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/localizing_into_japanese_3.png "アドオンの日本語化 手順3")|
|4|*[Language]* を *[Japanese (日本語)]* に変更し、日本語化する項目を選択すると、選択した項目のUIに関して日本語化されます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/localizing_into_japanese_4.png "アドオンの日本語化 手順4")|


# アドオンの種類

アドオンを使用する前に、アドオンのサポートレベルについて理解しましょう。

アドオンの **サポートレベル** はアドオンの品質やメンテナンスなどの将来性を示します。
サポートレベルが高ければよくメンテナンスされていて品質が高い傾向があります。
一方、サポートレベルが低いアドオンではメンテナンスがおろそかな傾向があり、正しく動作しないまま放置されているアドオンも少なからずあります。

サポートレベルが低くても非常に有用なアドオンはたくさんあります。
問題が起きても気にせず様々なアドオンを使いたい方はサポートレベルを気にせず使えばよく、安定した動作をするアドオンのみを使いたい方であればサポートレベルが高いアドオンだけを使用するのがよいと思います。

サポートレベルは、3段階から構成されます。

|サポートレベル|説明|
|---|---|
|Release|Blenderが公式にサポートするアドオンで、正式版のBlender本体と一緒に提供されます。アドオンの公開や更新の度に、Blenderの開発者による厳密なレビュー（審査）があるため、不具合が少なく安定しています。|
|Contrib|Blender本体には含まれませんが、テストビルドされたBlender本体と共に提供されます。サポートは各アドオン開発者が行うため、サポートレベルがReleaseであるアドオンに比べて品質が落ちます。Contribとして登録されるためには、Blenderの開発者のレビューで一定の評価を得る必要があるため、一定の品質が保証され、新規性があり有用な機能を持つアドオンが集まっています。|
|External|サポートレベルがReleaseおよびContrib以外のアドオンで、ユーザが自らアドオンをインストールする必要があります。Blenderの開発者によるアドオンのレビューが行われていないため、本サポートレベルのアドオンの利用は基本的に自己責任となります。作業効率化など、Blender本体の機能を補助するアドオンが多く含まれるようですが、中にはサポートレベルがReleaseやContribよりも優れた機能を持つアドオンも存在します。|


# アドオンのインストール

サポートレベルがReleaseであるアドオンは、正式版のBlender本体と共に提供されるためインストール作業は不要です。
また、テストビルドのBlenderを利用されている方は、サポートレベルがContribのアドオンについてもインストールすることなく利用可能です。

ここでは、正式版のBlender本体を利用されている方がサポートレベルContribのアドオンをインストールする場合や、サポートレベルがExternalであるアドオンをインストールする場合について説明します。
本節では、数あるインストール方法のうちの1つを紹介しています。詳しくは、 [1-4節](04_Understand_Install_Uninstall_Update_Add-on.html) を参照ください。

インストール手順を説明するにあたり、アドオン開発で筆者がいつもお世話になっているmifth氏のアドオンMira Toolsをサンプルとして取り上げます。
Mira Toolsの機能は、[https://github.com/mifth/mifthtools/wiki/Mira-Tools](https://github.com/mifth/mifthtools/wiki/Mira-Tools)から確認できます。
Mira Toolsは日本語をサポートしていないためアドオンを使う敷居がやや高くなりますが、サポートレベルがExternalのアドオンの中でも非常に高機能なアドオンの1つですので、ぜひ1度使ってみてください。

Mira Toolsのインストール方法は前述のURLにも記載されていますが、ここでもインストール方法を紹介します。


<div class="work"></div>

|||
|---|---|
|1|[https://github.com/mifth/mifthtools/archive/master.zip](https://github.com/mifth/mifthtools/archive/master.zip) からmifth氏が作成したアドオン一式をダウンロードします。|
|2|ダウンロードしたファイル `mifthtools-master.zip` を解凍します。|
|3|`mifthtools-master/blender/addons/2.7/mira_tools` がMira Tools本体です。このフォルダ一式を、 Blender アドオン用フォルダへコピーしたらインストール完了です。Blenderアドオン用フォルダは以下に示すように、OSごとにパスが異なります。インストール先のフォルダがない場合は、新たに作成してください。|


|OS|インストール先|
|---|---|
|Windows|C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons|
|Mac|/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons|
|Linux|/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons|


<div class="column">
コピーしたファイルの中に拡張子が .py であるファイルがあります。 このファイルはアドオンのソースコードと呼ばれ、プログラミング言語Pythonによりアドオンの動作が記述されたテキストファイルです。
</div>


# アドオンの有効化

インストールしたアドオンを有効化し、アドオンの機能を使えるようにします。
サポートレベルがRelease/Contrib/Externalのいずれのアドオンについても、これから紹介する方法で有効化できます。

以下の手順に従い、先ほどインストールしたMira Toolsを有効化します。

<div class="work"></div>

|||
|---|---|
|1|Blenderを起動します。|
|2|トップバーのメニューから、*[編集]* > *[プリファレンス...]* を選択します。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/enable_add-on_2.png "アドオンの有効化 手順2")|
|3|*[Blenderプリファレンス]* ウィンドウが別ウィンドウで開きますので、*[アドオン]* タブを選択します。|
|4|検索窓に *[mira tools]* と入力します。|
|5|ウィンドウ右側に *[Mira Tools]* が表示されますので、チェックボックスにチェックを入れるとアドオンが有効化されます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/enable_add-on_5.png "アドオンの有効化 手順5")|
|6|実際にアドオンが有効化されているかは、*[エディットモード]* 時に *[3Dビューポート]* スペースの右側のSidebarのタブに *[Mira]* が追加されていることで確認できます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/enable_add-on_6.png "アドオンの有効化 手順6")|


<div class="column">
Mira Tools の使い方をここで紹介するのは本書の範囲を超えてしまうので、ここでは説明しません。  
興味のある方は以下のページを参照してください。  
Mira Tools - [https://github.com/mifth/mifthtools/wiki/Mira-Tools](https://github.com/mifth/mifthtools/wiki/Mira-Tools)
</div>


# アドオンの無効化

Release/Contrib/Externalいずれのサポートレベルについても共通で、次に紹介する手順でアドオンを無効化できます。


<div class="work"></div>

|||
|---|---|
|1|アドオンを有効化した時と同様、*[Blenderプリファレンス]* ウィンドウを開きます。|
|2|*[アドオン]* タブを選択し、*[Mira Tools]* のチェックボックスのチェックを外すことでアドオンが無効化されます。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/disable_add-on_2.png "アドオンの無効化 手順2")|


# アドオンのアンインストール

インストール済みのMira Toolsをアンインストールします。

インストールと同様、本節では数あるアンインストール方法のうちの1つを紹介しています。
詳しくは、[1-4節](04_Understand_Install_Uninstall_Update_Add-on.html) を参照ください。


<div class="work"></div>

|||
|---|---|
|1|*[Blenderプリファレンス]* ウィンドウの *[アドオン]* タブを選択し、*[Mira Tools]* の左の矢印をクリックして詳細情報を開きます。|
|2|*[削除]* ボタンをクリックすると、アンインストールが完了します。<br>![](../../images/chapter_01/02_Use_Blender_Add-on/uninstall_add-on_2.png "アドオンのアンインストール 手順2")|
