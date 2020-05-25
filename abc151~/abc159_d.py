n = int(input())
a = list(map(int, input().split()))
num = [0] * n
cnt = 0

for i in a:
    num[i - 1] += 1

for i in num:
    cnt += i * (i - 1)//2

for i in range(n):
    tmp = num[a[i]-1]
    ans = cnt - (tmp-1)
    print(ans)
