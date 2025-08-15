# 問題集11章：statisticsモジュール
# ----- 問題8. -----

# また間違えました…orz
# なので、問題とは別の簡単なデータをChatGPTに用意してもらったので、これでやっていく
# 平均：mean()、中央値：median()は雰囲気でわかってた！
# が、variance()が不偏分散ってことを完全に忘れてた！

import statistics as st

data1 = [2, 4, 6]
data2 = [0, 0, 4, 4]
data3 = [2, 2, 2, 2, -3]

### data1 の平均、中央値、不偏分散
print(f"***** data: {data1} *****")

# 平均：mean()
print("平均：mean() =", st.mean(data1))
# 出力：4

# 中央値：median()
print("中央値：median() =", st.median(data1))
# 出力：4

# 不偏分散：variance()
print("不偏分散：variance() =", st.variance(data1))
# 出力：4

# 試験対策：暗算での解き方
# 分子：（平均との差の二乗）の和
#   (2-4)**2 + (4-4)**2 + (6-4)**2 = 4 + 0 + 4 = 8 
# 分母：要素数3 - 1 = 2
# 従って：8 / 2 = 4

### data2 の平均、中央値、不偏分散
print(f"***** data: {data2} *****")

# 平均：mean()
print("平均：mean() =", st.mean(data2))
# 出力：2

# 中央値：median()
print("中央値：median() =", st.median(data2))
# 出力：2.0
# 偶数の中央値：中央値は 0 と 4 の間なので、両者の平均で 2.0 となる

# 不偏分散：variance()
print("不偏分散：variance() =", st.variance(data2))
# 出力：5.3333...

# 試験対策：暗算での解き方
# 分子：2**2 + 2**2 + 2**2 + 2**2 = 16
# 分母：4 - 1 = 3
# 従って：16 / 3 = 5 + 0.3333... = 5.3333...（暗算の範囲か微妙だからたぶん試験には出なそうなパターン）

### data3 の平均、中央値、不偏分散
print(f"***** data: {data3} *****")

# 平均：mean()
print("平均：mean() =", st.mean(data3))
# 出力：1

# 中央値：median()
print("中央値：median() =", st.median(data3))
# 出力：2

# 不偏分散：variance()
print("不偏分散：variance() =", st.variance(data3))
# 出力：5

# 試験対策：暗算での解き方
# 分子：1**2 + 1**2 + 1**2 + 1**2 + -4**2 = 20
# 分母：5 - 1 = 4
# 従って：20 / 4 = 5
