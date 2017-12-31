<div id="sect_title_img_4_6"></div>

<div id="sect_title_text"></div>

# アドオンをBlender本体に取り込んでもらう

<div id="preface"></div>

###### [4-3節](03_Publish_your_Add-on.md)ではアドオンを多くの人に使ってもらう方法として、作成したアドオンをBlender本体に取り込んでもらうことを紹介しました。作成したアドオンをBlenderに取り込むまでには非常に手間がかかりますが、手間がかかった分だけアドオンのユーザが確実に増えます。<br>そこで本書の最後では、作成したアドオンをBlender本体に取り込んでもらうまでに必要な一連の流れを説明します。


## アドオンをBlender本体に取り込んでもらうために必要な条件

[1-2節](../chapter_01/02_Use_Blender_Add-on.md)ではアドオンのサポートレベルについて説明しましたが、作成したアドオンをBlender本体に取り込んでもらうためには、ReleaseまたはContribのサポートレベルとして認定される必要があります。また、Contribのサポートレベルではビルド時のBlenderのみしかインストールされないため、公式にリリースされたBlenderへ取り込んでもらうためには、Releaseのサポートレベルとして認定される必要があります。

ここでは、作成したアドオンがReleaseまたはContribのサポートレベルに認定されるまでの過程を紹介します。


## Blender本体に取り込んでもらうまでの流れ

Blender本体にアドオンを取り込んでもらうまでには、次に示す7つのステップをすべて終える必要があります。


<div id="custom_ol"></div>

1. アドオンの機能が存在しないこと確認する
2. アドオンのコーディング規約を守る
3. アドオンの機能レビューを受ける
4. アドオンのWikiページを作成する
5. アドオンのソースコードレビューを受ける
6. Blenderのリポジトリへアドオンを登録する
7. アドオンのサポートページを開設する


### 1. アドオンの機能が存在しないことを確認する

アドオンをBlender本体に取り込んでもらいたいと考えている場合、作成したアドオンの機能がBlender本体や、ReleaseまたはContribのサポートレベルのアドオンの機能の中に同じまたは似ている機能がないかを確認する必要があります。

ReleaseまたはContribのサポートレベルであるアドオンは、Blenderの公式wikiのアドオンカタログから一覧を参照できます。

<div id="webpage"></div>

