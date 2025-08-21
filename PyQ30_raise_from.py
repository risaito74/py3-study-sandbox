# PyQ模擬試験
# 30. 次のコードを正常に実⾏できるとき、空欄①に⼊る記述として正しいものを選択してください（1つ選択）
# A. as B. from C. in D. with

import traceback

# 正解はB：from
def divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError as e:
        raise ValueError("Illegal argument") from e
    else:
        return result

# fromないケース
def divide_not_from(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError as e:
        raise ValueError("Illegal argument")
    else:
        return result


# 問題文のケース：raise ~ from で送出
try:
    result = divide(1, 0)
except ValueError as e:
    print(e)
    # tracebackで例外の因果関係を詳細表示
    traceback.print_exc()

# fromないケース
try:
    result = divide_not_from(1, 0)
except ValueError as e:
    print(e)
    # tracebackで例外の因果関係を詳細表示
    traceback.print_exc()
