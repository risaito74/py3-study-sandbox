# 問題集8章 4.
# read() と readlines() と readline() のちがい

file_path = "./tmp/test.txt"

# fp.read() ：ファイル全体を1つの文字列として返す
# （問題文に沿ってwith文をを使わない記法で記述）
fp = open(file_path)
s = fp.read()
print(s)
fp.close()
# test1.
# test2.
# test3.
# end.

# fp.readlines() ：ファイル全体を行ごとに分割したリストとして取得する
fp = open(file_path)
s = fp.readlines()
print(s)
fp.close()
# ['test1.\n', 'test2.\n', 'test3.\n', 'end.\n']

# fp.readline()：ファイルを１行だけ読み込む
fp = open(file_path)
s = fp.readline()
print(s)
fp.close()
# test1.

# fp.read()でforを回すと、1文字ずつの出力になる
fp = open(file_path)
for s in fp.read():
    print(s, end="")
    # 改行コードでなければ半角スペースを入れる
    if s != "\n":
        print("", end=" ")
fp.close()
# t e s t 1 .
# t e s t 2 .
# t e s t 3 .
# e n d .
