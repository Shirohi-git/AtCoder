h, w, a, b = map(int, input().split())
mat = [[0 for j in range(w)] for i in range(h)]
for i in range(b, h):
    for j in range(a):
        mat[i][j] = 1
for i in range(b):
    for j in range(a, w):
        mat[i][j] = 1
for _ in mat:
    print(*_,sep='')
