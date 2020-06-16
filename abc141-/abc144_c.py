n = int(input())

cnt = 0
for i in range(1, int(n ** 0.5)+1):
    if n % i == 0:
        cnt = max(cnt, i)

print(cnt + n//cnt - 2)
