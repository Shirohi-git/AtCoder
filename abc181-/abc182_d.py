from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

acc = list(accumulate(a))
plus, pos, ans = 0, 0, 0
for i in range(n):
    plus = max(plus, acc[i])
    ans = max(ans, pos + plus)
    pos += acc[i]
print(ans)
