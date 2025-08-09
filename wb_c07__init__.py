# 問題集7章 6. 7.
# __init__.py がさっぱりわからん問題をどうにかする件

# wb_c07フォルダを作成し、その中に以下のファイルを用意した
#  ├ __init__.py：空ファイル。この存在によってwb_c07フォルダがパッケージとして認識される
#  └ test.py：動作確認用モジュール。hoge()関数が文字列を出力するだけ

# 基本的な書き方1
# パッケージ「wb_c07」のモジュール「test」をインポート
import wb_c07.test
# このimport文の動作
# 01. wb_c07 パッケージを読み込む
# 02. その中の test モジュールを読み込まれる（sys.modules に 'wb_c07.test' が登録）
# 03. ただし グローバルに束縛されるのは 'wb_c07' という名前だけ
#     → test は 'wb_c07' の属性として参照（wb_c07.test）／test という名前は作られない

# 「グローバルに束縛」ってどういうことバブ？👶🍼
# Pythonで変数やモジュールを import すると、その名前が手元（スクリプトの一番上の階層＝グローバル名前空間）に置かれる
# これを「束縛される」という

# パッケージ内モジュールを使うときはフルネームで参照しないとダメ
wb_c07.test.hoge()

# このimportの書き方なら test モジュールから書いてもいけるんじゃね？と思った件
try:
    test.hoge()
except Exception as e:
    print("＊例外：", type(e), e)
# ＊例外： <class 'NameError'> name 'test' is not defined

# 基本的な書き方2
# パッケージ「wb_c07」からモジュール「test」を直接インポート
# これでパッケージ名を省略できるが、大規模プロジェクトの場合、名前衝突や「test」がどのパッケージかわからない、といったデメリットもある
from wb_c07 import test

# 上の書き方でインポートすればパッケージ名の参照は不要になる
test.hoge()

# subパッケージをインポート
import wb_c07.sub

# フルネームで sub_hello() 関数を参照
s = wb_c07.sub.submod.sub_hello("Kotone")
print(s)
# 出力：Hello from submod, kotone!

# __init__.py内でインポートしてるから、subパッケージから直接 sub_hello() を呼ぶこともできる
s = wb_c07.sub.sub_hello("Ume")
print(s)
# 出力：Hello from submod, Ume!
