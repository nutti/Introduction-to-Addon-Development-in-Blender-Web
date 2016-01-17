# 4.4. アドオンをBlender本体に取り込んでもらうまでの流れ

そのような方のために本書最後の節では、作成したアドオンを公開する方法について紹介します。

## Blender本体に取り込まれる条件

[1.2節](../chapter_01/02_Use_Blender_Add-on.md) ではアドオンのサポートレベルについて紹介しましたが、Blender本体に取り込んでもらうためには *Release* または *Contrib* のサポートレベルになる必要があります。
なお *Contrib* のサポートレベルではビルド時のBlenderのみしかインストールされないため、公式にリリースされたBlenderへ取り込んでもらうためには、 *Release* のサポートレベルになる必要がります。

ここでは、作成したアドオンを *Release* または *Contrib* のサポートレベルにするまでの過程を紹介したいと思います。

## Blender本体に取り込んでもらうまでの流れ

### アドオンの機能が既に存在するか確認する

作成したアドオンの機能について、Blender本体や *Release* または *Contrib* のサポートレベルであるアドオンの中に同じまたは非常によく似ている機能がないか確認しましょう。
*Release* または *Contrib* のサポートレベルであるアドオンは以下から参照できます。

* Blender Wiki (Blender Add-ons Catalog) - http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts

もし作成したアドオンの機能が存在しない場合は、Blender本体に登録される可能性が高くなります。
しかし既に同様の機能があるアドオンが存在した場合でも、諦めるのはまだ早いです。
公開されているアドオンに性能面や機能面で問題点や改善点がないか確認してみましょう。
公開されているアドオンを改善すれば、作成したアドオンをBlender本体へ登録してもらえる可能性があります。
もちろん公開されているアドオンについて何も進展がないようなアドオンでは、Blender本体への登録は厳しいと思います。

### Blenderアドオンのコーディング規約を守る

Blender本体として公開するということは、言い換えれば **Blenderのソフトウェアの1つとして公開される** ことと同じになるため、アドオンのソース自体の品質的にも一定以上のものが求められます。
このため、Blender本体にアドオンを取り込んでもらうためには、ソースコード作成時に品質を意識して作成する必要があります。

品質をあげるといっても何をすれば良く分からないと思いますが、コーディング規約を守るように心がければ良いと思います。
もしコーディング規約が守られていなかった場合でも、後のソースコードレビューで指摘されて直す必要が出てくると思いますが、アドオン作成時にも意識しておくことが重要です。

Blenderアドオンのコーディング規約は、Pythonのコーディング規約であるpep8に準拠しています。
以下のサイトからpep8に沿っているか確認しながら、アドオンを作成しましょう。
なお、1行の最大文字数が79文字を超えてはならないpep8-80というのもありますが、ここまでは求められていないようです。

* PEP 0008 -- Style Guide for Python Code - https://www.python.org/dev/peps/pep-0008/


コーティング規約だけでなく、Blender本体に取り込まれるアドオンは処理も効率的でなくてはなりません。
アドオンを使う人にとっては、少しでも速く処理が終わったほうが良いのは考えてみれば当然です。
Blenderはアドオン開発について、処理を効率的に処理するために必要なベストプラクティスと呼ばれる記事を用意しています。
ベストプラクティスを参照し、効率的なコーディングを心がけましょう。

* Best Practice (API documentation - Blender 2.75a) - https://www.blender.org/api/blender_python_api_2_75a_release/info_best_practice.html

効率的なコーディングの実例を1つ紹介します。

リストに格納された値を2倍にしたリストを作成する、以下のソースコードを見てください。

```py: best_practice_before.py
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_l = []
for i in l:
    double_l.append(i * 2)
double_l

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
これをPythonの機能であるリスト内包表記で書くと、以下のようになります。

```py: best_practice_after.py
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_l = [i * 2 for i in l]
double_l

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

