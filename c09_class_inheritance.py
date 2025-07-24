# 9章クラス：継承、オーバーライド、多重継承

class Parent:
    """ 親クラス """
    def __init__(self):
        print("Parent constructor")

    def greet(self):
        print("Hello from Parent")

    def hoge(self):
        print("Hoge from Parent")

class Child(Parent):
    """ 子クラス（Parentを継承） """
    def __init__(self):
        # 親クラスの __init__() を super() 経由で呼び出す
        super().__init__()
        print("Child constructor")
    
    # 親クラスの greet() をオーバーライド
    def greet(self):
        print("Hello from Child")

# childクラスのインスタンスを生成
child = Child()

# 子クラスのインスタンスから継承された親クラスのメソッドを呼ぶ
child.hoge()

# 子クラス側でオーバーライドしたgreet()を呼ぶ
child.greet()

# 多重継承
# 複数の基底クラスを持つクラス定義、複数の基底クラスはいずれも子クラスに対する親クラス（同世代の基底クラス）になる
# 親クラス（基底クラス）は左から順番に解決される：メソッド解決順序（MRO: Method Resolution Order）
class Parent1:
    """ 親クラス1 """
    def __init__(self):
        print("Init from P1")

    def hello(self):
        print("Hello from P1")

class Parent2:
    """ 親クラス2 """
    def __init__(self):
        print("Init from P2")

    def hello(self):
        print("Hello from P2")

class Parent3:
    """ 親クラス3 """
    def __init__(self):
        print("Init from P3")

    def hello(self):
        print("Hello from P3")

class Child123(Parent1, Parent2, Parent3):
    """ 親クラス1,2,3から継承した子クラス """
    def __init__(self):
        # Parent1の__init__が呼ばれる
        # super() は MRO に従って、最初に見つかったクラスのメソッドだけを呼ぶ：つまりP2,P3は呼ばれない（全部呼びたい場合、親クラスにもsuper()を使う）
        super().__init__()
        print("Init from Child123")

# Child123クラスのインスタンスを生成
c123 = Child123()

# 親クラス1,2,3にあるhello()を呼び出す → メソッド解決順序MROによりParent1クラスのhello()が呼ばれる
c123.hello()

# メソッド解決順序(MRO)の確認
print(Child123.__mro__)

# 親・子・孫の継承
# 子クラスは親クラスを継承し、孫クラスは子クラスを継承する

# 既出のParentを親クラス、Childを子クラスとする、孫クラスを定義する
class GrandChild(Child):
    """ 子クラスを継承する孫クラス """
    def __init__(self):
        # 子クラスの __init__() を super() 経由で呼び出す
        super().__init__()
        print("GrandChild constructor")
    
    # 子クラスの greet() をオーバーライド
    def greet(self):
        print("Hello from GrandChild")

# クラスのインスタンスを作成して動作確認
grandchild = GrandChild()
grandchild.greet()
