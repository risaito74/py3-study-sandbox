# 問題集13章：問題35
# コマンドライン引数：sysモジュール
# コマンドライン引数は sys モジュールの argv 属性にリストとして格納されている

import sys

print(sys.argv)
# コマンドライン：python wb_c13_argv.py 1 2 aa
# この場合の出力：['wb_c13_argv.py', '1', '2', 'aa']

# sys.argv の型を確認
print(type(sys.argv))
# 出力：<class 'list'>
