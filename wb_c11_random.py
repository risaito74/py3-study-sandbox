# 問題集11章：randomモジュール
# ----- 問題7. -----
# 「-1から1未満の乱数」を生成するコードとして最も適切なものを選択

import random

# 選択肢A
li = []
for i in range(100):
    # 「0から1未満の乱数」- 1 だから「-1から0未満の乱数」になる
    n = random.random() - 1
    n = round(n, 2)
    li.append(n)
print(f"選択肢A : min = {min(li)}, max = {max(li)}")
# 「-1から0未満の乱数」だから：不正解

# 選択肢B
# ramdom()は引数を指定できない：エラーになる
try:
    n = random.random(2) - 1
except Exception as e:
    print("＊例外：", type(e), e)
# エラーになるから：不正解

# 選択肢C
# ramdom()は引数を指定できない：エラーになる
try:
    n = random.random(-1, 1)
except Exception as e:
    print("＊例外：", type(e), e)
# エラーになるから：不正解

# 選択肢D
li = []
for i in range(100):
    # 「0から1未満の乱数」* 2 - 1 だから「-1から1未満の乱数」になる
    n = random.random() * 2 - 1
    n = round(n, 2)
    li.append(n)
print(f"選択肢D : min = {min(li)}, max = {max(li)}")
# 「-1から1未満の乱数」だから：正解
