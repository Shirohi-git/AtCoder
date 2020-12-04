from itertools import accumulate

n, k = map(int, input().split())
a = [0] + list(accumulate(map(int, input().split())))

b = []
for i in range(n):
    b += [a[j] - a[i] for j in range(i + 1, n + 1)]

ans = 0
for i in range(50)[::-1]:
    num = ans + (1<<i)
    cnt = sum(num & bi == num for bi in b)
    ans += (cnt >= k) * (num - ans)
print(ans)
