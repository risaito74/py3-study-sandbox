# 9章クラス：プライベート変数
# オブジェクト内部からしかアクセスできない「プライベート」インスタンス変数はPythonには存在しない。
# つまり前提として、Python では厳密に可視性を制御することはできない。

# それを踏まえた上で、Python においてプライベート変数の定義方法として、以下の二つが存在する。
# (1) _single_leading_underscore    ：慣習的なマナー（人間に向けたメッセージ）
# (2) __double_leading_underscore   ：Pythonの仕様（マングリング機構）

# (1) _single_leading_underscore
# 名前の先頭に '_' を1つ付けると、慣習として「非public（内部用）」という意味を示す（非publicとして扱う）
# 「from module import *」ではimportされないが、明示的にimportすることは可能
class TestClass:
    # 非public なクラス変数（慣習上「内部用」とみなされる）
    _class_arg = 10

    def public_function(self):
        # 非public なインスタンス変数（これも慣習）
        self._private_arg = 20

    # 非public な関数（これも慣習）
    def _private_function(self):
        pass

# (2) __double_leading_underscore
# オブジェクト名の先頭に '_' を 2つ 付けると、マングリング機構を呼び出せる
# マングリング：名前の衝突を避けるための仕組みで、__name という属性は _ClassName__name に自動的に変換される
# マングリングはクラスにはできない。関数、変数にはできる
class ManglingTestClass:
    __mangling_num = 0

    def __init__(self):
        self.__mangling_str = "__init__"

    def __mangling_function(self):
        print("__mangling_function")

# インスタンスを生成
mang = ManglingTestClass()

#マングリングしたクラス変数にアクセスできるか？　→　エラーになる！（__name の形ではアクセスできない）
try:
    print(ManglingTestClass.__mangling_num)
except Exception as e:
    print("例外：__mangling_num:", type(e), e)

#マングリングした関数にアクセスできるか？　→　エラーになる！（__name の形ではアクセスできない）
try:
    mang.__mangling_function()
except Exception as e:
    print("例外：__mangling_function:", type(e), e)

#マングリングしたインスタンス変数にアクセスできるか？　→　エラーになる！（__name の形ではアクセスできない）
try:
    print(mang.__mangling_str)
except Exception as e:
    print("例外：__mangling_str:", type(e), e)

# 非推奨だけど…こうするとアクセスできる
# __hoge は _classname__hoge の形に置き換えられる、から…
try:
    print(mang._ManglingTestClass__mangling_str, "→ 例外にならなかった")
except Exception as e:
    print("例外：__mangling_str:", type(e), e)

# どうしても必要な場合は、getter/setterメソッドを使ってアクセスさせるのがマナー
