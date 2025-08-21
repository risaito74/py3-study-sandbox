# PyQ模擬試験
# 22. 次のコードを実⾏して期待する結果が表⽰されるとき、空欄①に⼊る記述として正しいものを選択してください（1つ選択）

# 期待する結果
# (0, 'carrot')
# (1, 'potato')
# (2, 'tomato')

vegetables = {0: "carrot", 1: "potato", 2: "tomato"}

# 選択肢A
# kv にはキーが渡される
for kv in vegetables:
    print(kv)
# 0
# 1
# 2

# 選択肢B
# kv にはキーだけのタプルが渡される
for kv in zip(vegetables):
    print(kv)
# (0,)
# (1,)
# (2,)

# 選択肢C
# kv にはキーと値のペアのタプルが渡される
for kv in vegetables.items():
    print(kv)
# (0, 'carrot')
# (1, 'potato')
# (2, 'tomato')

# 選択肢D
# enumerate()はイテラブルオブジェクトの要素と同時にインデックス番号を取得できる
# kv にはインデックス番号とキーのペアのタプルが渡される
for kv in enumerate(vegetables):
    print(kv)
# (0, 0)
# (1, 1)
# (2, 2)
