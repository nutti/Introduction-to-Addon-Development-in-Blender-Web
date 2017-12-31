<div id="sect_title_img_4_1"></div>

<div id="sect_title_text"></div>

# Blenderが提供するAPIを調べる

<div id="preface"></div>

###### これまで紹介したサンプルを作るために、Blenderが提供するさまざまなAPIを使いました。<br>ところで、サンプルで利用したAPIはどのようにして使い方を理解すればよいのでしょうか？<br>本節ではこの疑問に答えるため、Blenderが提供するAPIについて調べる方法を紹介します。


## Blenderが提供するAPIの情報源

Blenderが提供するAPIの情報を収集する主な方法としては、次の6つの方法があります。

* Blender公式のAPIリファレンスを読む
* *Pythonコンソール* でAPIを検索・実行する
* スクリプトのテンプレートを読む
* Blenderアドオン開発の参考サイトを読む
* 他者が作成したアドオンのソースコードを読む
* Googleで検索する
* Blenderのコミュニティサイトで質問する

ここで挙げたそれぞれの方法について、詳しく見ていきます。


## Blender公式のAPIドキュメントを読む

Blenderの情報を収集するのであれば、やはり公式のドキュメントが一番です。間違いや記述不足などのドキュメントとして不足しているところはありますが、公式として提供されるドキュメントであることから、他の情報源と比較して情報の信頼性が高いです。Blenderが提供するAPIについても、Blenderの公式のドキュメントから確認することができます。

<div id="webpage"></div>

