---
pagetitle: 3-3. タイマのイベントを扱う
subtitle: 3-3. タイマのイベントを扱う
---

[3-1節](01_Handle_Mouse_Event.html) と [3-2節](02_Handle_Keyboard_Event.html) では、マウスやキーボードといった、ユーザからの入力イベントを扱う方法を説明しました。
イベントを発生させるほかの方法として、一定時間経過したときにイベントを発生する、タイマを設定する方法もあります。
本節では、タイマから発生するイベントを扱う方法を説明します。


# 作成するアドオンの仕様

タイマのイベントを扱う方法を理解するため、定期的に発生するイベントを利用した、次の機能を備えるアドオンを作成します。

* *[3Dビューポート]* スペースのSidebarの *[サンプル 3-3]* > *[日時を表示]* に、日時をテキストオブジェクトとして表示するためのボタンを配置する
* 日時を表示するモード中は、テキストオブジェクトが作られ、現在の日時がテキストとして設定される


# アドオンを作成する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして次のソースコードを入力し、ファイル名を `sample_3-3.py` として保存してください。

[@include-source pattern="full" filepath="chapter_03/sample_3-3.py"]


# アドオンを使用する


## アドオンを有効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして作成したアドオンを有効化すると、コンソールウィンドウに次の文字列が出力されます。

```
サンプル 3-3: アドオン『サンプル 3-3』が有効化されました。
```

Sidebarを表示し、タブ *[サンプル 3-3]* にパネル *[日時を表示]* が追加されていることを確認します。

![](../../images/chapter_03/03_Handle_Timer_Event/enable_add-on.png "サンプルアドオン3-3 有効化")


## アドオンの機能を使用する

有効化したアドオンの機能を使い、動作を確認します。


<div class="work"></div>

|||
|---|---|
|1|*[3Dビューポート]* スペースのSidebarの *[サンプル 3-3]* > *[日時を表示]* に配置されている *[開始]* ボタンを押します。<br>![](../../images/chapter_03/03_Handle_Timer_Event/use_add-on_1.png "サンプルアドオン3-3 手順1")|
|2|テキストオブジェクトが作成され、日時がテキストとして表示されるようになります。<br>![](../../images/chapter_03/03_Handle_Timer_Event/use_add-on_2.png "サンプルアドオン3-3 手順2")|
|3|*[終了]* ボタンを押すと、テキストオブジェクトが削除されます。<br>![](../../images/chapter_03/03_Handle_Timer_Event/use_add-on_3.png "サンプルアドオン3-3 手順3")|


## アドオンを無効化する

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして有効化したアドオンを無効化すると、コンソールウィンドウに次の文字列が出力されます。

```
サンプル 3-3: アドオン『サンプル 3-3』が無効化されました。
```


# ソースコードの解説

本節では、タイマイベントを扱う処理と日時を表示する処理に限定し、サンプルアドオンのソースコードを解説します。
これまでに説明してきた内容については、説明を省いています。
本節のサンプルアドオンのソースコードに関して、ポイントとなる点を次に示します。

本節では、日時を表示するモードをモーダルモードと記載している部分があります。
以降、モーダルモードと書かれていたら、日時を表示するモードとして読みかえても問題ありません。


## タイマの登録

タイマイベントを発生させるためには、タイマを登録する必要があります。
タイマの登録処理は、次に示す `__handle_add` メソッドで行います。

[@include-source pattern="partial" filepath="chapter_03/sample_3-3.py" block="add_timer", unindent="True"]


タイマは、`context.window_manager.event_timer_add` メソッドを呼び出すことで登録できます。
`context.window_manager.event_timer_add` メソッドは次に示す引数を受け取り、戻り値としてタイマのハンドラを返します。

|引数|型|値の意味|
|---|---|---|
|第1引数|`float`|タイマイベントを発生させる間隔を秒単位で指定|
|第2引数|`bpy.types.Window`|タイマの登録先ウィンドウ|

