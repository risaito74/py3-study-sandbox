# 問題集13章：問題15
# 引数のデフォルト値とスコープ

# グローバル変数
default_name = "Taro"

# 引数のデフォルト値 name=default_name は、関数が定義された時点で評価され、関数の実行時に再評価は行われない
def hello1(name=default_name):
    return f"Hello {name}."

# 関数内で default_name を参照し、文字列を返す
def hello2(name=None):
    if name is None:
        # ここで参照する default_name はグローバル変数
        # 関数呼び出し時に「都度」評価されるため、最新の default_name が name に代入される
        name = default_name
    return f"Hello {name}."

# 関数内でグローバル変数 default_name と同名の変数を定義すると、これはグローバル変数とは別のローカル変数になる
def hello3():
    # この default_name はローカル変数！
    default_name = "Jiro"
    return f"Hello {default_name}."

def print_hello4():
    # この default_name はグローバル変数
    print("hello4:", default_name)

# グローバル変数の default_name に代入
default_name = "Hanako"

print(hello1(), hello2(), hello3())

# 関数内で default_name を表示
print_hello4()

# グローバル変数の default_name を表示
print("default_name:", default_name)
