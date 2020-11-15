from itertools import accumulate

n, w = map(int, input().split())
stp = [list(map(int, input().split())) for _ in range(n)]

cnt = [0] * (2 * 10 ** 5 + 1)
for s, t, p in stp:
    cnt[s] += p
    cnt[t] -= p
acc = list(accumulate(cnt))
ans = all(ai <= w for ai in acc)
print('Yes' if ans else 'No')
