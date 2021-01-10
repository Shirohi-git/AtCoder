n = int(input())
a = list(map(int, input().split()))

ans = a[:]
for i in range(n-1):
    a = [max(i, j) for i, j in zip(a[::2], a[1::2])]
print(ans.index(min(a)) + 1)
