# 問題集13章：問題38
# textwrapモジュール
# 文字列を任意の文字数で折り返し（改行）、切り詰め（省略）して整形するには、標準ライブラリのtextwrapモジュールを使う
# なお、文字列ではなくリストや辞書を整形して出力するにはpprintモジュールが便利

import textwrap

s = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages"

# wrap()関数
# 任意の文字数に収まるように単語の区切りで分割したリストが取得できる
s_wrap_list = textwrap.wrap(s, 40)
print(s_wrap_list)
# ['Python can be easy to pick up whether', "you're a first time programmer or you're", 'experienced with other languages']

# fill()関数
# リストではなく改行された文字列を返す。wrap()のあとで'\n'.join(list)するのと同じ
print(textwrap.fill(s, 40))
# Python can be easy to pick up whether
# you're a first time programmer or you're
# experienced with other languages

# 「単語の区切りで分割」のテスト
s = "my cat name is neko"
print(textwrap.fill(s, 5))
# my
# cat
# name
# is
# neko

print(textwrap.fill(s, 10))
# my cat
# name is
# neko
