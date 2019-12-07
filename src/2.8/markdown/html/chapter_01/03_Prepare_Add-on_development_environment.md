---
pagetitle: 1-3. アドオンの開発環境を整える
subtitle: 1-3. アドオンの開発環境を整える
---

本節では、アドオンを効率良く開発するために環境を整えます。
各自開発しやすい環境があると思いますので、すでに環境が整っている方は参考程度に見るだけでよいと思います。


# UIの日本語化

[1-2節](02_Use_Blender_Add-on.html) でも紹介しましたが、Blenderは日本語のUIを標準でサポートしています。

英語が苦手な方はBlenderのUIを日本語化することで、英語が原因でアドオンの開発に行き詰まることを少なくできます。
英語に不安のある方は [1-2節](02_Use_Blender_Add-on.html) を参考に日本語化しておきましょう。


# Blenderのエリア設定

アドオンを開発しやすくするために、Blenderのエリア設定を行います。
ここで示しているエリア設定は筆者の好みがそのまま反映されているため、各自作業しやすい環境に設定してください。

Blenderをダウンロードした直後のBlenderの起動画面は、以下のようになっています。

![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_initial.png "Blender 初期状態")

Blenderをダウンロードした直後の初期状態でもアドオンの開発は可能ですが、以下のようにアドオンを開発しやすい環境に整えることをお勧めします。

![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_final.png "Blender アドオン開発向け環境")


## エリアの分割

Blenderはアプリケーション内で複数のエリアに分割することができます。
エリアを分割することで、他のエリアで作業したいときに毎回エリアを変更する必要がなくなります。

アドオンの開発を行いやすくするため、ここでは以下のようにエリアを分割します。


<div class="work"></div>

|||
|---|---|
|1|*[3Dビューポート]* スペースが表示されたエリア左上を下側にドラッグ&ドロップしてエリアを横に2分割します。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_divide_window_1.png "ウィンドウの分割 手順1")|
|2|下側の *[3Dビューポート]* スペースが表示されたエリア左下を右側にドラッグ&ドロップしてエリアを縦に2分割します。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_divide_window_2.png "ウィンドウの分割 手順2")|
|3|左下側の *[3Dビューポート]* スペースが表示されたエリアの左下を上側にドラッグ&ドロップしてエリアを横に2分割します。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_divide_window_3.png "ウィンドウの分割 手順3")|
|4|これでエリア分割は完了です。分割後のエリアに表示されているスペースは全て *[3Dビューポート]* になります。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_divide_window_4.png "ウィンドウの分割 手順4")|


## スペースの変更

エリアを分割した後、それぞれのエリアに表示されているスペースを変更します。スペース変更の手順を以下に示します。


<div class="work"></div>

|||
|---|---|
|1|一番上の *[3Dビューポート]* スペースが表示されたメニューの一番左のボタンから、*[情報]* をクリックします。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_change_window_1.png "ウィンドウ表示の変更 手順1")|
|2|スペースが *[3Dビューポート]* から *[情報]* に変更されます。*[情報]* スペースには、アドオンの実行結果やエラーのログ（**オペレータメッセージ**）を表示する機能があり、アドオン開発時に役に立ちます。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_change_window_2.png "ウィンドウ表示の変更 手順2")|
|3|左下の *[3Dビューポート]* スペースが表示されたメニューの一番左のボタンから、*[テキストエディター]* をクリックします。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_change_window_3.png "ウィンドウ表示の変更 手順3")|
|4|スペースが *[3Dビューポート]* から *[テキストエディター]* に変更されます。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_change_window_4.png "ウィンドウ表示の変更 手順4")|
|5|左上の *[3Dビューポート]* スペースが表示されたエリアのメニューの一番左のボタンから、*[Pythonコンソール]* をクリックします。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_change_window_5.png "ウィンドウ表示の変更 手順5")|
|6|スペースが *[3Dビューポート]* から *[Pythonコンソール]* に変更されます。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_change_window_6.png "ウィンドウ表示の変更 手順6")|




## Blenderの初期状態として設定する

他にも不要なエリアを削除したり、エリアの配置を変更したりしてアドオン開発がしやすい環境にします。
Blenderのエリア設定は完了しましたが、このままBlenderを閉じてしまうと次にBlenderを起動した時に初期状態に戻ってしまいます。
そこで以下の手順に従い、Blenderが起動した時にエリア設定がすでに終わっている状態で起動するようにします。


<div class="work"></div>

|||
|---|---|
|1|トップバーのメニューから、*[編集]* > *[デフォルト]* > *[スタートアップファイルを保存]* を実行します。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_save_startup_file_1.png "Blenderの初期状態にする 手順1")|
|2|確認ポップアップが表示されるため、*[スタートアップファイルを保存]* をクリックします。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_save_startup_file_2.png "Blenderの初期状態にする 手順2")|


これで次にBlenderを起動するときには、エリア設定が完了した状態で起動します。
Blenderの起動直後の状態を設定する場合は、いつでもこの方法を使えるので覚えておきましょう。

なお以下の手順を踏むことで、Blenderをダウンロードした直後の状態に戻すことができます。


<div class="work"></div>

