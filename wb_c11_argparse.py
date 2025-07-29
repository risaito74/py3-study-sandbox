# 問題集11章：argparseモジュール
# ----- 問題4. -----

# 問題文の実行コマンド（※ファイル名は wb_c11_argparse.py に変える）
# > python parse.py --head=1 2 3

import argparse

# parser の作成：パーサ（構文解釈器）のオブジェクトを作成
parse = argparse.ArgumentParser()

# 引数 head の情報を追加
# 「-」「--」はオプション引数（指定しなくても良い引数）
# ハイフン1つは1文字の省略形、ハイフン2つは非省略系の引数（どちらを使ってもよい）
# なお「-h」はヘルプ(--help)で予約されているため衝突してエラーが出る。その回避策として「-H」としている
parse.add_argument("-H", "--head")

# 引数 body の情報を追加
# nargs="+"で1個以上の任意の引数を指定（リストになる）
parse.add_argument("body", nargs="+")

# 引数の情報を取得
args = parse.parse_args()

print(args)
# 出力：Namespace(head='1', body=['2', '3'])
