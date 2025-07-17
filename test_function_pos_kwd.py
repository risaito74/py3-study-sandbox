# 位置のみ引数とキーワードのみ引数テスト
def hoge(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    """ 各引数を出力：posは位置のみ引数、kwdはキーワードのみ引数 """
    print(pos1, pos2)
    print(pos_or_kwd)
    print(kwd1, kwd2)

# 第3引数を位置引数で渡す
hoge(1, 2, 3, kwd1=4, kwd2=5)

# 第3引数をキーワード引数で渡す
hoge(10, 20, pos_or_kwd=30, kwd1=40, kwd2=50)
