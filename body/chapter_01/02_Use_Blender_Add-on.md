<div id="sect_title_img_1_2"></div>

<div id="sect_title_text"></div>

# Blenderアドオンを使う

<div id="preface"></div>

###### Blenderアドオンの開発の説明に入る前に他の方が開発したアドオンを使い、アドオンのインストール・有効/無効化の手順を説明します。ここで紹介する手順は今後アドオンを開発する際に何度も行うことになりますので、必ず覚えておきましょう。

## Blenderの日本語化

Blenderは海外で開発されたソフトであるため、Blenderを初めて起動した時のUIは全て英語です。このため、Blenderを利用する敷居が高いと感じてしまう方もいると思いますが、幸いなことにBlenderは公式で日本語をサポートしています。

英語でも難なく使える方であればそのままでも良いですが、英語では敷居が高いと言う方のためにBlenderを日本語化する方法を紹介します。

なお本書では、 **Blenderが日本語化されていることを前提として解説します** ので、不安な方はここで日本語化することをお勧めします。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*Info* エリアのメニューから *File* > *User Preferences...* を実行します。|![アドオンの日本語化 手順1](https://dl.dropboxusercontent.com/s/8xx2l59wy2d7c8y/localizing_into_japanese_1.png "アドオン日本語化 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|*Blender User Preferences* ウィンドウが立ち上がりますので、 *System* タブを選択します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*International Fonts* にチェックを入れると、Blenderの言語を変更することができるようになります。|![アドオンの日本語化 手順2](https://dl.dropboxusercontent.com/s/6uwpij0r5riiqk3/localizing_into_japanese_2.png "アドオン日本語化 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*Language* を *Japanese（日本語）* に変更し、 *Translate* で日本語化する項目を選択すると、選択された項目が日本語化されます。|![アドオンの日本語化 手順3](https://dl.dropboxusercontent.com/s/s5mrd72si2xq910/localizing_into_japanese_3.png "アドオン日本語化 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---

## アドオンの種類

アドオンを使用する前に、アドオンのサポートレベルについて理解しましょう。

**アドオンのサポートレベルはアドオンの品質やメンテナンスなどの将来性を示しています。**

サポートレベルが高ければよくメンテナンスされていて品質が高い傾向があります。一方、サポートレベルが低いアドオンではメンテナンスがおろそかな傾向があり、正しく動作しないまま放置されているアドオンも少なからずあります。

サポートレベルが低くても非常に有用なアドオンはたくさんあります。問題が起きてもいろんなアドオンを使いたい方はサポートレベルを気にせず使えばよく、安定した動作をするアドオンのみを使いたい方であればサポートレベルが高いアドオンだけを使用するのがよいと思います。

サポートレベルは、以下の3段階から構成されます。

|サポートレベル|説明|
|---|---|
|Release|Blenderが公式にサポートするアドオンで、Blender本体と共に提供されます。<br>アドオンの公開や更新の度に厳密にレビュー（審査）されるため、 **不具合が少ない安定したアドオン** です。|
|Contrib|Blender本体には含まれませんが、テストビルドされたBlender本体と共に提供されます。<br>サポートは各アドオン開発者が行うため、サポートレベルがReleaseであるアドオンに比べて品質が落ちます。<br>Contribとして登録されるためには、Blender開発者のレビューで一定の評価を得る必要があるために **一定の品質が保証され、新規性のある有用な機能を持ったアドオン** が集まっています。|
|External|サポートレベルがReleaseおよびContrib以外のアドオンで、ユーザ自らアドオンをインストールする必要があります。<br>Blender開発者によるアドオンのレビューが行われていないため、**本サポートレベルのアドオンの利用は基本的に自己責任となります。**<br> 作業効率化など、Blender本体の機能を補助するアドオンが多く含まれるようですが、中にはサポートレベルがReleaseやContrib以上の機能を持つアドオンも存在します。|

## アドオンのインストール

サポートレベルがReleaseであるアドオンは、Blender本体と共に提供されるためインストール作業は不要です。また、テストビルドのBlenderを利用されている方は、サポートレベルがContribのアドオンについてもインストールすることなく利用可能です。

ここでは、Blender本体を利用されている方がサポートレベルContribのアドオンをインストールする場合や、サポートレベルExternalのアドオンをインストールする場合について説明します。

インストール手順を説明するにあたり、筆者がアドオン開発でいつもお世話になっているmifthさんのアドオンMira Tools をサンプルとして取り上げます。Mira Toolsの機能は、以下のWebサイトから確認できます。

<div id="webpage"></div>

|Mira Tools|
|---|
|https://github.com/mifth/mifthtools/wiki/Mira-Tools|
|![Mira Tools](https://dl.dropboxusercontent.com/s/gsr52gq7xbx37ch/mira_tools.png "Mira Tools")|

Mira Toolsは日本語未サポートのため、アドオンを使う敷居がやや高くなりますが、サポートレベルがExternalのアドオンの中でも非常に高機能なアドオンですので、ぜひ1度使ってみてください。

Mira Toolsのインストール方法は前述のURLにも記載されていますが、改めてここでもインストール方法を紹介します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|https://github.com/mifth/mifthtools/archive/master.zip からmifthさんが作成したアドオン一式をダウンロードします。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|ダウンロードしたファイル *mifthtools-master.zip* を解凍します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|```mifthtools-master/blender/addons/mira_tools``` がMira Tools本体です。このフォルダ一式を、 **Blenderアドオン用フォルダ** へコピーしたらインストール完了です。|
|---|---|

なお以下に示すように、Blenderアドオン用フォルダはOSごとにパスが異なります。
インストール先のフォルダがない場合は、新たに作成してください。

|OS|インストール先|
|---|---|
|Windows|```C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons```|
|Mac|```/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons```|
|Linux|```/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons```|

<div id="process_start_end"></div>

---

<div id="column"></div>

コピーしたファイルの中に拡張子が.pyであるファイルがあると思います。  
このファイルは アドオンのソースコードと呼ばれ、プログラミング言語Pythonによりアドオンの動作が記述されたテキストファイルです。


## アドオンの有効化

インストールしたアドオンを有効化して、アドオンの機能を使えるようにします。
サポートレベルがRelease、Contrib、Externalのいずれのアドオンについても、これから紹介する方法で有効化できます。

以下の手順に従い、先ほどインストールしたMira Toolsを有効化します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|Blenderを起動します|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*情報* エリアのメニューから、 *ファイル* > *ユーザ設定* を選択します。|![アドオンの有効化 手順1](https://dl.dropboxusercontent.com/s/9it3p8rth2heyqi/enable_add-on_1.png "アドオンの有効化 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|*Blenderユーザ設定* ウィンドウが別ウィンドウで開きますので、 *アドオン* タブを選択します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|検索窓に *mira tools* と入力します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|ウィンドウ右側に *Mira Tools* が表示されますので、チェックボックスにチェックを入れるとアドオンが有効化されます。|![アドオンの有効化 手順2](https://dl.dropboxusercontent.com/s/k4xq9zyhk0hbivp/enable_add-on_2.png "アドオンの有効化 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|実際にアドオンが有効化されているかは、 *3Dビュー* エリアの左側の *ツールシェルフ* のタブに *Mira* が追加されていることで確認できます。|![アドオンの有効化 手順3](https://dl.dropboxusercontent.com/s/qqvxodqbs67yy45/enable_add-on_3.png "アドオンの有効化 手順3")|
|---|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

Mira Tools の使い方をここで紹介するのは本書の範囲を超えてしまうので、ここでは説明しません。  
興味のある方は以下のページを参照してください。  
Mira Tools - https://github.com/mifth/mifthtools/wiki/Mira-Tools

<div id="space_l"></div>


## アドオンの無効化

次にアドオンを無効化する方法を説明します。

以下に紹介する手順により、 サポートレベルがRelease・Contrib・Externalのいずれについても共通の方法で無効化することができます。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|アドオンを有効化した時と同様、 *Blenderユーザ設定* ウィンドウを開きます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*アドオン* タブを選択し、 *Mira Tools* のチェックボックスのチェックを外すことでアドオンが無効化されます。|![アドオンの無効化](https://dl.dropboxusercontent.com/s/t15vvgofl5gs50d/disable_add-on.png "アドオンの無効化")|
|---|---|---|

<div id="process_start_end"></div>

---


## アドオンのアンインストール

インストール済みのMira Toolsをアンインストールします。

インストールしたアドオンをアンインストールする方法は、以下の2通りがあります。

* アドオンのソースコードを直接削除
* *Blenderユーザ設定* ウィンドウからアンインストール

### アドオンのソースコードを直接削除する方法

アドオンのインストール先からアドオンのソースコードを直接削除して、アドオンをアンインストールする手順を説明します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|アドオンのソースコードの場所が分からない場合は、 *Blenderユーザ設定* ウィンドウの *アドオン* タブから確認します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|アドオン名の隣にある左の矢印をクリックして *Mira Tools* の詳細情報を表示します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|詳細情報の *ファイル* がアドオンのソースコードが置かれた場所を示しています。|![アドオンの詳細情報を表示](https://dl.dropboxusercontent.com/s/7onrbdzxctp4uqw/show_add-on_detail.png "アドオンの詳細情報を表示")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|アドオンのソースコードを削除すると、アンインストールが完了します。|
|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

アドオンのソースコードが複数のファイルで構成される場合と、単一のファイルで構成される場合とで削除するファイルが異なります。  
詳細情報のファイルに書かれているファイル名が \_\_init\_\_.py である場合は、アドオンのソースコードが複数のファイルで構成されています。
この場合は、 \_\_init\_\_.py が置かれているディレクトリごと削除することでアンインストールが完了します。  
\_\_init\_\_.py 以外であれば単一ファイルで構成されていることを示していますので、詳細情報の ファイルに示されたファイルを削除すれば、アンインストールが完了します。詳しくは、 [1-4節](04_Understand_Install_Uninstall_Update_Add-on.md) を参照ください。

### Blenderユーザ設定からアンインストールする方法

他のアドオンのアンインストール方法として、 *Blenderユーザ設定* ウィンドウからアンインストールする方法があります。

<div id="space_m"></div>


<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*Blenderユーザ設定* ウィンドウの *アドオン* タブを選択し、 *Mira Tools* の左の矢印をクリックして詳細情報を開きます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*削除* ボタンをクリックすると、アンインストールが完了します。|![アドオンのアンインストール](https://dl.dropboxusercontent.com/s/0hkgrg49n0kh880/uninstall_add-on.png "アドオンのアンインストール")|
|---|---|---|

<div id="process_start_end"></div>

---


<div id="column"> </div>

アドオンのソースコードを直接削除する場合とは異なり、アドオンのソースコードが複数のファイルで構成されている場合でも単一のファイルで構成されている場合でも、同じ方法で削除することができます。

## まとめ

アドオンのサポートレベルについて解説し、アドオンのサポートレベルがExternalであるアドオンをインストール/アンインストールする手順を紹介しました。さらに、インストールしたアドオンが動作していることも確認しました。ここで紹介した手順はアドオン開発時に何度も行う操作であるため、必ず覚えておきましょう。

また、本節ではBlenderを日本語化する方法を紹介しました。本節以降は、Blenderが日本語化されていることを前提に解説していきますので、必要に応じて日本語化してください。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderは標準で日本語をサポートするため、必要に応じてUIを日本語化することができる。
* Blenderアドオンは、アドオンの品質や将来性を示すサポートレベルで分類できる。

<div id="space_xs"></div>

<div id="point_item"></div>

* Blenderアドオンのソースコードはプログラミング言語Pythonで書かれた、拡張子が.pyのテキストファイルである。
* Blenderアドオンのインストール/アンインストールは、ソースコードをBlenderアドオン用フォルダに直接置く方法と、Blender内のGUIを使って行う方法がある。
* ソースコードが複数ファイルで構成されるアドオンをインストールする場合は、ソースコードをBlenderアドオン用フォルダに直接置く必要がある。
