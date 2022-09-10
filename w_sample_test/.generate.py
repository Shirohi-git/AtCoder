#!/usr/bin/python3

# ランダムケース入力
from random import randint, choice, choices, shuffle


# 木構造
def tree():
    n = randint(2, 100000)
    top = randint(1, n)
    lst = [i for i in range(1, n+1) if i != top]
    shuffle(lst)
    flag = [top]

    print(n)
    for i in lst:
        j = choice(flag)
        flag.append(i)
        print(j, i)


if __name__ == '__main__':
    pass
