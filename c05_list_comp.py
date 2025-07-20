# 5章データ構造：リスト内包

# 基本形
li = [x for x in range(10)] # 0~9
print(f"0~9のリスト = {li}")

# xの2乗
li_sq = [x ** 2 for x in range(10)]
print(f"0~9の2乗 = {li_sq}")

# 偶数のリストを作る(ifとの組み合わせ)
li_ev = [x for x in range(10) if x % 2 == 0]
print(f"偶数のリスト = {li_ev}")

# 既存のリストの書く要素に+1ずつ加算
li_b = [x + 1 for x in li]
print(f"既存リストliに+1 = {li_b}")

# 文字列のリストを大文字に変換
li_w = ["apple", "banana", "cherry"]
li_upw = [w.upper() for w in li_w]
print(f"大文字リスト = {li_upw}")

# ネストの内包
li_x = [1, 2, 3]
li_y = [4, 5, 6]
li_z = [[x, y] for x in li_x for y in li_y]
print(li_z)

li_xy = [str(x) + str(y) for x in range(3) for y in range(3)]
print(li_xy)