|||
|---|---|
|1|トップバーのメニューから、*[編集]* > *[デフォルト]* > *[初期設定を読み込む]* を実行します。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_read_factory_setting_1.png "初期状態を読み込む 手順1")|
|2|確認ポップアップが表示されるため、*[初期設定を読み込む]* をクリックします。<br>![](../../images/chapter_01/03_Prepare_Add-on_development_environment/blender_read_factory_setting_2.png "初期状態を読み込む 手順2")|


<div class="column">
初期設定を読み込んだ後、先ほど紹介したスタートアップファイルを保存する手順を行わない限り、Blenderの起動直後の状態が更新されないことに注意が必要です。
</div>


# テキストエディタ

アドオンの開発は基本的にテキスト（ソースコード）を編集する作業が中心となるため、テキストを編集するテキストエディタが必要です。

各OSに標準で付随しているテキストエディタを使うことでも開発を始めることができます。
しかし、OSに標準で付随しているテキストエディタは最低限の機能しか備わっていないことが多く、テキスト編集が多いアドオンの開発では機能不足であることが多いです。
このためアドオンの開発向けに、ソースコードの編集が楽になるエディタを別途導入した方が良いと思います。



## Blender付随のテキストエディタ

Blenderはアドオン開発者やPythonスクリプトを実行したい人のために、テキストエディタを標準で備えています。
エリアのメニューの一番左のボタンから、*[テキストエディター]* を選ぶだけでBlender付随のテキストエディタを使うことができます。

<div class="column">
Blender付随のテキストエディタは、エディタで開いているソースコードをBlenderで実行できるという、他のテキストエディタにはない機能があります。
簡単なPythonスクリプトを試したいときなどに重宝するエディタです。
</div>


## その他のエディタ

これまで挙げたエディタ以外にも、世の中には様々なエディタがあります。
ここで紹介したエディタに限らず、自分にあったエディタを選ぶと良いと思います。

* PyCharm
* Visual Studio Code
* Atom


# アドオン開発時のBlenderの起動方法

Blenderを起動する時は、アプリケーションのアイコン（Windowsなら `blender.exe`）をダブルクリックして起動することが多いと思います。
しかしアドオン開発時はソースコードが正常に動作しているかを確認（デバッグ）しやすくするために、コンソールウィンドウからBlenderを起動することをおすすめします。

ここではWindows/Mac/Linuxについて、コンソールウィンドウからBlenderを起動する方法を紹介します。
コンソールウィンドウとは、Windowsでは *[コマンドプロンプト]*、Mac/Linuxでは *[ターミナル]* のことを指します。

本書ではコンソールウィンドウからBlenderを起動することを前提として説明しますので、ここで紹介する手順を覚えておいてください。


## Windowsの場合

WindowsのコマンドプロンプトからBlenderを起動する手順を以下に示します。
なお、Windowsのコマンドプロンプトの場合、以下のコマンドを実行して文字コードをUTF-8に変更する必要があります。
また、コマンドプロンプトで表示されるフォントは、日本語に対応しているもの（例えば、ＭＳ 明朝）を選んでください。

```
> chcp 65001
```


<div class="work"></div>

|||
|---|---|
|1|*[コマンドプロンプト]* を起動します。|
|2|以下のコマンドを実行します。（実行ファイル `blender.exe` が置かれているパスが `C:\path\blender.exe` であると仮定します。）<br>`> C:\path\blender.exe`|
|3|Blenderが起動します。|


## Macの場合

MacのターミナルからBlenderを起動する手順を以下に示します。


<div class="work"></div>

|||
|---|---|
|1|*[ターミナル]* を起動します。|
|2|以下のコマンドを実行します。（実行ファイル `Blender.app` が置かれているパスが `/path/Blender.app` であると仮定します。）<br>`$ /path/blender.app/Contents/MacOS/Blender`|
|3|Blenderが起動します。|


## Linuxの場合

LinuxのターミナルからBlenderを起動する手順を以下に示します。


<div class="work"></div>

|||
|---|---|
|1|*[ターミナル]* を起動します。|
|2|以下のコマンドを実行します。（実行ファイル `blender` が置かれているパスが `/path/blender` であると仮定します。）<br>`$ /path/blender`|
|3|Blenderが起動します。|


# まとめ

アドオンの開発を効率的に行うために、Blenderの環境を整える方法を紹介しました。
ここで紹介した環境はあくまで一例ですので、必ずしも紹介した手順を踏む必要はありません。
開発者によって、快適に開発を行える環境は異なると思いますので、試行錯誤しながら自分にあった環境を用意してください。


## ポイント

* 自分にあったアドオンの開発環境を整え、効率的にアドオンの開発を進められるようにしよう
* Blenderのエリア分割機能を利用することで、複数のエリアの状態を同時に確認することができる
* 開発環境の整備が終わったら、スタートアップファイルとして保存することを忘れないようにしよう
* スタートアップファイルを保存した後でも、ダウンロード時の初期状態に戻すことができる
* 世の中には様々なテキストエディタがある。各自が使いやすいエディタを選ぼう
* アドオン開発時に有益な情報を得るため、アドオン開発時はBlenderをコンソールウィンドウから起動しよう
