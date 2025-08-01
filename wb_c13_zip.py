# 問題集13章：問題21
# zip()
# 複数のイテラブル（リスト、タプル、セットなど）から要素を取り出す

names = ["スノハラ", "チノ", "カリンちゃん"]
scores = [95, 88]

# forループで複数のリストから要素を同時に取り出せる
# 短い方（scores）に合わせて途中で終了する
for name, score in zip(names, scores):
    print(name, score)

# タプルとリストを混ぜてもヨシ
# 3つ以上のイテラブルもできる
tp = (10, 20, 30)
for name, score, n in zip(names, scores, tp):
    print(name, score, n)

# for で回さない使い方
# 2つの要素がタプルのペアとしてまとめられる
combined = zip(names, scores)

print(type(combined))
# 出力：<class 'zip'>

print(list(combined))
# 出力：[('スノハラ', 95), ('チノ', 88)]

# zipオブジェクトは反復子（イテレータ）だから一度展開すると中身が空になる
print(list(combined))
# 出力：[]
