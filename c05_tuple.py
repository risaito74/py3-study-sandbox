# 5章データ構造：タプルとシーケンス
# 【ポイント】タプルは不変体(immutable)
tp = (1, 2, 3)
print(f"用意したタプルtp: {tp}")

# タプルは要素の変更、追加、削除はできない（エラーになる）
#tp[0] = 0
#tp.append(4)
#tp.pop()
#del tp[0]

# ただし、タプル自体の削除はできる
tp_tmp = (9, 8, 7)
del tp_tmp

# タプルをリストに変更（普通にできる）
li = list(tp)
print(f"タプルtpをリストに変換したli: {li}")

# タプル・パッキング（タプル梱包）：コンマがあればタプルと解釈される
tp_packing = 10, 20, 30
print(f"タプル・パッキングしたtp_packing: {tp_packing} ＊クラスは{type(tp_packing)}")

# シーケンス・アンパッキング（開梱）
x, y, z = tp_packing
print(f"タプルtp_packingをシーケンス・アンパッキングした x={x}, y={y}, z={z}")

# 要素数0のタプル、要素数1のタプル
tp0 = ()        #()があるからタプルと解釈される
tp1 = "hoge",   # 後ろにカンマ付けるとタプルと解釈される
print(f"tp0の要素数: {len(tp0)}, tp1の要素数: {len(tp1)}")

# タプルの内包表記：
# () 内包表記はタプルではなくジェネレータ式として書かれ、評価時にジェネレータオブジェクトを生成するため、tuple() でタプルに変換
tp_c = tuple(x for x in range(10))
print(f"内包表記で生成したタプル: {tp_c}")

