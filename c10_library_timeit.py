# 10章 標準ライブラリ：timeitモジュール
# timeit モジュールは、小さなコードの計測に適している
# timeit が微細な粒度レベルを見るのに対し、より大きなコードブロックの計測には profile / pstats モジュールを使う

# timeit モジュールの Timer クラスをインポート
from timeit import Timer

# Timer()の中に計測したい小さい処理を書く
t = Timer("x = sum(range(300))")

# 処理が何秒かかったか取得する（デフォルトは100万回）（単位は秒）
# 本当に100万回？とChatGPTと議論になったのでエビデンス：https://github.com/python/cpython/blob/main/Lib/timeit.py
print("式そのまま:", t.timeit())

# 関数で同じ処理をした時の処理時間比較
def sum_range(n):
    return sum(range(n))

# 関数を参照する場合は、globalsを設定する
t = Timer("sum_range(300)", globals=globals())
print("関数化　　:", t.timeit())

# 処理回数を1万回にして1回あたりの処理時間を求める
t = Timer("x = sum(range(300))")
count = 10000
pt = t.timeit(number=count)
print("回数1万回　:", pt)
print("回数1回平均:", pt/count)
