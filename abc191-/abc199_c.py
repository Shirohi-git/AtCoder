n, s, q = int(input()), list(input()), int(input())
tab = [list(map(int, input().split())) for _ in range(q)]

cnt = 0
for t, *ab in tab:
    ai, bi = ((x-1 + cnt) % (2*n) for x in ab)
    s[ai], s[bi] = s[bi], s[ai]
    cnt ^= n * (t == 2)
print(*(s[n:]+s[:n] if cnt else s), sep='')
