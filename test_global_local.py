# グローバルスコープとローカルスコープのテスト

# グローバル変数
my_name = "？？？"
lover_name = "藤田ことね"

# --------------------------------------------------
# globalを使ったテスト
# --------------------------------------------------

# グローバル変数を関数内で参照
def get_lover_name(flag):
    # ローカル変数 ret_name を用意してグローバル変数を代入
    ret_name = lover_name
    if flag == "1":
        # 条件でローカル変数を上書き
        ret_name = "チノ"
    # flag が "0", "1" 以外の時（Yes/No以外の時）
    elif flag not in ["0", "1"]:
        ret_name = "？？？"

    return ret_name

# 関数内でグローバル変数を直接上書きするテスト
def set_my_name(name):
    global my_name
    my_name = name

print("\n=== globalテスト ===")
flag = input("グローバル変数を上書きする？(Yes=1/No=0):")

lover_name = get_lover_name(flag)

# 関数内でグローバル変数 my_name を上書き
set_my_name("スノハラ")

print(f"{my_name}の恋人の名前は{lover_name}です")

# --------------------------------------------------
# nonlocalを使ったテスト
# --------------------------------------------------
print("\n=== nonlocalテスト ===")

def love_story():
    lover = "藤田ことね"  # 外側のローカル変数

    def change_lover():
        nonlocal lover  # 1つ外の変数を操作する宣言
        lover = "チノ"   # 外側のloverを書き換え

    print("変更前:", lover)  # → 藤田ことね
    change_lover()
    print("変更後:", lover)  # → チノ

love_story()
