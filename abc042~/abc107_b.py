h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

hlist, wlist = [], []
for i in range(h):
    if '#' in a[i]:
        hlist.append(i)
for j in range(w):
    if any(a[i][j] == '#' for i in range(h)):
        wlist.append(j)

for i in hlist:
    print(*[a[i][j] for j in wlist], sep='')
