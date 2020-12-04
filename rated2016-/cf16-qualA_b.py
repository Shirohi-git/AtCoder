n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i, ai in enumerate(a):
    cnt += (a[ai - 1] == i + 1)
print(cnt // 2)
