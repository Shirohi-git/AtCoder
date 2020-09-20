n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for d1, d2 in d:
    ans = (ans + 1) * (d1 == d2)
    if ans >= 3:
        break
print('Yes' if ans >= 3 else 'No')
