# 9章クラス：反復子（iterator）
# イテレータは「一度に一つずつ値を取り出せるオブジェクト」
# イテレータを使うと、巨大なデータセットをメモリを節約しながら処理することができる

# 具体的には、以下の2つの条件を満たすオブジェクトがイテレータと呼ばれる：
# __iter__()メソッドを持つ
# __next__()メソッドを持つ
# これらのメソッドによって、イテレータは次の要素を順番に取り出すことができる

# イテラブルとイテレータ
# リストやタプル、文字列なども「反復可能（イテラブル）」なオブジェクトだが、これらはイテレータそのものではない
# イテラブルをiter()関数に渡すことで、イテレータを生成する

# リストはイテラブル（iterable）
my_list = [1, 2, 3]

# イテレータを生成
my_iterator = iter(my_list)
print(my_iterator)

# イテレータはnext()で要素を一つずつ取り出せる
print(next(my_iterator))  # 出力: 1
print(next(my_iterator))  # 出力: 2
print(next(my_iterator))  # 出力: 3

# 要素が尽きるとStopIteration例外を送出する
try:
    print(next(my_iterator))
except Exception as e:
    print("例外：", type(e), e)
