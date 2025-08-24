# PyQ模擬試験
# 37. 標準ライブラリの説明として誤っているものを選択してください（1つ選択）

# A. csvモジュールは、スプレッドシートなどで使⽤されているCSV形式のファイルを読み書きできる
# B. emailパッケージは、電⼦メールのデコードやヘッダプロトコルの処理などメッセージの構築ができる
# C. jsonパッケージは、JSON形式のデータを安定的にパースできる
# D. sqlite1モジュールは、SQLを⽤いてSQLiteデータベースを更新できる　→ 誤り！！！（正しくは「sqlite3モジュール」）

# で、このうちのsqlite3モジュールを触ってみようってわけ（急にフランク

import sqlite3

# メモリ上にデータベース作成（ファイルじゃなく一時的に使える）
conn = sqlite3.connect(":memory:")

# データベース カーソルを作成
# データベースカーソルとは？：データベース内のデータを操作するために使用されるオブジェクト
cur = conn.cursor()

# まず、前提知識として...
# cur.execute()
# これは中にSQL文をいれて「このSQL文を実行してね！」というやつ

# usersテーブルを作成
# 列：id, name
# id INTEGER PRIMARY KEY：idを整数型として扱い、自動採番の主キーにしたい場合の定型の書き方
# 主キーとは？：重複しないユニークなデータで、かつ、NULLはNGで必ず何らかの値が入るもの（データをユニークにするため、実用上はカラムのどれかを主キーに設定した方が良い）
# name TEXT：nameを文字列型とする
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)")

# データ挿入
# usersテーブルのnameカラムに「スノハラ」を設定したデータを挿入する
# この時、idは自動採番されるから設定不要
cur.execute("INSERT INTO users (name) VALUES (?)", ("スノハラ",))
cur.execute("INSERT INTO users (name) VALUES (?)", ("チノ",))

# データ取得
# usersテーブルからデータを全件取得する
cur.execute("SELECT * FROM users")
# 今データベースカーソルに残ってるデータを全部まとめてリストで受け取る（大量データの取得には向かない）
# 1件ごとのタプルセットのリストで返される
print(cur.fetchall())  
# 出力：[(1, 'スノハラ'), (2, 'チノ')]

# データ取得（curをイテレーターとしてforで1件ずつ取得）
cur.execute("SELECT * FROM users")
for row in cur:
    print(row)
# (1, 'スノハラ')
# (2, 'チノ')

conn.close()
