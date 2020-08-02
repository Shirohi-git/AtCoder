k = int(input())

# 解説AC
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()

ans, num = 1, 7
while 1:
    if num % k == 0:
        print(ans)
        break
    ans += 1
    num = (num % k) * 10 + 7
