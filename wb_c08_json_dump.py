# 問題集8章：ファイル入出力
# ----- 問題6. -----
# 問題：次のコードを実行してファイルにJSON形式で出力する、誤っているものを選択

import json

file_path = "./tmp/"

data = [{"id": 1}, {"id": 2}]
print("dataの型:",type(data))

# 選択肢A
try:
    fp = open(file_path + "sample1.json", "w")
    # Pythonオブジェクト（ここではリスト）をJSONファイルとして保存する
    json.dump(data, fp)
    fp.close()
except Exception as e:
    print("例外：", type(e), e)
# これは正しくJSON形式で出力される：正しい

# 選択肢B
try:
    fp = open(file_path + "sample2.json", "w")
    # dumps() はJSON形式の文字列を返す関数であり、直接ファイルに書き込むものではない
    # 第2引数（fp）を渡すと、定義にない位置引数として扱われて例外が発生する
    json.dumps(data, fp)
    fp.close()
except Exception as e:
    print("例外：", type(e), e)
# 例外： <class 'TypeError'> dumps() takes 1 positional argument but 2 were given
# 位置引数を1個しか受け取らないのに、2個渡された → dumps()関数定義では位置引数は1つのみ、あとはキーワード引数になっているため
# これはJSONで出力されない：誤り（これを選択する）

# 選択肢C
try:
    fp = open(file_path + "sample3.json", "w")
    # Pythonオブジェクト（ここではリスト）をJSONファイルとして保存する
    # 第1引数 obj, 第2引数 fp をキーワード引数として渡す（キーワード引数なので順不同で問題ない）
    json.dump(fp=fp, obj=data)
    fp.close()
except Exception as e:
    print("例外：", type(e), e)
# これは正しくJSON形式で出力される：正しい

# 選択肢D
try:
    fp = open(file_path + "sample4.json", "w")
    # dumps()はJSON形式の文字列を返す
    # このJSON形式の返り値（文字列）をファイルに書き込むことで、結果的に dump() を使ったときと同じ内容がファイルに保存される
    fp.write(json.dumps(data)) 
    fp.close()
except Exception as e:
    print("例外：", type(e), e)
# これは正しくJSON形式で出力される：正しい
