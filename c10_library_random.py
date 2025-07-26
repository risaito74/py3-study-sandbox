# 10章 標準ライブラリ：randomモジュール
# randomモジュールは無作為抽出のツールを提供する

import random

# ダイスロール（6面ダイス1個を1回振る）
dice = random.randint(1, 6) # 1~6まで出る
print(f"6面ダイスを振った結果:", dice)

# リストから1つを無作為抽出する
li = ["花海咲季", "月村手毬", "藤田ことね", "根緒先生"]
print(f"あなたがプロデュースするアイドルは{random.choice(li)}です")

# 重複なしの抽出
# 0~99から重複せず10個抽出しリストで返す
li_n = random.sample(range(100), 10)
print(li_n)

# random.random()
# 0.0以上1.0未満の浮動小数点数float型の乱数を生成する
num_f = random.random()
print(f"random() = {num_f}")

# randrange()
# range(start, stop, step)の要素からランダムに選ばれた要素（整数int型）を返す
dice = random.randrange(1, 7) # range()と同じ挙動だからstop未満 → stop=7にしないと最大値6が出ない
print(f"6面ダイスを振った結果:", dice)
