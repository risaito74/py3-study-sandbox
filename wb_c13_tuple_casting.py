# 問題集13章：問題22
# tuple()関数による変換

# tuple()関数は、シーケンス（リストや文字列など）をタプル型に変換するための組み込み関数

### 問題の選択肢C：これはエラーになる
try:
    tp = tuple("spam", "ham", "eggs")
    print(tp)
except Exception as e:
    print("例外：", type(e), e)
# 例外： <class 'TypeError'> tuple expected at most 1 argument, got 3
# タプル型データを渡してるじゃん！…と思ったら、ちがった！
# tuple()に渡している引数は文字列型を3つ！→タプルじゃないよ！（囲むカッコにだまされたやつ！）

### タプル型をtuple()に渡すと：エラーは起きず、そのまま、タプル型がタプル型になり変化なし
try:
    tp = tuple(("spam", "ham", "eggs"))
    print(tp)
except Exception as e:
    print("例外：", type(e), e)
# 出力：('spam', 'ham', 'eggs')

### 問題の選択肢D：要素1つのタプル型データ（後ろにカンマつけたらタプルになる）
tp = "spam",
print("選択肢D:", type(tp), tp)
# 選択肢D: <class 'tuple'> ('spam',)

### 文字列の場合：文字単位のタプルデータになる
tp = tuple("spam")
print(tp)
# 出力：('s', 'p', 'a', 'm')
