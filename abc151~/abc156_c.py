import sys
input = sys.stdin.readline


n = int(input())
x = list(map(int, input().split()))

x2 = [i ** 2 for i in x]
ans = float('inf')
sum1 = sum(x)
sum2 = sum(x2)
for p in range(1, 101):
    cnt = sum2 + (sum(x) * (-1) * 2 * p) + (p**2*n)
    ans = min(ans, cnt)
print(ans)
