---
pagetitle: 4-2. アドオンをデバッグする
subtitle: 4-2. アドオンをデバッグする
---

Blenderのアドオンで発生したバグの原因を調べて修正するためにかかる時間は、アドオン開発において大半の時間を占めることが多いです。
このため、アドオンのデバッグ手段を知っておくことは、アドオンの開発効率を高める1つの方法になります。
本節では、効率的にデバッグするために、Visual Studio Codeを使ったデバッグの方法を紹介します。


# Visual Studio Codeを利用したデバッグ

Visual Studio Codeを使って、アドオンをデバッグするための手順を次に示します。

1. ptvsdパッケージのインストール
2. デバッグサーバの立ち上げ処理の追加
3. デバッグ対象のアドオン有効化
4. Visual Studio Codeのデバッグ設定
5. デバッグサーバのプロセスへのアタッチ


## 1. ptvsdパッケージのインストール

Pythonプログラム内で、デバッグサーバを立ち上げるために必要となるパッケージ、『ptvsd』をインストールします。

```sh
$ pip install ptvsd
```


## 2. デバッグサーバの立ち上げ処理の追加

ptvsdパッケージを利用し、デバッグ対象とするアドオン側でデバッグサーバを立ち上げます。
アドオンを有効化したときに、デバッグサーバを立ち上げるコード例を次に示します。

```python
def launch_debug_server():
    # ptvsdパッケージの場所を、sys.pathに追加する。
    # ptvsdパッケージは、Pythonの実行ファイルが配置されているディレクトリの
    # site-packages配下に配置されていることが多い（環境によって異なるため、
    # 各自で確認が必要）。
    # ここでは、pythonの実行ファイルが/usr/bin/pythonに配置されていることを想定する。
    ptvsd_path = "/usr/bin/python/site-packages"
    import sys
    sys.path.append(ptvsd_path)

    # ptvsdパッケージのインポート
    import ptvsd

    # デバッグサーバの立ち上げ
    # IPアドレス0.0.0.0（ローカルホスト）、ポート5678として立ち上げる
    ptvsd.enable_attach(address=("0.0.0.0", 5678))

    # Visual Studio Codeからのデバッグリクエストを待ち受ける
    ptvsd.wait_for_attach()


def register():
    launch_debug_server()

    # 初期化コード
```


## 3. デバッグ対象のアドオン有効化

[1-5節](../chapter_01/05_Install_Own_Add-on.html) を参考にして、2の処理を追加したアドオンを有効化します。
アドオンを有効化すると、デバッグサーバが立ちあがります。
この状態になると、Blender自体がデバッグリクエストを受け付けるまで待機してしまうため、Blenderに対して一切操作できなくなることに注意が必要です。


## 4. Visual Studio Codeのデバッグ設定

Visual Studio Codeのデバッグ設定を行います。
Visual Studio Codeの *[Debug]* タブを開き、*[Open 'launch.json']* ボタンをクリックすると、`launch.json` が開くため、次のような設定を追加します。

```json
{
    "configurations": [
        {
            // デバッグ名
            "name": "Python: Debug Blender Add-on",
            // デバッグ対象プログラミング言語
            "type": "python",
            // デバッグの種類。attachを設定
            "request": "attach",
            // 2で設定したデバッグサーバの待ち合わせポートを設定
            "port": "5678",
            // 2で設定したデバッグサーバの待ち合わせホストアドレスを設定
            "host": "0.0.0.0"
        }
    ]
}
```

![](../../images/chapter_04/02_Debug_Add-on/configure_vscode.png "Visual Studio Codeのデバッグ設定")


## 5. デバッグサーバのプロセスへのアタッチ

Visual Studio Codeの *[Debug]* タブを開き、左上のリストボックスから `launch.json` で指定したデバッグ名（今回の場合は、*[Python: Debug Blender Add-on]*）を見つけて選択します。
そして、リストボックスの隣にあるボタン *[Start Debugging]* をクリックすると、デバッグサーバのプロセスにデバッガがアタッチされます。

![](../../images/chapter_04/02_Debug_Add-on/attach_process.png "プロセスへのアタッチ")

3でデバッグリクエストを待機していたアドオンは、この段階で実行が再開されます。
以降、ブレークポイントを設定して各変数の値を確認することをはじめとして、Visual Studio Code上でアドオンをデバッグできます。


# まとめ

本節では、Visual Studio Codeを用いて、アドオンをデバッグする方法を説明しました。
Visual Studio Codeを用いたデバッグは非常に強力で、より効率よくアドオンをデバッグできます。

Visual Studio Codeは更新頻度が高く、UIも頻繁に変更されるため、本節を執筆した時点から大きく変更されている可能性がある点には注意してください。
このため、実際にデバッグ環境を整えるときは、Web上にあるVisual Studio Codeの記事なども確認する必要があります。


## ポイント

* Visual Studio Codeを用いたデバッグ環境を整えることで、アドオンのデバッグを効率化できる
