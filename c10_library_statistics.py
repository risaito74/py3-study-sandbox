# 10章 標準ライブラリ：statisticsモジュール（統計モジュール）
# statisticsモジュールは数値データの基本統計量（平均、中央値、分散など）を求めるもの

import statistics

dat1 = [1.0, 2.0, 3.0, 4.0, 5.0]
dat2 = [1.0, 2.0, 3.0, 4.0, 50.0]

# 平均
ave1 = statistics.mean(dat1)
ave2 = statistics.mean(dat2)
print(f"平均1: {ave1}")
print(f"平均2: {ave2}")

# 中央値：データを小さい順に並べたときに真ん中に位置する数値
med1 = statistics.median(dat1)
med2 = statistics.median(dat2)
print(f"中央値1: {med1}")
print(f"中央値2: {med2}")

# 分散：データのばらつきの度合いを示す指標で、データが平均からどれだけ離れているかを数値で表す
vari1 = statistics.variance(dat1)
vari2 = statistics.variance(dat2)
print(f"分散1: {vari1}")
print(f"分散2: {vari2}")
