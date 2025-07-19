# 5章データ構造：del文
li = [x for x in range(10)] # 0~9
print(f"元のリスト: {li}")

del li[0]
del li[-1]
print(f"index=0,-1削除: {li}")

# スライスで複数削除
del li[0:2]
print(f"スライス[0:2]削除: {li}")

del li[-2:]
print(f"スライス[-2:]削除: {li}")

# 全要素削除
del li[:]
print(f"全要素削除: {li}")

# 変数削除
x = 100
print(f"x = {x}")
del x
# print(x)  # これコメント外すとNameErrorになる