最終結果はどちらも同じですが、リスト内包表記を用いた場合の方が実行速度が速いです。
最初の例では **append属性を取り出して関数を呼び出す** という関数の呼び出し処理を ```append()``` 関数を呼び出すたびに行っているのに対して、リスト内包表記を用いた例では **リストに要素を追加する** という処理（関数を呼び出さず直接リストに要素を追加する処理）になるからです。

### アドオンの機能レビューを受ける

アドオンが完成して、コーディング規約に対応できたらいよいよ次はアドオンのレビューを受けます。
いきなりアドオンのソースレビューを行うのではなく、作成したアドオンが実用的なものかを判断する機能レビューを最初に行います。
レビューの申請は、developer.blender.org（通称D.B.O）から行います。

* developer.blender.org - https://developer.blender.org

＠＠＠図を追加＠＠＠

D.B.Oは会員制のため、ユーザ登録が必要です。
会員登録したら、右上の＋からManiphest Taskをクリックして新しいタスクを作成します。

＠＠＠図を追加＠＠＠

新しいタスクを作成する時に以下の項目を入力します。

|入力欄|入力するもの|
|---|---|
|Title|作成したプラグインの機能がはっきりと分かるようなタイトルをつけます|
|Assigned To|タスクを誰に割り当てるかを指定します。B.P.O内に知り合いがいる場合は、追加してみるのもよいでしょう。レビューに参加して参加してもらえるかもしれません。追加しなくてもタスクを見た人がレビューしてくれますので、知り合いがいない場合は何も追加しなくても良いです。ちなみに筆者自身もB.P.Oに登録しているので、タスクを割り当てていただければレビューできるかもしれません。（ユーザ名：Nutti）|
|CC|自分自身を含む開発関係者を追加しておけばよいでしょう|
|Priority|タスクの緊急度を設定します。新規機能はNormalを指定すると良いでしょう。既存の機能のバグ修正であれば、高め優先度を指定しても良いかもしれません|
|Projects|プロジェクト名を指定します。アドオンに関するタスクであるため、Addonsを指定します|
|Type|新規機能のアドオンであればPatchを選択し、バグ報告やバグ修正であればBugを指定します|
|Description|作成したアドオンの詳細を記載します。フォーマットは特に決まっていませんが、筆者がよく利用する下記のテンプレートが参考になるかもしれません(★はコメントです)|

```
Project: Blender Extensions
Tracker: Python Scripts Upload
Blender: X.XX - Y.YY     ★アドオンの動作を保証するBlenderバージョン(bl_infoのblenderと一致させる)
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
筆者の経験から、登録までの一連の手順の中でこの機能レビューが最も厳しいと感じます。
レビュー中に発生した機能の改善提案への対応も厳しいですが、作成したアドオンに対して賛同を得る人を増やすのが何よりも難しいです。
しかしここは辛抱強く待つしかありません。
もし人が集まらないようであれば、 [4.3節](03_Publish_your_Add-on.md) で紹介したような方法でアドオンを宣伝してもよいかもしれません。
特に、Blender Artistsに投稿するのが効果的です。

レビュワーによる機能の改善提案への対応は積極的に行いましょう。
レビュワーの意見を聞くことで、このアドオンはサポートもしっかりしてるし今後も期待できそうだと思うようになり、作成したアドオンに対する支持者が増えていきます。
そしてレビュワーからBlender本体に登録したらどうですか、というコメントがもらえたら・・・おめでとうございます！
Blender本体へのアドオン登録はもうすぐそこです！


### Blender Wikiページの作成

機能レビューが通ったら、Blender公式のWikiページに作成したアドオンのページを作成しましょう。

* Blender Wiki (Blender Add-ons Catalog) - http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts

Wikiページに掲載する内容は、他のアドオンのWikiページを見ながら作成していくとよいでしょう。
なおWikiページのアカウントはD.B.Oのアカウントとは異なりますので、ユーザ登録していない場合は追加してください。

機能レビューが通る前でも、Blender Wikiページを作成することができます。
D.B.Oで作成したタスクの説明文においてBlender Wikiのページを参照したい場合は、レビュー依頼を出す前にWikiページを作成しても良いでしょう。

### アドオンのソースコードレビューを受ける

機能レビューが終わり、アドオンのWikiページを作成したら、アドオンのソースコードをレビューしてもらいましょう。
機能レビューと同様、アドオンのソースコードレビューはdeveloper.blender.orgにて行います。
ソースコードレビューを受けるまでの流れを以下に示します。
なお、BlenderのWikiページにもソースコードレビューの手順が書いてありますので、こちらも参考にしてみてください。

* Blender Wiki (Code Review) - http://wiki.blender.org/index.php/Dev:Doc/Tools/Code_Review

#### 最新のBlenderリポジトリを取得

Blenderのリポジトリを取得します。
Blenderのサポートレベルに応じてリポジトリが異なります。
機能レビュー時に、サポートレベルがReleaseかContribのどちらかに決まりますので、サポートレベルに対応したリポジトリを取得してください。
以降では、サポートレベルがContribの場合について解説します。

|サポートレベル|リポジトリ|
|---|---|
|Release|```git://git.blender.org/blender-addons.git```|
|Contrib|```git://git.blender.org/blender-addons-contrib.git```|

