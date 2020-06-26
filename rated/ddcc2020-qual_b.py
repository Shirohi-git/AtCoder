from itertools import accumulate

n = int(input())
a = list(accumulate(map(int, input().split())))

ans = a[-1]
for i in a:
    ans = min(ans,abs(2*i-a[-1]))
print(ans)