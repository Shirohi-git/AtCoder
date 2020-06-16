n, k = map(int, input().split())
a = list(map(int, input().split()))

ball = [0] * n
for i in a:
    ball[i - 1] += 1
ball.sort(reverse=True)

ans = n
for i in range(k):
    ans -= ball[i]
print(ans)
