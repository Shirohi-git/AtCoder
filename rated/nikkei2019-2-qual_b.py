from collections import Counter

n = input()
d = list(map(int, input().split()))
mod = 998244353

dcnt = Counter(d)
if d[0] > 0 or dcnt[0] > 1:
    print(0)
else:
    ans = 1
    for i in dcnt:
        if i > 0:
            ans = ans * dcnt[i - 1]**dcnt[i] % mod
    print(ans)
