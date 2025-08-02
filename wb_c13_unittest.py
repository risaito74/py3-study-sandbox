# 問題集13章：問題37
# unittest

import unittest

# テストケースは unittest.TestCase を継承したクラスとして定義する
# クラス名は任意だが、慣例として頭に Test を付ける
# （unittest はデフォルトで TestCase を継承したクラスの test_～ メソッドを探索する）
class TestApp(unittest.TestCase):
    # test_ の関数を自動で実行する（原則1テスト1関数）
    def test_equal_day(self):
        """ actual と expected が等しいかのテスト """
        actual = "Sunday"
        expected = "Monday"

        # 第一引数と第二引数が等しいか
        self.assertEqual(actual, expected)
        # AssertionError が送出されて、ここでテストが止まる（この後に次のテストを入れても実行されない）
    
    def test_not_equal_day(self):
        """ actual と expected が等しくないかのテスト """
        actual = "Sunday"
        expected = "Monday"

        # 第一引数と第二引数が等しくないか
        self.assertNotEqual(actual, expected)
        # 結果：OK
    
    def test_not_equal_num(self):
        """ 数値1と文字列"1"が等しくないかのテスト """
        actual = 1
        expected = "1"

        # 第一引数と第二引数が等しくないか
        self.assertNotEqual(actual, expected)
        # 結果：OK

# unittestの実行方法
# 01.コマンドラインから右のように実行：python -m unittest wb_c13_unittest.py
# 02.下記のコードを入れて通常実行

# このモジュールを直接実行した場合にユニットテストを実行する
if __name__ == "__main__":
    unittest.main()

# テスト結果出力（抜粋）
# F..　→　テスト結果が「FAIL」「OK」「OK」（".":成功/OK, "F":失敗/FAIL, "E":エラー）
# Ran 3 tests in 0.001s　→　3テスト実行して、かかった時間
