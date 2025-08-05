# strip()系のテスト

### 引数がない場合
# strip():先頭と末尾の空白文字を削除
# lstrip():先頭の空白文字を削除
# rstrip():末尾の空白文字を削除
# 空白文字は、半角スペース、全角スペース、改行(\n)、改ページ(\f)、タブ(\t)、垂直タブ(\v)、復帰(\r)を表す

# リストの作成（data2,data3は不要な半角スペースがある）
data = ["data1", "  data2", "data3  "]

# リストをそのまま表示
print("strip()前:", data)

for i in range(len(data)):
    # リストの各要素をstrip()で、前後の空白文字を削除
    data[i] = data[i].strip()

# 削除後のリストを表示
print("strip()後:", data)
# 出力：['data1', 'data2', 'data3']

### 引数を指定する場合
# str.strip(chars)
# 引数charsは、削除したい文字の組み合わせを指定する

data = ["＊データ1。", "※データ2。", "・データ3。"]

# リストをそのまま表示
print("strip()前:", data)

for i in range(len(data)):
    # リストの各要素をstrip()で、前後の指定文字を除外
    data[i] = data[i].strip("＊※・。")

# 削除後のリストを表示
print("strip()後:", data)
# 出力：['データ1', 'データ2', 'データ3']
