# 問題集10章：クラスとオブジェクトの操作（問題）
# ----- 問題3. -----
# メソッド内にインスタンス変数と同名の変数がある場合、それらは別の変数として扱われる
# メソッド内でインスタンス変数を参照・変更する場合は、変数名の先頭にself.を付ける必要がある

class Duck:
    def __init__(self):
        # インスタンス変数
        self.birdsong = "quack"

    def sing(self):
        # この birdsong はメソッドのローカル変数、インスタンス変数とは別物になる
        birdsong = "ga-ga-"
        print(birdsong)

        # インスタンス変数 birdsong の出力
        print(self.birdsong)

        #インスタンス変数の値を変更、ローカル変数には影響しない
        self.birdsong = "coin"
        print(self.birdsong)

        # メソッドのローカル変数 birdsong の出力
        print(birdsong)

duck = Duck()
duck.sing()
