# 問題集6章 問9.
# 辞書(dictionary) と in演算子

dic = {"name": "ことね", "age": 15, "hometown":"埼玉県"}

# 値 in ディクショナリ：キーの存在を確認
print("name" in dic)
# 出力：True
print("ことね" in dic)
# 出力：False

# keys()メソッド：辞書のすべてのキーを取り出す
print(dic.keys())
# 出力：dict_keys(['name', 'age', 'hometown'])
print("name" in dic.keys())
# 出力：True

# 辞書をlist()でリスト化するとキーのリストが生成される
print(list(dic))
# 出力：['name', 'age', 'hometown']
print("name" in list(dic))
# 出力：True

# おまけ
# value()メソッド：辞書のすべてのバリューを取り出す
print(dic.values())
# 出力：dict_values(['ことね', 15, '埼玉県'])
print("ことね" in dic.values())
# 出力：True
