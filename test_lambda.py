# lambda式サンプル
add = lambda x, y: x + y
hello = lambda name: print(f"hello, {name}")

print(add(2, 3))
hello("taro")

#mapとラムダの組み合わせ
li = [10, 20, 30, 40, 50]

li2 = list(map(lambda x: x * 2, li))

print(li2)