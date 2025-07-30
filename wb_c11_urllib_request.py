# 問題集11章：urllib.requestモジュール
# ----- 問題9. -----
# インターネット上のURLからデータを取得する関数として正しいものを選択
# 正解：urllib.request.urlopen

import urllib.request

# URL：阿部寛ホームページの管理者のページ（超シンプル！）
url = "http://abehiroshi.la.coocan.jp/kanri/kanri.htm"

# urlopen() で引数のURLにアクセスする
with urllib.request.urlopen(url) as res:
    for line in res:
        # Shift_JISでバイトを文字列に
        # 対象ページは「charset=x-sjis」なので引数で'shift_jis'を渡す
        line = line.decode('shift_jis')
        # お尻のnewlineを外す
        print(line.rstrip())

# url を open するから urlopen() ってもう暗記するしかない！
