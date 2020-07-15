from itertools import accumulate

n = int(input())
a = list(accumulate(map(int, input().split())))

ans = abs(a[n - 1] - 2 * a[0])
for i in range(1, n - 1):
    ans = min(ans, abs(a[n - 1] - 2 * a[i]))
print(ans)
