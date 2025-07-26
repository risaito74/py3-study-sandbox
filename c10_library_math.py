# 10章 標準ライブラリ：mathモジュール

import math

# 円周率
# 半径rの円周を求める（2πr）
r = 5
ans = 2 * math.pi * r
# ans を小数点以下2桁で表示（小数点以下第三位を四捨五入）
print(f"半径{r}の円周は{ans:.2f}です。")

# 三角関数（sin,cos）
# 角度をラジアンに変換（90度 → π/2ラジアン）
angle_deg = 45
angle_rad = math.radians(angle_deg)

# サインとコサインを求める
s = math.sin(angle_rad)
c = math.cos(angle_rad)

print(f"{angle_deg}度の sin は {s:.2f}")
print(f"{angle_deg}度の cos は {c:.2f}")

# 任意の底の対数
# log_2(8)：2を何回かけたら8になるか = 3
result_base2 = math.log(8, 2)  
print(f"log_2(8) = {result_base2}")

# 切り上げ（Ceiling = 天井）
num = 3.01
print(f"{num}の切り上げ: {math.ceil(num)}")

# 切り下げ（Floor = 床）
num = 3.98
print(f"{num}の切り下げ: {math.floor(num)}")

# 平方根
num = 16
print(f"{num}の平方根: {math.sqrt(num)}")

# べき乗
x, y = 2, 3
print(f"{x}の{y}乗: {math.pow(x, y)}")