|Blender Wiki (Blender Add-ons Catalog)|
|---|
|http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts|
|![Blender Wiki (Blender Add-ons Catalog)](https://dl.dropboxusercontent.com/s/eqhblsox8zibbh8/blender_add-on_catalog.png "Blender Wiki (Blender Add-ons Catalog)")|

作成したアドオンの機能が、カタログで掲載されているアドオンやBlender本体に存在しない場合には、Blender本体に登録されるまでの大きな山の1つを越えたことになります。なぜこのステップが大きな山になるのかというと、すでに存在する機能や似たような機能がBlenderから提供されている場合は、アドオンをBlender本体に取り込んでもらうことが非常に困難になるからです。

しかし、もし仮に同様の機能を持つアドオンが存在した場合でも、諦めるのはまだ早いです。公開されているアドオンに性能面や機能面で問題点や改善点がないか、確認してみましょう。公開されているアドオンを改善すれば、修正したアドオンをBlender本体に反映できるかもしれません。もちろん公開されているアドオンについて何も進展がないようなアドオンでは、Blender本体への登録は厳しいので、そのような場合はアドオンの登録は諦めましょう。


### 2. アドオンのコーディング規約を守る

アドオンをBlender本体と一緒に公開するということは、言い換えると **Blenderのソフトウェアの1つとして公開する** ことと同じですので、アドオンのソースコード自体の品質もある一定以上のものが求められます。このため、Blender本体にアドオンを取り込んでもらうためには、ソースコード作成時に品質を意識する必要があります。

品質をあげるといっても、何をすれば良いのかわからない方が多いと思います。品質というと製品レベルのものが求められるのではないか、と思ってしまう方もいると思いますが、Blenderの開発者はアドオンに対して、製品レベルの品質までは求めていないようです。このため、コーディング規約を守ってコーディングすることを心がければ、品質に対する意識は十分であると思います。仮に、もしコーディング規約を守らなかった場合でも、後のソースコードレビューで指摘されます。とはいえコーディング規約は、きれいなソースコードを書く上で知っておくとよいことですので、レビューで指摘されてから直すのではなく、アドオン作成時に常に意識しておくことが大切です。

なお本書では、アドオンの機能レビューの前にコーディング規約に対応させる手順となっていますが、必ずしもこの順番を守る必要はありません。このため、機能レビューに通ったあとにコーディング規約に対応しても問題ありません。むしろ機能レビューが必ず通ることは保証できないため、先にレビューを実施し、作成したアドオンがBlender本体と一緒に公開できそうか見極めることで、万が一レビューに通らなかったときに無駄な作業が発生しなくなります。

コーディング規約を意識する必要があるとはいえ、毎回コーディング規約に従っているのかを目で追って確認するのは大変です。そこで、コーディング規約が守られているかを確認するためのツール（lintとか文法チェッカーと呼ばれる）を利用します。Pythonの文法チェッカーの代表的なものを次に示します。もちろんここで挙げたツール以外にも、多数の文法チェッカーがWeb上で公開されています。

* pep8
* pyflakes
* flake8
* pylint

Blenderのアドオン開発では、**文法チェッカーflake8によるコードチェックに合格していること** がコーディング規約となっています。flake8の使い方については、Web上に使い方などをまとめたサイトがたくさんありますので、ここでは説明しません。

<div id="webpage"></div>

|flake8|
|---|
|https://pypi.python.org/pypi/flake8|
|![flake8](https://dl.dropboxusercontent.com/s/d9hx6l3lgolp5vi/flake8.png "flake8")|


コーティング規約を守るだけでなく、Blender本体に取り込まれるアドオンは処理自体も効率的である必要があります。アドオンを使う人にとっては、少しでも速くアドオンの処理が終わるほうがBlenderでの作業効率が向上して嬉しいはずです。

ただし、効率的な処理と呼ばれるものがどのようなものか、わからない方もいるでしょう。このため、Blenderはアドオン開発者に対して、効率的なコーディングをするために必要な、ベストプラクティスとよばれる記事を公開しています。普通にアドオンを作っていただけでは意識しないようなことも書かれているため、これからアドオンを開発する人だけでなく、すでにアドオンを何度か作ったことのある方も一度目を通しておきましょう。

<div id="webpage"></div>

|Best Practice (API documentation - Blender 2.75a)|
|---|
|https://docs.blender.org/api/blender_python_api_2_75a_release/info_best_practice.html|
|![Best Practice](https://dl.dropboxusercontent.com/s/30rrshlzu3jnajy/best_practice.png "Best Practice")|


ここでは、上記のページで紹介されている、効率的なコーディングの実例を1つ紹介します。

最初に、リストに格納された値を2倍にしたリストを作成する、次のコードを見てください。

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_l = []
for i in l:
    double_l.append(i * 2)
double_l

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

上記のコードは正しく動作しているため、記述に間違いはありません。しかしベストプラクティスでは、この記述が非効率なものとして取り上げられています。ベストプラクティスの記事には、for文で配列に要素を追加する処理の代わりにリスト内包表記を使うべきと書かれています。そこで、Pythonの機能であるリスト内包表記を用いて書き換えると、次のようなコードになります。

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_l = [i * 2 for i in l]
double_l

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

最終結果はどちらも同じですが、リスト内包表記を用いた方が実行速度が速いことが知られているため、Blenderではこのような書き方を推奨しています。もちろんベストプラクティスには、リスト内包表記以外にも処理を効率化するための細かいtipsがたくさん紹介されています。


<div id="column"></div>

なぜ、リスト内包表記を使った方が処理が速くなるのでしょうか。その答えをここで説明します。最初の例では、append属性を取り出して関数を呼び出して要素を追加するという処理を、append()メソッドを呼び出すたびに行っています。一方、リスト内包表記を用いた例では、リストに要素を追加する処理だけを行います。このため、リスト内包表記では、append属性を取り出して関数を呼び出す処理が発生しないため、最初の例と比較してより高速に実行されるのです。



### 3. アドオンの機能レビューを受ける

次はいよいよ、Blender開発者によるアドオンの機能レビューを受けます。

レビューと書くとソースコードのレビューを想像する方が多いかもしれませんが、Blenderのアドオン開発ではソースコードレビューを行う前に、作成したアドオンが実用的なものかを判断するための機能レビューを行います。機能レビューでは、Blender本体に取り込むに値する機能を持つアドオンであるか判断します。Blenderの開発者は忙しい方が多く、全てのソースコードのレビューを行う時間がないことから、まずは機能面でレビューするのです。

アドオンの機能レビューは、developer.blender.org（通称D.B.O）から申請することができます。なお、D.B.Oは会員制であるため、事前にユーザ登録する必要があります。

<div id="webpage"></div>

|developer.blender.org|
|---|
|https://developer.blender.org|
|![developer.blender.org](https://dl.dropboxusercontent.com/s/z9uvc1epwm2wi2e/dbo.png "developer.blender.org")|


D.B.Oへの会員登録が完了したら、次の手順に従って機能レビューのためのタスクを作成します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|右上のアイコン *★* をクリックして表示されるメニューから、*Maniphest Task* をクリックします。|![Create New Task 手順1](https://dl.dropboxusercontent.com/s/3zzr089rpl1i244/create_new_task_1.png "Create New Task 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|タスクを投稿するためのフォームが表示されるため、各入力欄に必要事項を記載して新しいタスクを作成します。|![Create New Task 手順2](https://dl.dropboxusercontent.com/s/4m757n2ubrqz4au/create_new_task_2.png "Create New Task 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---


新しいタスクを作成するために、フォームに入力する必要がある項目を次に示します。

|入力欄|入力するもの|
|---|---|
|Title|タスクのタイトルを入力します。<br>作成したアドオンの機能が分かるようなタイトルを入力します。|
|Assigned To|タスクの担当者を指定します。<br>D.B.O上で知り合いがいる場合はレビューに参加してもらえる可能性があるため、追加するとよいと思います。ここで無理して追加しなくてもタスクを見た人がレビューしてくれますので、特に知り合いがいない場合は何も追加しなくても問題ありません。ちなみに筆者自身もD.B.Oに登録しているため、タスクを割り当てていただければレビューできるかもしれません。（ユーザ名：Nutti）|
|Status|タスクの状態を指定します。新たにタスクを作成する場合は、```Open``` を指定してください。|
|Priority|タスクの緊急度を設定します。<br>新規機能は ```Normal``` を設定します。既存機能のバグ修正に関してタスクを投稿する場合は、優先度を高めに指定します。|
|Description|作成したアドオンの詳細を記載します。<br>フォーマットは特に決められていませんが、筆者がよく利用する下記のテンプレートが参考になるかもしれません。（★はコメントです）|
|Visible To|タスクの公開範囲を設定します。通常は、```Public (No Login Required)``` を指定すれば問題ありません。|
|Editable By|タスクの編集可能範囲を設定します。タスクの内容に合わせて自由に選んで問題ありません。```All Users``` などの公開範囲が広いほうが、タスクを見ることのできる人が増えるため、レビューしてくれる人も増えます。|
|Tags|プロジェクト名を指定します。<br>アドオンに関するタスクであるため、```Addons``` を指定します。|
|Subscribers|自分自身を含む、タスクをみてもらいたい人を指定します。|
|Type|新規機能のアドオンであれば ```Patch``` を選択し、バグ報告やバグ修正であれば ```Bug``` を指定します。|


```
Project: Blender Extensions
Tracker: Python Scripts Upload
Blender: X.XX - Y.YY     ★ アドオンの動作を保証するBlenderバージョン
                         ★  （bl_infoのblenderに書いたバージョンと一致させる）
Category: UV             ★ アドオンのカテゴリ
                         ★  （bl_infoのcategoryに書いたバージョンと一致させる)
Python: Z.ZZ - W.WW      ★ 本アドオンが動作するPythonのバージョン
                         ★  （4-5節で説明した方法で、Pythonのバージョンを調査する）
Script name: MyScript    ★ アドオン名
                         ★  （bl_infoのnameに書いたアドオン名と一致させる）
Author(s): Nutti         ★ アドオン作成者
                         ★  （bl_infoのauthorに書いた作成者と一致させる）
Status: Open

★ アドオンの紹介文をここに書く

[Code]
https://github.com/TTTT/UUUUUU    ★ アドオン本体をダウンロードできるリンクを書く

[Usage]
1. VVVVVVV      ★ アドオンの使い方を書く
2. WWWWWWW

Any problems and comments are welcome.

Thanks.
```


タスクを作成したあとは、レビュワーからの反応をひたすら待ちます。

筆者の経験によると、Blenderへアドオンを登録するまでの一連の手順の中でこの機能レビューが最も厳しく、最も時間がかかると思っています。レビュー中に発生する機能の改善提案への対応も大変ではあるのですが、そもそも作成したアドオンに対して改善提案を行ってくれるアドオン支持者がなかなか現れません。すでにアドオンが広く知られているのであれば話は別ですが、D.B.Oでの投稿がアドオンの初めての公開となる場合は特に時間がかかるため、辛抱強く待つしかありません。もしどうしてもレビュワーが集まらないようであれば、[4-3節](03_Publish_your_Add-on.md)で紹介したような方法でアドオンを宣伝してみましょう。

レビュワーから反応があったからとしても、それで終わりではありません。レビュワーによって提案された機能改善は、たとえ面倒で大変なものであっても積極的に行いましょう。レビュワーの意見をきちんと聞くことで、このアドオンはサポートがしっかりしているとBlenderのアドオン開発者に印象付けることができます。その結果、作成したアドオンをBlender本体に取り込んでもらえる可能性が高くなります。

そして、レビュワーやBlender開発者からBlender本体にアドオンを登録したらどうですか、といったコメントがもらえたら・・・Blender本体へのアドオンの登録はもうすぐそこです！おめでとうございます！


### 4. アドオンのWikiページを作成する

機能レビューに合格したらBlender本体へのアドオンの登録はほぼ確実ですが、登録の前にやらなければいけないことがいくつかあります。その1つが、Blender公式のWikiページに作成したアドオンのページを作成することです。機能レビュー時に指定されたサポートレベルの箇所に、アドオンのWikiページを作成します。Blenderにアドオンが登録されることが決まっている場合は、ReleaseまたはContribのいずれかサポートレベルになります。もし決まっていない場合は、D.B.Oのタスクなどで質問しましょう。

<div id="webpage"></div>

|Blender Wiki (Blender Add-ons Catalog)|
|---|
|http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts|
|![Blender Wiki (Blender Add-ons Catalog)](https://dl.dropboxusercontent.com/s/eqhblsox8zibbh8/blender_add-on_catalog.png "Blender Wiki (Blender Add-ons Catalog)")|


Wikiページの編集の仕方については、本書では説明しません。Wikiページの編集の仕方やWikiページに掲載する内容がわからない場合は、他のアドオンのWikiページを見ながら作成していくとよいです。もし仮にWikiページの内容に不備がある場合は、D.B.Oで作成したタスクなどで指摘を受けるので、その時に直せば問題ありません。参考のため、筆者が作成したアドオン『Magic UV』のWikiページのリンクを次に示します。この例のように、すでにGitHubやBlender Artists Communityをはじめとした他のWebサイトで情報を提供している場合は、情報を提供しているWebサイトへのリンクを追加するだけでもよいです。

https://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/UV/Magic_UV


機能レビューに合格する前でもBlender Wikiページを作成することができます。D.B.Oで作成したタスクの説明文においてBlender Wikiのページをリンクしたい場合などは、レビュー依頼を出す前にWikiページを作成しておくとよいと思います。なおその場合は、機能レビューに合格していない状態であることから、サポートレベルがExternalの箇所にWikiページを作成するようにしてください。

<div id="column"></div>

Blenderの公式WikiページのアカウントはD.B.Oのアカウントとは異なりますので、ユーザ登録していない場合は登録してください。



### 5. アドオンのソースコードレビューを受ける

機能レビューに合格してアドオンのWikiページを作成したら、アドオンのソースコードをBlender開発者にレビューしてもらいます。機能レビューと同じく、D.B.Oでソースコードのレビューを依頼します。

ソースコードレビューを依頼する流れを次に示します。なお、BlenderのWikiページにもソースコードレビューの手順が書かれていますので、こちらも参考にしてください。

<div id="webpage"></div>

|Blender Wiki (Code Review)|
|---|
|http://wiki.blender.org/index.php/Dev:Doc/Tools/Code_Review|
|![Blender Wiki (Code Review)](https://dl.dropboxusercontent.com/s/ugfs7ecqh0t4fao/code_review.png "Blender Wiki (Code Review)")|


#### 最新のBlenderのアドオンのリポジトリを取得

最初に、Blenderのアドオンのリポジトリを取得します。リポジトリに対する変更内容をレビュワーが確認できるようにするため、この作業が必要になります。

取得するリポジトリは、Blenderのサポートレベルによって異なることに注意が必要です。機能レビューを行ったときに、サポートレベルがReleaseまたはContribのどちらかに決まりますので、サポートレベルに対応したリポジトリを取得してください。以降では、サポートレベルがContribの場合について説明します。サポートレベルがReleaseの場合は、本節の後半で説明します。

|サポートレベル|リポジトリ|
|---|---|
|Release|```git://git.blender.org/blender-addons.git```|
|Contrib|```git://git.blender.org/blender-addons-contrib.git```|


<div id="column"></div>

サポートレベルがReleaseとして登録されているアドオンは、アドオンがすでに完成していて、すぐにでもBlenderに取り込むべきものであると判断された場合です。一方、レビュー時にアドオンが開発中である場合や、ユーザにアドオンの有用度の判断を仰ぎたい場合は、Contribのサポートレベルとして登録されます。


アドオンのリポジトリを取得するためには、次の手順に従います。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|次のコマンドを実行し、最新のリポジトリ（サポートレベルがContribであるリポジトリ）を取得します。|
|---|---|

```sh
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons-contrib.git
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|次のコマンドを実行し、作成したアドオンを、取得したリポジトリのディレクトリへコピーします。|
|---|---|

```sh
$ cd blender-addons-contrib
$ cp [作成したアドオン] .
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|次のコマンドを実行してソースコードの差分を出力し、出力結果をコピーします。|
|---|---|

```sh
$ git diff
```

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|D.B.Oの左側にあるメニューから、*Differential* をクリックします。|![Create Diff 手順1](https://dl.dropboxusercontent.com/s/2wcu3f3ho59x3ia/create_diff_1.png "Create Diff 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|続いて、*Create Diff* をクリックします。|![Create Diff 手順2](https://dl.dropboxusercontent.com/s/w9rhl9pwcwqjef3/create_diff_2.png "Create Diff 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|手順3でコピーしたソースコードの差分を *Raw Diff* にペーストし、*Repository* に ```rBAC Blender Add-ons Contrib``` を入力したあと、一番下の *Create Diff* ボタンをクリックします。|![Create Diff 手順3](https://dl.dropboxusercontent.com/s/c37hha0316mh124/create_diff_3.png "Create Diff 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


ソースコードレビューでは、作成したソースコードに対して指摘されることがあります。指摘された部分は、少なくともレビュワーが読んで気になった部分ですので、たとえアドオンの動作に影響を与えないような指摘であってもきちんと反映しましょう。


### 6. Blenderのリポジトリへアドオンを登録する

ソースコードのレビューが完了したら、次の手順に従ってリポジトリに修正内容を登録（push）します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|Blenderのアドオンのリポジトリへソースコードをpushするためは、リポジトリ管理者からリポジトリへのpush権を与えてもらう必要があります。<br>執筆時点では、Meta-Androcto氏がアドオンのリポジトリ管理を担当されているようです。push権をもらうためには、IRC（チャットのようなもの）に入ってMeta-Androcto氏に話しかけるか、Blender Artists Communityでメッセージを送るのが一番確実かと思います。場合によっては、D.B.O上でやり取りしていく中でpush権をもらえるかもしれません。<br>なお、IRCではすぐに反応を得られる反面、英語でのチャットになるため、英語がある程度できないと間違いなく苦戦します。|
|---|---|

<div id="webpage"></div>

|IRC|
|---|
|http://webchat.freenode.net|
|![IRC](https://dl.dropboxusercontent.com/s/wnfps2d61f88rqu/irc.png "IRC")|


<div id="space_s"></div>


<div id="column"></div>

Blender開発者専用のチャンネルは#blendercodersですので、Channelsに#blendercodersを入力し、Nicknameに自分のニックネームを入力しましょう。  
・・・ちなみにチャットに入るときには、必ず自分のニックネームを入力しましょう。筆者がpush権をもらった当初、IRCの使い方がわからず、チャットで話したい人の名前を入力するのかと思っていたので、Ideasman（当時のリポジトリ管理者であり、Blenderの開発者としてはかなり有名な人）というニックネームで入ってしまい、色々と騒ぎになってしまいました。（筆者の無知さが面白かったから気にしないでなど、チャットに参加していた方々からの厳しいコメントは特にありませんでしたが、さすがに焦りました。）

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|push権を与えてもらったら、Blenderのアドオンのリポジトリを取得します。<br>リポジトリは、次の手順で取得します。4つ目以降のコマンドでリポジトリの最新化を行っているところがポイントです。リポジトリが古い状態のままpushしてしまうと、rejectされてしまいます。なお、Gitの使い方に関しては、BlenderのWikiページも参考になります。|
|---|---|

<div id="webpage"></div>

|Blender Wiki (Git Usage)|
|---|
|http://wiki.blender.org/index.php/Dev:Doc/Tools/Git|
|![Blender Wiki (Git Usage)](https://dl.dropboxusercontent.com/s/9wbrn6frzxdvzvy/git_usage.png "Blender Wiki (Git Usage)")|

```sh
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons-contrib.git
$ cd blender-addons-contrib
$ git submodule update --init --recursive
$ git submodule foreach --recursive git checkout master
$ git submodule foreach --recursive git pull --rebase origin master
$ git pull --rebase
$ git submodule foreach --recursive git pull --rebase origin master
```

<div id="process_sep"></div>

---


<div id="process_noimg"></div>

|<div id="box">3</div>|ローカルリポジトリへcommitする前に以下のコマンドを実行し、commit時に付加されるcommitした人の名前や連絡先を設定します。この設定は、設定を変えたりOSを変えたりしない限り、再度行う必要はありません。|
|---|---|

```sh
$ git config --global user.name "[名前（ニックネーム可、できればD.B.Oのアカウント名と合わせる）]"
$ git config --global user.email "[連絡先メールアドレス（できればD.B.Oで利用しているメールアドレスに合わせる）]"
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|次のコマンドを実行し、push先のリモートリポジトリを設定します。|
|---|---|


```sh
$ git remote set-url origin git@git.blender.org:blender-addons-contrib.git
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">5</div>|ssh鍵をD.B.Oに登録します。|
|---|---|

ssh鍵は、次のコマンドにより作成することができます。

```sh
$ ssh-keygen
```

上記のコマンドを実行すると、作成したssh鍵の公開鍵が ```~/.ssh/id_rsa.pub``` に配置されるため、これをD.B.Oに登録します。

D.B.Oの右上の *（自分で設定したアイコン）* をクリックして表示されるメニューから *Settings* をクリックします。そして、表示されるページの左のメニューから *SSH Public Keys* をクリックします。次に、*SSH Key Actions* をクリックして表示される *Upload Public Key* をクリックし、公開鍵 ```id_rsa.pub``` のファイルの中身をコピーしたものを、*Public Key* にペーストします。*Name* に適当な名前をつけて *Add Key* ボタンをクリックすることで、ssh鍵の登録が完了します。

これで、リモートリポジトリに対して修正をpushすることができるようになりました。以降、リモートリポジトリに対してpushする時は、自分がpushした内容がBlenderのリポジトリにダイレクトに反映できるようになっていることを意識し、修正内容をきちんと確認したうえで行ってください。リポジトリへの修正が可能になったことで、すべてのアドオンを削除することもできてしまいます。もちろん、これは悪意の持ったユーザがいることを考えるとあまりに危険な状態ですので、元に戻す方法はきちんと用意されています。ただ、Blender開発者は忙しいため、このようなミスが開発者に対して非常に迷惑をかける、ということは覚えておいてください。

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">6</div>|登録するアドオンのソースコードをリポジトリ内に配置します。ここでは、```blender-addons-contrib``` 直下にアドオンのソースコードを置いた場合のコマンドの実行例を示します。|
|---|---|


```sh
$ cd blender-addons-contrib
$ cp [作成したアドオンのソースコード] .
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">7</div>|次のコマンドを実行し、ローカルリポジトリへcommitします。|
|---|---|

```sh
$ git add [作成したアドオンのソースコード]
$ git commit
```

なお、```git commit``` を実行するとエディタが開きますので、コミットメッセージを入力します。

コミットメッセージには、commitした内容がわかるように英語で記載します。コミットメッセージの書き方については、次のWikiページが参考になると思います。ただ、```git log``` コマンドで過去のコミットメッセージを見てもらえればわかると思いますが、Wikiページに書かれていることがすべてのcommitについて守られているかというと、必ずしもそうではありません。基本的に、```git log``` コマンドで他の人のコミットメッセージを参考にして書けばよいですが、修正内容がすぐに理解できるようなコミットメッセージを書くように心がけてください。


<div id="webpage"></div>

|Blender Wiki (Commit Logs)|
|---|
|http://wiki.blender.org/index.php/Dev:Doc/New_Committer_Info#Commit_Logs|
|![Blender Wiki (Commit Logs)](https://dl.dropboxusercontent.com/s/oycvo2exxzjrgjx/commit_logs.png "Blender Wiki (Commit Logs)")|


<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">8</div>|リポジトリへのアドオンの登録も最後の段階まできました。<br>いよいよ、リモートリポジトリへ修正内容をpushします。次のコマンドを実行し、リモートリポジトリへ修正内容をpushしてください。リポジトリを最初に取得したときからリモートリポジトリに対して変更があった場合を想定し、push前に ```git pull --rebase``` でローカルリポジトリを最新化しているところがポイントです。|
|---|---|


```sh
$ git pull --rebase
$ git push
```

おめでとうございます！これで作成したアドオンがBlender本体へ取り込まれました。ここで説明した手順は、サポートレベルContribを対象としていますので、作成したアドオンはテストビルドされたBlender本体に含まれることになります。

リポジトリへの取り込み作業はこれで終わりですが、最後の作業として作成したアドオンの宣伝やバグ修正報告のためのサポートページを作成しましょう。


### 7. アドオンのサポートページを開設する

Blender本体にアドオンが取り込まれると、Blenderをダウンロードしたユーザがアドオンをインストールせずに使えるようになるため、ユーザが多くなります。ユーザが多くなるとアドオンのバグ修正依頼や新機能追加の要望などが増えると予想されるため、ユーザが開発者に対してコンタクトの取れる場が必要になります。このため、[4-3節](03_Publish_your_Add-on.md)を参考にして、アドオンのサポートページを作りましょう。


## サポートレベルContribからReleaseへ

アドオンの機能レビューの結果、サポートレベルContribとしてアドオンを登録することになった場合、ある一定の手続きを行うことでReleaseレベルへサポートレベルを上げることができます。

ContribからReleaseへサポートレベルを上げるためには、例えば次のような方法があります。ちなみに、筆者が開発しているアドオン『Magic UV』は、Blender Artists CommunityにてBlender 2.79に登録すべきアドオンをユーザから意見を集めているスレッドで、ユーザから推薦いただいたことがきっかけとなり、Blenderのアドオン開発代表者であるMeta-Androcto氏からReleaseレベルに招待していただきました。

* Blenderのアドオン開発関連のメーリングリストbf-python（bf-python@blender.org）へ、Releaseサポートレベルへの登録レビュー申請メールを出し、Releaseサポートレベルへの登録承認を得る
* Blenderが新バージョンをリリースするときに、Blenderのアドオン開発代表者（Meta-Androcto氏など）から招待を受ける
* アドオンのユーザからReleaseレベルへの推薦を受ける

このように、アドオンのサポートレベルをReleaseに上げるためには、ユーザからアドオンに対して一定の支持を受ける必要があります。ユーザからアドオンに対して支持を受けるための確実な方法はありませんが、Releaseサポートレベルとして登録されたアドオンを見てみると、以下のようなアドオンがReleaseサポートレベルとして登録されているように思えます。

* アドオンの機能が優れていて、かつ完成している
  * ここで優れているとは、既存の機能の組み合わせによる改良（単なる作業効率化のためのアドオン）ではなく、Blenderに新たな機能を提供してくれるアドオンのことを指します
* ユーザが多く、かつアドオンの機能が有用であるなどの高評価を多数もらっている
  * Releaseサポートレベルへの承認を担当しているアドオン開発代表者は海外の方ですので、海外ユーザが多いほうが開発代表者の目にとまりやすいという意味で、海外ユーザが多い方がよいです
* 積極的にユーザからの意見（機能追加リクエスト、バグ報告）を聞き、アドオンの改良を続けている
  * Releaseレベルのアドオンは、Contribレベルに比べて多くのユーザに使ってもらうことになるため、開発が継続して行われ、将来にわたってきちんと動作することが約束できるアドオンが望まれているようです


### サポートレベルReleaseのリポジトリへの登録手順

サポートレベルReleaseのリポジトリへの登録は、サポートレベルContribの場合とほぼ同じ手順で行うことができます。


<div id="custom_ol"></div>

1. アドオンの機能が存在しないこと確認する
2. アドオンのコーディング規約を守る
3. アドオンの機能レビューを受ける
4. アドオンのWikiページを作成する
5. アドオンのソースコードレビューを受ける
6. Blenderのリポジトリへアドオンを登録する
7. アドオンのサポートページを開設する
8. Release Noteを書く


上記のうち、1〜4,7についてはサポートレベルContribへの登録手順と同じであるため、割愛します。ここでは、サポートレベルReleaseへの登録手順で異なる部分について説明します。


### 5. アドオンのソースコードレビューを受ける

Contribサポートレベルと同じように、D.B.Oでアドオンのソースコードのレビューを受ける必要があります。Releaseレベルのリポジトリが ```git://git.blender.org/blender-addons.git``` であり、リポジトリの取得元が異なること以外は、Contribと手順はほとんど同じです。


<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|次のコマンドを実行し、最新のリポジトリ（サポートレベルがReleaseであるリポジトリ）を取得します。取得するリポジトリが、サポートレベルContribの場合と異なることに注意が必要です。|
|---|---|

```sh
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons.git
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|次のコマンドを実行し、作成したアドオンを、取得したリポジトリのディレクトリへコピーします。|
|---|---|

```sh
$ cd blender-addons
$ cp [作成したアドオン] .
```

<div id="process_sep"></div>

---


<div id="process_noimg"></div>

|<div id="box">3</div>|Contribサポートレベルで示した手順を参考に、ソースコードの差分をD.B.Oに登録します。なお、Create Diffページの入力欄 *Repository* には、Releaseサポートレベルのアドオンに関する投稿であることを示す、```rBA Blender Add-ons``` を指定する必要があります。|
|---|---|


<div id="process_start_end"></div>

---

### 6. Blenderリポジトリへ登録する

リポジトリへのソースコード登録についても、サポートレベルReleaseとサポートレベルContribとの間で大きな違いはありません。唯一、リポジトリのURIが異なることに注意してください。

```sh
# サポートレベルReleaseのアドオンリポジトリを取得
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons.git
$ cd blender-addons
$ git submodule update --init --recursive
$ git submodule foreach --recursive git checkout master
$ git submodule foreach --recursive git pull --rebase origin master
$ git pull --rebase
$ git submodule foreach --recursive git pull --rebase origin master

# コミット情報（名前と連絡先）の設定
$ git config --global user.name "[名前（ニックネーム可、できればD.B.Oのアカウント名と合わせる）]"
$ git config --global user.email "[連絡先メールアドレス（できればD.B.Oで利用しているメールアドレスに合わせる）]"

# サポートレベルReleaseのアドオンリポジトリを取得
$ git remote set-url origin git@git.blender.org:blender-addons.git

# 作成したアドオンのソースコードをローカルリポジトリへ配置
$ cd blender-addons-contrib
$ cp [作成したアドオンのソースコード] .

# アドオンのソースコードをローカルリポジトリへコミット
$ git add [作成したアドオンのソースコード]
$ git commit

# ローカルリポジトリを最新化し、修正内容をリモートリポジトリへpush
$ git pull --rebase
$ git push
```


### 8. Release Noteを書く

最後に、Release Noteを書きます。Release Noteとは、ソフトウェアを公開または更新した時に公表する、ソフトウェアの特徴点や利用にあたって注意することをまとめた文章のことを指します。Blenderでも新しいバージョンがリリースされるたびにRelease Noteが公開され、開発者はBlenderがリリースされる前にRelease Noteを書く必要があります。


<div id="webpage"></div>

|Blender Wiki (Release Notes 2.75a)|
|---|
|https://wiki.blender.org/index.php/Dev:Ref/Release_Notes/2.75|
|![Blender Wiki (Release Notes 2.75a)](https://dl.dropboxusercontent.com/s/v2wt20vv88wltjc/release_notes_2_75a.png "Blender Wiki (Release Notes 2.75a)")|


Blender本体の機能はもちろんのこと、Blender本体と一緒に提供されるサポートレベルReleaseのアドオンについても、アドオンに機能を追加した場合や機能を更新した場合には、Release Noteを書く必要があります。実際にBlenderのRelease Noteを確認するとわかると思いますが、アドオンのRelease Noteを書くためのページが用意されています。

サポートレベルContribのアドオンはあくまでコミニティが提供するアドオンとして位置付けられており、Release Noteを書く必要は必ずしもありません。むしろ、サポートレベルContribのアドオンは、テストビルドとしてのみユーザへ提供されるため、ユーザを混乱させないためにも書かない方がよいかもしれません。もしどうしてもRelease Noteを書きたいのであれば、テストビルドとして提供されることを書き、正式にリリースされたBlenderと一緒に提供されないことを明示すべきです。なお、Externalレベルのアドオンは、公式のいずれのリポジトリにも含まれていないことから、Release Noteを書いてはいけません。

Release Noteの書き方について特に明確なルールは設けられていませんが、基本的には過去に書かれたRelease Noteを参考にして書けばよいです。Release Noteに書くべき内容としては、次のようなものがあります。

* アドオン名
* アドオンの作者
* アドオンの更新内容、新規機能の概要
* アドオンカタログ、サポートページ、D.B.Oのタスクページなど、アドオンの情報が得られるWebサイトへのリンク
* チュートリアル（動画やWikiページへのリンクでもよい）


なお、Blender 2.79に『Magic UV』が登録されたときに筆者が書いたRelease Noteへのリンクを載せておきます。

<div id="webpage"></div>

|Blender Wiki（Release Note 2.79 Add-ons）|
|---|
|https://wiki.blender.org/index.php/Dev:Ref/Release_Notes/2.79/Add-ons|
|![Blender Wiki（Release Note 2.79 Add-ons）](https://dl.dropboxusercontent.com/s/4r3o0ra7bk6awoy/release_notes_2_79.png "Release Note 2.79 Add-ons")|


### サポートレベルReleaseへの登録にあたり注意したいこと

サポートレベルReleaseのアドオンはBlender本体と一緒に提供されるため、サポートレベルContribのアドオンに比べてユーザが多くなるメリットがあります。しかし、サポートレベルReleaseはレビューがより一層厳しくなるため、他のサポートレベルと比べて機能追加を容易に行うことができないというデメリットもあります。また、サポートレベルReleaseであるアドオンは、何の告知もなくBlender開発者の手が入ることが多いことから、ときどき公式のリポジトリを確認して修正された内容を確認する必要があります。このようにサポートレベルによってメリット・デメリットがありますので、よく考えてからレビュー依頼するようにしましょう。


## より詳細な情報源

本節で取り上げた手順に従うことでアドオンを本体へ取り込むことができますが、より詳細な情報を得たい場合は、次に示すBlenderの公式Wikiページが参考になります。ただしWikiページに書かれている内容にすべて従う必要があるかというと、必ずしもそうではありません。リポジトリ登録時には必ず1人以上のサポーターが登録するアドオンごとに割り当てられますので、サポーターの指示に従って作業を進めれば問題ありません。筆者は、ContribレベルとReleaseレベルへの登録をそれぞれ1回ずつ経験しているため、もし不安な点がありましたら、問い合わせいただければ可能な範囲で対応できると思います。

<div id="webpage"></div>

|Blender Wiki（Process Addons）|
|---|
|https://wiki.blender.org/index.php/Dev:Doc/Process/Addons|
|![Blender Wiki（Process Addons）](https://dl.dropboxusercontent.com/s/c95eh6ycsjrqevq/addons.png "Blender Wiki（Process Addons）")|


## まとめ

本節では、アドオンをBlender本体に取り込んでもらうまでの手順を説明しました。

Blender本体へアドオンを取り込んでもらうための道のりは非常に長く大変ですが、Blender本体へ登録される（＝自分の作成したアドオンが評価される）ことによる達成感は非常に大きいです。またBlender本体へ公開する過程で、機能レビュー・ソースコードレビューなどのソフトウェア開発工程（の一部分）も体験できるため、今後ソフトウェアを開発する方にとってスキルアップできるよい機会にもなります。

そして、これはBlender本体へ登録されたときに限らず、アドオンを公開したときにも言えることですが、アドオンを使ってくれた人（特に海外の人！）から感想をもらえると、作り手としては大変うれしいものです。たとえ勉強の過程で作ったアドオンであっても、アドオンのソースコードは少なからず他のアドオン開発者にとって有益な情報になります。このため、作成したアドオンに含まれる技術を公開したくないなどの特別な理由がなければ、作成したソースコードを公開することをぜひ検討しましょう！！

これまで本書を通してアドオン開発の解説を行ってきましたが、筆者がアドオン開発のために知っておいて欲しいと思ったことはこれですべてとなります。長くなりましたが、お疲れ様でした！


<div id="point"></div>

### ポイント

<div id="point_item"></div>

* 作成したアドオンをBlender本体に取り込んでもらうためには、ソースコードレビューやWikiページ作成など数多くの手順を踏む必要がある
* Blender本体へアドオンを取り込んでもらうためには、アドオンが新規性のある機能を持っていることが最低限必要である
* Blender本体へアドオンを取り込むか否かにかかわらず、効率的でメンテナンスしやすいようなソースコードとなるように意識してコーディングすべきである
* Blender本体へアドオンを取り込むまでの手順を踏むことで、通常のソフトウェア開発工程の一部分を経験できる
* Blender本体に取り込まれると、新規機能を追加しにくくなるなどのデメリットもあるため、メリットとデメリットを理解して取り込むか否かを検討しよう
* 公開したアドオンに関してユーザからフィードバックをもらえることは、作り手として非常に嬉しいことである。特別な理由がなければ、作成したアドオンを公開することを検討しよう

<div id="space_page"></div>
