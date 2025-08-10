# 問題集8章 1.
# open() の mode引数

# 乱数生成用にrandomをインポート
import random

file_path = "./tmp/rand.txt"

print("r : 読み込み専用でオープン")
with open(file_path, "r", encoding="utf-8") as f:
    s = f.read().strip()
    print(s)

print("w : 新規書き込み専用でオープン")
with open(file_path, "w", encoding="utf-8") as f:
    r = random.randint(1,6) # 1~6の乱数
    f.write(f"{r}")
    print(f"書き込んだ数値: {r}")

print("a : 追加書き込みでオープン")
with open(file_path, "a", encoding="utf-8") as f:
    r = random.randint(1,6) # 1~6の乱数
    f.write(f"{r}")
    print(f"書き込んだ数値: {r}")

print("rb : 読み込み専用（バイナリモード）でオープン")
with open(file_path, "rb") as f:
    b = f.read()
    print(f"{b}, hex() = {b.hex()}")

print("a+ : 読み書き両用（追加書き込み）でオープン")
with open(file_path, "a+", encoding="utf-8") as f:
    r = random.randint(1,6) # 1~6の乱数
    f.write(f"{r}")
    print(f"書き込んだ数値: {r}")

    ### 書きこんだ後の状態を読み込み
    # 同じファイルで書き込んだ直後に読むときは flush() して seek() が作法

    # バッファをファイルに反映（writeを反映させる）
    f.flush()
    # シーク位置が末尾になってるから頭に設定
    f.seek(0)

    s = f.read().strip()
    print(s)
