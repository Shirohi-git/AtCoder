n = int(input())
a = set(map(int, input().split()))

n, r = max(a), -pow(10, 9)
a.remove(n)
for ai in a:
    if abs(n // 2 - r) > abs(n // 2 - ai):
        r = ai
print(n, r)
