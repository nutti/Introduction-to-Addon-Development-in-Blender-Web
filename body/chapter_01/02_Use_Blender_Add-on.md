<div id="sect_title_img_1_2"></div>

<div id="sect_title_text"></div>

# Blenderアドオンを使う

<div id="preface"></div>

###### Blenderアドオンの開発の説明に入る前に他の方が開発したアドオンを使い、アドオンのインストール・有効/無効化の手順を説明します。ここで紹介する手順は今後アドオンを開発する際に何度も行うことになりますので、必ず覚えておきましょう。

## Blenderの日本語化

Blenderは海外で開発されたソフトであるため、Blenderを初めて起動した時のUIは全て英語です。このため、Blenderを利用する敷居が高いと感じる方もいると思いますが、幸いなことにBlenderは公式で日本語のUIをサポートしています。

英語でも難なく使える方であればそのままでも良いのですが、英語では敷居が高いと言う方のためにBlenderを日本語化する方法を紹介します。

なお本書では、**Blenderが日本語化されていることを前提として解説します** ので、不安な方はここで日本語化することをお勧めします。

<div id="process_title"></div>

##### Work

<div id="process"></div>

|<div id="box">1</div>|*Info* エリアのメニューから *File* > *User Preferences...* を実行します。|![アドオンの日本語化 手順1](https://dl.dropboxusercontent.com/s/8xx2l59wy2d7c8y/localizing_into_japanese_1.png "アドオン日本語化 手順1")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|*Blender User Preferences* ウィンドウが立ち上がるので、 *System* タブを選択します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">3</div>|*International Fonts* にチェックを入れると、UIの言語を変更することができるようになります。|![アドオンの日本語化 手順3](https://dl.dropboxusercontent.com/s/6uwpij0r5riiqk3/localizing_into_japanese_3.png "アドオン日本語化 手順3")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">4</div>|*Language* を *Japanese（日本語）* に変更し、*Translate* で日本語化する項目を選択すると、選択した項目のUIに関して日本語化されます。|![アドオンの日本語化 手順4](https://dl.dropboxusercontent.com/s/s5mrd72si2xq910/localizing_into_japanese_4.png "アドオン日本語化 手順4")|
|---|---|---|

<div id="process_start_end"></div>

---

## アドオンの種類

アドオンを使用する前に、アドオンのサポートレベルについて理解しましょう。

**アドオンのサポートレベルはアドオンの品質やメンテナンスなどの将来性を示しす。** サポートレベルが高ければよくメンテナンスされていて品質が高い傾向があります。一方、サポートレベルが低いアドオンではメンテナンスがおろそかな傾向があり、正しく動作しないまま放置されているアドオンも少なからずあります。

サポートレベルが低くても非常に有用なアドオンはたくさんあります。問題が起きても気にせず様々なアドオンを使いたい方はサポートレベルを気にせず使えばよく、安定した動作をするアドオンのみを使いたい方であればサポートレベルが高いアドオンだけを使用するのがよいと思います。

サポートレベルは、3段階から構成されます。

|サポートレベル|説明|
|---|---|
|Release|Blenderが公式にサポートするアドオンで、正式版のBlender本体と一緒に提供されます。<br>アドオンの公開や更新の度に、Blenderの開発者による厳密なレビュー（審査）があるため、**不具合が少なく安定しています** 。|
|Contrib|Blender本体には含まれませんが、テストビルドされたBlender本体と共に提供されます。<br>サポートは各アドオン開発者が行うため、サポートレベルがReleaseであるアドオンに比べて品質が落ちます。<br>Contribとして登録されるためには、Blenderの開発者のレビューで一定の評価を得る必要があるために **一定の品質が保証され、新規性があり有用な機能を持つアドオン** が集まっています。|
|External|サポートレベルがReleaseおよびContrib以外のアドオンで、ユーザが自らアドオンをインストールする必要があります。<br>Blenderの開発者によるアドオンのレビューが行われていないため、**本サポートレベルのアドオンの利用は基本的に自己責任となります。**<br> 作業効率化など、Blender本体の機能を補助するアドオンが多く含まれるようですが、中にはサポートレベルがReleaseやContribよりも優れた機能を持つアドオンも存在します。|

## アドオンのインストール

サポートレベルがReleaseであるアドオンは、正式版のBlender本体と共に提供されるためインストール作業は不要です。また、テストビルドのBlenderを利用されている方は、サポートレベルがContribのアドオンについてもインストールすることなく利用可能です。

ここでは、正式版のBlender本体を利用されている方がサポートレベルContribのアドオンをインストールする場合や、サポートレベルがExternalであるアドオンをインストールする場合について説明します。本節では、数あるインストール方法のうちの1つを紹介しています。詳しくは、 [1-4節](04_Understand_Install_Uninstall_Update_Add-on.md) を参照ください。

インストール手順を説明するにあたり、アドオン開発で筆者がいつもお世話になっているmifth氏のアドオンMira Toolsをサンプルとして取り上げます。Mira Toolsの機能は、以下のWebサイトから確認できます。

<div id="webpage"></div>

|Mira Tools|
|---|
|https://github.com/mifth/mifthtools/wiki/Mira-Tools|
|![Mira Tools](https://dl.dropboxusercontent.com/s/gsr52gq7xbx37ch/mira_tools.png "Mira Tools")|

Mira Toolsは日本語をサポートしていないためアドオンを使う敷居がやや高くなりますが、サポートレベルがExternalのアドオンの中でも非常に高機能なアドオンの1つですので、ぜひ1度使ってみてください。

Mira Toolsのインストール方法は前述のURLにも記載されていますが、ここでもインストール方法を紹介します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|https://github.com/mifth/mifthtools/archive/master.zip からmifth氏が作成したアドオン一式をダウンロードします。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">2</div>|ダウンロードしたファイル *mifthtools-master.zip* を解凍します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|```mifthtools-master/blender/addons/mira_tools``` がMira Tools本体です。このフォルダ一式を、 Blender アドオン用フォルダへコピーしたらインストール完了です。|
|---|---|

Blenderアドオン用フォルダは以下に示すように、OSごとにパスが異なります。インストール先のフォルダがない場合は、新たに作成してください。

|OS|インストール先|
|---|---|
|Windows|```C:\Users\<ユーザ名>\AppData\Roaming\Blender Foundation\Blender\<Blenderのバージョン>\scripts\addons```|
|Mac|```/Users/<ユーザ名>/Library/Application Support/Blender/<Blenderのバージョン>/scripts/addons```|
|Linux|```/home/<ユーザ名>/.config/blender/<Blenderのバージョン>/scripts/addons```|

<div id="process_start_end"></div>

---

<div id="column"></div>

コピーしたファイルの中に拡張子が .py であるファイルがあります。 このファイルはアドオンのソースコードと呼ばれ、プログラミング言語Pythonによりアドオンの動作が記述されたテキストファイルです。


## アドオンの有効化

インストールしたアドオンを有効化し、アドオンの機能を使えるようにします。サポートレベルがRelease/Contrib/Externalのいずれのアドオンについても、これから紹介する方法で有効化できます。

以下の手順に従い、先ほどインストールしたMira Toolsを有効化します。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|Blenderを起動します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*情報* エリアのメニューから、*ファイル* > *ユーザー設定...* を選択します。|![アドオンの有効化 手順2](https://dl.dropboxusercontent.com/s/9it3p8rth2heyqi/enable_add-on_2.png "アドオンの有効化 手順2")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">3</div>|*Blenderユーザー設定* ウィンドウが別ウィンドウで開きますので、*アドオン* タブを選択します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process_noimg"></div>

|<div id="box">4</div>|検索窓に *mira tools* と入力します。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">5</div>|ウィンドウ右側に *Mira Tools* が表示されますので、チェックボックスにチェックを入れるとアドオンが有効化されます。|![アドオンの有効化 手順5](https://dl.dropboxusercontent.com/s/k4xq9zyhk0hbivp/enable_add-on_5.png "アドオンの有効化 手順5")|
|---|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">6</div>|実際にアドオンが有効化されているかは、*エディットモード* 時に *3Dビュー* エリアの左側の *ツールシェルフ* のタブに *Mira* が追加されていることで確認できます。|![アドオンの有効化 手順6](https://dl.dropboxusercontent.com/s/qqvxodqbs67yy45/enable_add-on_6.png "アドオンの有効化 手順6")|
|---|---|---|

<div id="process_start_end"></div>

---

<div id="column"></div>

Mira Tools の使い方をここで紹介するのは本書の範囲を超えてしまうので、ここでは説明しません。  
興味のある方は以下のページを参照してください。  
Mira Tools - https://github.com/mifth/mifthtools/wiki/Mira-Tools


## アドオンの無効化

Release/Contrib/Externalいずれのサポートレベルについても共通で、次に紹介する手順でアドオンを無効化できます。


<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|アドオンを有効化した時と同様、*Blenderユーザー設定* ウィンドウを開きます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*アドオン* タブを選択し、*Mira Tools* のチェックボックスのチェックを外すことでアドオンが無効化されます。|![アドオンの無効化 手順2](https://dl.dropboxusercontent.com/s/t15vvgofl5gs50d/disable_add-on_2.png "アドオンの無効化 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---


## アドオンのアンインストール

インストール済みのMira Toolsをアンインストールします。

インストールと同様、本節では数あるアンインストール方法のうちの1つを紹介しています。
詳しくは、 [1-4節](04_Understand_Install_Uninstall_Update_Add-on.md) を参照ください。

<div id="process_title"></div>

##### Work

<div id="process_noimg"></div>

|<div id="box">1</div>|*Blenderユーザー設定* ウィンドウの *アドオン* タブを選択し、 *Mira Tools* の左の矢印をクリックして詳細情報を開きます。|
|---|---|

<div id="process_sep"></div>

---

<div id="process"></div>

|<div id="box">2</div>|*削除* ボタンをクリックすると、アンインストールが完了します。|![アドオンのアンインストール 手順2](https://dl.dropboxusercontent.com/s/0hkgrg49n0kh880/uninstall_add-on_2.png "アドオンのアンインストール 手順2")|
|---|---|---|

<div id="process_start_end"></div>

---



## まとめ

アドオンのサポートレベルについて解説し、アドオンのサポートレベルがExternalであるアドオンをインストール・アンインストールする方法を紹介しました。さらに、インストールしたアドオンが動作していることも確認しました。ここで紹介した手順はアドオン開発時に何度も行う操作であるため、必ず覚えておきましょう。

また、本節ではBlenderを日本語化する方法も紹介しました。本節以降は、Blenderが日本語化されていることを前提に解説しますので、必要に応じて本節を参考に日本語化してください。

<div id="point"></div>

### ポイント

<div id="point_item"></div>

* Blenderは標準で日本語をサポートするため、必要に応じてUIを日本語化することができる。
* Blenderのアドオンは、アドオンの品質や将来性を示すサポートレベルで分類できる。
* Blenderのアドオンのソースコードは、プログラミング言語Pythonで書かれた拡張子が.pyのテキストファイルである。
