n = int(input())
a = list(map(int, input().split()))

cnt, high = 0, 0
for ai in a:
    cnt += max(0, high - ai)
    high = max(high, ai)
print(cnt)
