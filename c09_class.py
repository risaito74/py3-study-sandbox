# 9章クラス：はじめてのクラス

class TestClass:
    # 初期処理：新規生成されたインスタンスに対して自動的にコールされる
    def __init__(self):
        # インスタンスに属するインスタンス変数
        self.num = 10
    
    #クラスのメソッド
    def get_num(self):
        return self.num

# TestClassクラスのインスタンスを生成
test = TestClass()

# インスタンスの変数を直接参照できる
test.num += 10

# インスタンスのメソッドをコール
print(test.get_num())
