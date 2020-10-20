a, b, t = map(int, input().split())

cnt = sum(a * i <= t for i in range(1, 21))
print(b * cnt)
