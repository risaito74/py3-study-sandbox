# 問題集8章 4.
# read() と readlines() と readline() のちがい

file_path = "./tmp/read_text_sample.txt"

### fp.read() ：！！！文字列！！！
# ファイル全体を1つの文字列として返す
fp = open(file_path)
s = fp.read()
print(s)
fp.close()
# test1.
# test2.
# test3.
# end.

### fp.readlines() ：！！！リスト！！！
# ファイル全体を行ごとに分割したリストとして取得する
fp = open(file_path)
s = fp.readlines()
print(s)
fp.close()
# ['test1.\n', 'test2.\n', 'test3.\n', 'end.\n']

### fp.readline()：！！！文字列で1行！！！
# ファイルを１行だけ文字列として読み込む
fp = open(file_path)
s = fp.readline()
print(type(s), s)
fp.close()
# <class 'str'> test1.
