n = int(input())
a = sorted(map(int, input().split()))

ai, aj = a[-1], a[-2]
for i in a[:-1]:
    if abs(ai - 2 * aj) > abs(ai - 2 * i):
        aj = i
print(ai, aj)
