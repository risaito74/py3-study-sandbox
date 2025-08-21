# PyQ模擬試験
# 34. osモジュールの特徴として誤っているものを選択してください（1つ選択
# A. os.chdir(移動先)でカレントディレクトリを変更できる
# B. os.pwd()でカレントディレクトリを取得できる
# C. dir(os)で osモジュールの全属性名を取得できる
# D. help(os)で osモジュールのヘルプを確認できる

import os

# カレントディレクトリを表示
# getcwd : get current working directory
print(os.getcwd())
# C:\GitHub\py3-study-sandbox

# getcwd()のdocstringを表示
help(os.getcwd)
# Help on built-in function getcwd in module nt:
#
# getcwd()
#    Return a unicode string representing the current working directory.

# カレントディレクトリを変更
os.chdir("./tmp")
print(os.getcwd())
# C:\GitHub\py3-study-sandbox\tmp

# システム側のシェルでコマンドを実行
# Windows環境だから「ls」ではなく「dir」を使う
os.system("dir")

# dir()でgetcwd()の全属性を表示
print(dir(os.getcwd))

# getcwd()の__name__属性を表示
print(os.getcwd.__name__)
