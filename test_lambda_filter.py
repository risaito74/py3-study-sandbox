# lambda式とfilter()の組み合わせ

# filter(関数, iterableなオブジェクト)
# 関数の戻り値がTrueとなる要素のみをもつ、filterクラスのコレクションを生成する

nums = [1, 2, 3, 4, 5, 6]

# 関数とfilter()で偶数を抽出
def is_even(n):
    """ 偶数ならTrueを返す """
    return n % 2 == 0

li_e = list(filter(is_even, nums))
print(li_e)
# 出力：[2, 4, 6]

# これをlambda式で書くと
lmd = lambda n: n % 2 == 0
li_e = list(filter(lmd, nums))
print(li_e)
# 1行版：print(list(filter(lambda n: n % 2 == 0, nums)))
# 出力：[2, 4, 6]
