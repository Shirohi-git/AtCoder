n = int(input())
a = list(map(int, input().split()))

cnt, ans, num = 0, 0, 10 ** 10
for ai in a:
    cnt += (ai < 0)
    ans += abs(ai)
    num = min(num, abs(ai))
print(ans if cnt % 2 == 0 else ans - 2 * num)
