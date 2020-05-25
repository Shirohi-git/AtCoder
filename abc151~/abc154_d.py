import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = list(map(int, input().split()))

cnt = 0
dice = [(i+1)/2 for i in p]

ans = sum(dice[:k])
exp = sum(dice[:k])

for i in range(k, n):
    exp = exp-dice[i-k]+dice[i]
    ans = max(ans, exp)
print(ans)
