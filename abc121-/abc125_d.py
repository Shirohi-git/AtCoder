n = int(input())
a = list(map(int, input().split()))

cnt = sum(i < 0 for i in a)
ans = sum(abs(i) for i in a)
if cnt % 2 == 0:
    print(ans)
elif cnt % 2 == 1:
    print(ans - 2 * min(abs(i) for i in a))
