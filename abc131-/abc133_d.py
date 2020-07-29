n = int(input())
a = list(map(int, input().split()))

cnt, minus = 0, 1
for i in a:
    cnt += minus * i
    minus *= -1

x = [cnt]
for i in range(1,n):
    x.append(2 * a[i - 1] - x[i - 1])
print(*x)
