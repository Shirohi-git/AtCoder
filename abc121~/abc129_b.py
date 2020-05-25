from itertools import accumulate

n = int(input())
w = [0] + list(accumulate(map(int, input().split())))

ans = w[n]
for i in range(1, n):
    ans = min(ans, abs(w[n] - 2 * w[i]))

print(ans)