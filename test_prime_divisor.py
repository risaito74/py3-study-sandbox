# 約数求めてから素数かどうか判定する

# 約数をリストで返す関数
def get_divisor(n):
    """ 引数 n の約数をリストで返す """
    li = []
    for i in range(1,n+1):
        if n % i == 0:
            li.append(i)
    
    return li

# 素数かどうかを返す関数
def is_prime(n):
    """ 引数 n は素数か？をTrue/Falseで返す """
    li = get_divisor(n)

    return len(li) == 2

try:
    n = int(input("素数か調べたい整数を入力してください："))

    print(f"{n}は素数か？：{is_prime(n)}")
    print(f"{n}の約数：{get_divisor(n)}")
except Exception as e:
    print("例外：入力値が不正です。", type(e), e)
