n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i, ai in enumerate(a):
    if (i + 1) % 2 == 1 and ai % 2 == 1:
        cnt += 1
print(cnt)
