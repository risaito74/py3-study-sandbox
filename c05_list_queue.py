# 5章データ構造：リストをキューとして使う(first-in, first-out)
# 公式本ではcollections.dequeを使うべきである。とあるが、いったんリストで実装する
# （長いリストだと遅くなるので非推奨だが、今回はリストをキューをとして使うテストなので、ヨシ！）
import random

#会場に来た人から帰る
li_mem = ["花海咲季", "月村手毬", "藤田ことね", "紫雲清香", "倉本千奈", "葛城リーリヤ", "花海佑芽"]

li_join = ["根尾亜紗里"]
offset = 0
turn_num = 20 # ターン数
for i in range(turn_num):
    print(f"会場にいる人：{li_join}")
    r = random.randint(1, 6) # 六面ダイスの疑似的な乱数

    if r >= 3: # 来た（ダイス3~6）
        print(f"{li_mem[offset]} が来た")
        li_join.append(li_mem[offset])
        offset += 1
        # offsetオーバーフロー判定（参加者が全員来たら終了）
        if offset >= len(li_mem):
            print("参加予定者が全員来たので終了")
            print(f"最後まで会場にいた人：{li_join}")
            break

    else: # 帰る
        if li_join: # 会場に人いる
            print(f"{li_join[0]} が帰った")
            li_join.pop(0)
        else: # 会場に人いない
            print("会場には誰もいない…")
