# 問題集5章 10.
# docstring を参照する属性は「__doc__」（また間違えた！！）

def func():
    """ これはdocstringです """
    pass

print(f"{func.__name__}関数のdocstring:\n{func.__doc__}")

# __docstring__ではない！そんな属性ない！
try:
    print(func.__docstring__)
except Exception as e:
    print("＊例外：", type(e), e)

# ビルトイン関数のdocstringをのぞいてみる

# id()
print(f"{id.__name__}関数のdocstring:\n{id.__doc__}")

# int()
print(f"{int.__name__}関数のdocstring:\n{int.__doc__}")
