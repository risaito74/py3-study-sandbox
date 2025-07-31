# not and or のテスト
# 演算子の優先順位： not > and > or
# ポイント1：短絡演算子（and,or）は左から評価する
#   andの場合：左から評価して、「最初に偽」になった評価結果が最終結果となり、そこで評価を止める
#   orの場合 ：左から評価して、「最初に真」になった評価結果が最終結果となり、そこで評価を止める
# ポイント2：not は単項演算子

# 式が評価される順番と、評価されたか否かを確認する用の関数
def exp(num):
    print(f"式({num})を評価")
    return num

print("結果:", exp(1) or exp(2) or exp(3))

print("結果:", exp(1) and exp(2) and exp(3))

print("結果:", exp(1) and exp(2) or exp(3))
# 優先は((1 and 2) or 3) 計算順は左から

print("結果:", exp(0) or exp(2) and exp(3))
# 優先は(0 or (2 and 3)) 計算順は左から

print("結果:", not exp(0))
# 出力：True
# 0 を bool(0)=False と評価して not演算子で True になる

print("結果:", not exp(0) or exp(1) and exp(0))
# 出力：True
# 左から評価して、最初の not 0 = Trueになり、真なので以降は評価しない
