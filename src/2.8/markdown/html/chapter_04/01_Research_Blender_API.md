---
pagetitle: 4-1. Blenderが提供するAPIを調べる
subtitle: 4-1. Blenderが提供するAPIを調べる
---

[2章](../chapter_02/index.html) や [3章](../chapter_03/index.html) で紹介したサンプルアドオンでは、Blenderが提供するさまざまなAPIを使われていました。
ところで、サンプルアドオンで利用したAPIはどのように調べたのでしょうか？
また、サンプルアドオンで紹介していないAPIはどのように調べたらよいのでしょうか？
本節ではこの疑問に答えるため、Blenderが提供するAPIについて調べる方法を紹介します。


# Blenderが提供するAPIの情報源

Blenderが提供するAPIの情報を収集する主な方法としては、次の方法があります。

* Blender公式のAPIリファレンスを読む
* Blenderに付随するスクリプトのテンプレートを読む
* BlenderのUIからAPIを調べる
* Blenderアドオン開発の参考サイトを読む
* 他者が作成したアドオンのソースコードを読む
* Googleで検索する
* Blenderのコミュニティサイトで質問する
* PythonコンソールでAPIを検索・実行する


# Blender公式のAPIリファレンスを読む

Blenderの情報を収集するのであれば、やはり公式のドキュメント（[https://docs.blender.org/api/](https://docs.blender.org/api/)）が一番です。
公式として提供されるドキュメントであることから、他の情報源と比較して情報の信頼性が高いです。

Blenderは、過去のBlenderのバージョン含めたすべてのバージョンのAPIについて、ドキュメント化しています。
Blenderのバージョンに応じて提供されるAPIが変わるため、対象とするバージョンのドキュメントを参照する必要があります。
例えば、Blenderのバージョンが2.80のAPIドキュメントは、[https://docs.blender.org/api/2.80/](https://docs.blender.org/api/2.80/)) から参照できます。

仮に `bpy.context` で提供されているAPIを調べたい場合は、左側のメニューより *[APPLICATION MODULES]* > *[Context Access (bpy.context)]* のページ（[https://docs.blender.org/api/blender2.8/bpy.context.html](https://docs.blender.org/api/blender2.8/bpy.context.html)）を開くとよいでしょう。


## BlenderからAPIリファレンスへ移動する

Blenderの機能に対応するAPIのリファレンスに、Blenderから直接移動することもできます。
ここでは、*[3Dビューポート]* スペースのメニュー *[オブジェクト]* > *[トランスフォーム]* > *[移動]* のAPIドキュメントを表示する方法を説明します。


<div class="work"></div>

|||
|---|---|
|1|*[3Dビューポート]* スペースのメニュー *[オブジェクト]* > *[トランスフォーム]* > *[移動]* を右クリックして表示されるメニューから、[Blender PythonAPI リファレンス] をクリックします。<br>![](../../images/chapter_04/01_Research_Blender_API/move_to_api_reference_1.png "APIリファレンスへの移動 手順1")|
|2|クリックした機能に関するAPIドキュメントが存在する場合、該当するAPIのドキュメントページが表示されます。<br>![](../../images/chapter_04/01_Research_Blender_API/move_to_api_reference_2.png "APIリファレンスへの移動 手順2")|


# Blenderに付随するスクリプトのテンプレートを読む

Blenderは、各テーマに関してスクリプトのテンプレートを提供しています。
テンプレートはBlender本体が提供しているため、正常に動作することが保証されています。

Blenderが提供するAPIの概要を一通り学んでおきたい場合に、これらのテンプレートが参考になります。
テンプレートは、*[テキストエディター]* スペースのメニュー *[テンプレート]* > *[Python]* から参照できます。

![](../../images/chapter_04/01_Research_Blender_API/template_1.png "スクリプトテンプレート 手順1")

提供されているテンプレートの中で最も簡単なテンプレートは、図に示す *[Operator Simple]* です。
*[Operator Simple]* は、*[3Dビューポート]* スペースに配置されたオブジェクトの一覧を、コンソールウィンドウに表示するスクリプトです。

![](../../images/chapter_04/01_Research_Blender_API/template_2.png "スクリプトテンプレート 手順2")


# BlenderのUIからAPIを調べる

BlenderのUIを構築する処理は、Pythonで記述されています。
このため、BlenderのUIから対称のAPIを調べることができます。
APIを調べる具体的な方法は、[2-7節](../chapter_02/07_Control_Blender_UI.html) に記載されています。


# Blenderアドオン開発の参考サイトを読む

新たなAPIを知るきっかけとして、Blenderのアドオン開発について解説したWebページを参照することも考えられます。
ここでは、アドオン開発の参考になる日本語のサイトをいくつか紹介します。

|サイト|概要|
|---|---|
|[Blender Wiki](https://wiki.blender.org/wiki/Python)|Blenderの公式Wikiページです。|
|[BlenderのWiki](https://wiki3.jp/blugjp/page/12)|BLUG.jpさんが管理されているWikiページです。アドオンのページアドオン開発に関する情報があります。|
|[blugjpまとめサイト](https://sites.google.com/site/blugjp/blenderpython)|BLUG.jpさんが管理されているサイトです。BlenderでPythonを使うときの情報が公開されていますが、2.80へ移行中であるために不完全なページがあります。|
|[Qiita](https://qiita.com/tags/blender)|プログラマ向けの情報共有サイトです。Blender専用のタグもあります。|
|[YouTube](https://www.youtube.com/)|BlenderのPythonに関するチュートリアル動画がアップロードされています。*[blender]* や *[python]* などで検索しましょう。|


# 他者が作成したアドオンのソースコードを読む

他者が作成したアドオンのソースコードを読むことでも、Blenderが提供するAPIを調べることができます。
なお、ソースコードを参照して処理を流用する場合は、[4-3節](03_Determine_License_of_Add-on.html) で説明するアドオンのソースコードに適用されているライセンスに気をつけてください。
ライセンスによっては流用できない場合もありますし、流用に必要な条件が決められている場合もあります。

インストール済みのアドオンのソースコードが置かれている場所は、トップバーのメニュー項目 *[編集]* > *[プリファレンス...]* で開いたプリファレンスにおいて、左の *[アドオン]* を選択したときに表示されるアドオンの情報から確認できます。
Web上に公開されているアドオンなど、非公式に提供されるアドオンの場合はソースコードがそのまま提供されていることが多いため、直接ソースコードを読むことができるかもしれません。

![](../../images/chapter_04/01_Research_Blender_API/read_addon_source_code.png "アドオンのソースコードを読む")


# Googleで検索する

実現したいことや発生した問題が明らかである場合は、Google検索が問題解決のために役立ちます。
例えば、検索ワードとして「bpy」や「blender」、「python」を指定すると、BlenderのAPIに関して調べることができます。
また、問題が発生したときに、コンソールウィンドウやオペレータメッセージにエラーメッセージが出力されているのであれば、エラーメッセージをそのまま検索ワードに指定することで、発生した問題に対する解決方法が見つかるかもしれません。

Googleの検索はとても強力であるため、アドオン開発時に生じるほとんどの問題は、この方法で解決できます。
ただし、発生した問題があまり一般的ではなかったり、Blenderから提供され始めたばかりのAPIに関する問題であったりした場合は、Google検索を利用しても解決できないことがあります。


# Blenderのコミュニティサイトで質問する

APIドキュメントを調べたり、他のアドオンを参考にしたりしても問題が解決しないときは、コミュニティサイトで質問してみましょう。
幸いなことに、Blenderアドオンの開発に関して質問できるサイトはいくつかあります。

ここでは、Blenderのアドオン開発について質問できるコミュニティサイトを紹介しますが、いずれも海外のサイトであるため、英語で質問を投稿する必要があります。

|サイト|概要|
|---|---|
|[Blender Artists Community](https://blenderartists.org)|海外最大のBlenderコミュニティサイトです。アドオン開発に関して質問する場合は、*[Coding]* > *[Python Support]* にトピックを立てましょう。|
|[Blender Stack Exchange](http://blender.stackexchange.com)|Stack Overflow（http://stackoverflow.com）という、プログラマの間で有名な情報共有サイトがありますが、Blender Stack Exchangeはその派生サイトで、Blenderに特化されています。 アドオン開発に関して質問をする場合、*[Python]* や *[add-on]*、*[scripting]* のタグを追加しましょう。|
|[reddit](https://www.reddit.com)|ニュース記事などのトピックを立てて、コメントをもらうためのWebサービスです。BlenderのPythonに関する投稿は、[/r/blenderpython](https://www.reddit.com/r/blenderpython) で行いましょう。|


# PythonコンソールでAPIを検索・実行する

[2-2節](../chapter_02/02_Register_Multiple_Operation_Classes.html) で紹介したように、Pythonコンソールを活用し、Blenderが提供するAPIを検索して実行できます。

APIリファレンスだけではわからなかった、APIの動作を確認できる点がPythonコンソールを利用するメリットになります。
APIを使ったときに、リファレンスから期待した動作と異なることはよくあることですし、そもそもAPIのリファレンスが存在しないこともあります。
Pythonコンソールを活用することで、よりAPIへの理解が深まると思いますので、積極的に活用していきましょう。


# まとめ

本節では、Blenderが提供するPython APIを調べる方法について紹介しました。
筆者がAPIを調べるときは、基本的にGoogleで似たような処理を行っているアドオンを検索し、そのアドオンのソースコードを参考にします。
そして次に、公式のAPIリファレンスで仕様を確認したあと、Pythonコンソールを使って動作確認します。
もし欲しい情報が得られなかった場合は、コミュニティサイトで質問します。

アドオン開発に限ったことではなく、プログラミング全般に言えることですが、アドオン開発において、他者が作成したプログラムは最も参考になります。
さまざまなアドオンのソースコードを読んで真似して改造しつつ、わからないところを調べるという流れを繰り返すことで、独自のアドオンが作れるようになってきます。
ただし、他者のソースコードを扱う場合、[4-3節](03_Determine_License_of_Add-on.html) で説明するソースコードのライセンスには注意しましょう。


## ポイント

* 公式のリファレンスやサンプルを読む以外にも、他者が作成したアドオンのソースコードを読んだり、実際にAPIを実行して確かめたりすることでも、Blenderが提供するAPIを調査できる
* アドオンの開発に慣れるもっとも効率的な方法は、他者が作成したアドオンのソースコードを読んで具体的なAPIの使い方を知り、改造してその効果を実際に確かめることである
