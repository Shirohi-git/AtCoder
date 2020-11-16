a, b, k = map(int, input().split())
cnt = 0
for i in range(1, 101)[::-1]:
    cnt += (a % i == 0) & (b % i == 0)
    if cnt == k:
        exit(print(i))
