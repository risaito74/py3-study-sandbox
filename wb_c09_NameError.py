# 問題集9章：例外処理
# 問題 2.
# NameError になるケース

# NameError（未定義名エラー）
# 変数・関数・モジュールなどの名前が定義されていないときに発生する

### 変数 x が未定義
try:
    print(x)
except Exception as e:
    print("  ＊例外：", type(e),  e)
# ＊例外： <class 'NameError'> name 'x' is not defined

### 関数名のタイポ → 関数が未定義
try:
    purint("Hello！")
except Exception as e:
    print("  ＊例外：", type(e),  e)
# ＊例外： <class 'NameError'> name 'purint' is not defined

### スコープ外での変数使用
def say_hello():
    # ローカル変数を定義
    message = "Hello!"

try:
    print(message)
except Exception as e:
    print("  ＊例外：", type(e),  e)
# ＊例外： <class 'NameError'> name 'message' is not defined

### インポートされていないモジュールや関数の使用
try:
    print(random.randint(1,6))
except Exception as e:
    print("  ＊例外：", type(e),  e)
# ＊例外： <class 'NameError'> name 'random' is not defined

### 関数定義より前に呼び出し
try:
    say_pardon()
except Exception as e:
    print("  ＊例外：", type(e),  e)

def say_pardon():
    print("pardon?")
# ＊例外： <class 'NameError'> name 'say_pardon' is not defined
