# 5章データ構造：集合(set)
# 集合のためのデータ型
# 集合とは重複しない要素を順不同で集めたもの

# 集合の生成は{}またはset()関数を使用する
set_num = {1, 2, 3, 2, 1, 4}
print(f"集合num_s: {set_num}")

li = [1, 2, 3, 2, 1, 4]
print(f"リストliをset()で集合化: {set(li)}")

#　文字列に対する集合：1文字単位で重複しない要素を集める
str_a = set("sunohara")
print(f"'sunohara'の文字単位の集合: {str_a}")

# 和集合（集合の和）
# パイプ演算子（|）で集合と集合の和（和集合）を演算する
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
uni_ab = a | b
print(f"aとbの和集合: {uni_ab}")

# 積集合（集合の積）
itsc_ab = a & b
print(f"aとbの積集合: {itsc_ab}")

# 差集合（集合の差）: a - b と b - a で結果が変わるので順序が重要
# 集合aに存在し、bに存在しないもの（a -b）
diff_ab = a - b
print(f"aからbを引いた差集合: {diff_ab}")
# 集合bに存在し、aに存在しないもの（b -a）
diff_ba = b - a
print(f"bからaを引いた差集合: {diff_ba}")

# 対象差集合（積集合じゃないやつ）（和集合 - 積集合）：XOR（排他的論理和）と同じ
sym_diff_ab = a ^ b
print(f"aとbの対象差集合: {sym_diff_ab}")
