n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

mia = sorted([i for i in a if i < 0], reverse=True)
pla = sorted([i for i in a if i >= 0])
ans, num = 1, []

if len(pla) == 0 and k % 2 == 1:
    for i in mia[:k]:
        ans = ans * i % mod
    print(ans)
    exit()

for _ in range(k):
    if len(mia) == 0 or (len(pla) > 0 and abs(mia[-1]) <= pla[-1]):
        tmp = pla.pop()
    elif len(pla) == 0 or (len(mia) > 0 and abs(mia[-1]) > pla[-1]):
        tmp = mia.pop()
    num.append(tmp)

cnt = sum(i < 0 for i in num)
for i in num:
    ans = ans * i % mod

if cnt % 2 == 1:
    p, q, r, s = 1, 0, -1, 0
    if len(mia) > 0 and cnt != k:
        p, q = min(i for i in num if i >= 0), mia[-1]
    if len(pla) > 0:
        r, s = max(i for i in num if i < 0), pla[-1]
    if len(mia) > 0 or (len(pla) > 0 and cnt != k):
        if q * r >= p * s:
            ans *= q * pow(p, mod - 2, mod)
        if q * r < p * s:
            ans *= s * pow(r, mod - 2, mod)
    ans %= mod
print(ans)
