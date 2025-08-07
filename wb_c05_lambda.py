# 問題集5章9.
# lambda式
# 書き方：lambda 引数:処理内容

# 基本例1：x + y を返す
xy = lambda x, y: x + y

print(type(xy))
# 出力：<class 'function'>
# この xy は関数オブジェクト
# lambda を使って定義された無名関数（関数オブジェクト）が、そのまま xy に代入された状態

print(xy(2, 3))
# 出力：5

# 基本例2：引数がないパターン
say_hello = lambda: "Hello lambda"
# 文字列 "Hello lambda" を返す

print(say_hello()) 
# 出力：Hello lambda

# 基本例3：文字列の先頭と末尾だけの文字列を返す
str = "Kotone Fujita"
head_foot = lambda str: str[0] + str[-1]

print(head_foot(str))
# 出力：Ka

# ちょっと応用？：第n話までのタイトルのリストを作る
make_title = lambda n: [f"第{n}話" for n in range(1,n+1)]

print(make_title(5))
# 出力：['第1話', '第2話', '第3話', '第4話', '第5話']
