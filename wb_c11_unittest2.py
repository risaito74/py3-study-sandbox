# 問題集11章：unittestモジュール
# ----- 問題12. -----
# 正解：self.assertEqual(actual, expected)

# 2周目では「self.」をつけることを間違えて不正解になった…
# なんで assertEqual() に「self.」が必要なの？？

# assertEqual() は unittest モジュールの TestCase クラス内に定義されたインスタンスメソッドだから！

import unittest

# テストケースの定義：unittest.TestCase を継承したクラス
class TestSample(unittest.TestCase):
    def test_it(self):
        actual = sum([1, 2, 3])
        expected = 5
        # unittest.TestCase 内に定義されたインスタンスメソッドだから「self.」をつける
        self.assertEqual(actual, expected)

# テストの実行
unittest.main()
# 出力（一部抜粋）：
# AssertionError: 6 != 5
