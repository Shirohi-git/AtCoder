a, b, c = map(int, input().split())

b = pow(b, c, 4) + 4
print(pow(a % 10, b, 10))
