# 問題集13章：問題29
# ValueErrorになるケース（毎回TypeErrorと間違える件）

try:
    times = input("分割回数：")
    value = 100 / int(times)
    print(value)

# 例外を送出するケース
# 01. 入力値が「0」だとゼロ除算で ZeroDivisionError
# 02. 入力値が「a」など整数に変換できないときは ValueError
#   → TypeErrorじゃない！（文字列"1"は通るんだから型違いではなく値違い）
except (ZeroDivisionError, ValueError) as e:
    print("エラーが発生しました")
    print(type(e), e)
# 入力値が「a」の場合の例外の内容
# <class 'ValueError'> invalid literal for int() with base 10: 'a'

# じゃあ...
# int()でTypeErrorが出るケースってなんだよ！（涙目）

# 01.int()にリスト、辞書など違う型（引数として扱えない型）を渡す
try:
    int([1, 2])
except Exception as e:
    print("＊例外：", type(e), e)
# 出力：<class 'TypeError'> int() argument must be a string, a bytes-like object or a real number, not 'list'

# 02.引数の数が合わない（第2引数はbase用だけど特殊）
try:
    int("a", "b", "c")
except Exception as e:
    print("＊例外：", type(e), e)
# 出力：<class 'TypeError'> int expected at most 2 arguments, got 3

# 03.Noneを渡す
try:
    int(None)
except Exception as e:
    print("＊例外：", type(e), e)
# 出力：<class 'TypeError'> int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

# そもそも...
# int()の引数は「str型」だから、文字列型を渡してTypeErrorになるはずがない！
