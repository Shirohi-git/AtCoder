n, x = map(int, input().split())
a = list(map(int, input().split()))

cnt, a[0] = sum(a), min(a[0], x)
for i in range(1, n):
    if a[i - 1] + a[i] > x:
        a[i] = x - a[i - 1]
print(cnt - sum(a))
