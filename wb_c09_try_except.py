# 問題集9章：例外処理
# ----- 問題2. -----
# TypeError と ValueError のちがいを理解する

# TypeError
# 意図していないデータ型が与えられた場合や、データ型が対応していない演算を行った場合に発生

try:
    print("文字列'2'で除算テスト")
    ans = 100 / "2"
except TypeError as e:
    print("  ＊例外：", type(e),  e)

try:
    print("リストをint型に変換テスト")
    int([1, 2, 3])  # リスト → int は無理
except TypeError as e:
    print("  ＊例外：", type(e),  e)

# ValueError
# 意図していない値が与えられた場合に発生

try:
    print("文字列'7那由多'をint型に変換テスト")
    n = "7那由多"
    int(n)
except ValueError as e:
    print("  ＊例外：", type(e),  e)

# 上記の例の場合、"1"なら例外は発生しないので、型がおかしいのではなく、あくまで値がおかしい、だからValueError

try:
    print("文字列'100'をint型に変換テスト")
    n = "100"
    int(n)
except ValueError as e:
    print("  ＊例外：", type(e),  e)
else:
    print("  例外は発生せず")

