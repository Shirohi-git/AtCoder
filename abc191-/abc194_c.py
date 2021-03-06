n = int(input())
a = list(map(int, input().split()))

ans = 0
sa = sum(a)
for ai in a:
    ans += n * (ai ** 2) - ai * sa
print(ans)
