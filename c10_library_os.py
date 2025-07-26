# 10章 標準ライブラリめぐり：osモジュール
# Pythonチュートリアルに沿った試験勉強だと、以下の関数が理解できていればよさそう
# os.getcwd()
# os.chdir()
# os.system()

import os

# 今いるディレクトリを返す
# getcwd は「get current working directory」の略
print("現在のディレクトリ:", os.getcwd())

# カレントディレクトリのディレクトリ＆ファイル一覧を取得
print(os.listdir("."))

# カレントディレクトリの変更：上の階層に移動
os.chdir("..")
print("現在のディレクトリ:", os.getcwd())

# カレントディレクトリの変更：元の階層に戻る
os.chdir("./py3-study-sandbox")
print("現在のディレクトリ:", os.getcwd())

# 「today」が存在してなければ、ディレクトリを作成
if not os.path.exists("today"):
        print("today ディレクトリを作成")
        # システム側のシェルで「mkdir」コマンドを実行：「today」ディレクトリが作成される
        os.system("mkdir today")

# 「today」は存在する：それはディレクトリか？
elif os.path.isdir("today"):
        print("today は既にあります（ディレクトリ）")

# 「today」は存在する：それはファイルか？
elif os.path.isfile("./today"):
        print("today は既にあります（ファイル）")

else:
        print("today は既にある…けどディレクトリでもファイルでもないっぽい（シンボリックリンクなど")

# モジュールの関数がすべて入ったリストを返す
#print(dir(os))
