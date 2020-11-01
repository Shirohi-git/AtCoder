n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ans = sum(b * (b + 1) - a * (a - 1) for a, b in ab)
print(ans // 2)
