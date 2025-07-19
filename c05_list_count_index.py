# 5章データ構造：リストのメソッド：count(),index()
li_n = [x for x in range(10)] # 0~9 のリスト
print(f"li_n = {li_n}")

# count(x): リストの中のxの個数を返す
li_n += [2, 2, 2]
cnt = 2
print(f"リストの {cnt} の個数 = {li_n.count(cnt)}")

# index(x): リスト内から最初のxのindexを返す
li_s = ["a", "b", "c", "b"]
idx_b = li_s.index("b")
print(f"b の最初のindex = {idx_b}")

# リストから最大値のindexを表示
li_m = [30, 40, 900, 80, 10]
idx_max = li_m.index(max(li_m))
print(f"リストの最大値 {max(li_m)} のindex = {idx_max}")

# リストの開始コード"start"から終了コード"end"の範囲から最初のxのindexを返す
li_p = ["青森", "岩手", "宮城", "start", "福島", "宮城", "岩手", "end", "宮城", "青森"]
idx_start = li_p.index("start") + 1
idx_end = li_p.index("end")
idx_miyagi = li_p.index("宮城", idx_start, idx_end)
print(f"開始コードから終了コードの範囲 = {li_p[idx_start:idx_end]}")
print(f"開始コードから終了コードの範囲で最初の「宮城」のindex = {idx_miyagi}")
