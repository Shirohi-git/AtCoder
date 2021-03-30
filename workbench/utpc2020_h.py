from collections import deque

h, w = map(int, input().split())
s = [input() for _ in range(h)]

hlst, wlst = [[0, 0] for _ in range(h)], [[0, 0] for _ in range(w)]
hset, wset = set(range(h)), set(range(w))
for i, si in enumerate(s):
    for j, sij in enumerate(si):
        idx = ['.', '#'].index(sij)
        hlst[i][idx] += 1
        wlst[j][idx] += 1
hque = deque([i for i, (w, b) in enumerate(hlst) if w * b == 0])
wque = deque([j for j, (w, b) in enumerate(wlst) if w * b == 0])

ans = 0
while hque or wque:
    mque, mset, mlst = wque, wset, wlst
    sque, sset, slst = hque, hset, hlst
    if (len(hset) > len(wset) and hque) or (not wque):
        mque, mset, mlst = hque, hset, hlst
        sque, sset, slst = wque, wset, wlst

    q = mque.popleft()
    if q in mset:
        mset.remove(q)
    if sum(mlst[q]) == 0:
        continue
    c = (mlst[q][0] == 0)
    ans += 1
    for i in sset:
        slst[i][c] -= 1
        if slst[i][c] == 0:
            sque.append(i)
print(ans)
