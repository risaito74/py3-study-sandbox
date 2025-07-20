# 5章データ構造：ディクショナリ
# 中カッコ{}で囲った「キー:値」ペア（エントリ）の集合（キーは重複不可、値は重複OK）

dict = {"名前": "藤田ことね", "年齢": 15, "趣味": "お金を稼ぐこと"}
print(f"辞書の初期値: {dict}")

# キー指定で値を引き出す
print(f"名前は: {dict["名前"]}")
print(f"年齢は: {dict.get("年齢")}") # get()メソッドでも引き出せる

# 「キー:値」ペアの追加
dict["出身地"] = "埼玉県"
print(f"辞書に出身地を追加: {dict}")

# キー指定で値の変更
dict["名前"] = "ことねちゃん"
print(f"辞書の名前を変更: {dict}")

# forループで辞書のkeyをすべて引き出す
for key in dict:
    print(f"辞書のキーを列挙: {key}")

# forループで辞書の値をすべて引き出す
for val in dict.values():
    print(f"辞書の値を列挙: {val}")

# items()メソッドを使えば、keyとvalueをセットで引き出せる
for key, val in dict.items():
    print(f"キー'{key}'の値: {val}")

# あるキーが辞書に存在するかチェックしたい時はinを使う
if "趣味" in dict:
    print("辞書にキー'趣味'はある")

# 「キー:値」ペアの削除
del dict["趣味"]
dict.pop("年齢") # pop()メソッドでも削除できる（指定キーを削除＆値を戻り値で返す）
print(f"削除後の辞書: {dict}")
