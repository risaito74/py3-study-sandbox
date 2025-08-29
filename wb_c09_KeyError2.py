# 問題集9章：例外処理
# 問題 2. KeyError になるケース
# いや、3周目で正解はしたけど「あれ？KeyErrorなんてあったっけ？？」とド忘れしてたから、もう一回...ね？💋

# 辞書の作成
dic = {"name": "Kotone", "age": 15, "hometown": "Saitama"}
# 要素の追加
dic["three_sizes"] = (75, 55, 75)

print(dic)

# 存在しないキーを参照：KeyError
try:
    print(dic["bust"])
except Exception as e:
    print("例外：", type(e), e)
# 例外： <class 'KeyError'> 'bust'

# 存在しないキーを参照：KeyError
# いやらしい例：dic["Kotone"]なので、そんなキーは存在しないから、KeyError
try:
    name = "Kotone"
    print(dic[name])
except Exception as e:
    print("例外：", type(e), e)
# 例外： <class 'KeyError'> 'Kotone'

# 未定義：NameError
# キー"age"を指定したつもりでクォート""を忘れると変数ageの参照となり、未定義だから、NameError
try:
    print(dic[age])
except Exception as e:
    print("例外：", type(e), e)
# 例外： <class 'NameError'> name 'age' is not defined
