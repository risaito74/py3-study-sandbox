# 7章 入出力：jsonモジュール

import json

# Pythonの辞書を用意
data = {"name": "スノハラ", "age": 30, "is_gal": False}

# 辞書 → JSON文字列に変換する（dumps = dump + string）
# ※ dumps() は JSON形式の文字列を返す
json_str = json.dumps(data)
print(json_str)
# 出力: {"name": "\u30b9\u30ce\u30cf\u30e9", "age": 30, "is_gal": false}

# デフォルトでは全角文字などの非ASCII文字がUnicodeエスケープされて出力される
# 引数ensure_asciiをFalseとすると、Unicodeエスケープされずそのまま出力される
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
# 出力: {"name": "スノハラ", "age": 30, "is_gal": false}

# dumps()は文字列型を返す
print(type(json_str))
# 出力: <class 'str'>

# JSON文字列 → 辞書に変換する（load + string）
new_data = json.loads(json_str)
print(new_data)
# 出力： {'name': 'スノハラ', 'age': 30, 'is_gal': False}

# loads()は辞書型を返す
print(type(new_data))
# 出力: <class 'dict'>

# 辞書 → JSONファイルへ保存
try:
    # mode="w"：ファイルが存在しない場合は新規作成、存在する場合は上書き保存される
    # encoding="utf-8"：日本語を含むデータの文字化け防止のためにUTF-8で保存する
    with open("./tmp/data.json", "w", encoding="utf-8") as f:
        # ensure_ascii=False：日本語などの非ASCII文字をUnicodeエスケープ（\uXXXX形式）せず、そのまま出力する
        # 指定しない場合は日本語などの非ASCII文字が \uXXXX の形式でUnicodeエスケープされる
        json.dump(data, f, ensure_ascii=False)
    # ここまで来たら正常終了なので、メッセージを出す
    print("＊ファイル保存が正常終了")
except Exception as e:
    print("例外：", type(e), e)

# JSONファイル → 辞書へ読み込み
try:
    # encoding="utf-8"：日本語を含むデータの文字化け防止のためにUTF-8を明示する
    with open("./tmp/data.json", "r", encoding="utf-8") as f:
        load_data = json.load(f)
    # 読み込みが正常終了
    print("＊ファイル読み込みが正常終了")
except Exception as e:
    print("例外：", type(e), e)

# JSONファイルから読み込んだ辞書データを表示
print("load()で読み込んだデータ:", load_data)
