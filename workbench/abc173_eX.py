n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

mia, pla = [], []
for ai in a:
    if ai < 0:
        mia.append(ai)
    elif ai >= 0:
        pla.append(ai)
mia.sort(reverse=True)
pla.sort()

ans, cnt = 1,[]
for _ in range(k):
    if len(mia) > 0 and len(pla) > 0:
        if abs(mia[-1]) <= pla[-1]:
            tmp = pla.pop()
        elif abs(mia[-1]) > pla[-1]:
            tmp = mia.pop()
    elif len(mia) == 0:
        tmp = pla.pop()
    elif len(pla) == 0:
        tmp = mia.pop()
    cnt.append(tmp)
    ans = ans * tmp % mod
print(cnt)
if k != n and ans < 0:
    for i in range(len(cnt), 0, -1):
        print(cnt[i])
        if cnt[i] < 0:
            pass
            

