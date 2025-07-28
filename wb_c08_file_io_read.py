# 問題集8章：ファイル入出力
# ----- 問題4. -----
# for でファイルを繰り返し読み込む処理
# 問題：1行ずつファイルを読み込んで出力する処理として、誤っているものを選択

file_path = "./tmp/test.txt"

# 選択肢A
print("***** 選択肢A *****")
fp = open(file_path)
# 反復可能体（イテレータ）は、for文で繰り返すことにより、要素を1つずつ取り出せる
# ファイルオブジェクト fp はイテレータとして動作するため、forで1行ずつ読み込める
for s in fp:
    print(s)
fp.close()
# これは一行ずつ出力される：正しい

# 選択肢B
print("***** 選択肢B *****")
fp = open(file_path)
# fp.read() はファイル全体を1つの文字列として返すため、
# for文でループすると1文字ずつ処理される（つまり、行単位ではないため誤り）
for s in fp.read():
    print(s)
fp.close()
# これは1文字ずつ出力される：誤り（これを選択する）

# 選択肢C
print("***** 選択肢C *****")
fp = open(file_path)
# readlines() はファイルを行単位で分割したリストとして返す
# だから　for s in list と同じように反復可能体として、forで繰り返すことで1行ずつファイルから読み込める
for s in fp.readlines():
    print(s)
fp.close()
# これは一行ずつ出力される：正しい

# 選択肢D
print("***** 選択肢D *****")
fp = open(file_path)
# ファイルオブジェクト fp はそのままでも反復可能体となり、forで1行ずつファイルから読み込めるが、
# list(fp) によってファイルオブジェクトが行単位のリストに変換され、forで1行ずつ処理できる
for s in list(fp):
    print(s)
fp.close()
# これは一行ずつ出力される：正しい