① 以下のコマンドを実行し、最新のBlenderのリポジトリを取得します。

```sh:source_review_1.sh
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons-contrib.git
```

② 以下のコマンドを実行し、リポジトリ取得後に作成したアドオンをリポジトリへ移動します。

```sh:source_review_2.sh
$ cd blender-addons-contrib
$ cp [作成したプラグイン] .
```

③ 以下のコマンドを実行し、ソースコードの差分を取得した結果をコピーします。

```sh:source_review_3.sh
$ git diff
```

④ レビューを依頼する

developer.blender.orgの左側にある *Differential* をクリックした後に表示される、 *Create Diff* をクリックします。

＠＠＠図を追加＠＠＠

先ほどコピーしたソースコードの差分を *Raw Diff* にペーストし、 *Repository* に *rBAC Blender Add-ons Contrib* を入力した後、一番下のCreate Diffのボタンをクリックします。

＠＠＠図を追加＠＠＠

ソースコードレビューでは、作成したソースコードに対して指摘されることがあります。
指摘された部分は少なくともソースコードを読んだ人が気になった部分でもあるので、たとえ反映不要な指摘であっても反映するようにしましょう。

### Blenderリポジトリへの登録

ソースコードレビューが完了したら、以下の手順に従ってBlenderのリポジトリに登録しましょう。

① リポジトリに対するcommit権を取得する

Blenderのリポジトリへ登録（commit）するためは、リポジトリ管理者からリポジトリへのcommit権をもらう必要があります。
執筆時点で、リポジトリの管理はIdeasmanさんという方が行っているようです。
IRC(チャットのようなもの)に入り、Ideasmanさんにリポジトリのcommit権を与えてもらえるようにお願いしましょう。

* IRC - http://webchat.freenode.net

＠＠＠図を追加＠＠＠

Blender開発者のチャンネルは *#blendercoders* ですので、 *Channels* に *#blendercoders* を入力し、 *Nickname* に自分のニックネームを入力しましょう。
・・・ちなみにチャットに入るときには、必ず自分のニックネームを入力しましょう。
筆者はコミット権をもらった当初IRCの使い方がわからず、話したい人の名前を入力するのかと思っていたので、Ideasmanという名前で入ってしまい色々と騒ぎになってしまいました。（私の無知さが面白かったから気にしないでなど、厳しいコメントはありませんでしたがさすがに焦りました。）

IRCでは英語でのチャットになりますが、わからない単語をWebで調べつつ、こちらが言いたいことをはっきり伝えていけば良いのでなんとかなるでしょう。


