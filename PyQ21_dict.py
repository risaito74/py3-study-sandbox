# PyQ模擬試験
# 21. ディクショナリの作成⽅法として誤っているものを選択してください（1つ選択）
# A. {"carrot": 80, "tomato": 100} 
# B. dict("carrot"=80, "tomato"=100) 
# C. dict([("carrot", 80), ("tomato", 100)]) 
# D. {k: v for k, v in [("carrot", 80), ("tomato", 100)]}

# 選択肢A
dic = {"carrot": 80, "tomato": 100}
print(dic)
# 出力：{'carrot': 80, 'tomato': 100}

# 選択肢B：エラーになる
# dic = dict("carrot"=80, "tomato"=100) 
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

# dict()で定義する場合、キーワード引数としてkeyを渡すため""をつけない
dic = dict(carrot=80, tomato=100) 
print(dic)

# 選択肢C
# タプルのペアのリスト、リストのペアのタプル等をdict()に渡して生成できる
dic = dict([("carrot", 80), ("tomato", 100)]) 
print(dic)
# 出力：{'carrot': 80, 'tomato': 100}

# 選択肢D
# 内包表記で作成
dic = {k: v for k, v in [("carrot", 80), ("tomato", 100)]}
print(dic)
# 出力：{'carrot': 80, 'tomato': 100}

# おまけ
# 2つのリストから内包表記で作成
# 辞書の内包表記：2つのリストから生成
li_k = ["name", "age", "from"]
li_v = ["Kotone", 15, "Saitama"]

dic = {k: v for k, v in zip(li_k, li_v)}
print(dic)

# 上の書き方の場合、dict()でより簡単に記述できる：内包表記を使う必要はない
dic = dict(zip(li_k, li_v))
print(dic)
