# 問題集11章：datetimeモジュール
# ----- 問題11. -----
# 次のコードを実行した結果として正しいものを選択してください

from datetime import date

dt1 = date(2001, 1, 1)
dt2 = date(2002, 2, 2) # 2002年を見落として間違った！
diff = dt2 - dt1
print(diff.days)
# 出力：397

# 以下、間違ったアレもあるので、基本的な日付の差を確認

# 1ヶ月後（2025年の7/1 ~ 8/1）
dt1 = date(2025, 7, 1)
dt2 = date(2025, 8, 1)
diff = dt2 - dt1
print(f"{dt1} ~ {dt2} の日数: {diff.days}")
# 出力：31

# 1ヶ月後（2025年の11/1 ~ 12/1）
dt1 = date(2025, 11, 1)
dt2 = date(2025, 12, 1)
diff = dt2 - dt1
print(f"{dt1} ~ {dt2} の日数: {diff.days}")
# 出力：30

# 1ヶ月後（2025年の2/1 ~ 3/1）
dt1 = date(2025, 2, 1)
dt2 = date(2025, 3, 1)
diff = dt2 - dt1
print(f"{dt1} ~ {dt2} の日数: {diff.days}")
# 出力：28

# 1年後（2024年1/1 ~ 2025年1/1）
dt1 = date(2024, 1, 1)
dt2 = date(2025, 1, 1)
diff = dt2 - dt1
print(f"{dt1} ~ {dt2} の日数: {diff.days}")
# 出力：366　→　※2024年はうるう年（2月29日あり）だから日数は366日になる

# 1年後（2025年1/1 ~ 2026年1/1）
dt1 = date(2025, 1, 1)
dt2 = date(2026, 1, 1)
diff = dt2 - dt1
print(f"{dt1} ~ {dt2} の日数: {diff.days}")
# 出力：365


