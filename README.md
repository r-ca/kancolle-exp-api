# kancolle-exp-api
目標レベルまでの必要経験値を返してくれるAPIサーバー（つくりかけ）


## インストール
- `pip3 install -r require.txt` 依存しているパッケージのインストール
- `uvicorn main:app --host 0.0.0.0` 起動して0.0.0.0をListen

## Endpoints
- `/exp/kanmusu/`
  - 艦娘経験値用のエンドポイント
  - 必要なパラメータ
    - current: 現在のレベル(int型, 1~175)
    - target: 目標レベル(int型, 1~175)

