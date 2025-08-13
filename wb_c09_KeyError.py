# 問題集9章：例外処理
# 問題 2.
# KeyError になるケース

# KeyErrorは基本的に辞書で参照しようとしたキーが存在しない時に送出される

dic = {"name": "Kotone", "age": 15, "from": "Saitama"}

try:
    print(dic["bustsize"])
except Exception as e:
    print("＊例外：", type(e), e)
    print(type(e).__name__) # エラー名だけを取得する場合
# ＊例外： <class 'KeyError'> 'bustsize'
# KeyError

# 他に、集合でremove()で削除しようとしたデータがない場合にも送出される
# discard()ならエラーにならない

name_set = {"Saki", "Temari", "Kotone", "Ume"}

print(type(name_set), name_set)

# 存在するデータを削除：エラー起きない
try:
    name_set.remove("Saki")
    print(name_set)
except Exception as e:
    print("＊例外：", type(e), e)
# {'Temari', 'Ume', 'Kotone'}

# remove()で存在しないデータを削除：KeyError
try:
    name_set.remove("Sumika")
    print(name_set)
except Exception as e:
    print("＊例外：", type(e), e)
# ＊例外： <class 'KeyError'> 'Sumika'

# discard()で存在しないデータを削除：エラー起きない
try:
    name_set.discard("Sumika")
    print(name_set)
except Exception as e:
    print("＊例外：", type(e), e)
# {'Kotone', 'Temari', 'Ume'}

# pop()は要素を削除し、その値を返す。どの要素を削除するかは選択できない
# 空集合だとKeyError
try:
    s = set()
    s.pop()
except Exception as e:
    print("＊例外：", type(e), e)
# ＊例外： <class 'KeyError'> 'pop from an empty set'
