# PyQ模擬試験
# 33. 次のコードを実⾏して0 1 1 2 3 5 8が 表⽰されるとき⼊る記述として正しいものを選択してください（1つ選択）

def fibonacci(limit):
    i, j = 0, 1
    while i <= limit:
        yield i
        i, j = j, i + j

# 10未満のフィボナッチ数を取得して出力
for i in fibonacci(10):
    print(i, end=" ")
# 出力：0 1 1 2 3 5 8 

# 100未満のフィボナッチ数を取得して出力
for i in fibonacci(100):
    print(i, end=" ")
# 出力：0 1 1 2 3 5 8 0 1 1 2 3 5 8 13 21 34 55 89 
