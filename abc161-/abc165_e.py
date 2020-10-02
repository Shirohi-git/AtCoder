n, m = map(int, input().split())

# 解説AC
c = n // 2 + 1
for i in range(1, m + 1):
    if i % 2:
        print(1 + i // 2, n - i // 2)
    elif 1 - i % 2:
        print(c + i // 2, c - i // 2)
