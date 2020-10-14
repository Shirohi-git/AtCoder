a, b = map(int, input().split())

# 解説ver
a -= 1
xa = (a * (1 - a % 2)) ^ ((a + 1) // 2 % 2)
xb = (b * (1 - b % 2)) ^ ((b + 1) // 2 % 2)
print(xa ^ xb)
