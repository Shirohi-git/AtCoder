n, m = map(int, input().split())
lrc = sorted(tuple(map(int, input().split())) for _ in range(m))

lst = [0] + [10 ** 15] * (n - 1)

print(-1 if ans == 10 ** 15 else ans)
