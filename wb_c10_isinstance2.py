# 問題集10章：クラスとオブジェクトの操作
# ----- 問題6. -----
# isinstance()関数

# リストかタプルの要素が数値の時、合計値を返す
def sum_data(data):
    res = "集計できないデータでした"

    try:
        # dataがリスト型またはタプル型か？
        if isinstance(data, (list, tuple)):
            res = sum(data)
    except TypeError as e:
        res = f"{res} {type(e)} {e}"

    return res

data1 = [1, 2, 3, 4]
data2 = "test data"
data3 = (10, 20, 30)
data4 = [0.5, 2, 3.5]
data5 = []
data6 = {"t1": 10, "t2": 20}
data7 = [1, 2, 3, "4"]

print(sum_data(data1))
# 出力：10

print(sum_data(data2))
# 出力：集計できないデータでした

print(sum_data(data3))
# 出力：60

print(sum_data(data4))
# 出力：6.0

print(sum_data(data5))
# 出力：0

print(sum_data(data6))
# 出力：集計できないデータでした

print(sum_data(data7))
# 出力：集計できないデータでした <class 'TypeError'> unsupported operand type(s) for +: 'int' and 'str'
