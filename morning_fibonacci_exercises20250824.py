# 朝のフィボナッチ体操 2025/08/24

def fibonacci(limit):
    """ limit未満のフィボナッチ数を遅延評価で1つずつ返す """
    i, j = 0, 1
    while i <= limit:
        yield i
        i, j = j, i + j

print("*** フィボナッチ体操・第一 ***")
for i in fibonacci(100):
    print(i, end=" ")

print("\n")

print("*** フィボナッチ体操・第二 ***")
for i in fibonacci(1000):
    print(i, end=" ")
