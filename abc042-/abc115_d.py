n, x = map(int, input().split())

pate, slice = [1], [1]
for _ in range(n+1):
    pate.append(2 * pate[-1] + 1)
    slice.append(2 * slice[-1] + 3)

ans = 0
while n >= 0 and x > 0:
    if n == 0 and x > 0:
        ans += 1
        x -= 1
    elif x >= slice[n - 1] + 2:
        ans += pate[n - 1] + 1
        x -= slice[n - 1] + 2
    elif x < slice[n - 1] + 2:
        x -= 1
    n -= 1
print(ans)
