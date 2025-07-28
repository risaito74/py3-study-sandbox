# 11章：標準ライブラリめぐり Part2
# repr() と str() のちがい

# reprとは？
# レパーと読むことが多い
# オブジェクトを“公式的に”文字列で表現する関数
# representation（表現、表示）の略

# repr() と str() の比較（例：日付、文字列、数値などで違いが出る）

# str(object)
# 見やすさ重視、人間向け
# 戻り値：人間にわかりやすい形（日時なら "2025-07-28" のような）で表現された文字列を返す
# 用途：画面表示・ログ出力など、ユーザー向け表示に使われる

# repr(object)
# 再現性重視、プログラム向け
# 戻り値：objectの「再現可能な文字列表現」（可能な限りeval()で復元できる形式）を返す　※復元できないケースもあるがここでは省略...
# 用途：デバッグやログ出力、開発者向けの内部的確認など

# ----- 例：datetime -----
import datetime
today = datetime.date.today()

print("str(today):", str(today))        # 2025-07-28 →この文字列からdateオブジェクトには戻れない（不可逆）
print("repr(today):", repr(today))      # datetime.date(2025, 7, 28)　→dateオブジェクトだとわかる

# todayは何型？　→　<class 'datetime.date'>
print("todayの型:", type(today))

# str(today)は何型？ → <class 'str'>
print("str(today)の型:", type(str(today)))

# repr(today)は何型？ → <class 'str'>
print("repr(today)の型:", type(repr(today)))

# repr()はeval()で元の型にもどる
r_today = repr(today)
e_today = eval(r_today)
print("e_today:", e_today)
print("e_todayの型:", type(e_today))

# ----- 例：エスケープシーケンス -----
text = "kotone\t156\t40\nume\t158\t50"

# str()はエスケープシーケンス（改行、タブ）が解釈されて整形されたテキストになる
print(str(text))
# repr()はクォートとエスケープシーケンスがそのまま出力される
print(repr(text))
