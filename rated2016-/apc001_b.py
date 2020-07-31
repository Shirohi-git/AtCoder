n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = sum(b) - sum(a)
ans1, ans2 = 0, 0
for ai, bi in zip(a, b):
    ans1 += max(0, ai - bi)
    ans2 += max(0, (bi - ai + 1) // 2)
print('Yes' if max(ans1, ans2) <= cnt else 'No')
