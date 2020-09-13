n = int(input())
a = list(map(int, input().split()))

ans = any((i % 3) * (i % 5) for i in a if i % 2 == 0)
print('DENIED' if ans else 'APPROVED')
