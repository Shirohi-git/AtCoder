h = int(input())

cnt = 1
ans = 0
while cnt <= h:
    ans += cnt
    cnt *= 2

print(ans)
