# 問題集6章：タプルの定義
# ----- 問題2. -----

# 選択肢A.はタプルが出力される
sample_tuple = ("spam", "ham", "eggs")
print(sample_tuple)

# 選択肢B.はタプルが出力される
sample_tuple = "spam", "ham", "eggs"
print(sample_tuple)

# 選択肢C.はタプルが出力される
sample_tuple = "spam",
print(sample_tuple)

# 選択肢D.はエラーになる：tupleの引数はリスト等の反復可能体（iterable）である必要がある
# sample_tuple = tuple("spam", "ham", "eggs")
# print(sample_tuple)
