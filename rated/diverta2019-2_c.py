n = int(input())
a = sorted(map(int, input().split()))

plus, minus = a[0], a[-1]
ans = []
for ai in a[1:-1]:
    if ai < 0:
        ans.append((minus, ai))
        minus -= ai
    elif ai >= 0:
        ans.append((plus, ai))
        plus -= ai
else:
    ans.append((minus, plus))

print(minus - plus)
for x, y in ans:
    print(x, y)
