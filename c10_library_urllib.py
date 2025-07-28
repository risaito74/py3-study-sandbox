# 10章 標準ライブラリ：urllibモジュール

from urllib.request import urlopen

# URL：阿部寛ホームページの管理者のページ（超シンプル！）
url = "http://abehiroshi.la.coocan.jp/kanri/kanri.htm"

with urlopen(url) as res:
    for line in res:
        # Shift_JISでバイトを文字列に
        # 対象ページは「charset=x-sjis」なので引数で'shift_jis'を渡す
        line = line.decode('shift_jis')
        # お尻のnewlineを外す
        print(line.rstrip())
