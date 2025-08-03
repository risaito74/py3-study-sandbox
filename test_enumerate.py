# enumerate()のテスト
# forループの中でリストやタプルなどのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる
# インデックスは任意の値から開始可能

words = ["ホタテ", "シジミ", "イカ"]
names = ["亜鳥先輩", "るー先輩", "誰？？"]

# リスト words とインデックス番号を同時に取得する
# 第二引数：インデックス番号は1から始める（取得するリストには影響しない）
for i, word in enumerate(words, 1):
    print(f"{i}位 {word}先輩")
# 1位 ホタテ先輩
# 2位 シジミ先輩
# 3位 イカ先輩

# zip() と組み合わせる
# zip() で取得する変数はタプルとして()内に記載する
for i, (word, name) in enumerate(zip(words, names), 1):
    print(f"{i}位 {word}先輩 is {name}")

# itertools モジュールの count() を使う手もある
import itertools

# こうすると()使わずに書ける（が、importする手間を考えるとどっこいどっこいか...）
for i, word, name in zip(itertools.count(1), words, names):
    print(f"{i}位 {word}先輩 is {name}")

# itertools.count()
# 無限にカウントアップまたはカウントダウンする値を返すイテレータを生成する
for i in itertools.count():
    print(i, end="")
    if i >= 30:
        break
    else:
        print(" ", end="")
