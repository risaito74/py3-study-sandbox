# doctest
# テストを加えたい関数のdocstringにPython対話モードの形式で関数の呼び出しと期待される出力値を記述し、
# doctest.testmod()で実行する。

import doctest

def add(a, b):
    """
    >>> add(1, 2)
    3
    >>> add(2, 3)
    5
    """
    return a + b

# メインモジュールとして実行されている時にtestmod()を実行
if __name__ == '__main__':
    # デフォルトでは、エラーがない場合は何も出力されない
    # 常に出力したい場合「verbose=True」を引数で渡す
    doctest.testmod(verbose=True)
