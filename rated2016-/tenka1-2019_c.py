n, s = int(input()), input()

ans, lb, rw = s.count('.'), 0, s.count('.')
for i in s:
    if i == '#':
        lb += 1
    elif i == '.':
        rw -= 1
    ans = min(ans, lb + rw)
print(ans)
