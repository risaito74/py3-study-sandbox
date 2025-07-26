# 10章 標準ライブラリ：sysモジュール
# ※ターミナルから下記のようにコマンドを直接入力して実行する前提のコードです
# > python c10_library_sys.py (name) (age)
# （例）
# > python c10_library_sys.py スノハラ 28

import sys

# コマンドライン引数を確認
# argv[0] にスクリプト名が入り、argv[1]以降がコマンドライン引数になる
print("sys.argv:", sys.argv)

# コマンドライン引数が3つ未満の時はメッセージを出して異常終了
if len(sys.argv) < 3:
    print("使い方: python script.py 名前 年齢")

    # sys.exit(1) は異常終了を示す（0なら正常終了、それ以外は異常終了）
    sys.exit(1)

# コマンドライン引数を参照して変数に代入
name = sys.argv[1]
age = sys.argv[2]
print(f"こんにちは、{name}さん。{age}歳ですね！")
