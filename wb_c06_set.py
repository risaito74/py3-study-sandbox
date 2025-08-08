# 問題集6章：集合(set)での要素の追加、削除
# ----- 問題4. -----
# 要素の追加について、リストではappend()メソッドを使い、setではadd()メソッドを使う

### 要素の追加：

# 空の集合を作成
# 空の集合を生成するには {} でなく set() を使う必要がある（ {} は空の辞書を生成するから）
set1 = set()
print("空の集合:", set1)
# 出力：set()

# 要素を追加
set1.add(1)
print("要素を追加:", set1)
# 出力：{1}

# 同じ要素を追加しても集合だから重複しない
set1.add(1)
print("同じ要素を追加:", set1)
# 出力：{1}

# int型の1とstr型の1はもちろん違う値なので両方セットされる
set1.add("1")
print("違う型を追加:", set1)
# 出力：{1, '1'}

### 要素の削除：
# セットから要素を指定して削除するには、remove() か discard() を使用する

set2 = {"咲季", "ことね", "手毬"}
print("集合set2の初期状態:", set2)

# remove()で削除
set2.remove("ことね")
print("remove()でことねを削除:", set2)
# 出力：{'咲季', '手毬'}

# discard()で削除
set2.discard("手毬")
print("discard()で手毬を削除:", set2)
# 出力：{'咲季'}

### 集合にない要素を削除しようとした時、remove()はエラーが出る、discard()はエラーが出ない

# remove()で削除：エラーが出る
try:
    set2.remove("根緒先生")
except Exception as e:
    print("＊例外：", type(e), e)
# 出力：＊例外： <class 'KeyError'> '根緒先生'

# discard()で削除：例外は送出されない
try:
    set2.discard("星南")
except Exception as e:
    print("＊例外：", type(e), e)
