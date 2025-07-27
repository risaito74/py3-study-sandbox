# 7章 ファイルの読み書き

# with
# open()したファイルオブジェクトはclose()メソッドでクローズする必要がある
# withブロックを使うとブロックの終了時に自動的にクローズされ、閉じ忘れがなくなるので便利
try:
    # 第2引数(mode)：r=読み込み専用（デフォルト）, w=書き出し専用, a=追加（ファイル末尾に自動に加える）, r+=読み書き両用
    with open("./tmp/test.txt", "r") as f:
        print(f)
        # ファイル全体を文字列として読み込み
        s = f.read()
        print(s)
except Exception as e:
    print("例外：", type(e), e)

# 閉じたファイルから読み込もうとする（ValueError）
try:
    f.read()
except Exception as e:
    print("例外：", type(e), e)

# 存在しないファイルを開こうとする（FileNotFoundError）
try:
    with open("./tmp/xxxx.xxx", "r") as f:
        print(f)
except Exception as e:
    print("例外：", type(e), e)

# readline() : 行単位の読み込み
try:
    with open("./tmp/test.txt", "r") as f:
        print(f)
        # ファイルを一行単位で読み込み
        while True:
            s = f.readline()
            # 空の文字列を返せばファイルの末尾に達した
            if s == "":
                break
            else:
                 # 改行含めて一行分読み込むため、print()では改行をつけない
                 print(s, end="")
        print()
except Exception as e:
    print("例外：", type(e), e)

# 行単位の読み込みには、ファイルオブジェクトにループをかける方法もある
# これはメモリ効率に優れ、高速な上、コードが簡単になるので推奨される
try:
    with open("./tmp/test.txt", "r") as f:
        print(f)
        # ファイルを一行単位で読み込み
        for line in f:
            # 改行含めて一行分読み込むため、print()では改行をつけない
            print(line, end="")
        print()
except Exception as e:
    print("例外：", type(e), e)

# write() : ファイルの書き込み（mode=a:ファイルの末尾に追記）
try:
    with open("./tmp/test.txt", "a") as f:
        print(f)
        # ファイルの末尾に書き込み
        num = f.write("This is a test.\n")
        print("書き込まれたキャラクタ数:", num)
except Exception as e:
    print("例外：", type(e), e)
