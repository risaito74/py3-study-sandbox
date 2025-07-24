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
hoge = TestClass()

# インスタンスの変数を直接参照できる
test.num += 10
hoge.num = 999

# インスタンスのメソッドをコール
print("test.num:", test.get_num())
print("hoge.num:", hoge.get_num())

class TestClass2:
    """ インスタンス生成時、関数コール時に引数を受け取る """

    # どのインスタンスも持つことになる共通のクラス変数
    count = 0

    # 引数 init_num でインスタンスを生成する初期処理
    def __init__(self, init_num):
        self.num = init_num
    
    # クラスのメソッド：引数 add_num を加算して返す
    def add_num(self,add_num):
        self.num += add_num
        return self.num

# TestClass2クラスのインスタンスを生成
test2 = TestClass2(10)
hoge2 = TestClass2(100)

# クラス変数 count の参照
# 【注意】：クラス変数をインスタンスからアクセスしようとすると、代入時に「新しいインスタンス変数」が作られるなど、
# クラス変数を意図せず上書き・無効化してしまう可能性がある！
# クラス変数を明示的に扱うには、基本的に (クラス名).(クラス変数名) でアクセスするのが安全
TestClass2.count = 20
print("TestClass2.count: ", TestClass2.count)

# インスタンスのメソッドをコール
print("test2.num:", test2.add_num(1))
print("hoge2.num", hoge2.add_num(1))

# 注意：以下の count はクラス変数 count とは無関係に新しく作られたインスタンス変数
test2.count = 10
hoge2.count = 5
print("インスタンス変数のcount:", test2.count, hoge2.count)
print("TestClass2.count: ", TestClass2.count)
