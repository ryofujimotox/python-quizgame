# How To Use

## Lambda レイヤー作成

### ライブラリフォルダ生成

```bash
# ライブラリ出力
pip install -e '/xxxxxxxx/chatgpt' -t python

# コピー
cp -R chatgpt python/chatgpt

# 圧縮
zip upload python
```

### レイヤー作成

`レイヤー` -> `レイヤーの作成` -> `アップロード`

## Lambda 関数追加

`関数` -> `関数の作成` ->

1. コードソース入力
2. レイヤーの追加


## Test

`イベントJSON`

```json
{"body": {"api_key": "sk-xxxxxx", "answer": "東京タワー", "message": "赤いですか"}}
```