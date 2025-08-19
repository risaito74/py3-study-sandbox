# 問題集13章：問題38
# textwrapモジュール
# 文字列を任意の文字数で折り返し（改行）、切り詰め（省略）して整形するには、標準ライブラリのtextwrapモジュールを使う
# なお、文字列ではなくリストや辞書を整形して出力するにはpprintモジュールが便利

import textwrap
import pprint

# 内包表記でテキストのリストを作成
text = [f"{i} sheep jumped a fence." for i in range(1, 4)]

# リストをそのまま出力
print(text)
# ['1 sheep jumped a fence.', '2 sheep jumped a fence.', '3 sheep jumped a fence.']

# リストを", "でジョインしてfill()で改行位置を整形
# width=24：改行は24文字に収まるように単語の区切りで行われる
print(textwrap.fill(", ".join(text), width=24))
# 1 sheep jumped a fence.,
# 2 sheep jumped a fence.,
# 3 sheep jumped a fence.

# 改行を40文字以内にした場合
print(textwrap.fill(", ".join(text), width=40))
# 1 sheep jumped a fence., 2 sheep jumped
# a fence., 3 sheep jumped a fence.

# ", ".join(text) だけを出力
print(", ".join(text))
# 1 sheep jumped a fence., 2 sheep jumped a fence., 3 sheep jumped a fence.

# pprintの場合
# リストの要素ごとに整形して出力してくれる
pprint.pprint(text)
# ['1 sheep jumped a fence.',
#  '2 sheep jumped a fence.',
#  '3 sheep jumped a fence.']

# 辞書のpprint()
dic = {"name": "Kotone Fujita", "age": 15, "from": "Saitama", "three_sizes": [75, 55, 75]}
pprint.pprint(dic)
# {'age': 15,
#  'from': 'Saitama',
#  'name': 'Kotone Fujita',
#  'three_sizes': [75, 55, 75]}
# 自動的にキーのソートがされてしまう

# キーのソートをしないで出力
pprint.pprint(dic, sort_dicts=False)
# {'name': 'Kotone Fujita',
#  'age': 15,
#  'from': 'Saitama',
#  'three_sizes': [75, 55, 75]}
