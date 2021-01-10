x, y = map(int, input().split())

if x < y:
    x, y = y, x
print('Yes' if x < y + 3 else 'No')
