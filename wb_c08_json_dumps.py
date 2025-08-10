# 問題集8章：ファイル入出力
# 問題6：JSON と dumps()

import json

# JSONに変換する辞書データを用意
dic = {"key1": 10, "key2": 20}

# dumps()：JSON形式の文字列データに変換
js = json.dumps(dic)

print(type(js))
# 出力：<class 'str'>
print(js)
# 出力：{"key1": 10, "key2": 20}

# キーの無いリストもJSONになる
li = [x for x in range(10)] # 0~9のリスト
js = json.dumps(li)
print(js)
# 出力：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 単一の文字列もJSONになる
js = json.dumps("a")
print(js)
# 出力："a"

# 単一の数値もJSONになる
js = json.dumps(8)
print(js)
# 出力：8

### dump() と load() 
# JSONに変換してファイル書き込み、JSONをファイルから読んでオブジェクトに変換
file_path = "./tmp/sample5.json"

# 書き込み用でファイルオープン
with open(file_path, "w") as fp:
    # dump()で辞書をJSONに変換したものをファイルに書きこむ
    json.dump(dic, fp)

# 読み込み用でファイルオープン
with open(file_path, "r") as fp:
    # load()：ファイルからJSONを読み込んでオブジェクトに戻す
    obj = json.load(fp)

print(type(obj), obj)
# 出力：<class 'dict'> {'key1': 10, 'key2': 20}
