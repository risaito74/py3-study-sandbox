# 11章：標準ライブラリめぐり Part2
# reprlibモジュール
# 巨大な、または深く入れ子になったコンテナオブジェクトを省略して表示する

import reprlib

text = "Kotone Fujita is a character from 'Gakuen Idolmaster' a cheerful 15-year-old mood-maker aiming to become a money-making idol. She's lively, expressive, and surprisingly hardworking."

# repr()だとオブジェクトをそのまま表示する
print(repr(text))

# reprlib.repr()だと途中が省略される（冒頭と最後が確認できる）
print(reprlib.repr(text))
# 出力内容：'Kotone Fujit... hardworking.'
