# 5章データ構造：リスト：sort(), reverse()のテスト
li = [4, 3, 5, 2, 1] 
print(f"素のリスト = {li}")

# リストを逆順にする（ソートはしない!!!!!）
li.reverse()
print(f"リストを逆順にする = {li} ＊ソートはしない!!!!!")

li.sort()
print(f"ソート後 = {li}")

li.sort(reverse=True)
print(f"逆順ソート後 = {li}")

# リストに負の数を追加して、絶対値でソート
li += [-5, -3, -9]
print(f"負の数を追加 = {li}")

li.sort()
print(f"通常ソート後 = {li}")

li.sort(key=abs)
print(f"絶対値ソート後 = {li}")

#文字列のソート
li_s = ["banana", "apple", "dog", "cat",]
print(f"\n素のリスト = {li_s}")

# リストを逆順にする（ソートはしない!!!!!）
li_s.reverse()
print(f"リストを逆順にする = {li_s} ＊ソートはしない!!!!!")

li_s.sort()
print(f"ソート後 = {li_s}")

#要素の長さでソート
li_s.sort(key=len)
print(f"要素の長さでソート後 = {li_s}")
