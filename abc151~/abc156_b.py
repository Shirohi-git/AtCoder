import sys
input = sys.stdin.readline


n, k = map(int, input().split())
cnt, ans = 1, 0

while cnt <= n:
    cnt *= k
    ans += 1
print(ans)