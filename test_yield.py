# fizzbuzz
# 1からnまでの数字を画面に表示する
# 3の倍数のときは数字の代わりにFizzと表示する
# 5の倍数のときは数字の代わりにBuzzと表示する
# 3かつ5の倍数のときは数字の代わりにFizzBuzzと表示する

def fizzbuzz_y(limit):
    """ yieldで返すfizzbuzz関数 """
    i = 1
    while i <= limit:
        if i % 3 == 0 and i % 5 == 0:
            ans = "FizzBuzz"
        elif i % 3 == 0:
            ans = "Fizz"
        elif i % 5 == 0:
            ans = "Buzz"
        else:
            ans = i
        
        yield ans
        i += 1

def fizzbuzz_r(i):
    """ returnで返すfizzbuzz関数 """
    if i % 3 == 0 and i % 5 == 0:
        ans = "FizzBuzz"
    elif i % 3 == 0:
        ans = "Fizz"
    elif i % 5 == 0:
        ans = "Buzz"
    else:
        ans = i
        
    return ans

# yieldでfizzbuzz
for i in fizzbuzz_y(20):
    print(i)

# returnでfizzbuzz
for i in range(1, 21):
    print(fizzbuzz_r(i))

