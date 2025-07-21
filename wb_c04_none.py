# 問題集4章：判定と繰り返し：None
# ----- 問題3. -----
value = None

# 適切な選択肢
if value is None:
    print("if value is None:")

# 不適切な選択肢B
if not value:
    print("if not value:")

# 不適切な選択肢D
if value == None:
    print("if value == None:")

# ----- 以下、この問題を理解するためのテストコード -----

# Noneとは？
# Noneは、値が何も存在しない状態を表す。
# 「value = None」で、値を持たない変数 value を作成できる

# 不適切な選択肢B：これはvalue = 0でも真になるので不正解
value = 0
if not value:
    print(f"if not value: value = {value}")

# 不適切な選択肢D：これは「ほとんどの場合にNoneかどうかを判定」できる（問題集の解説より）
# ただし、実行速度が遅い、プログラマが==の動作を変更可能なため（__eq__の件）、最も適切なものは「is」演算子となる
# →is None はピンポイントで「Noneか？」を判定してくれる
value = None
if value == None:
    print("if value == None:")

# おまけ
# NoneはPythonに1つだけ存在する特殊なオブジェクトであり、NoneTypeクラスのインスタンス
print(f"None = {None}")                 # 出力: None
print(f"type(None) = {type(None)}")     # 出力: <class 'NoneType'>
