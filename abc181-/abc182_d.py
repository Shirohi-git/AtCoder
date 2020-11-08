from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

acc = [0] + list(accumulate(a))
plus, pos, ans = 0, 0, 0
for i in range(n):
    plus = max(plus, acc[i + 1])
    ans = max(ans, pos + plus)
    pos += acc[i+1]
print(ans)
