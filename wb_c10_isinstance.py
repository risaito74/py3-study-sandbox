# 問題集10章：isinstance()関数
# ----- 問題6. -----

# 親クラスの定義
class ParentClass:
    def __init__(self):
        print("init Parent")

# 子クラスの定義
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        print("init Child")

# 子クラスのインスタンスを生成
child = ChildClass()

# child は ChildClass に属するインスタンスか？
print("child は ChildClass のインスタンス？：", isinstance(child, ChildClass))
# 出力：True

# child は ParentClass に属するインスタンスか？
# インスタンスの親クラス（基底クラス）も属しているクラスに該当する
print("child は ParentClass のインスタンス？：", isinstance(child, ParentClass))
# 出力：True

# 組み込みのデータ型にも使える
print("'abc' は str のインスタンス？：",isinstance("abc", str))
# 出力：True

print("1 は int のインスタンス？：", isinstance(1, int))
# 出力：True

print("1 は str のインスタンス？：", isinstance(1, str))
# 出力：False

# 複数のデータ型をタプルで指定することもできる
# どれかが True なら True になる（論理和）
print("'hello' は int, str, float のどれかのインスタンス？：", isinstance("hello", (int, str, float)))
# 出力：True（strにマッチ）

print("'hello' は dict, list, tuple のどれかのインスタンス？：", isinstance("hello", (dict, list, tuple)))
# 出力：False
