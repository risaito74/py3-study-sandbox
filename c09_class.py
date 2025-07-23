# 9章クラス：はじめてのクラス

class TestClass:
    """ クラスの基本を理解するためのテスト用クラス """

    # 初期処理：新規生成されたインスタンスに対して自動的にコールされる
    def __init__(self):
        # インスタンスに属するインスタンス変数
        self.num = 10
    
    #クラスのメソッド
    def get_num(self):
        return self.num

# クラスのdocstringを表示
print(TestClass.__doc__)

# TestClassクラスのインスタンスを生成
test = TestClass()

# インスタンスの変数を直接参照できる
test.num += 10

# インスタンスのメソッドをコール
print(test.get_num())
