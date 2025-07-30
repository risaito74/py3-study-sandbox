# 問題集11章：unittestモジュール
# 1) unittest.TestCase を継承したクラス内に test_ の関数を作る
# 2) 「unittest.main()」でテストが実行され、test_ 関数が自動で処理されて結果が出力される
# ----- 問題12. -----
# 正解：self.assertEqual(actual, expected)　→　self.assertEqual() の書式を覚える

import unittest

# テスト対象の関数
def add(a, b):
    return a + b

# テストケースの定義：unittest.TestCase を継承したクラス
class TestMathOperations(unittest.TestCase):

    # 関数名は必ず test_ で始まる → unittest が自動認識
    def test_add(self):
        # assertEqual(first, second, msg=None)
        # first == second ならテスト成功、そうでなければ失敗して AssertionError を投げる。
        # msg はテストが失敗したときに表示するメッセージ（省略可）デフォルトは '{first} != {second}' みたいな自動生成
        self.assertEqual(add(2, 3), 5)  # 正常ケース
        self.assertEqual(add(-1, 1), 0)  # 負の値を含むケース

    # 関数名は必ず test_ で始まる → unittest が自動認識
    def test_add_fail(self):
        # assertNotEqual(first, second, msg=None)
        # first != second ならテスト成功、そうでなければ失敗。
        self.assertNotEqual(add(2, 2), 5)  # 異常ケース

    # 動作確認用にテスト関数をもう1個追加（これで3テストになる）
    def test_more_add(self):
        self.assertEqual(add(0, 0), 0)  # 正常ケース

# テストの実行
unittest.main()
# ファイルを直接実行すると、この1行でテストを全部探して実行
# test_ で始まるメソッドが順番に呼ばれる
# 戻り値がすべて正しければ OK、失敗すると FAIL が出る

# テスト実行後の出力について
# ドット . は 1テスト成功 の印（test_の関数1つで1テスト）
# 今回は 3つのtest_関数 → ... と表示
# エラーなしなので OK
