# 11章：標準ライブラリめぐり Part2
# stringモジュール：Templateクラス

from string import Template

# テンプレート文字列：
# プレースホルダ（置き換え記号）として$の後ろに有効な識別子（英数字とアンダースコア）を付けたものを使う。後で辞書のキーで置換できる
# $name：キャラクター名
# $height：身長
# $weight：体重
tmp_text = "$name is a charming character from 'Gakuen Idolmaster' standing at $height cm tall and weighing $weight kg."

# プレースホルダを置換するための辞書（キーが変数名に対応）
dic = {"name": "Kotone", "height": 156, "weight":40}

# テンプレート文字列をTemplateオブジェクトに変換
t = Template(tmp_text)

# t はテンプレートクラスオブジェクト
print("type(t):", type(t))
# 出力：<class 'string.Template'>

# substitute() を使ってテンプレート内の変数を辞書で置換し、文字列にする
print(t.substitute(dic))

# substitute() は置換後の文字列（str型）を返す
print("type(t.substitute(dic)):", type(t.substitute(dic)))
# 出力：<class 'str'>

# substitute メソッドは、プレースホルダを辞書かキーワード引数で渡さないとKeyErrorを送出する
# 以下は、渡すキーワードが足りない例
try:
    print(t.substitute(name="Temari"))
except Exception as e:
    print("＊例外：", type(e), e)

# safe_substitute() は、辞書にない変数があってもエラーにならず、$変数名 のまま出力する
# substitute() は対応するキーが辞書にないと KeyError になるため、実用的には safe_substitute() の方が安全
try:
    print(t.safe_substitute(name="Ume"))
except Exception as e:
    print("＊例外：", type(e), e)
