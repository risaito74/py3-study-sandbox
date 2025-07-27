# 10章 標準ライブラリ：zlibモジュール
# データ圧縮でよく使われるフォーマットのサポートが zlib, gzip, bz2, lzma, zipfile, tarfile といったモジュールにより提供されている

import zlib

# b文字列（バイト文字列）を作成
str = (
    b"Kotone Fujita is a 15-year-old idol featured in Gakuen Idolmaster. "
    b"Confident in her cute looks, she works hard to become a successful idol who can support her financially struggling family. "
    b"Cheerful and expressive, she's a talented dancer and a natural mood-maker."
)

# なお非ASCII文字（マルチバイト）の文字列をb文字列にしようとするとエラーになる
try:
    # そのままだとSyntaxErrorで実行できないので、eval()で式を評価する形にするとtry文で例外をキャッチしてくれる
    # str = b"テスト"
    eval('b"テスト"')
except Exception as e:
    print("例外：", type(e), e)

# 素のバイト文字列の長さ
print("圧縮前のバイト文字列:", len(str))

# zlibで圧縮
str_c = zlib.compress(str)
print("圧縮後のバイト文字列:", len(str_c))

# zlib圧縮したやつを解凍
str_d = zlib.decompress(str_c)
print("解凍後のバイト文字列:", len(str_d))
