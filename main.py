import numpy as np, pandas as pd
from pulp import *

df = df = pd.read_csv("menu.csv") # csvファイルを読み込む

df["個数"] = LpVariable.dicts("個数",df["料理名"], 0,2, cat='Integer').values()

problem = LpProblem(sense=LpMaximize) # 最大化問題
problem.setObjective(lpDot(df["カロリー"], df["個数"])) # 許容カロリー内でなるべく多く食べたい

# 条件を設定
problem += lpDot(df["カロリー"], df["個数"]) <= 2200
problem += lpDot(df["タンパク質"], df["個数"]) >= 100
problem += lpDot(df["タンパク質"], df["個数"]) <= 130
problem += lpDot(df["脂質"], df["個数"]) <= 60
problem += lpDot(df["炭水化物"], df["個数"]) >= 250
problem += lpDot(df["炭水化物"], df["個数"]) <= 350
problem.solve()

total_protein = sum([df["タンパク質"][i] * value(df["個数"][i]) for i in range(len(df))])
total_fat = sum([df["脂質"][i] * value(df["個数"][i]) for i in range(len(df))])
total_carbo = sum([df["炭水化物"][i] * value(df["個数"][i]) for i in range(len(df))])
total_calories = value(problem.objective)
selected_menu = [f'{df["料理名"][i]}: {value(df["個数"][i])}' for i in range(len(df)) if value(df["個数"][i]) >= 1]

# 結果を出力
print(f"摂取カロリー: {total_calories}")
print(f"タンパク質: {total_protein}, 脂質: {total_fat}, 炭水化物: {total_carbo}")
for m in selected_menu:
    print(m)