n = int(input())
s, t = input().split()

ans = []
for si, ti in zip(s, t):
    ans += [si, ti]
print(*ans, sep='')
