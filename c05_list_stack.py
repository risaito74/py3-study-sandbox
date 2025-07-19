# 5章データ構造：リストをスタックとして使う（LIFO: Last-in First-out）
li_st = []

box_n = 1
cmd = True
while cmd == True:
    print(f"スタックの状態 = {li_st}")

    # ゲームオーバー判定（積みすぎ、積み木切れ）
    if len(li_st) >= 5:
        print(f"積み木が多すぎて崩れてしまった！\n*** GAME OVER ***")
        break
    elif box_n > 10:
        print(f"積み木がもうない！\n*** GAME OVER ***")
        break

    n = input("スタックコマンドは？(1=積む, 2=取り出す, 他=終了)：")

    # 積み木を積む（スタックに追加）
    if n == "1":
        li_st.append(box_n)
        box_n += 1

    # 積み木を取り出す（スタックから取り出す）
    elif n == "2":
        if li_st: # リストに要素があるか？
            li_st.pop()
        else:
            print("リストは空です")

    # 終了
    else:
        print("終了します")
        break
