# 問題集5章：引数をタプルや辞書として参照
# ----- 問題7. -----

def function(name, *args, **kwargs):
    print(name)
    print(args)     # タプル
    print(kwargs)   # 辞書

function("spam", "ham", kwarg1="egg", kwarg2="spamhameggs")

# ----- 以下、この問題を理解するためのテストコード -----
# *が先頭についた仮引数には、位置引数のタプルが入る（指定済みの実引数を除く）
# **が先頭についた仮引数には、キーワード引数の辞書が入る（指定済みの実引数を除く）

def gakumasu(*args, **kwargs):
    print(args)     # タプル
    print(kwargs)   # 辞書

gakumasu("咲季", "ことね", "手毬", 年齢=16, 身長=152, 出身地="愛知県")

# ↑ちなみに、**kwargsをアンパックした実引数で渡す場合、keyはシンボル扱いなのでクォートで囲まない（囲むとエラー）
