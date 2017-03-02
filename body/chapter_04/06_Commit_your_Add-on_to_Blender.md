<div id="sect_title_img_4_6"></div>

<div id="sect_title_text"></div>

# アドオンをBlender本体に取り込んでもらう

<div id="preface"></div>

###### [4-3節](03_Publish_your_Add-on.md)ではアドオンを多くの人に使ってもらう方法として、作成したアドオンをBlender本体に取り込んでもらうことが良いの方法であることを紹介しました。作成したアドオンがBlenderに取り込まれると、アドオンのユーザが多くなる可能性がありますが、アドオンをBlender本体に取り込むまでに必要な作業は非常に多く大変です。そこで本書最後の節では、作成したアドオンをBlender本体に取り込んでもらうまでの一連の流れを解説します。

## アドオンがBlender本体に取り込まれる条件

[1-2節](../chapter_01/02_Use_Blender_Add-on.md) ではアドオンのサポートレベルについて説明しましたが、作成したアドオンをBlender本体に取り込んでもらうためにはReleaseまたはContribのサポートレベルとして認定される必要があります。また、Contribのサポートレベルではビルド時のBlenderのみしかインストールされないため、公式にリリースされたBlenderへ取り込んでもらうためには、Releaseのサポートレベルとして認定される必要があります。

ここでは、作成したアドオンをReleaseまたはContribのサポートレベルにするまでの過程を紹介したいと思います。

## Blender本体に取り込んでもらうまでの流れ

### アドオンの機能が既に存在するか確認する

作成したアドオンの機能が、Blender本体やReleaseまたはContribのサポートレベルのアドオンの中に同じまたは非常によく似ている機能がないか確認します。

ReleaseまたはContribのサポートレベルであるアドオンは、Blender公式wikiのアドオンカタログから参照できます。

<div id="webpage"></div>

