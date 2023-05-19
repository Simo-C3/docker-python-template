# Dockerfile概要
- Baseイメージ：`nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04`
- python version: 3.11.0
- 導入したパッケージ：
    | パッケージ名 | バージョン | 概要 |
    | :--- | :---: | :--- |
    | pipenv | 最新 | プロジェクト毎のパッケージ管理や仮想環境の構築を簡単に自動で行ってくれるツール<br><h3>参考</h3>- https://pipenv-ja.readthedocs.io/ja/translate-ja/<br>- https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a<br>- https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html |

# 使い方
## 環境変数の設定
compose.ymlにある以下のような環境変数の記述部分を書き換える
```yml
environment:
    - USER_NAME=<ユーザー名>
    - USER_ID=<ユーザーID>
    - GROUP_NAME=<グループ名>
    - GROUP_ID=<グループID>
```

例）ユーザー名がshimomaeの場合
- 確認
    ```sh
    $ id shimomae
    uid=2301(shimomae) gid=2301(shimomae) groups=2301(shimomae),27(sudo),998(docker)
    ```

- 環境変数
    ```yml
    environment:
        - USER_NAME=shimomae
        - USER_ID=2301
        - GROUP_NAME=shimomae
        - GROUP_ID=2301
    ```

## イメージのビルド
```sh
docker compose build cuda --no-cache
```

## コンテナ起動
```sh
docker compose up -d cuda
```

## コンテナに入る
```sh
docker compose exec cuda bash
```

## コンテナから出る
```sh
exit
```

## Pythonファイルの実行
### コンテナ外の場合
- dockreコマンド
    ```sh
    docker compose exec cuda pipenv run python torch_test.py
    ```
- シェルスクリプト
    ```sh
    docker-run torch_test.py
    ```

### コンテナ内の場合
- pipenvコマンド
    ```sh
    pipenv run python torch_test.py
    ```

- シェルスクリプト
    ```sh
    run torch_test.py
    ```

### コンテナ内のpipenvシェル内
```sh
python torch_test.py
```

## pipenv使い方
### パッケージの追加
```sh
pipenv install <パッケージ名>
```

### pipenvシェル(仮想環境)に入る
```sh
pipenv shell
```
### pipenvシェル(仮想環境)から出る
```sh
exit
```

### 仮想環境を作る
```sh
pipenv --python <Pythonバージョン>
```

### Pythonファイル実行
- 仮想環境外
    ```sh
    pipenv run python <Pythonファイルパス>
    ```

- 仮想環境内
    ```sh
    python  <Pythonファイルパス>
    ```
