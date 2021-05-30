h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

row = [sum(ai) for ai in a]
col = [sum(a[i][j] for i in range(h)) for j in range(w)]
for i in range(h):
    for j in range(w):
        print(row[i] + col[j] - a[i][j], end=' ')
    print()
