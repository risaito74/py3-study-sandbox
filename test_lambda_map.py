# lambda式とmap()の組み合わせ

li = [1, 2, 3, 4]

### リストを2倍にする
lmd = lambda x: x * 2
li_w = list(map(lmd, li))
print(li_w)
# 1行版：print(list(map(lambda x: x * 2, li)))
# 出力：[2, 4, 6, 8]

### リストを「第n章」の文字列に置き換え
lmd = lambda x: f"第{x:02d}章"
li_c = list(map(lmd, li))
print(li_c)
# 1行版：print(list(map(lambda x: f"第{x:02d}章", li)))
# 出力：['第01章', '第02章', '第03章', '第04章']

### 文字列を参照してタプルのリストにする
str = "abcdefg"
lmd = lambda x: (x,str[x-1])
li_t = list(map(lmd, li))
print(li_t)
# 1行版：print(list(map(lambda x: (x,str[x-1]), li)))
# 出力：[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
