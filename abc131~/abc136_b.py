n = int(input())
ans = min(n, 9)
if n > 99:
    ans = min(n-90, 909)
if n > 9999:
    ans = n-9000-90
if n > 99999:
    ans = 90909
print(ans)
