s = [input() for _ in range(3)]

d = {'a': 0, 'b': 1, 'c': 2}
nxt, cnt = 0, [0, 0, 0]
for _ in range(sum(len(si) for si in s)):
    now = nxt
    nxt = d[s[now][cnt[now]]]
    cnt[now] += 1
    if len(s[nxt]) <= cnt[nxt]:
        print(['A', 'B', 'C'][nxt])
        break
