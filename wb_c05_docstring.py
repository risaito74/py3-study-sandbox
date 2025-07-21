# 問題集5章：docstring
# ----- 問題10. -----

def func():
    """これはdocstringです"""
    pass

print(func.__doc__)

# ビルトイン関数のdocstring確認

# print()のdocstring確認
print(f"----- print()のdocstring -----\n{print.__doc__}")

# range()のdocstring確認
print(f"----- range()のdocstring -----\n{range.__doc__}")
