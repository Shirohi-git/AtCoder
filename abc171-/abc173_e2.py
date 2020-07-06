n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

mia = sorted([i for i in a if i < 0], reverse=True)
pla = sorted([i for i in a if i >= 0])

cnt = 1
if len(pla) == 0 and k % 2 == 1:
    for i in mia[:k]:
        cnt = cnt * i % mod
    print(cnt)
    exit()

while k > 0:
    if k == 1 or len(mia) <= 1:
        if len(pla) == 0:
            cnt *= mia.pop()
        elif len(pla) > 0:
            cnt *= pla.pop()
        k -= 1
    elif len(pla) <= 1:
        cnt *= mia.pop() * mia.pop()
        k -= 2
    elif pla[-1] * pla[-2] > mia[-1] * mia[-2]:
        cnt *= pla.pop()
        k -= 1
    elif pla[-1] * pla[-2] <= mia[-1] * mia[-2]:
        cnt *= mia.pop() * mia.pop()
        k -= 2
    cnt %= mod
else:
    print(cnt)
