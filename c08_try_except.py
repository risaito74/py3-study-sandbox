# 8章エラーと例外：try文

# 例外処理の基本（ValueError）
# try節の実行中に例外が発生すると、try節中の残りはスキップされる
# 発生した例外の型がexceptキーワードの後ろで指定した例外と一致すれば、except節が実行される
# そしてtry文の後のプログラム実行がそのまま続けられる（whileループが続く）
while True:
    try:
        x = int(input("数字を入力してください： "))
        break
    except ValueError:
        print("これは有効な数字ではありません。もう一度入力してください")

print(f"入力値は {x} でした。")

# except に複数の例外を指定することもできる
# その場合、タプルを使う
try:
    print(hoge + guga)
except (NameError, ValueError):
    print("＊例外：名前エラーか値エラーです")

# except 例外の指定 の後に as を使うと発生した例外オブジェクトを受け取れる
try:
    print(hoge + guga)
except (NameError, ValueError) as e:
    print(f"＊例外：発生した例外は {type(e).__name__} です : type(e) = {type(e)}, e = {e}")

# try文に複数のexcept節を入れることができる
# 最初にマッチしたexcept節が走る（並びによって走るexcept節が変わることがある）
try:
    print(hoge + guga)
except NameError:
    print("＊例外：発生した例外は名前エラーです")
except ValueError:
    print("＊例外：発生した例外は値エラーです")

# 最後に置いたexcept節は、例外を省略することでワイルドカード（全部）にすることができる
# ただし、見つけにくくなるため実務上の使用は注意（エラーメッセージを表示すべき）
try:
    print(hoge + guga)
except ValueError:
    print("＊例外：発生した例外は値エラーです")
except: # ワイルドカード
    color_red = "\033[31m"
    color_clear = "\033[0m"
    print(f"{color_red}＊例外：予期せぬエラーです{color_clear}")

# else節：try...except文には、オプションでelse節が入れられる
# 位置はすべてのexcepr節より後ろでなければならない
# else節はtry節が例外を送出しなかった時にのみ実行される
try:
    x = 10
except ValueError:
    print("＊例外：発生した例外は値エラーです")
except: # ワイルドカード
    print("＊例外：予期せぬエラーです")
else:
    print("else節：例外を送出しませんでした。")

# raise文：例外の送出
# 指定の例外を強制的に発生させられる（デバッグ用というより、バリデーションとして本番処理で使うもの）
try:
    age = -999
    if not (age >= 0 and age <= 130):
        raise ValueError(f"年齢が正常値の範囲外です: {age}歳")
except ValueError as e:
    # ValueError()の引数がeで渡される
    print(f"＊例外：{e}")

# finally節：クリーンアップ動作の定義。すべての状況で必ず実行される
# finally節はtry文が完了する前の最後のタスクとして実行される
# finally節はtry文が例外を発生しようがしまいが実行される
try:
    print(hoge)
except NameError:
    print("＊例外：名前エラーです")
finally:
    print("finally節実行中")

# 正常終了の場合：else節→finally節
try:
    x = 10
except:
    pass
else:
    print("else節実行中")
finally:
    print("finally節実行中")
