n = int(input())

ans = n
for b in range(61):
    a, c = divmod(n, pow(2, b))
    ans = min(ans, a+b+c)
print(ans)
