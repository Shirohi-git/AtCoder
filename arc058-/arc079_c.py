n = int(input())
a = list(map(int, input().split()))

ans = 0
while max(a) >= n:
    cnt = sum(ai // n for ai in a)
    a = [ai + cnt - (n + 1) * (ai // n) for ai in a]
    ans += cnt
print(ans)
