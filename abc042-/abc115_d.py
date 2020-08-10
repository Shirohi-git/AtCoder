n, x = map(int, input().split())

pate, slice = [1], [1]
for _ in range(n):
    pate.append(2 * pate[-1] + 1)
    slice.append(2 * slice[-1] + 3)

ans = 0
for i in range(n)[::-1]:
    if x >= slice[i] + 2:
        ans += pate[i] + 1
        x -= slice[i] + 2
    elif x < slice[i] + 2:
        x -= 1
print(ans + (x > 0))
