n, a, b = map(int, input().split())

if (n == 1) or (a > b):
    print(1 if a == b else 0)
else:
    print((n - 2) * (b - a) + 1)
