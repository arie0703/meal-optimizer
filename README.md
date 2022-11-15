# meal-optimizer
献立最適化ツール

## Docker立ち上げ
`docker-compose up -d`  
`docker-compose exec app bash`  

## 実行
`python main.py`  

## CSVファイルの記述
`touch menu.csv`  

```csv
料理名,カロリー,タンパク質,脂質,炭水化物
親子丼,412,22.4,8.6,63
ビッグマック,525,26,42.6,41.8
生姜焼き,445,25,25,30
```

先頭行に「料理名,カロリー,タンパク質,脂質,炭水化物」というヘッダーを加える。  
以下の行に任意の料理とカロリー等の情報をカンマ区切りで入力する。