# 5章データ構造：条件についての補足

# 演算子 in および not in 
# <要素> in <集合> → 要素が集合に含まれる場合True、含まれない場合Falseになる。
li = [1, 2, 3]
for i in range(5):
    print(f"{i} はリストに含まれる？: {i in li}")

se = {1, 2, 3}
for i in range(5):
    print(f"{i} は集合に含まれない？: {i not in se}")

# 演算子 is および is not
# Pythonにおいて、==演算子は2つのオブジェクトの値が等価（同値）かを比較・判定し、
# is演算子は2つのオブジェクトが同一かを比較・判定する。
l1 = [1, 2, 3]
l2 = [1, 2, 3]

# == は「値が等しいか」の比較（値が同じならTrue）
# is は「同一オブジェクトか」の比較（後述のid()が同じならTrue）
print(f"l1 と l2 は同値か？: {l1 == l2}") # True
print(f"l1 と l2 は同じオブジェクトか？: {l1 is l2}") # False : 値が同じだけで別のオブジェクト

l3 = l1 # ミュータブルの代入は浅いコピーで同じidを参照する
print(f"l1 と l3 は同じオブジェクトか？: {l1 is l3}") # True
print(f"l1 と l3 は同じオブジェクトではないか？: {l1 is not l3}")

# オブジェクトの同一性はid()関数で判定される
print(f"l1のid: {id(l1)}")
print(f"l2のid: {id(l2)}")
print(f"l3のid: {id(l3)}")

# 比較は連鎖させられる
a, b, c = 10, 20, 30
# a (演算子) b (演算子) c : 「a (演算子) b」かつ「b (演算子) c」か？
print(f"a < b < c は？: {a < b < c}")
print(f"a < b == c は？: {a < b == c}")

# ブール演算子 not > and > or → not の優先順位が最も高く or が最も低い
# ex: a == b or not b == c は (a == b) or (not (b == c))
# 演算対象の評価が左から右に行われ、結論が決定した時点で評価をやめる
print(f"a < b and b < c and a < c は？: {a < b and b < c and a < c}")
print(f"a == b or not b == c or a == c は？: {a == b or not b == c or a == c}")
