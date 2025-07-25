# 9章クラス：ジェネレータ（generator）
# ジェネレータは反復子（iterator）を作るための関数
# データを返す部分で yield（イールド）を使う

# yield（イールド）の仕事
# 1) 値を返す
# 2) 処理を一時停止する＆次にその処理後から再開できる

# ジェネレータ関数（yield が含まれる関数がジェネレータ関数）
def test_gen():
    print("処理1")
    # 1を返して処理一時停止
    yield 1

    print("処理2")
    # 2を返して処理一時停止
    yield 2

    print("処理3")
    # 3を返して処理一時停止
    yield 3

# test_gen() を呼ぶ、ジェネレータオブジェクトが返って来る
gen = test_gen()
print(gen)

# next() で yield まで処理を進め yield の値を順番に取り出す
print(next(gen))
print(next(gen))
print(next(gen))

# yield の値（＝データ）が尽きると StopIteration 例外を送出する
try:
    print(next(gen))
except Exception as e:
    print("例外：", type(e), e)

# for ループで yield を使う例
def for_gen():
    for i in range(5):
        print("処理", i)
        yield i

# ジェネレータオブジェクトを生成
gen_f = for_gen()

# 例外が出るまで for で next() を繰り返す
try:
    for i in range(10):
        print(next(gen_f))
except Exception as e:
    print("例外：", type(e), e)
