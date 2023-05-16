# python3.11 template

## 前提
- pipenvの環境がローカルにあること

## ローカルの環境
### 手順
1. pipの仮想環境の作成とパッケージのインストール

    ```sh
    pipenv install
    ```
    実行は初回だけで良い
### 新しいパッケージをインストール

`1.`を実行し、pipの仮想環境ができた状態で以下のように実行することでパッケージをインストールすることができる
```sh
pipenv install <パッケージ名>
```

## Docker環境

### イメージビルド
```sh
docker compose build
```

### コンテナの起動
```sh
docker compose up -d python3.11
```

