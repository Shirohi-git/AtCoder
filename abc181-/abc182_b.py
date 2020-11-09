n = int(input())
a = list(map(int, input().split()))

ans, cnt = 0, 0
for i in range(2, 1001):
    tmp = sum(ai % i == 0 for ai in a)
    if tmp > cnt:
        ans, cnt = i, tmp
print(ans)
