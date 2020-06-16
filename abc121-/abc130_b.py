n, x = map(int, input().split())
l = list(map(int, input().split()))

cnt = 0
for i, li in enumerate(l):
    cnt += li
    if cnt > x:
        print(i + 1)
        break
else:
    print(n + 1)