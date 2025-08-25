# CSVモジュールのテスト

import csv

# テスト用に作った都道府県データ
filepath = "./tmp/csv_tdfk.csv"

# CSVファイルを開き、全件取得して表示
# 日本語（マルチバイト）がある場合、「UnicodeDecodeError」になるため encoding="utf-8" を指定する
with open(filepath, encoding="utf-8") as f:
    fr = f.read()
    print(type(fr))
    # 出力：<class 'str'>
    print(fr)
    # 全件の出力

# イテレーターを取得してforで回しながら1件ずつ取得して表示
with open(filepath, encoding="utf-8") as f:
    # イテレーターを取得
    reader = csv.reader(f)
    for row in reader:
        # row はリストで渡される
        # 県以外の都道府県を検知したら印も出力（1件単位の取得だとこういうことができるよ、の例）
        p_name = row[1]
        if "県" in p_name:
            print(row)
        else:
            print(row, "*** 県以外 ***")
