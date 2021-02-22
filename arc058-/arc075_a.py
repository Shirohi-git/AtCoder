n = int(input())
s = sorted([int(input()) for _ in range(n)])

ans = sum(s)
for si in s:
    if ans % 10 == 0 and si % 10 > 0:
        ans -= si
        break
print(ans if ans % 10 else 0)
