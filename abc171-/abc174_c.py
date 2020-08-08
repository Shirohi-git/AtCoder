k = int(input())

# 解説AC
if k % 2 == 0 or k % 5 == 0:
    print(-1)
    exit()

num = 7
for i in range(k):
    if num % k == 0:
        print(i + 1)
        break
    num = (num % k) * 10 + 7
