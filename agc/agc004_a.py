a, b, c = sorted(map(int, input().split()))

res = a % 2 + b % 2 + c % 2
print(a * b if res == 3 else 0)
