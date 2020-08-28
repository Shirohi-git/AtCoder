x, y = map(int, input().split())

ans = any(2 * i + 4 * (x - i) == y for i in range(x + 1))
print('Yes' if ans else 'No')
