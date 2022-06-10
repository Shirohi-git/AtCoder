from itertools import accumulate

n, c = map(int, input().split())
stc = sorted(list(map(int, input().split())) for _ in range(n))

cnt, end = [0] * (10 ** 5 + 1), [0] * c
for s, t, ci in stc:
    cnt[s] += (s == end[ci - 1])
    cnt[s - 1] += (s != end[ci - 1])
    cnt[t] -= 1
    end[ci - 1] = t
acc = accumulate(cnt)
print(max(acc))
