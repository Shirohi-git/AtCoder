from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]

num, seta = Counter(a), set(a)
for b, c in bc:
    num[c] += b
    seta.add(c)
sorta = sorted(list(seta), reverse=True)

cnt, ans = n, 0
for i in sorta:
    ans += i * min(num[i], cnt)
    cnt -= num[i]
    if cnt <= 0:
        break
print(ans)