|Blender Wiki (Blender Add-ons Catalog)|
|---|
|http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts|
|![Blender Wiki (Blender Add-ons Catalog)](https://dl.dropboxusercontent.com/s/eqhblsox8zibbh8/blender_add-on_catalog.png "Blender Wiki (Blender Add-ons Catalog)")|

作成したアドオンの機能がこれらの中にない場合は、Blender本体に登録されるまでの長い道のりの第1段階を通過したことになります。

もし仮に同様の機能があるアドオンが存在した場合でも、諦めるのはまだ早いです。公開されているアドオンに性能面や機能面で問題点や改善点がないか確認してみましょう。公開されているアドオンを改善すれば、作成したアドオンをBlender本体へ登録してもらえる可能性があります。もちろん公開されているアドオンについて何も進展がないようなアドオンでは、Blender本体への登録は厳しいと思います。

### Blenderアドオンのコーディング規約を守る

Blender本体として公開するということは、言い換えれば **Blenderのソフトウェアの1つとして公開される** ことと同じですので、アドオンのソースコード自体の品質も一定以上のものが求められます。このため、Blender本体にアドオンを取り込んでもらうためには、ソースコード作成時に品質を意識して作成する必要があります。

品質をあげるといっても何をすれば良いのかわからない方が多いと思いますが、特にコーディング規約を守ってコーディングすることを心がければ良いと思います。もしコーディング規約を守らなかった場合でも、後のソースコードレビューで指摘されて直す必要が出てくると思いますが、アドオン作成時にも意識しておくことが重要です。

Blenderアドオンのコーディング規約は、Pythonのコーディング規約であるpep8に準拠しています。以下のサイトからpep8に沿っているか確認しながら、アドオンを作成しましょう。なお、1行の最大文字数が79文字を超えてはならないpep8-80というのもありますが、これはあくまで推奨であってここまでは求められていないようです。

<div id="webpage"></div>

|PEP 0008 -- Style Guide for Python Code|
|---|
|https://www.python.org/dev/peps/pep-0008/
|![PEP 0008](https://dl.dropboxusercontent.com/s/d3t0sjr0mu9wnrk/pep8.png "PEP 0008")|

コーティング規約を守るだけでなく、Blender本体に取り込まれるアドオンは処理も効率的でなくてはなりません。アドオンを使う人にとっては少しでも速く処理が終わったほうが良いので、当たり前といえば当たり前です。

Blenderはアドオン開発者に対し、効率的なコーディングをするために必要なベストプラクティスと呼ばれる記事を用意しています。アドオン作成時には、ベストプラクティスおよびコーディング規約を参照しながらコーディングしましょう。

<div id="webpage"></div>

|Best Practice (API documentation - Blender 2.75a)|
|---|
|https://www.blender.org/api/blender_python_api_2_75a_release/info_best_practice.html|
|![Best Practice](https://dl.dropboxusercontent.com/s/30rrshlzu3jnajy/best_practice.png "Best Practice")|

効率的なコーディングの実例を1つ紹介します。

リストに格納された値を2倍にしたリストを作成する、以下のソースコードを見てください。

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_l = []
for i in l:
    double_l.append(i * 2)
double_l

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

これをPythonの機能であるリスト内包表記を用いて書くと、以下のようになります。

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_l = [i * 2 for i in l]
double_l

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

最終結果はどちらも同じですが、リスト内包表記を用いた場合の方が実行速度が速いことが知られています
。

<div id="column"></div>

最初の例では、append属性を取り出して関数を呼び出すという関数の呼び出し処理をappend()関数を呼び出すたびに行っているのに対して、リスト内包表記を用いた例ではリストに要素を追加するという処理（関数を呼び出さず直接リストに要素を追加する処理）になるため、高速化されます。

### アドオンの機能レビューを受ける

アドオンを作成して、コーディング規約に対応できたらいよいよ次はアドオンのレビューを受けます。

いきなりアドオンのソースコードレビューを行うのではなく、作成したアドオンが実用的なものかを判断する機能レビューを最初に行います。レビューの申請は、developer.blender.org（通称D.B.O）から申請することができます。

<div id="webpage"></div>

|developer.blender.org|
|---|
|https://developer.blender.org|
|![developer.blender.org](https://dl.dropboxusercontent.com/s/z9uvc1epwm2wi2e/dbo.png "developer.blender.org")|

D.B.Oは会員制のため、ユーザ登録が必要です。
会員登録完了後、以下の手順に従ってタスクを作成します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|右上の＋からManiphest Taskをクリックします。|![Create New Task 手順1](https://dl.dropboxusercontent.com/s/3zzr089rpl1i244/create_new_task_1.png "Create New Task 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|各入力欄に必要事項を記載し、新しいタスクを作成します。|![Create New Task 手順2](https://dl.dropboxusercontent.com/s/4m757n2ubrqz4au/create_new_task_2.png "Create New Task 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---


新しいタスクを作成する時に記載が必要な項目を以下に示します。

|入力欄|入力するもの|
|---|---|
|Title|タスクのタイトルを入力します。<br>作成したプラグインの機能がはっきりと分かるようなタイトルをつけます。|
|Assigned To|タスクの担当者を指定します。<br>B.P.O内に知り合いがいる場合はレビューに参加してもらえる可能性があるので、追加するとよいと思います。ここで無理して追加しなくてもタスクを見た人がレビューしてくれますので、知り合いがいない場合は何も追加しなくても良いです。ちなみに筆者自身もB.P.Oに登録しているので、タスクを割り当てていただければレビューできるかもしれません。（ユーザ名：Nutti）|
|CC|自分自身を含む開発関係者を追加します。|
|Priority|タスクの緊急度を設定します。<br>新規機能はNormalを指定します。既存の機能のバグ修正であれば、優先度を高めに指定しても良いかもしれません。|
|Projects|プロジェクト名を指定します。<br>アドオンに関するタスクであるため、Addonsを指定します。|
|Type|新規機能のアドオンであればPatchを選択し、バグ報告やバグ修正であればBugを指定します。|
|Description|作成したアドオンの詳細を記載します。<br>フォーマットは特に決められていませんが、筆者がよく利用する下記のテンプレートが参考になるかもしれません。(★はコメントです)|

```
Project: Blender Extensions
Tracker: Python Scripts Upload
Blender: X.XX - Y.YY     ★アドオンの動作を保証するBlenderバージョン
                          (bl_infoのblenderと一致させる)
Category: UV             ★アドオンのカテゴリ(bl_infoのcategoryと一致させる)
Python: Z.ZZ - W.WW      ★本アドオンが動作するPythonのバージョン(基本は3.3以上)
Script name: MyScript    ★アドオン名(bl_infoのnameと一致させる)
Author(s): Nutti         ★アドオン作成者(bl_infoのauthorと一致させる)
Status: Open

★アドオンの紹介文をここに書く

[Code]
https://github.com/TTTT/UUUUUU    ★アドオン本体が置かれたリンクを書く

[Usage]
1. VVVVVVV      ★アドオンの使い方を書く
2. WWWWWWW

Any problems and comments are welcome.

Thanks.
```

タスクを作成したら、後はレビュワーからの反応をひたすら待つのみです。

筆者の経験から、登録までの一連の手順の中でこの機能レビューが最も厳しいと感じます。レビュー中に発生した機能の改善提案への対応も厳しいですが、作成したアドオンを支持してくれる人を見つけるのが何よりも難しいです。しかしここは辛抱強く待つしかありません。

もし人が集まらないようであれば、[4-3節](03_Publish_your_Add-on.md) で紹介したような方法でアドオンを宣伝してもよいかもしれません。特に、Blender Artistsに投稿するのが効果的です。

レビュワーによる機能の改善提案への対応は積極的に行いましょう。レビュワーの意見を聞くことで、このアドオンはサポートもしっかりしてるし今後も期待できそうだとレビュワーが思うようになると思いますので、結果として作成したアドオンに対する支持者が増えていくことに繋がります。

そしてレビュワーからBlender本体に登録したらどうですか、というコメントがもらえたら・・・おめでとうございます！Blender本体へのアドオンの登録はもうすぐそこです！

<div id="space_l"></div>


### Blender Wikiページの作成

機能レビューに合格したら、Blender公式のWikiページにアドオンのページを作成します。

<div id="webpage"></div>

|Blender Wiki (Blender Add-ons Catalog)|
|---|
|http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts|
|![Blender Wiki (Blender Add-ons Catalog)](https://dl.dropboxusercontent.com/s/eqhblsox8zibbh8/blender_add-on_catalog.png "Blender Wiki (Blender Add-ons Catalog)")|


Wikiページに掲載する内容は、他のアドオンのWikiページを見ながら作成していくとよいと思います。

<div id="column"></div>

WikiページのアカウントはD.B.Oのアカウントとは異なりますので、ユーザ登録していない場合は登録してください。

機能レビューに合格する前でも、Blender Wikiページを作成することができます。D.B.Oで作成したタスクの説明文においてBlender Wikiのページを参照したい場合は、レビュー依頼を出す前にWikiページを作成してもよいと思います。

### アドオンのソースコードレビューを受ける

機能レビューに合格し、アドオンのWikiページを作成したら、アドオンのソースコードをレビューしてもらいます。

機能レビューと同様、アドオンのソースコードレビューはdeveloper.blender.orgで行います。

ソースコードレビューを受けるまでの流れを以下に示します。なお、BlenderのWikiページにもソースコードレビューの手順が書かれていますので、こちらも参考にしてみてください。

<div id="webpage"></div>

|Blender Wiki (Code Review)|
|---|
|http://wiki.blender.org/index.php/Dev:Doc/Tools/Code_Review|
|![Blender Wiki (Code Review)](https://dl.dropboxusercontent.com/s/ugfs7ecqh0t4fao/code_review.png "Blender Wiki (Code Review)")|


#### 最新のBlenderリポジトリを取得

Blenderのリポジトリを取得します。

取得するリポジトリは、Blenderのサポートレベルに応じて異なります。機能レビュー時に、サポートレベルがReleaseかContribのどちらかに決まりますので、サポートレベルに対応したリポジトリを取得してください。以降では、サポートレベルがContribの場合について解説します。

|サポートレベル|リポジトリ|
|---|---|
|Release|```git://git.blender.org/blender-addons.git```|
|Contrib|```git://git.blender.org/blender-addons-contrib.git```|

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|以下のコマンドを実行し、最新のBlenderのリポジトリを取得します。|
|---|---|

```sh
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons-contrib.git
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|以下のコマンドを実行し、リポジトリ取得後に作成したアドオンをリポジトリへコピーします。|
|---|---|

```sh
$ cd blender-addons-contrib
$ cp [作成したプラグイン] .
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|以下のコマンドを実行してソースコードの差分を出力し、出力結果をコピーします。|
|---|---|

```sh
$ git diff
```

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|developer.blender.orgの左側にあるDifferentialをクリックします|![Create Diff 手順1](https://dl.dropboxusercontent.com/s/2wcu3f3ho59x3ia/create_diff_1.png "Create Diff 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|Create Diffをクリックします。|![Create Diff 手順2](https://dl.dropboxusercontent.com/s/w9rhl9pwcwqjef3/create_diff_2.png "Create Diff 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|コピーしたソースコードの差分をRaw Diffにペーストし、RepositoryにrBAC Blender Add-ons Contribを入力した後、一番下のCreate Diffのボタンをクリックします。|![Create Diff 手順3](https://dl.dropboxusercontent.com/s/c37hha0316mh124/create_diff_3.png "Create Diff 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---


ソースコードレビューでは、作成したソースコードに対して指摘されることがあります。少なくとも指摘された部分についてはソースコードを読んだ人が気になった部分ですので、たとえ反映不要な指摘であっても反映するように心がけましょう。

### Blenderリポジトリへの登録

ソースコードレビューが完了したら、以下の手順に従ってBlenderのリポジトリに登録します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|Blenderのリポジトリへソースコードを登録（commit）するためは、リポジトリ管理者からリポジトリへのcommit権をもらう必要があります。<br>執筆時点で、リポジトリの管理はIdeasmanさんという方が行っているようです。commit権をもらうためには、IRC(チャットのようなもの)に入ってIdeasmanさんに話しかける必要があります。<br> IRCでは英語でのチャットになりますが、わからない単語をWebで調べつつこちらが言いたいことを片言でも良いので、伝えていけばなんとかなるでしょう。|
|---|---|

<div id="webpage"></div>

|IRC|
|---|
|http://webchat.freenode.net|
|![IRC](https://dl.dropboxusercontent.com/s/wnfps2d61f88rqu/irc.png "IRC")|

<div id="column"></div>

Blender開発者専用のチャンネルは#blendercodersですので、Channelsに#blendercodersを入力し、Nicknameに自分のニックネームを入力しましょう。   ・・・ちなみにチャットに入るときには、必ず自分のニックネームを入力しましょう。筆者はコミット権をもらった当初はIRCの使い方がわからず、話したい人の名前を入力するのかと思っていたので、Ideasmanというニックネームで入ってしまい色々と騒ぎになってしまいました。（筆者の無知さが面白かったから気にしないでなど、厳しいコメントはありませんでしたがさすがに焦りました。）

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|commit権をもらったら、Blenderのリポジトリを取得します。<br>リポジトリの取得については、以下の手順で行います。BlenderのWikiページも参考になると思います。|
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

|<div id="box">3</div>|リポジトリへcommitする前に以下のコマンドを実行し、commitを行った時に付加する、commitした人の名前や連絡先を設定します。この設定を一度行っておけば、設定を変えたりOSを変えたりしない限り、再び実施する必要はありません。|
|---|---|

```sh
git config --global user.name "[名前（ニックネーム可）]"
git config --global user.email "[連絡先メールアドレス]"
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|commit先を設定します。|
|---|---|

以下のコマンドを実行し、commit先の設定を行います。

```sh
$ git remote set-url origin git@git.blender.org:blender-addons-contrib.git
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">5</div>|ssh鍵を登録します。|
|---|---|

以下のコマンドを実行し、ssh鍵を作成します。

```sh
$ ssh-keygen
```

作成したssh鍵の公開鍵は~/.ssh/id_rsa.pubに置かれているので、これをD.B.Oに登録します。

D.B.Oの右上の工具マークをクリックし、左メニューのSSH Public Keysをクリックします。そして、Upload Public Keyをクリックし、Public Keyに ```id_rsa.pub``` の内容をコピー＆ペーストします。Nameに適当な名前をつけてAdd Keyをクリックすることで、ssh鍵の登録が完了します。

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">6</div>|登録するアドオンのソースコードをリポジトリ内に配置します。|
|---|---|

以下では、 ```blender-addons-contrib``` 直下にアドオンのソースコードを置いています。

```sh
$ cd blender-addons-contrib
$ cp [作成したアドオンのソースコード] .
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">7</div>|ローカルリポジトリへcommitします。|
|---|---|

以下のコマンドを実行し、ローカルのリポジトリへcommitします。

```sh
$ git add [作成したアドオンのソースコード]
$ git commit
```

なお ```git commit``` を実行するとエディタが開きますので、commitメッセージを入力します。

コミットメッセージはcommitした内容がわかるように英語で記載します。コミットメッセージの書き方については、以下のWikiページが参考になると思います。

<div id="webpage"></div>

|Blender Wiki (Commit Logs)|
|---|
|http://wiki.blender.org/index.php/Dev:Doc/New_Committer_Info#Commit_Logs|
|![Blender Wiki (Commit Logs)](https://dl.dropboxusercontent.com/s/oycvo2exxzjrgjx/commit_logs.png "Blender Wiki (Commit Logs)")|


<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">8</div>|いよいよアドオンの登録も最終段階です。<br>リモートリポジトリ（Blender本体のリポジトリ）へソースコードを登録(push)します。|
|---|---|

以下のコマンドを実行し、アドオンをBlender本体のリポジトリに登録します。

```sh
$ git pull --rebase
$ git push
```

おめでとうございます！これで作成したアドオンがBlender本体へ取り込まれました。今回はContribのサポートレベルですので、テストビルドされたBlender本体にあなたの作成したアドオンが含まれることになります。

リポジトリへの取り込み作業はこれで終わりですが、最後の作業として作成したアドオンの宣伝＆バグ修正報告のためのサポートページを作成しましょう。

### サポートページの開設

Blender本体にアドオンが取り込まれるとユーザも増えますので、アドオンのバグや新機能追加の要望など、ユーザが開発者に対してコンタクトの取れる場が必要になってきます。

宣伝も含めて、開発したアドオンのサポートページを作成しましょう。サポートページは、[4-3節](03_Publish_your_Add-on.md) で紹介した方法で開設すると良いと思います。

### サポートレベル Release への審査

もしアドオンのレビューの結果、サポートレベルContribとしてアドオンを登録することになった場合、ユーザへの要望を聞いてアドオンを継続的に改良することによって、サポートレベルをReleaseに上げることができるかもしれません。

ContribからReleaseへサポートレベルを上げるための審査は、Blenderのメーリングリストbf-python(bf-python@blender.org)へメールを出すことで申請できます。

サポートレベルがReleaseのアドオンはBlender本体と一緒に提供されるため、サポートレベルがContribのアドオンに比べてユーザが多くなるメリットがあります。しかしサポートレベルがReleaseになるとレビューがより一層厳しくなるため、機能追加を容易に行うことができないというデメリットもあります。このようにサポートレベルによってメリット・デメリットがありますので、よく考えてからレビュー依頼を出すようにしましょう。

## まとめ

作成したアドオンをBlender本体に取り込んでもらうまでの手順を説明しました。

Blender本体へアドオンを取り込むまでの道のりは非常に長いですが、Blender本体へ登録される（＝自分の作成したソフトウェアが評価される）ことによる達成感は非常に大きいと思います。またBlender本体へ公開する過程で、機能レビュー・ソースレビューなどのソフトウェア開発工程も体験できるため、今後ソフトウェアを開発する方にとってスキルアップできる良い経験にもなります。

そしてこれはBlender本体へ登録に限らずアドオンを公開した時に言えることですが、アドオンを使ってくれた人（特に海外の人！）から感想をもらえると、作り手としては大変うれしいものです。たとえ勉強の過程で作ったアドオンであっても、アドオンのソースコードは少なからず他のアドオン開発者にとって有益な情報になります。このため作成したアドオンに含まれる技術を公開したくないなどの特別な理由がなければ、作成したアドオンを公開することをぜひ検討してみましょう！！

これまで本書を通してアドオン開発の解説を行ってきましたが、これで最後となります。長くなりましたが、お疲れ様でした！

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* 作成したアドオンをBlender本体に取り込んでもらうためには、ソースコードレビューやWikiページ作成など数多くの工程を経る必要がある

<div id="space_xxs"></div>


<div id="point_item"></div>

* Blender本体へアドオンを取り込んでもらうためには、アドオンが新規性のある機能を持つ必要がある
* Blneder本体へアドオンを取り込むか否かにかかわらず、効率的でメンテナンスしやすいようなソースコードになるよう意識しつつコーディングすべきである
* Blender本体へアドオンを取り込むまでの手順を踏むことで、通常のソフトウェア開発の工程を経験できる
* Blender本体に取り込まれると新規機能を追加しにくくなるデメリットもあるため、メリットとデメリットを理解してからレビューに出すべきである
* 公開したアドオンに関してユーザからフィードバックをもらえることは、作り手として非常に嬉しいことである。特別の理由がなければ、作成したアドオンを公開することを検討しよう
