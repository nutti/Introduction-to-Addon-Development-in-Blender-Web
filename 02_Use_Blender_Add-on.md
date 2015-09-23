# 2. Blenderのアドオンを使ってみよう

Blenderのアドオンの開発に入る前に、他の人が作成したアドオンを使ってみましょう。
解説はBlenderの言語が日本語になっていることを前提としていますので、Blenderの言語を日本語にしていない方は、[3章](03_Prepare_Add-on_development_environment)を参考に日本語化してください。

## アドオンの種類

Blenderのアドオンには、**サポートレベル** により以下の3種類に分類されます。

|サポートレベル|説明|
|---|---|
|Release|Blenderが公式にサポートしているアドオンで、Blender本体と共に提供されます。アドオンは厳密にレビュー（審査）され、不具合が比較的少ない安定したアドオンです。|
|Contrib|Blender本体と共に提供されます。サポートは各個人が行うためofficialに比べて品質は落ちます。しかしContribとして登録されるためには、コミュニティのレビューにて一定の評価を得る必要があるため、一定の品質が保たれテイルと共に、新規性のある機能が集まっています。|
|External|Blender本体には含まれないアドオンで、ユーザ自らアドオンをインストールする必要があります。レビューされていないため、利用は自己責任となります。作業効率化等のBlenderの機能をサポートするものが多く含まれるようですが、中にはContrib以上の機能性を持つアドオンも存在します。|

## アドオンのインストール

**Release** と **Contrib** は、Blender本体と共に提供されるため、インストール作業は不要です。
ここでは、 **External** のアドオンのインストール方法について説明します。
筆者がアドオン開発でいつもお世話になっている **mifth** さんのアドオン **Mira Tools** をインストールしてみます。
**Mira Tools** の機能は、 https://github.com/mifth/mifthtools/wiki/Mira-Tools から確認することができます。
すべて英語であるため、やや敷居が高くなってしまっていますが、 **External** のアドオンの中でも非常に高機能なアドオンですので、ぜひ1度使ってみてください。
**Mira Tools** のインストール方法は前述のURLにも記載されていますが、改めてここでもインストール方法を紹介します。

1. アドオンのダウンロード
  * https://github.com/mifth/mifthtools/archive/master.zip からmifthさんが作成したアドオン一式をダウンロードします。
2. ダウンロードした **mifthtools-master.zip** を解凍します
3. **Mira Tools** は、解凍してできたディレクトリの中から ```mifthtools-master/blender/addons/mira_tools``` にあります。このフォルダ一式を、Blenderが用意しているフォルダ内にコピーします。フォルダのコピー先はOSによって異なります。コピーが完了したら、インストールが完了です。

OSごとのアドオンのインストール先を以下に示します。
インストール先のフォルダが無い場合は、新たに作成してください。

|OS|インストール先|
|---|---|
|Windows||
|Mac|```/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons```|
|Linux||


## アドオンの有効化

アドオンを有効化して、使えるようにしましょう。
紹介する手順は、 **Release**・**Contrib**・**External** いずれのアドオンについても共通の方法で有効化できます。
ここでは、先ほどダウンロードした **Mira Tools** を有効化します。

最初にBlenderを開きます。
Blenderを開いたら、**情報** ウィンドウの **ファイル** > **ユーザ設定** を選択してください。

![アドオンの有効化 手順1](https://dl.dropboxusercontent.com/s/9it3p8rth2heyqi/enable_add-on_1.png "アドオン有効化 手順1")

ユーザ設定画面が表示されるので、**アドオン** タブを選択しましょう。
検索窓に *mira tools* と入力しましょう。
すると右側にインストールした **Mira Tools** が表示されるので、チェックボックスにチェックを入れます。

![アドオンの有効化 手順2](https://dl.dropboxusercontent.com/s/k4xq9zyhk0hbivp/enable_add-on_2.png "アドオン有効化 手順2")

これでアドオン **Mira Tools** が有効化されました。
実際にアドオンが有効化されているかは、 **3Dビュー** の左側の **ツールシェルフ** のタブに **Mira** が追加されていることで確認できます。

![アドオンの有効化 手順3](https://dl.dropboxusercontent.com/s/qqvxodqbs67yy45/enable_add-on_3.png "アドオン有効化 手順3")

## アドオンの無効化