② リポジトリを取得する。

commit権をもらったら、Blenderのリポジトリを取得しましょう。
リポジトリの取得については、以下の手順で行います。
BlenderのWikiページも参考になるでしょう。

* Blender Wiki (Git Usage) - http://wiki.blender.org/index.php/Dev:Doc/Tools/Git

＠＠＠図を追加＠＠＠

```sh:source_commit_1.sh
$ cd [作業用ディレクトリ]
$ git clone git://git.blender.org/blender-addons-contrib.git
$ cd blender-addons-contrib
$ git submodule update --init --recursive
$ git submodule foreach --recursive git checkout master
$ git submodule foreach --recursive git pull --rebase origin master
$ git pull --rebase
$ git submodule foreach --recursive git pull --rebase origin master
```

③ 著者・連絡先を設定する。

リポジトリへcommitする前に以下のコマンドを実行し、commitを行った人物や連絡先を設定します。
この設定を一度行っておけば、設定を変えたりOSを変えたりしない限り、2度目以降は実施する必要がありません。

```sh:source_commit_2.sh
git config --global user.name "[名前（ニックネーム可）]"
git config --global user.email "[連絡先メールアドレス]"
```

④ commit先を設定する。

以下のコマンドを実行し、commit先の設定を行います。

```sh:source_commit_3.sh
$ git remote set-url origin git@git.blender.org:blender-addons-contrib.git
```

⑤ ssh鍵を登録する。

以下のコマンドを実行し、ssh鍵を作成します。

```sh:source_commit_4.sh
$ ssh-keygen
```

作成したssh鍵の公開鍵は~/.ssh/id_rsa.pubに置かれているので、これをD.B.Oに登録します。
D.B.Oの右上の工具マークをクリックし、左メニューの *SSH Public Keys* をクリックします。
そして、 *Upload Public Key* をクリックし、*Public Key* に ```id_rsa.pub``` の内容をコピー＆ペーストして、*Name* に適当な名前をつけて *Add Key* をクリックすることで、ssh鍵の登録が完了します。

⑥ 登録するアドオンのソースコードをリポジトリ内に配置する。

登録するアドオンのソースコードをリポジトリ内に置きましょう。
以下では、 ```blender-addons-contrib``` 直下にアドオンのソースコードを置いています。

```sh:source_commit_5.sh
$ cd blender-addons-contrib
$ cp [作成したアドオンのソースコード] .
```

⑦ ローカルリポジトリへcommitする。

以下の手順に従って、ローカルのリポジトリへcommitします。

```sh:source_commit_6.sh
$ git add [作成したアドオンのソースコード]
$ git commit
```

なお、 ```git commit``` を実行するとエディタが開きます。
エディタでは修正内容がわかるように英語で記載します。
以下のWikiページが参考になると思います。

* Blender Wiki (Commit Logs) - http://wiki.blender.org/index.php/Dev:Doc/New_Committer_Info#Commit_Logs

⑧ リモートリポジトリ（Blender本体のリポジトリ）へpushする

いよいよアドオンの登録も最終段階です。
アドオンをBlender本体のリポジトリへ登録しましょう。
以下の手順でアドオンをBlender本体のリポジトリで登録します。

```sh:source_commit_7.sh
$ git pull --rebase
$ git push
```

おめでとうございます！
これで作成したアドオンがBlender本体へ取り込まれました。
今回はContribのサポートレベルですので、テストビルド時にBlender本体にあなたの作成したアドオンが含まれることになります。
リポジトリへの取り込み作業はこれで終わりですが、最後に作成したプラグインの宣伝＆バグ修正などの報告のためのサポートページを作成しましょう。

### サポートページの開設


### サポートレベル Release への審査


## まとめ

### ポイント

* 作成したアドオンをBlender本体に取り込んでもらうためには、ソースコードレビューやWikiページ作成など数多くの準備が必要である
