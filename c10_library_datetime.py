# 10章 標準ライブラリめぐり：datetimeモジュール
# UNIX時間を取得する（実行時間計測）ならtimeモジュール、日時を取得するならdatetimeモジュールを使う

# datetimeモジュール内のdateクラスをインポート
from datetime import date

# 今日の日付を取得
now = date.today()
print(type(now), now)

# date.strftime()：日付型を与えられた書式に従って文字列に変換
# %wを日本語曜日に変換するタプルを用意（0 が日曜日で 6 が土曜日）
tp_d = ("日", "月", "火", "水", "木", "金", "土")

# strftime()で曜日の%wだけ取得
dow_n  = int(now.strftime("%w"))
# %wを〇曜日に変換
dow_s = f"{tp_d[dow_n]}曜日です。"

# 年月日の部分を取得
ymd_s = now.strftime("今日は %Y 年 %m 月 %d 日、")

# 年月日と曜日を合体させて完成
print(ymd_s + dow_s)

# 誕生日の曜日を取得
birthday = date(1974, 9, 4)
dow_n = int(birthday.strftime("%w"))
dow_s = tp_d[dow_n]
print(f"あなたの誕生日 {birthday} は {dow_s}曜日です。")

# dateはカレンダー計算をサポートしている
age = now - birthday
print(f"age.days = {age.days}")
