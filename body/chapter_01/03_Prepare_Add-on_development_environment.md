<div id="sect_title_img_1_3"></div>

<div id="sect_title_text"></div>

# アドオンの開発環境を整える

<div id="preface"></div>

###### 本節では、アドオンを効率良く開発するために環境を整えます。各自開発しやすい環境があると思いますので、すでに環境が整っている方は参考程度に見るだけでよいと思います。

## UIの日本語化

[1-2節](02_Use_Blender_Add-on.md) でも紹介しましたが、Blenderは日本語のUIを標準でサポートしています。

英語が苦手な方はBlenderのUIを日本語化することで、英語が原因でアドオンの開発に行き詰まることを少なくできます。英語に不安のある方は [1-2節](02_Use_Blender_Add-on.md) を参考に日本語化しておきましょう。

## Blenderのエリア設定

アドオンを開発しやすくするために、Blenderのエリア設定を行います。ここで示しているエリア設定は筆者の好みがそのまま反映されているため、各自作業しやすい環境に設定してください。

<div id="sidebyside"></div>

|Blenderをダウンロードした直後のBlenderの起動画面は、右図のようになっています。|![Blender 初期状態](https://dl.dropboxusercontent.com/s/jj7knj6wpu29mrd/blender_initial.png "Blender 初期状態")|
|---|---|

<div id="sidebyside"></div>

|Blenderをダウンロードした直後の初期状態でもアドオンの開発は可能ですが、右図のようにアドオンを開発しやすい環境に整えることをお勧めします。|![Blender アドオン開発向け環境](https://dl.dropboxusercontent.com/s/8htta1qv05kt900/blender_final.png "Blender アドオン開発向け環境")|
|---|---|


### スクリプト実行ログの表示

Blenderの初期状態では隠れてしまっていますが、*情報* エリアには、アドオンの実行結果やエラーを表示する機能（以降、スクリプト実行ログと呼びます）があります。

スクリプト実行ログを表示させるための手順を以下に示します。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*情報* エリアの上端を下に向かってドラッグ＆ドロップします。|![スクリプト実行ログの表示 手順1](https://dl.dropboxusercontent.com/s/ho9x3vdwrfp1bqr/blender_show_console_window_1.png "スクリプト実行ログの表示 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|スクリプト実行ログが表示されます。|![スクリプト実行ログの表示 手順2](https://dl.dropboxusercontent.com/s/49km722w99jxygf/blender_show_console_window_2.png "スクリプト実行ログの表示 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---

スクリプト実行ログはアドオン開発時に大変役立つ機能ですので、**アドオン開発中は常に表示しておく** とよいと思います。


### エリアの分割

Blenderはアプリケーション内で複数のエリアに分割することができます。エリアを分割することで、他のエリアで作業したい時に毎回エリアを変更する必要が無くなります。

アドオンの開発を行いやすくするため、ここでは以下のようにエリアを分割します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|左下の三角マークを右側にドラッグ&ドロップしてエリアを縦に2分割します。|![ウィンドウの分割 手順1](https://dl.dropboxusercontent.com/s/hnc8c8qfonfnnyp/blender_divide_window_1.png "ウィンドウの分割 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|左側のエリアの左下の三角マークを上側にドラッグ&ドロップして左側のエリアを横に2分割します。|![ウィンドウの分割 手順2](https://dl.dropboxusercontent.com/s/g6ifc1mn5wu120e/blender_divide_window_2.png "ウィンドウの分割 手順2")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="process"></div>

|<div id="box">3</div>|これでエリア分割は完了です。<br>分割後のエリアは全て *3Dビュー* になります。|![ウィンドウの分割 手順3](https://dl.dropboxusercontent.com/s/i3bbl8f5vbmazhk/blender_divide_window_3.png "ウィンドウの分割 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---

### エリアの変更

エリアを分割した後、それぞれのエリアを変更します。

エリア変更の手順を以下に示します。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|左下のエリアのメニューの一番左のボタンから、*テキストエディター* をクリックします。|![ウィンドウ表示の変更 手順1](https://dl.dropboxusercontent.com/s/v56yihqny5qy83q/blender_change_window_1.png "ウィンドウ表示の変更 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|左下のエリアが *3Dビュー* から *テキストエディター* に変更されます。|![ウィンドウ表示の変更 手順2](https://dl.dropboxusercontent.com/s/9edhgrh27ulak4p/blender_change_window_2.png "ウィンドウ表示の変更 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|左上のエリアのメニューの一番左のボタンから、*Pythonコンソール* をクリックします。|![ウィンドウ表示の変更 手順3](https://dl.dropboxusercontent.com/s/owvn6git978ja7i/blender_change_window_3.png "ウィンドウ表示の変更 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|左上のエリアが *3Dビュー* から *Pythonコンソール* に変更されます。|![ウィンドウ表示の変更 手順4](https://dl.dropboxusercontent.com/s/9ws6g0tr3xhpc94/blender_change_window_4.png "ウィンドウ表示の変更 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---


### Blenderの初期状態として設定する

他にも不要なエリアを削除したり、エリアの配置を変更したりしてアドオン開発がしやすい環境にします。Blenderのエリア設定は完了しましたが、このままBlenderを閉じてしまうと次にBlenderを起動した時に初期状態に戻ってしまいます。そこで以下の手順に従い、Blenderが起動した時にエリア設定がすでに終わっている状態で起動するようにします。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*情報* エリアのメニューから、*ファイル* > *スタートアップファイルを保存* を実行します。|![Blenderの初期状態にする 手順1](https://dl.dropboxusercontent.com/s/kbro7t4evkim2au/blender_save_startup_file_1.png "Blenderの初期状態にする 手順1")|
|---|---|---|

<div id="process_sep"></div>

---


<div id="space_s"></div>


<div id="process"></div>

|<div id="box">2</div>|確認ポップアップが表示されるので、*スタートアップファイルを保存* をクリックします。|![Blenderの初期状態にする 手順2](https://dl.dropboxusercontent.com/s/pm74e5k1atjgu0a/blender_save_startup_file_2.png "Blenderの初期状態にする 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---

これで次にBlenderを起動する時には、エリア設定が完了した状態で起動します。Blenderの起動直後の状態を設定する場合は、いつでもこの方法を使えるので覚えておきましょう。

なお以下の手順を踏むことで、Blenderをダウンロードした直後の状態に戻すことができます。


<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*情報* エリアの *ファイル* > *初期設定を読み込む* を実行します。|![初期設定を読み込む 手順1](https://dl.dropboxusercontent.com/s/fzhbvpp60xf76a6/blender_read_factory_setting_1.png "初期状態を読み込む 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|確認ポップアップが表示されるので、*初期設定を読み込む* をクリックします。|![初期設定を読み込む 手順2](https://dl.dropboxusercontent.com/s/sc2dvqqw19twg12/blender_read_factory_setting_2.png "初期状態を読み込む 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

初期設定を読み込んだ後、先ほど紹介したスタートアップファイルを保存する手順を行わない限り、Blenderの起動直後の状態が更新されないことに注意が必要です。

## テキストエディタ

アドオンの開発は基本的にテキスト（ソースコード）を編集する作業が中心となるため、テキストを編集するテキストエディタが必要です。

各OSに標準で付随しているテキストエディタを使うことでも開発を始めることができます。しかし、OSに標準で付随しているテキストエディタは最低限の機能しか備わっていないことが多く、テキスト編集が多いアドオンの開発では機能不足であることが多いです。このためアドオンの開発向けに、ソースコードの編集が楽になるエディタを別途導入した方が良いと思います。

ちなみに筆者はアドオンのソースコード編集にVim、READMEなどの文章編集にAtomを利用することが多いです。

### Blender付随のテキストエディター

Blenderはアドオン開発者やPythonスクリプトを実行したい人のために、テキストエディタを標準で備えています。

エリアのメニューの一番左のボタンから、*テキストエディター* を選ぶだけでBlender付随のテキストエディタを使うことができます。なお、Blenderのエリア設定をすでに行っている方は、左下のウィンドウが *テキストエディター* です。

<div id="column"></div>

Blender付随の *テキストエディター* は、*テキストエディター* で開いているソースコードをBlenderで実行できるという、他のテキストエディタにはない機能があります。  簡単なPythonスクリプトを試したい時などに重宝するエディタです。

### Vim

Vimについて詳しく書くとEmacsとのエディタ論争に巻き込まれそうなので、簡単に紹介するだけにします。

VimはEmacsと共にUnix/Linuxでよく利用されるエディタの1つで、コマンドモードと入力モードと呼ばれる2つのモードを備えていることが特徴なエディタです。gVimと呼ばれるWindows版のVimも存在するため、一度Vimの使い方を習得すればOSを変えてもエディタの使い方を再度勉強する必要がありません。

有志によってVimを使いやすくするためのプラグインや記事がインターネット上にたくさんありますので、初期状態のVimが使いづらいと感じたら検索してみると良いかもしれません。

### Emacs

Vimと共に、Unix/Linuxでよく利用されるエディタです。

Vimと同様にemacsにもWindows版が用意されているため、一度使い方を習得すればOSを変えてもエディタの使い方を再度勉強する必要がありません。

ユーザが多いエディタであるため、Emacsを使いやすくするためのプラグインや記事がインターネット上にたくさんあります。

### その他のエディタ

これまで挙げたエディタ以外にも、世の中には様々なエディタがあります。ここで紹介したエディタに限らず、自分にあったエディタを選ぶと良いと思います。

他のエディタとしては例えば以下のようなものがあります。

|エディタ名|Windows|Mac|Linux|
|---|---|---|---|
|Atom|◯|◯|◯|
|秀丸|◯|×|×|
|TeraPad|◯|×|×|
|nano|×|◯|◯|
|SublimeText|◯|◯|◯|


## アドオン開発時のBlenderの起動方法

Blenderを起動する時は、アプリケーションのアイコン（Windowsなら ```blender.exe``` ）をダブルクリックして起動することが多いと思います。しかしアドオン開発時はソースコードが正常に動作しているかを確認（デバッグ）しやすくするために、 **コンソールウィンドウからBlenderを起動** することをおすすめします。

ここではWindows/Mac/Linuxについて、コンソールウィンドウからBlenderを起動する方法を紹介します。コンソールウィンドウとは、Windowsでは *コマンドプロンプト* 、Mac/Linuxでは *ターミナル* のことを指します。

本書ではコンソールウィンドウからBlenderを起動することを前提として説明しますので、ここで紹介する手順を覚えておいてください。

### Windowsの場合

WindowsのコマンドプロンプトからBlenderを起動する手順を以下に示します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*コマンドプロンプト* を起動します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|以下のコマンドを実行します。<br>（実行ファイル ```blender.exe``` が置かれているパスが ```C:\path\blender.exe``` であると仮定します。）|
|---|---|

```dos
> C:\path\blender.exe
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|Blenderが起動します。|
|---|---|

<div id="process_start_end"></div>

---

### Macの場合

MacのターミナルからBlenderを起動する手順を以下に示します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*ターミナル* を起動します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>| 以下のコマンドを実行します。<br>（実行ファイル ```Blender.app``` が置かれているパスが ```/path/Blender.app``` であると仮定します。）|
|---|---|

```sh
$ /path/blender.app/Contents/MacOS/blender
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|Blenderが起動します。|
|---|---|

<div id="process_start_end"></div>

---

### Linuxの場合

LinuxのターミナルからBlenderを起動する手順を以下に示します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*ターミナル* を起動します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>| 以下のコマンドを実行します。<br>（実行ファイル ```blender``` が置かれているパスが ```/path/blender``` であると仮定します。）|
|---|---|

```sh
$ /path/blender
```

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|Blenderが起動します。|
|---|---|

<div id="process_start_end"></div>

---

## まとめ

アドオンの開発を効率的に行うために、Blenderの環境を整える方法を紹介しました。ここで紹介した環境はあくまで一例ですので、必ずしも紹介した手順を踏む必要はありません。開発者によって、快適に開発を行える環境は異なると思いますので、試行錯誤しながら自分にあった環境を用意してください。



<div id="point"></div>

### ポイント

<div id="point_item"></div>

* 自分にあったアドオンの開発環境を整え、効率的にアドオンの開発を進められるようにしよう
* Blenderのエリア分割機能を利用することで、複数のエリアの状態を同時に確認することができる
* 開発環境の整備が終わったら、スタートアップファイルとして保存することを忘れないようにしよう
* スタートアップファイルを保存した後でも、ダウンロード時の初期状態に戻すことができる
* 世の中には様々なテキストエディタがある。各自が使いやすいエディタを選ぼう
* アドオン開発時に有益な情報を得るため、アドオン開発時はBlenderをコンソールウィンドウから起動しよう
