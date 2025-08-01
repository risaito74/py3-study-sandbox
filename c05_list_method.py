# 5章 データ構造：リストのメソッドのテスト
li_n = [1, 2, 3, 4, 5]
li_s = ["a", "b", "c"]

# 末尾に追加　
for i in range(6,10):
    li_n.append(i)

print(f"li_n = {li_n}")

for i in range(ord("d"),ord("h")):
    li_s.append(chr(i))

print(f"li_s = {li_s}")

# extendメソッド：イテラブルの全アイテムを追加してリストを伸長
li_ex = []
li_ex.extend(range(10))
print(f"li_ex = {li_ex}")

# 指定位置にアイテム挿入
li_s.insert(0, "a0") # リスト先頭に挿入
li_s.insert(1, "a1") # index=1に挿入
li_s.insert(-1, "z") # この段階でのリスト末尾位置（index=-1）に挿入して、末尾にあったgは後ろに押し出される

print(f"li_s = {li_s}")

# リストから削除：popとremove
pop_i = li_s.pop(-1) # リストの末尾を削除
print(f"li_s = {li_s}")
print(f"削除した値：{pop_i}")

pop_i = li_s.pop() # indexの指定がないと、リストの末尾を削除
print(f"li_s = {li_s}")
print(f"削除した値：{pop_i}")

li_m = [1, 2, 3, 2, 5, 2]
li_m.remove(2) #リストの最初の2を削除
#li_m.remove(999) # リストに無い値を指定するとエラーになる
print(f"li_m = {li_m}")
