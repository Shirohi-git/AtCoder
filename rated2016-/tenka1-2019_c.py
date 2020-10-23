n, s = int(input()), input()

ans = s.count('.')
lb, rw = 0, s.count('.')
for i in s:
    lb += (i == '#')
    rw -= (i == '.')
    ans = min(ans, lb + rw)
print(ans)
