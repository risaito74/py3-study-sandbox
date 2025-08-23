# ジェネレーターとしてyieldを活用するテスト
# ゾンビが無限に生成されるゲーム風テスト

import random

def generate_zombie():
    """ ゾンビを無限に生成する """
    i = 0
    hp = 100
    x, y = 0, 0
    while True:
        dic_z = {"id": i, "hp": hp, "x": x, "y": y}
        yield dic_z
        i += 1
        hp += random.randint(1,10)
        x = random.randint(0,9)
        y = random.randint(0,9)

# ジェネレーターオブジェクトを取得（このgzからnext()で生成する）
gz = generate_zombie()
# print(type(gz))
# <class 'generator'>

while True:
    # 生成したゾンビの辞書データを取得
    z = next(gz)
    print(f"座標{z["x"]},{z["y"]}に体力{z["hp"]}のゾンビ{z["id"]}が出現した！")

    cmd = input("コマンド？(1=さらに生成する, 2=ゲームオーバー)：")

    if cmd != "1":
        break

print("*** ゲームオーバー ***")
