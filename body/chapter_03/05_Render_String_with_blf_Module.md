<div id="sect_title_img_3_5"></div>

<div id="sect_title_text"></div>

# blfモジュールを使って文字列を描画する

<div id="preface"></div>

###### [3-4節](04_Use_API_for_OpenGL.md) ではOpenGLのAPIを利用した図形描画を行う方法を説明しましたが、本節のサンプルでは文字列を描画する方法を説明します。本節では [3-3節](03_Handle_Timer_Event.md) のサンプルを改造したアドオンを用いて説明しますが、可能な限り文字列描画の説明に閉じて説明しますので、必ずしも [3-3節](03_Handle_Timer_Event.md) をすべて理解する必要はありません。


## 作成するアドオンの仕様

* [3-3節](03_Handle_Timer_Event.md) を改造し、作業時間を *3Dビュー* エリアのウィンドウ上部に表示する

## アドオンを作成する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考にして以下のソースコードをテキスト・エディタに入力し、ファイル名 ```sample_3-5.py``` として保存してください。

[import](../../sample/src/chapter_03/sample_3-5.py)

## アドオンを使用する

### アドオンを有効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md) を参考に作成したアドオンを有効化すると、コンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル3-5: アドオン「サンプル3-5」が有効化されました。
```



### アドオンの機能を使用する

以下の手順に従って、作成したアドオンの機能を使ってみます。

<div id="process_title"></div>

##### Work

<div id="process"></div>


|<div id="box">1/div>|||
|---|---|---|

<div id="process_start_end"></div>

---


### アドオンを無効化する

[1-5節](../chapter_01/05_Install_own_Add-on.md)を参考に有効化したアドオンを無効化すると、コンソールウィンドウに以下の文字列が出力されます。

```sh
サンプル3-5: アドオン「サンプル3-5」が無効化されました。
```

## ソースコードの解説

### OpenGLへアクセスするためのAPIを利用する

本節のサンプルでは、図形を描画するためにBlenderが提供するOpenGLへアクセスするためのAPIを利用します。

OpenGLへアクセスするAPIをアドオンから利用するためには、 ```bgl``` モジュールをインポートする必要があります。

```python
import bgl
```



## まとめ




<div id="point"></div>

### ポイント

<div id="point_item"></div>

*
