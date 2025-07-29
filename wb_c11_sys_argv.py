# 問題集11章：コマンドライン引数（sys.argv）
# ----- 問題3. -----

# 例）ターミナルで以下のように手打ちで実行する
# > python wb_c11_sys_argv.py 1 2
# 上記の場合 1 が第一引数 2 が第二引数になる

import sys

# sysモジュールのargv属性でコマンドライン引数をリストで取得する
print(sys.argv)
# 出力例：['wb_c11_sys_argv.py', '1', '2']

# コマンドライン引数の要素数を取得
argv_len = len(sys.argv)
print("argv_len:", argv_len)

# コマンドライン引数の数だけ、引数の値を表示
for arg in range(1, argv_len):
    print(f"sys.argv[{arg}]: {type(sys.argv[arg])} {sys.argv[arg]}")
    # コマンドライン引数の型は：<class 'str'>
