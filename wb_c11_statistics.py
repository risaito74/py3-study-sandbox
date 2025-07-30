# 問題集11章：statisticsモジュール
# ----- 問題8. -----
# 次のコードを実行した結果として正しいものを選択

import statistics

data = [-1, -1, -1, -1, 4]

# mean() データの平均を求める
# mean とは、統計学上の平均を意味する英単語、より正確には arithmetic mean（算術平均）
print("mean:", statistics.mean(data))
# 出力：0

# median() データの中央値を求める
# median とは中央値を意味する英単語（まんま）
# 中央値とは、データを小さい順に並べたときの真ん中にある値
print("median:", statistics.median(data))
# 出力：-1.0

# variance() データの不偏分散を求める
# 不偏分散とは、平均との差の2乗の和を「データ数-1」で割って求める
print("variance:", statistics.variance(data))
# 出力：

# そもそも不偏分散（平均との差の2乗の和を「データ数-1」で割る）ってなんじゃー！！！って思うので、計算処理を書いてみる

# 平均(0)
mean = statistics.mean(data)

# 平均との差の2乗
data2 = []
for f in data:
    data2.append((f - mean) ** 2)

# 平均との差の2乗を合算
sum_d2 = sum(data2)

# それを「データ数 - 1」で割る
ans = sum_d2 / (len(data) - 1)

print("手動計算で求めた不偏分散:", ans)
