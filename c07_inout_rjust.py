# 7章 入出力：手動で文字列のフォーマッティング
# rjust(), center(), ljust()
# 文字列を右寄せ、中央寄せ、左寄せ

tp = ("Kotone", "Ume", "Lilja")

# rjust() : 右寄せ
for s in tp:
    print(s.rjust(8))

# center() : 中央寄せ
for s in tp:
    print(s.center(8))

# x、x2乗、x3乗を右寄せで表示
for x in range(1,11):
    print(str(x).rjust(2), str(x*x).rjust(3), str(x**3).rjust(4))

# zfill() : 数字の文字列の左側をゼロ埋めする
for x in range(1,11):
    print(str(x).zfill(2), str(x*x).zfill(3), str(x**3).zfill(4))
