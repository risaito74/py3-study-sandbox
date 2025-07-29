# 11章：標準ライブラリめぐり Part2
# decimalモジュール
# decimalモジュールは、浮動小数点10進数で計算するためのデータ型Decimalをもたらす

# decimalモジュールのDecimalクラスをインポート
from decimal import Decimal

# decimalモジュールの全部をインポートする方法もある
# 名前の衝突を起こす可能性があるため非推奨
# from decimal import *

# Decimal型で計算（70セントの電話料金に税金5%を加える計算）
tax_d = Decimal("0.70") * Decimal("1.05")
print(f"{str(type(tax_d)):30} {tax_d}")

# デフォルトのfloat型で計算（同上）
tax_f = 0.70 * 1.05
print(f"{str(type(tax_f)):30} {tax_f}")

# それぞれを小数点以下第2位で四捨五入
print("tax_d:", round(tax_d, 2)) # 0.7335 → 0.74
print("tax_f:", round(tax_f, 2)) # 0.7335 → 0.73
# float型の四捨五入では誤差が出ているが、Decimal型の計算は正しく四捨五入できる

# 【注意】Decimal型は文字列型で数値を渡す！
# 数値のまま（つまりfloat型リテラルで）渡すと引数を渡す段階で誤差が発生するため、文字列で渡す必要がある！
print(Decimal("0.5") / Decimal("0.1"))  # 正しく計算できる(5)
print(Decimal(0.5) / Decimal(0.1))      # 誤差が出る(4.999...)
