from bisect import bisect_left, bisect_right

n = int(input())
a = sorted(map(int, input().split()))

ans = 0
for ai in a:
    cnt1 = bisect_left(a, ai)
    cnt2 = bisect_right(a, ai)
    ans += ai * cnt1 - ai * (n - cnt2)
print(ans)
