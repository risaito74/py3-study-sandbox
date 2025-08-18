# 問題集13章：問題30
# raise文による例外の送出

# raise文は、プログラム内で意図的に例外を発生させるために使用される
# デバッグ用じゃなくて、実用のバリデーションとかでバリバリ使うよ！

def set_age(age: int):
    """ 年齢のバリデーションと登録処理 """
    if  age > 130:
        raise ValueError(f"年齢が著しく高齢です。正しい値か確認してください: {age}")
    elif age <= 0:
        raise ValueError(f"年齢の値が不正です: {age}")
    print(f"{age}歳を登録しました")

try:
    age = int(input("年齢を入力してください："))
    set_age(age)
except Exception as e:
    print("例外：", type(e), e)
