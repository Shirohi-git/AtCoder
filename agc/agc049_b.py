n = int(input())
s, t = input() + '1', input() + '1'

scnt = 0
for si, ti in zip(s[::-1], t[::-1]):
    scnt += int(si)
    if int(ti) > 0 >= scnt:
        exit(print(-1))
    scnt -= int(ti)

ans, bfo, j = 0, -1, 0
for i in [idx for idx in range(n + 1) if int(t[idx])]:
    while j < i or bfo >= 0 or s[j] == '0':
        if int(s[j]):
            ans += (j - bfo) * (bfo >= 0)
            bfo = (j + 1) * (bfo < 0) - 1
        j += 1
    ans += j - i
    j += 1
print(ans)
