# 問題集10章：クラスとオブジェクトの操作（問題）
# ----- 問題1. -----
# クラス変数の定義と参照
# 定義：クラス変数はクラスブロック内で定義する（self.は付けない）
# 参照：クラス名.family が明示的で安全。
#   self.family でも参照できるが、同名のインスタンス変数が存在するとそちらが優先される（シャドーイング）

class Duck:
    # クラス変数familyの定義（アヒルはAnatidae科＝カモ科）
    family = "Anatidae"

    # コンストラクタの定義
    def __init__(self):
        # インスタンス変数birdsongの定義
        self.birdsong = "quack"

    # show_familyメソッドの定義
    def show_family(self):
        return f"Ducks belong to the family {self.family}."
    
    # show_family_instanceメソッドの定義（self.familyをインスタンス変数で用意）
    def show_family_instance(self):
        # クラス変数と同名のインスタンス変数を定義すると、インスタンス変数が優先的に参照される（クラス変数に影響なし）
        self.family = "カモ科"
        return f"Ducks belong to the family {self.family}."

# Duckクラスのインスタンスduckを生成
duck = Duck()

print(duck.show_family())
# 出力：Ducks belong to the family Anatidae.

print(duck.show_family_instance())
# 出力：Ducks belong to the family カモ科.

# クラス変数familyを直接出力
print("クラス変数family:", Duck.family)
# 出力：Anatidae

# duckインスタンスの属性familyを出力：インスタンス変数が優先的に参照される
print("duckインスタンスのfamily:", duck.family)
# 出力：カモ科

# duckインスタンスの属性としてのクラス変数familyを参照するには、インスタンス変数familyを削除する必要がある
del duck.family
print("duckインスタンスの属性family（インスタンス変数削除後）:", duck.family)
# 出力：Anatidae
