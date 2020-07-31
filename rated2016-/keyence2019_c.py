n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted([ai - bi for ai, bi in zip(a, b)])
if sum(c) < 0:
    print(-1)
    exit()

ans, cnt = 0, 0
for i in c:
    if i >= 0:
        break
    ans += 1
    cnt += i
for i in c[::-1]:
    if cnt >= 0:
        print(ans)
        break
    ans += 1
    cnt += i
