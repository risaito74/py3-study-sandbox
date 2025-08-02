# 問題集13章：問題35
# コマンドライン引数：argparseモジュール
# argparseモジュールは、プログラム実行時にコマンドラインで引数を受け取る処理を簡単に実装できる標準ライブラリ
# sys.argv より応用的なことができる

# コマンドライン入力例：python wb_c13_argparse.py a i1 i2 --arg2=100 -a=aaa

import argparse

# まずパーサを作る
parser = argparse.ArgumentParser(description="このプログラムの説明（なくてもよい）")

# parser.add_argumentで受け取る引数を追加していく
parser.add_argument("arg1")

# 複数個（不定）受け取りたい
# nargs="+" は引数を1個以上受け取る（リストで受け取る）
# なお nargs="*" の場合は0個以上受け取るオプション引数となる
# さらに nargs="+"/nargs="*" は位置引数の最後に置かないと、後ろの位置引数の分まで全部拾ってしまうため、挙動がおかしくなる（エラーになる）
parser.add_argument("items", nargs="+")

# オプション引数（指定しなくても良い引数）を追加
# コマンドライン入力時は「--arg2 b」「--arg2=b」のようにキーワードをつける
parser.add_argument("--arg2")

# よく使う引数なら1文字の省略形を設定することもできる
# 【注意】：省略形「-h」はヘルプで予約されているので使えない、使うとエラーになる
parser.add_argument('-a', '--arg3')

# 引数を解析
args = parser.parse_args()

print(args)
# 出力例：Namespace(arg1='a', items=['i1', 'i2'], arg2='100', arg3='aaa')

print("arg1:", args.arg1)

# nargs="+" で指定した items を表示
print("items:", args.items)
# 出力例：['i1', 'i2']

print("arg2:", args.arg2)
# コマンドライン引数が無かった場合：None

print("arg3:", args.arg3)
# コマンドライン引数が無かった場合：None
