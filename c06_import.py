# 6章モジュール：import
# モジュールとは？：.pyで書かれたファイルのこと。 
# モジュールの全体を利用するのがimportで、 モジュールの一部(変数や関数)を利用するのがfrom

# fiboモジュール（fibo.py）をインポート
import fibo

# モジュール内の関数は「モジュール名.関数名」で使う
fibo.fib(100)

# モジュール名の確認
print("モジュール名:", fibo.__name__)

# ----- from ~ import ~ 構文 -----
# モジュール(.py)から任意の名前（変数、関数）を指定して直接取り込む（モジュール名は取り込まない）

from gakumasu_member import get_name, get_weight

# 関数名を直接インポートしたので、モジュール名はいらない
print(f"{get_name(1)}の体重: {get_weight(1)}kg")

# ----- import ~ as ~ 構文 -----
# モジュール名の後に as がある場合、as に続く名前がモジュール名の省略名になる
import hoge as h

# hogeモジュールの関数hoge()を呼び出す
print(h.hoge())

# ----- from ~ import ~ as ~ の場合 -----
# この場合、モジュール名は取り込まず、名前（変数、関数）を直接取り込んでいるので、その取り込んだ名前がas以降の省略名になる
from hoge2 import hoge2 as h2

#関数hoge2()を省略名h2()で呼び出す
print(h2())

# dir()関数
# モジュールが定義している名前を文字列リストで返す
print(dir(fibo))
