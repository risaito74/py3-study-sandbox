# 問題集7章 4.
# from ~ import ~ as ~

# 当たり前だけど、import文手前でモジュールを呼んでもエラーになる
try:
    n = wb_c07_calc.add(2, 3)
except Exception as e:
    print("＊例外：", type(e), e)
# ＊例外： <class 'NameError'> name 'wb_c07_calc' is not defined

# モジュールをインポートする基本形：インポートしたモジュール名が使えるようになる
import wb_c07_calc

n = wb_c07_calc.add(2, 3)
print(n)
# 出力：5

# as を使うと別名（省略名）でインポートできる
import wb_c07_calc as cal

n = cal.add(3,4)
print(n)
# 出力：7

# from を使ってモジュールの関数を直接インポート
# この場合、モジュール名はインポートされない（使えない）
from wb_c07_name import add_name_kun

name = add_name_kun("Kotone")
print(name)
# 出力：Kotone君

# インポートしてないモジュール名から使うとエラーになる
try:
    name = wb_c07_name.add_name_kun("Kotone")
except Exception as e:
    print("＊例外：", type(e), e)
# ＊例外： <class 'NameError'> name 'wb_c07_name' is not defined

# from でモジュールの関数を直接インポートして as で別名をつける
from wb_c07_name import add_name_chan as chan

name = chan("ことね")
print(name)
# 出力：ことねちゃん

# 別名をつけたら元の名前は使えない（今からお前の名前は「千」だ！）
# chanとしてインポートしてるから add_name_chan とか知らんし
try:
    name = add_name_chan("リーリア")
except Exception as e:
    print("＊例外：", type(e), e)
# ＊例外： <class 'NameError'> name 'add_name_chan' is not defined
