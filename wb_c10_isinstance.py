# 問題集10章：isinstance()関数
# ----- 問題6. -----

class ParentClass:
    def __init__(self):
        print("init Parent")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print("init Child")

# 子クラスのインスタンスを生成
child = ChildClass()

# child は ChildClass に属するインスタンスか？
print("child は ChildClass のインスタンス？：", isinstance(child, ChildClass))

# child は ParentClass に属するインスタンスか？
# インスタンスの親クラス（基底クラス）も属しているクラスに該当する
print("child は ParentClass のインスタンス？：", isinstance(child, ParentClass))

# 組み込みのデータ型にも使える
print("'abc' は str のインスタンス？：",isinstance("abc", str))
print("1 は int のインスタンス？：", isinstance(1, int))
print("1 は str のインスタンス？：", isinstance(1, str))

# 複数のデータ型をタプルで指定することもできる
# どれかが True なら True になる（論理和）
print("'hello' は int, str, float のどれかのインスタンス？：", isinstance("hello", (int, str, float)))  # → True（strにマッチ）
print("'hello' は dict, list, tuple のどれかのインスタンス？：", isinstance("hello", (dict, list, tuple)))
