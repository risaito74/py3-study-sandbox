# 5章データ構造：collections.deque
# collectionsとは？：標準ライブラリのモジュール。リストや辞書を拡張した高機能データ構造を提供する
# dequeとは？：デック（両端キュー）＝「Double Ended Queue」の略。両端からの追加・削除が高速

# collectionsモジュールからdequeクラスをインポートして使用する
from collections import deque
import random

# リストをキューとして使う：collections.deque版 （＊リスト版はc05_list_queue.py参照）
# キュー：先入れ先出し（first-in, first-out）先に来た人から帰る

#リストをdeque型データにする
que_mem = deque(["花海咲季", "月村手毬", "藤田ことね", "紫雲清香", "倉本千奈", "葛城リーリヤ", "花海佑芽"])

que_join = deque(["根尾亜紗里"])
turn_num = 20 # ターン数
for i in range(turn_num):
    print(f"会場にいる人：{list(que_join)}")
    r = random.randint(1, 6) # 六面ダイスの疑似的な乱数

    if r >= 3: # 来た（ダイス3~6）
        mem = que_mem.popleft() # deque独自のメソッド
        print(f"{mem} が来た")
        que_join.append(mem)
        # 参加者が全員来たら終了
        if len(que_mem) <= 0:
            print("参加予定者が全員来たので終了")
            print(f"最後まで会場にいた人：{list(que_join)}")
            break

    else: # 帰る
        if que_join: # 会場に人いる
            mem = que_join.popleft() # deque独自のメソッド
            print(f"{mem} が帰った")
        else: # 会場に人いない
            print("会場には誰もいない…")
