# 任意引数と辞書の引数のセットのテスト
def hoge(*args, **dict):
    for i in args:
        print(i)

    for key, val in dict.items():
        print(f"{key}: {val}")

hoge(1, 2, 3, a=1, b=2, c=3)
