n, k = map(int, input().split())
a = sorted(map(int, input().split()))
mod = 10 ** 9 + 7

mia, pla, zero = [], [], []
for ai in a:
    if ai < 0:
        mia.append(ai)
    elif ai > 0:
        pla.append(ai)
    elif ai == 0:
        zero.append(ai)

cnt = 1
while k > 0:
    if len(pla) == 0 and len(mia) == 0:
        print(0)
        break
    elif len(pla) == 0:
        cnt = cnt * mia.pop() % mod
        k -= 1
    elif len(mia) <= 1 or k == 1:
        cnt = cnt * pla.pop() % mod
        k -= 1
    elif len(pla) == 1:
        if k % 2 == 1:
            cnt = cnt * pla.pop() % mod
            k -= 1
        elif k % 2 == 0 and len(mia) >= 2:
            cnt = cnt * mia.pop() * mia.pop() % mod
            k -= 2
        elif k % 2 == 0 and len(mia) == 1:
            cnt = cnt * pla.pop() % mod
            k -= 1
    elif len(pla) >= 2 and len(mia) >= 2:
        if pla[-1] * pla[-2] >= mia[-1] * mia[-2]:
            cnt = cnt * pla.pop() % mod
            k -= 1
        elif pla[-1] * pla[-2] < mia[-1] * mia[-2]:
            cnt = cnt * mia.pop() * mia.pop() % mod
            k -= 2
else:
    print(cnt)
