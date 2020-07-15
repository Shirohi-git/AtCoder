n = int(input())
a = list(map(int, input().split()))

b = [-1] * n
for i in range(n, 0, -1):
    cnt = sum(b[j - 1] for j in range(i + i, n + 1, i))
    b[i - 1] = int(a[i - 1] != cnt % 2)

print(sum(b))
if sum(b) > 0:
    print(*[i + 1 for i in range(n) if b[i] == 1])
