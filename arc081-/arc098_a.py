n, s = int(input()), input()

ans, e, w = n, s.count('E'), 0
for i in s:
    if i == 'E':
        e -= 1
    ans = min(ans, e + w)
    if i == 'W':
        w += 1
print(ans)
