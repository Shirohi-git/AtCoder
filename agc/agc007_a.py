h, w = map(int, input().split())
a = sum(input().count('#') for _ in range(h))
print('Possible' if a == h + w - 1 else 'Impossible')
