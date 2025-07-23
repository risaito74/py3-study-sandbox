# 9章クラス：globalとnonlocal

# ----- まず、グローバルスコープとローカルスコープについての確認 -----
print("----- test.1: グローバルスコープとローカルスコープ -----")

def scope_test():
    def do_local():
        # ローカルスコープのspamなので、スコープ（有効範囲）はこの関数内のみ
        spam = "local spam"
        print("do_local()内のspam:",spam)
    
    # このスコープでspamに値を代入（グローバルスコープには影響しない）
    # このspamはscope_test()関数のローカルスコープのもの、グローバルスコープには何も影響しない
    spam = "test spam"
    do_local()
    # do_local()内での変更はこのスコープに影響しない（例外：nonlocal文）
    print("scope_test()内のspam:", spam)

# グローバルスコープでspamに値を代入
spam = "global spam"
scope_test()
# scope_test()内での変更はグローバルスコープに影響しない（例外：global文）
print("グローバルスコープのspam:", spam)

# ----- 次に、global文を使った例 -----
print("----- test.2: global文を使った例 -----")

# ローカルスコープ内でグローバルスコープの変数を使えるようにするのがglobal文
def local_scope_test():
    # global文でspamがグローバルスコープにあることを指定
    global spam
    # なので、グローバルスコープの変数spamに"local spam"を代入している
    spam = "local spam"

# グローバルスコープでspamに値を代入
spam = "global spam"
local_scope_test()
# local_scope_test()内において、global文でspamをグローバルスコープと指定したので、この関数内での変更が反映される
print("グローバルスコープのspam:", spam)

# ----- そして、nonlocal文が登場 -----
print("----- test.3: nonlocal文を使った例 -----")

# nonlocal文とは、def内のdefなどの入れ子構造において
# グローバル・ローカルの関係に対して中間スコープ（外関数のローカル変数）の変数として扱えるようにするもの
def nonlocal_scope_test():
    def local_scope_test():
        # nonlocal文でspamが外関数のスコープ、つまりnonlocal_scope_test()のスコープにあることを指定
        nonlocal spam
        spam = "local spam"
    
    spam = "nonlocal spam"
    local_scope_test()
    # local_scope_test()内において、nonlocal文でspamをこのスコープと指定したので、関数内での変更が反映される
    print("nonlocal_scope_test()内のspam:", spam)

# グローバルスコープでspamに値を代入
spam = "global spam"
nonlocal_scope_test()
# nonlocal_scope_test()内での変更はグローバルスコープに影響しない
print("グローバルスコープのspam:", spam)

# ----- 罠！入れ子の最内スコープでglobal文を使った時の中間スコープのふるまい -----
print("----- test.4: 入れ子の最内スコープでglobal文を使った時の中間スコープのふるまい -----")

# 最内スコープでglobal指定した変数は、中間スコープに影響しない！

def nest_out_scope():
    def nest_in_scope():
        global spam
        spam = "nest in spam"
    
    spam = "nest out spam"
    nest_in_scope()
    # nest_in_scope()内でglobal文で指定したspamは、このスコープには影響しない
    print("nest_out_scope()内のspam:", spam)

spam = "glabal spam"
nest_out_scope()
# nest_in_scope()内でglobal文で指定したspamの変更が反映される
print("グローバルスコープのspam:", spam)
