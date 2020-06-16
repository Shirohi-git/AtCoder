n = int(input())

cnt = 0
for i in range(n+1):
    if (i % 3 == 0) or (i % 5 == 0):
        continue
    cnt += i

print(cnt)
