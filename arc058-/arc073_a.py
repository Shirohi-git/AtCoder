n, T = map(int, input().split())
t = list(map(int, input().split())) + [10 ** 10]

ans = 0
for i in range(n):
    ans += min(T, t[i + 1] - t[i])
print(ans)
