# 7章 入出力：f文字列とformat()

# piを使うためにmathモジュールをインポート
import math

n1, n2 = 12, 5
uni = "個"
# f文字列の基本
print(f"{n1}{uni}の{n2}倍は{n1 * n2}{uni}です。")

# f文字列でπの表示
# 小数点以下第二位（第三位で四捨五入）
print(f"πの値（小数点以下第二位）: {math.pi:.2f}")
# 小数点以下第三位（第四位で四捨五入）
print(f"πの値（小数点以下第三位）: {math.pi:.3f}")
# 小数点以下第四位（第五位で四捨五入）
print(f"πの値（小数点以下第四位）: {math.pi:.4f}")

# 辞書のkeyを文字列として整列（左揃え）valueを整数として右揃えで表示
# 文字列が日本語の場合はマルチバイト対応が別途必要なので今回は省略...
dic = {"saki":900, "temari": 2000, "kotone":50000, "ume":90}
for key, val in dic.items():
    print(f"{key:10} => {val:8d}")

# format()の基本形：{}の順番に引数を渡す
print("{}{}の{}倍は{}{}です。".format(n1, uni, n2, n1 * n2, uni))

#　{}内に数字を入れて第n引数を参照する形もできる（数字は順不同にもできる）
print("{0}{1}の{2}倍は{3}{4}です。".format(n1, uni, n2, n1 * n2, uni))

# {}内にキーワードを入れて、キーワード引数で参照する形もできる
# 2か所ある{unit}はformat()内ではキーワード引数1個用意すればいい
print("{num1}{unit}の{num2}倍は{ans}{unit}です。".format(num1=n1, unit=uni, num2=n2, ans=n1*n2))

# x, x2乗, x3乗 をフォーマットを整えて出力する例
for x in range(1,11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x*x, x**3))

# 左寄せ(<)、中央寄せ(^)、右寄せ(>)
for key, val in dic.items():
    print(f"{key:<8} | {key:^8} | {key:>8} => {val:8d}")

# 0埋め、文字埋め
for key, val in dic.items():
    print(f"{key:*<8} | {key:_^8} | {key:.>8} => {val:08d}")

# 数値のカンマ区切り
# フォーマット指定子の順番（カンマの位置）：[全体の最小幅][,][小数点以下桁数][型(d/f)]
for key, val in dic.items():
    print(f"{key:10} => {val:8,d}")
