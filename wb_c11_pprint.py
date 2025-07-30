# 問題集11章：pprintモジュール
# ----- 問題13. -----
# pprint = pretty print（きれいに整形して表示）
# 標準の print() だと1行で長くなる辞書やリストを見やすくしてくれる

import pprint

lines = [f"sample test string {i:04}" for i in range(3)]

# まず普通にprint
print(lines)

# 次にpprint
pprint.pprint(lines)
# 要素ごとに改行かつインデントをして見やすく整形してくれる（かわいい！）

# pprint()の引数 indent width について
# indent = 1 : ネストされた要素を改行したときに付く空白の幅（半角スペースn文字）デフォルトは1
# width = 80 : 何文字を超えたら改行するかの目安。デフォルトは80文字

data = [
    {'name': 'スノハラ', 'scores': [95, 88, 92, 100, 99]},
    {'name': 'チノ', 'scores': [100, 99, 98, 97, 96]},
    {'name': 'まゆ', 'scores': [80, 85, 82, 84, 88]},
]

print("デフォルト")
pprint.pprint(data)

print("indent=1")
pprint.pprint(data, indent=1, width=40)  # widthを狭くして強制改行

print("indent=2")
pprint.pprint(data, indent=2, width=40)

# pprint()が効かないパターン
li2 = [f"str{i:03}" for i in range(3)]
# デフォルトwitdh=80未満だから整形されない
print(len(repr(li2))) # 30文字
pprint.pprint(li2)
# 出力：['str000', 'str001', 'str002']
