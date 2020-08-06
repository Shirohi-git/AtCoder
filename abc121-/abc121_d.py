a, b = map(int, input().split())

cnt = b - a + 1
cnt -= (a % 2 == 1) + (b % 2 == 0)
a, b = a * (a % 2 == 1), b * (b % 2 == 0)
print((cnt // 2 % 2) ^ a ^ b)
