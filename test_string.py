# 文字列のあれこれテスト
# Pythonチュートリアル：3章 気楽な入門編

# 列挙された文字列リテラルは自動的に連結される
str = ("Kotone Fujita is a character from 'Gakuen Idolmaster' a cheerful 15-year-old"
       " mood-maker aiming to become a money-making idol.")

print(str)

# 文字列はインデックス指定ができる
print(str[0], str[1], str[-1])

# 文字列はスライス操作もサポートされている
print(str[:6], str[-5:])

# 文字列は改変できない：不変体（イミュータブル）
try:
    str[0] = "J"
except Exception as e:
    print("＊例外：", type(e), e)