本節のサンプルアドオンでは、第1引数に `0.5` を指定することで、タイマによるイベントを0.5秒ごとに発生させます。
*[開始]* ボタンが存在するウィンドウでタイマイベントを発生させたいため、第2引数には `context.window` を指定します。

戻り値として返されたハンドラは、タイマを登録解除するときに使用するため、クラス変数 `__timer` に保存します。

`__handle_add` メソッドは、最後にモーダルモードへ移行しますが、必ずしも `__handle_add` メソッド内で行う必要はありません。
`__handle_add` メソッド自体が、`invoke` メソッドから呼び出されていることになるため、[3-1節](01_Handle_Mouse_Event.html) や [3-2節](02_Handle_Keyboard_Event.html)  と同様に、`invoke` メソッドの処理内で `context.window_manager.modal_handler_add` メソッドを呼び出して、モーダルモードへ移行しても問題ありません。


## タイマの登録を解除

タイマを登録すると、登録解除するまでタイマイベントが発生します。
このため、タイマが不要になったら登録を解除する必要があります。

タイマの登録解除処理は、次に示す `__handle_remove` メソッドで行っています。

[@include-source pattern="partial" filepath="chapter_03/sample_3-3.py" block="remove_timer", unindent="True"]

`context.window_manager.event_timer_remove` メソッドを呼び出すことで、タイマを登録解除できますが、引数には、 `context.window_manager.event_timer_add` メソッドの戻り値として返されたタイマのハンドラを渡す必要があります。
本節のサンプルアドオンでは、タイマのハンドラを保存したクラス変数 `__timer` を引数に渡し、タイマを登録解除します。
なお、登録解除済のタイマのハンドラにアクセスすることによる不正な動作を避けるために、クラス変数 `__timer` に `None` を代入します。


## modalメソッド

タイマイベントが発生すると、`modal` メソッドが呼ばれます。

[3-1節](01_Handle_Mouse_Event.html) や [3-2節](02_Handle_Keyboard_Event.html) と同様に、`modal` メソッドの最初で *[3Dビューポート]* スペースを持つエリアの画面更新と、`modal` メソッドの終了判定処理を行います。

[3-1節](01_Handle_Mouse_Event.html) や [3-2節](02_Handle_Keyboard_Event.html) で説明したように、`modal` メソッドはキーボードやマウスのイベントが発生したときにも呼ばれます。
このため、タイマイベントが発生したとき（`event.type` が `'TIMER'` のとき）のみ、日時を更新するようにします。

[@include-source pattern="partial" filepath="chapter_03/sample_3-3.py" block="handle_timer_event", unindent="True"]


## invokeメソッド

*[開始]* ボタンが押されたとき、日時を表示するためのテキストオブジェクトを作成する必要があります。
テキストオブジェクトは、`bpy.ops.object.text_add` 関数を使って作成できます。
作成したテキストオブジェクトは、モーダルモード終了時に削除できるように、テキストオブジェクトの名前をクラス変数 `__text_object_name` に保存しておきます。
また、テキストオブジェクトのテキストには、空文字列を設定します。

[@include-source pattern="partial" filepath="chapter_03/sample_3-3.py" block="make_text_object", unindent="True"]


# まとめ

本節では、タイマのイベントを扱う方法を説明しました。
タイマを使うと、指定した間隔でイベントを発生させることができるため、定期的に処理を実行するような機能を実現できます。

[3-1節](01_Handle_Mouse_Event.html) から本節まで、3節にわたってイベントを扱う処理を説明しましたが、イベントを扱う場合は、`modal` メソッドや `invoke` メソッドを実装する必要があることを、理解できたのではないでしょうか。


## ポイント

* タイマを登録することで、一定間隔でタイマイベントを発生させることができる
* タイマの登録は `context.window_manager.event_timer_add` メソッドで行い、不要になったタイマは `context.window_manager.event_timer_remove` メソッドで登録を解除する
* タイマイベントが発生すると、`context.window_manager.modal_handler_add` の引数に指定したオペレータクラスの `modal` メソッドが呼び出され、引数 `event` のメンバ変数 `event.type` に `TIMER` が設定される
