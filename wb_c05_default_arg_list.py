# 問題集5章：引数のデフォルト値がリストの場合の挙動（実務では避けるべき by 問題集）
# ----- 問題6. -----

def function(number, default_arg_list=[]): 
    default_arg_list.append(number)
    return default_arg_list

# default_arg_listの実引数なし　→　デフォルト値を使う
# デフォルト値[] → [1]
print(function(1))

# 実引数あり[3, 4] → [3, 4, 2]
# デフォルト値は変化しない
print(function(2, [3, 4]))

# default_arg_listの実引数なし　→　デフォルト値を使う
# デフォルト値[1] → [1, 3]
print(function(3))

# 実引数あり[5, 6] → [5, 6, 4]
# デフォルト値は変化しない
print(function(4, [5, 6]))

# default_arg_listの実引数なし　→　デフォルト値を使う
# デフォルト[1, 3] → [1, 3, 5]
print(function(5))

# 重要：引数のデフォルト値をリストにすると、その引数に値が加えられるたびにデフォルト値も変更される（前回の変化が残っている）

# デフォルト引数のリストは1回だけ作られて関数に残る
# 実引数が来た場合はそのリストが使われるので共有されない