|API documentation|
|---|
|https://docs.blender.org/api/|
|![API documentation](https://dl.dropboxusercontent.com/s/3pgs57v7b29ngo8/blender_api_doc.png "API documentation")|


Blenderは、過去のBlenderのバージョン含めたすべてのバージョンのAPIについて、ドキュメント化しています。Blenderのバージョンに応じて提供されるAPIが変わるため、アドオン開発者は、利用しているBlenderのバージョンのドキュメントを参照する必要があります。

本書のサンプルは2.75aのBlenderを対象としているため、以降はBlenderのバージョンが2.75aであるドキュメントを参照することを前提として説明します。

<div id="webpage"></div>

|API documentation (Blender 2.75a)|
|---|
|https://docs.blender.org/api/blender_python_api_2_75a_release/|
|![API documentation 2.75a](https://dl.dropboxusercontent.com/s/hmzkcciai4ooigb/blender_api_doc_2_75a.png "API documentation 2.75a")|


APIドキュメントの右側のページには、提供されているAPIがモジュールごとにメニュー化されて表示されています。APIは大きく分けて次の3つのモジュールのグループに分けられています。

|項目|内容|
|---|---|
|Application Modules|基本モジュール(bpyモジュール)。<br>Blender本体のデータにアクセスするために最低限必要なモジュール|
|Standalone Modules|拡張モジュール。<br>Application Modulesを簡単に利用できるようにするためのAPIなど、アドオン開発の際に便利なAPIが提供されているモジュール|
|Game Engine Modules|Blender Game Engine向けのAPIが提供されているモジュール|

Game Engine Modulesは、Blenderに備わっているゲームエンジン『Blender Game Engine（BGE）』を利用するためのモジュールであるため、アドオン開発時には使用しません。このため、アドオン開発に限ってAPIを利用するのであれば、Application ModulesとStandalone Modulesのみを確認すれば問題ありません。


### Application Modules

Application Modulesである ```bpy``` モジュールは、非常に大きなモジュールであるため、次に示す複数のサブモジュールから構成されています。アドオン開発時に必ず必要となるモジュールであるため、一度目を通しておき、どのようなモジュールが提供されているかを確認しておきましょう。

|サブモジュール名|概要|
|---|---|
|```bpy.context```|現在のBlenderの実行状態（コンテキスト）を取得するためのAPI群|
|```bpy.data```|メッシュや画像データなど、Blenderの内部情報へアクセスするためのAPI群|
|```bpy.ops```|Blenderの内部情報に対して操作を行うAPI群や、アドオンで登録した操作|
|```bpy.types```|Blenderの内部情報で使用するデータを表す型|
|```bpy.utils```|アドオンで作成したクラスの登録など、Blenderの内部情報へ影響を与えない便利API群|
|```bpy.path```|ファイルのパスを簡単に扱うためのAPI群|
|```bpy.app```|Blenderのバージョンなど、Blender本体の情報を取得するためのAPI群|
|```bpy.props```|プロパティクラス|



### Standalone Modules

Standalone Modulesは、```bpy``` モジュールを拡張するモジュールです。Application Modulesを使っただけでは実装が大変な処理を、簡単かつ効率的に実現できるAPIが提供されています。

Standalone Modulesに含まれるモジュールを次に示します。```bgl``` モジュールや ```blf``` モジュールなどの独自にUIを構築できるモジュールや、```aud``` モジュールのようにオーディオファイルを扱うことのできるモジュールも、Standalone Modulesに含まれています。

|モジュール名|概要|
|---|---|
|```mathutils```|行列やベクトルなどのクラスや、行列演算やベクトル演算を簡単に行うことができる関数群<br> ```geometry``` や ```kdtree``` サブモジュールを利用することで、図形の交差判定や3D空間内のオブジェクト探索を高速に行うことも可能|
|```bgl```|PythonからOpenGLへアクセスするためのラッパー関数群|
|```blf```|テキスト描画を簡単に行うための関数群|
|```gpu```|GLSLを扱うための関数群|
|```aud```|オーディオファイルの読み込みや再生などを行うための関数群|
|```bpy_extras```|```bpy``` モジュールのみでは実装が大変な処理について、アドオン開発者が簡単に実現できるようにした便利関数群|
|```bmesh```|メッシュデータを容易に扱うための関数群|


APIドキュメントの使い方を理解するために、*3Dビュー* エリアでアクティブ状態のオブジェクトを取得するためのAPI ```bpy.props.EnumProperty``` を調べてみましょう。

<div id="sidebyside"></div>

|APIドキュメントのWebページを開いた後、*Application Modules* > *Property Definitions (bpy.props)* をクリックし、```bpy.props.EnumProperty``` を探します。<br>すると右図のように、APIの説明に加えて引数や各引数の説明を見ることができます。|![API documentation EnumProperty](https://dl.dropboxusercontent.com/s/xvi335558nxtwhi/blender_api_doc_enum_property.png "API documentation EnumProperty")|
|---|---|



## PythonコンソールでAPIを検索・実行する

[2-2節](../chapter_02/02_Register_Multiple_Operation_Classes.md)で紹介しましたが、*Pythonコンソール* を活用し、Blenderが提供するAPIを検索・実行することができます。ここでは、*Pythonコンソール* を使って *3Dビュー* エリア上のオブジェクトを操作するAPIを調べてみます。


<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*3Dビュー* エリア上にあるオブジェクトの一覧を参照できるAPI、```bpy.data.objects``` を *Pythonコンソール* に入力します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*ctrl* + *space* キーを押すと、*3Dビュー* エリア上のオブジェクトの一覧が入力候補として表示されます。|![Pythonコンソールウィンドウ 手順1](https://dl.dropboxusercontent.com/s/6tqu81bbk6l6qy8/python_console_1.png "Pythonコンソールウィンドウ 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*3Dビュー* エリア上にあるオブジェクト名が候補として表示されるため、適当なオブジェクト名を入力します。ここでは、```Cube``` を入力しました。入力したあと、再度 *ctrl* + *space* キーを押して次の入力候補を表示します。|![Pythonコンソールウィンドウ 手順2](https://dl.dropboxusercontent.com/s/yu890kcedpewpih/python_console_2.png "Pythonコンソールウィンドウ 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|入力候補の中にある ```select``` を入力し、実行します。すると、選んだオブジェクトが選択状態である場合には ```True``` が、選択状態でない場合は ```False``` が表示されます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|手順4で入力した変数に対して ```True``` を代入すると、オブジェクトを選択状態にすることができます。一方、```False``` を代入するとオブジェクトを非選択状態にします。|![Pythonコンソールウィンドウ 手順3](https://dl.dropboxusercontent.com/s/0aph2y0pq6edyxf/python_console_3.png "Pythonコンソールウィンドウ 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


これらの一連の動作から、```select``` はオブジェクトが選択状態か非選択状態かを調べるためのAPIであると予想できます。

ここで、Blender公式のAPIドキュメント（```https://docs.blender.org/api/blender_python_api_2_75a_release/bpy.types.Object.html#bpy.types.Object.select```）を調べてみると、次のように記載されています。

<div id="quote"></div>

> Object selection state


*Pythonコンソール* における調査から予想した機能と一致しています。このように *Pythonコンソール* を利用することで、APIの動作を確認することができます。APIのドキュメントを確認することも重要ですが、実際に *Pythonコンソール* でAPIを使ってその効果を確認することも重要です。APIを使った時に、ドキュメントで期待した動作と異なることはよくあることですし、時にはドキュメントが間違っていることや、そもそもドキュメントが存在しない場合もあります。*Pythonコンソール* を活用することでよりAPIへの理解が深まると思いますので、積極的に活用していきましょう。


## スクリプトのテンプレートを読む

<div id="sidebyside"></div>

|BlenderでPythonスクリプトを書く人向けに、Blenderはスクリプトのテンプレートを用意しています。<br>テンプレートはBlender本体が提供しているため、正常に動作することが保証されています。実現したい処理のテンプレートが存在する場合は、一度確認してみるとよいでしょう。また、Blenderが提供するAPIの概要をひととおり学んでおきたい場合にも、本サンプルは参考になると思います。<br>テンプレートは、*テキストエディター* エリアのメニュー *テンプレート* > *Python* から参照することができます。|![テンプレート 手順1](https://dl.dropboxusercontent.com/s/bvnb1360j99fd1t/template_1.png "テンプレート 手順1")|
|---|---|



<div id="sidebyside"></div>

|提供されているテンプレートの中で最も簡単なテンプレートは、右図に示す *Operator Simple* です。*Operator Simple* は、*3Dビュー* エリアにあるオブジェクトの一覧をコンソールウィンドウに表示するスクリプトです。|![テンプレート 手順2](https://dl.dropboxusercontent.com/s/8nt0v8zdkhl1egd/template_2.png "テンプレート 手順2")|
|---|---|


## Blenderアドオン開発の参考サイトを読む

Blenderが提供するAPIを調べる手段として、Blenderアドオン開発の参考サイトを読む方法もあります。しかし、この方法はあまり効率がよいとは言えません。Blender本体の使い方を解説しているサイトはそれなりに存在するものの、アドオン開発の解説サイトは非常に少ないからです（アドオン開発の解説サイトが少なかったことがきっかけで、本書を執筆しました）。特に日本語の解説サイトは、数を数えられるくらい少ないです。

ここでは、アドオン開発で筆者がよく参考にするサイトをピックアップしてみました。


<div id="webpage"></div>

|Blender Wiki|
|---|
|https://wiki.blender.org/index.php/Dev:Py/Scripts|
|![Blender Wiki](https://dl.dropboxusercontent.com/s/wjaloh1eov0ij73/blender_wiki.png "Blender Wiki")|

Blenderの公式Wikiページです。アドオン開発のチュートリアルやベストプラクティスなど、アドオンの開発に必要な知識を得ることができます。特にテーマに応じて簡単なサンプルを紹介しているCode Snippetsは、特定の処理を実現する時に役立つでしょう。

また、アドオンの公開手順についても書かれていますので、初心者だけでなく、ある程度アドオン開発に慣れた方もよくお世話になるサイトです。


<div id="webpage"></div>

|blugjpまとめサイト|
|---|
|https://sites.google.com/site/blugjp/blenderpython|
|![blugjpまとめサイト](https://dl.dropboxusercontent.com/s/7t6ho0xohl45yrv/blugjp.png "blugjpまとめサイト")|

Blenderを使っている方はおそらくご存知であろう、BLUG.jpさんによるまとめサイトです。BlenderPythonのページにアドオン開発の情報があります。BlenderPythonのページは現在も更新され続けていますので、アドオン開発者はブックマークしてときどき見に行くとよいでしょう。Blenderのアドオン開発に慣れてきて、ぜひ他のアドオン開発者のために情報を共有したい、ということであれば、BlenderPythonページの更新を依頼してみてください。BLUG.jpさん（Twitter：@blug_jp）に連絡すれば、編集権限を与えてもらえるかもしれません。


<div id="webpage"></div>

|Qiita|
|---|
|https://qiita.com|
|![Qiita](https://dl.dropboxusercontent.com/s/hfbzff310mmph6m/qiita.png "Qiita")|


Qiitaはプログラマのための情報共有サイトです。数は多くないですが、Blenderに関係する投稿がいくつかあります。Blenderに関する投稿の一覧は、Blenderタグ（http://qiita.com/tags/blender ）で確認できます。


## 他者が作成したアドオンのソースコードを読む

Blenderのアドオンは、Pythonのソースコードとして配布されていますので、他者が作成したアドオンのソースコードを読むことでも、Blenderが提供するAPIを調べることができます。もしアドオンを作っている時に、実現しようとしている処理が他のアドオンで使われていれば、そのアドオンのソースコードを参照することで、実装方法や使われているAPIを知ることができます。なお、ソースコードを参照して処理を流用する場合は、[4-4節](04_Determine_License_of_Add-on.md)で説明するアドオンのソースコードに適用されているライセンスに気をつけてください。ライセンスによっては流用できない場合もありますし、流用に必要な条件が決められている場合もあります。


<div id="sidebyside"></div>

|インストール済みのアドオンのソースコードが置かれている場所は、*ファイル* > *ユーザ設定...* で開くユーザー・プリファレンスの *アドオン* タブから確認することができます。<br>Web上に公開されているアドオンなど、非公式にインストールするアドオンの場合はソースコードとして提供されていることが多いため、直接ソースコードを読むことができます。|![アドオンのソースコードを読む1](https://dl.dropboxusercontent.com/s/0gkzz3ww1gjb955/read_addon_source_code_1.png "アドオンのソースコードを読む1")|
|---|---|


### Blender内でソースコードを確認する方法

[2-8節](../chapter_02/08_Control_Blender_UI_1.md)で説明したように、UIをはじめとしたBlenderが標準で提供している機能については、一部Blender内でソースコードを確認することができます。ここでは、*3Dビュー* エリアのメニュー *オブジェクト* のソースコードを確認する方法を説明します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*3Dビュー* エリアのメニュー *オブジェクト* にマウスカーソルを置いて右クリックし、表示されたメニューから *ソース編集* をクリックします。|![アドオンのソースコードを読む2](https://dl.dropboxusercontent.com/s/7gw1t5faq9eyl67/read_addon_source_code_2.png "アドオンのソースコードを読む2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*テキストエディター* エリアにソースコードが表示されます。|![アドオンのソースコードを読む3](https://dl.dropboxusercontent.com/s/bdvh1yevo0m6j5s/read_addon_source_code_3.png "アドオンのソースコードを読む3")|
|---|---|---|

<div id="process_start_end"></div>

---

### APIドキュメントへ移動する方法

Blenderが標準で提供している機能のソースコードを確認することに加え、APIドキュメントへ移動することもできます。ここでは、*3Dビュー* エリアのメニュー *メッシュ* > *ミラー* > *ローカルX軸* のAPIドキュメントを表示する方法を説明します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*3Dビュー* エリアのメニュー *メッシュ* > *ミラー* > *ローカルX軸* を右クリックして表示されるメニューから、*Blender PythonAPI リファレンス* をクリックします。|![アドオンのソースコードを読む4](https://dl.dropboxusercontent.com/s/as7l6gpnylb8qvc/read_addon_source_code_4.png "アドオンのソースコードを読む4")|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|クリックした機能に関するAPIドキュメントが存在する場合、該当するAPIのドキュメントページが表示されます。|![アドオンのソースコードを読む5](https://dl.dropboxusercontent.com/s/15i3rc3jspnoqp3/read_addon_source_code_5.png "アドオンのソースコードを読む5")|
|---|---|

<div id="process_start_end"></div>

---


<div id="space_s"></div>


## Googleで検索する

実現したいことや発生した問題が明らかにわかっている場合は、Google検索が問題解決のために役立ちます。例えば、検索ワードとして *bpy* や *blender* 、*python* を指定すると、BlenderのAPIに関して調べることができます。また、もし問題が生じたときに、コンソールウィンドウやスクリプト実行ログにエラーメッセージが出力されているのであれば、エラーメッセージをそのまま検索ワードに指定することで、発生した問題に対する解決方法が見つかるかもしれません。

Googleの検索はとても強力ですので、アドオン作成時に生じたほとんどの問題は、この方法で解決することができます。しかし、発生した問題があまり一般的ではなかったり、提供され始めたばかりのAPIに関する問題であったりした場合は、Google検索を利用しても解決できないことがあります。


## Blenderのコミュニティサイトで質問する

APIドキュメントを調べたり、他のアドオンを参考にしたりしても問題が解決しない場合もあります。このときは最終手段になりますが、コミュニティサイトで質問してみましょう。

幸いなことに、Blenderアドオンの開発に関して質問できるサイトはいくつかあります。ただし、執筆時点でアドオン開発に関して質問できる国内のサイトは存在しません。このため、アドオン開発について質問できるのは海外サイトしかなく、英語で質問を投稿する必要があります。海外サイトで投稿することに抵抗がある方も多いと思いますが、高等学校の英語レベルがあれば十分通用しますので、ぜひチャレンジしてみてください。

ここでは、Blenderのアドオン開発について質問できるコミュニティサイトを紹介します。


<div id="webpage"></div>

|Blender Artists Community|
|---|
|http://blenderartists.org/forum/|
|![Blender Artists Community](https://dl.dropboxusercontent.com/s/0e6nkncctmwl0ak/blender_artists.png "Blender Artists Community")|

海外最大のBlenderコミュニティサイトで、略してBAと呼ばれることもあります。Blenderで制作した作品を投稿するのが主な目的であるサイトですが、アドオン開発についても活発な議論が行われています。作ったアドオンを投稿してフィードバックをもらうこともできますし、既存のアドオンに対して意見や要望を出すこともできます。また、アドオン開発に関して質問することもできます。

非常に有名なサイトであるため、Blenderを使っている方は1度は見たり聞いたりしたことがあるのではないでしょうか。まだ一度も閲覧したことがない方は、海外のBlenderのコミュニティの雰囲気を知るよい機会でもあるため、ぜひ訪れてみてください。なお海外サイトですので、英語で投稿する必要がありますが、高等学校レベルの英語力があれば困ることはないと思います。

アドオンに関して質問したい場合は、アカウントを登録した後に *CODING* > *Python Support* の *POST NEW THREAD* ボタンからスレッドを立てます。


<div id="webpage"></div>

|Blender Stack Exchange|
|---|
|http://blender.stackexchange.com|
|![Blender Stack Exchange](https://dl.dropboxusercontent.com/s/0zrdm4aebb5xm20/blender_stack_exchange.png "Blender Stack Exchange")|

Stack Overflow（http://stackoverflow.com ）と呼ばれる、プログラマ間では非常に有名な情報共有サイトがあります。本サイトはその派生サイトで、Blenderに特化した情報共有サイトです。Blender Artists Communityに負けず、本サイトでもアドオン開発に関して活発な議論が行われています。情報共有に特化したサイトであることから、アドオン開発に関してはBlender Artists Communityよりも得られる情報が多く、質問に対して回答が得られやすいように思えます。また、アドオン開発だけでなくBlenderの使い方に関して質問することもできます。

Blender Stack Exchangeで質問するためには、Blender Artists Communityと同様にアカウントを登録し、英語で投稿する必要があります。質問の投稿は、*Ask Question* ボタンから行うことができます。アドオン開発に関する質問の場合、*Python* や *add-on* 、*scripting* のタグに加えて、質問内容に応じて関連するタグ（*mathematics* や *opengl* など）を設定すると回答が得られやすくなります。

本サイトでは、質問したり他人の質問に回答したり誤字や脱字などを編集したりすることで、ユーザがポイントを得られる仕組みがあり、それぞれのユーザの貢献度を見ることができます。さらにポイントを獲得していくことで、PS4のトロフィーやXBoxの実績のようなバッジを獲得することができ、登録直後の段階で制限されていた機能が使えるようになる仕組みもあります。


<div id="webpage"></div>

|Blender.jp|
|---|
|https://blender.jp|
|![Blender.jp](https://dl.dropboxusercontent.com/s/m74dd41qm8xpw7c/blender_jp.png "Blender.jp")|

国内では最大と思われる、Blenderのコミュニティサイトです。本コミュニティサイトには、Blenderについて議論できるフォーラムがあり、かつてフォーラム内の質問板でアドオン開発について質問することができました。なお、現時点でフォーラムはリードオンリーになっており、投稿することができなくなっています。


<div id="webpage"></div>

|reddit|
|---|
|https://www.reddit.com/|
|![reddit](https://dl.dropboxusercontent.com/s/k0bsrmk29gyuta4/reddit_blender_python.png "reddit")|

ニュース記事などのトピックを立てて、コメントをもらうためのWebサービスです。電子掲示板のようなものと考えるとわかりやすいかもしれません。redditではプログラミングに関する質問を投稿することができ、数は多くないですが、BlenderにおけるPythonスクリプトに関する投稿もされています（もちろんBlender本体に関する質問も投稿されています）。

redditにはsubredditと呼ばれる、特定のジャンルに特化した投稿を見ることができる機能（他のWebサービスでのタグのようなもの）があります。BlenderのPythonに関する投稿を見る場合は、次に示すsubredditを確認するとよいと思います。

* /r/blender - https://www.reddit.com/r/blender/
  * Blender全般に関する投稿
* /r/blenderpython - https://www.reddit.com/r/blenderpython/
  * BlenderでのPythonスクリプトに関する投稿


### コミュニティサイトで質問する前に

アドオンの情報を得られるコミュニティサイトについて紹介してきましたが、コミュニティサイトで質問する時には、相手が理解しやすい投稿を心がけましょう。投稿内容をわかりやすく書くのはもちろんのこと、ソースコードや実行結果を一緒に投稿すると問題点が相手に伝わりやすくなります。そして忘れてはならないのが、回答に対するお礼です。回答者も時間を費やして回答してくれていますので、回答により問題が解決したか否かに関わらず、回答に対するお礼をすることを忘れてはいけません。

なお、コミュニティサイトで質問すれば、欲しい情報をストレートに得られる可能性がありますが、回答する側も回答の記事を作成するのに時間を費やすため、何でもかんでも質問するのは控えるべきです。コミュニティサイトで質問する前に、まず次のことを全て行ったかを確認してから質問することを心がけてください。余談ですが、Blender Stack Exchangeで質問を投稿する際に質問のタイトルを入力すると、タイトルに入力された単語と関連性の高い質問が表示されます。

* 公式のAPIドキュメントを調べること
* 心当たりのあるアドオンのソースコードを確認すること
* Googleなどの検索で、解決方法がないか確認すること
* コミュニティサイトで似たような質問がないか確認すること。（ただし、似たような質問がすでに投稿されていた場合でも、回答の内容を試してうまくいかない場合は再度質問してもよいと思います。ただしその時は、参考にした投稿へのリンクなどを質問内容に含めるようにしましょう。）


## まとめ

本節では、Blenderが提供するAPIを調べる方法について紹介しました。筆者がAPIを調べる時はGoogle検索を利用し、まず最初に似たような処理を行っているアドオンのソースコードを参考にします。そしてソースコードの中でわからない部分は、公式のAPIドキュメントで仕様を確認したあと、*Pythonコンソール* を使って動作確認します。ここまで行っても欲しい情報が得られない場合は、コミュニティサイトで質問します。

アドオン開発に限ったことではなくプログラミング全般に言えることですが、他者が作成したプログラムのソースコードはアドオン開発において最も参考になります。他者が作ったソースコードを読んで真似して改造しつつ、わからないところを調べるという流れを繰り返すことで、独自のアドオンが作れるようになっているはずです。ただし、他者のソースコードを扱う場合、[4-4節](04_Determine_License_of_Add-on.md)で説明するソースコードのライセンスには注意しましょう。


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderが提供するAPIは、公式のリファレンスやサンプルを読む以外にも、他者が作成したソースコードを読んだり、実際にAPIを実行して確かめたりすることでも調査できる
* 一番効率的なAPIの調査方法は、他者が作成したアドオンのソースコードを読んでAPIの具体的な使い方を知ることである
* コミュニティサイトで質問する場合は、自分自身が可能な範囲で調査を行ってから、質問を投稿しよう
