c = [list(map(int, input().split())) for _ in range(3)]

a = [c[i][0] - 0 for i in range(3)]
b = [c[0][j] - a[0] for j in range(3)]

res = 1
for i in range(3):
    for j in range(3):
        res *= (c[i][j] == a[i] + b[j])
print('Yes' if res else 'No')
