# 問題集13章：問題16
# リストやタプルとして与えられた引数をアンパックして渡す

def print_name(n1, n2, n3):
    """ 3つの引数を出力 """
    print(f"第1引数 n1: {n1}")
    print(f"第2引数 n2: {n2}")
    print(f"第3引数 n3: {n3}")

li = ["Kotone", "Temari", "Saki"]

# ついでに：print_name()のdocstringを表示
print(f"***** {print_name.__name__} : {print_name.__doc__} *****")

# リストに「*」をつけてアンパックして関数に渡す
print_name(*li)
# 第1引数 n1: Kotone
# 第2引数 n2: Temari
# 第3引数 n3: Saki

def print_dic(name="Kotone", age=15):
    """ 名前と年齢を表示 """
    print(f"name: {name}, age: {age}")

dic = {"name": "Saki", "age":16}

# ついでに：print_dic()のdocstringを表示
print(f"***** {print_dic.__name__} : {print_dic.__doc__} *****")

# 引数なし：デフォルト引数が使われる
print_dic()
# name: Kotone, age: 15

# 辞書に「**」をつけてアンパックして関数に渡す
print_dic(**dic)
# name: Saki, age: 16

