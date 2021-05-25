n = int(input())
a, b, c = sorted(map(int, input().split()))[::-1]

ans = 10**5
for i in range(n//a + 1):
    for j in range((n-i*a)//b + 1):
        div, mod = divmod(n - a*i - b*j, c)
        if mod == 0:
            ans = min(ans, i+j+div)
print(ans)
