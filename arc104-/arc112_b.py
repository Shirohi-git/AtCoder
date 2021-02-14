b, c = map(int, input().split())

cnt = 0
if b > 0:
    cnt += min(c // 2 + 1, b + 1) + max(c - 2, 0) // 2
    cnt += min((c - 1) // 2, b - 1) + (c - 1) // 2 + 1
elif b == 0:
    cnt += c // 2 + (c - 1) // 2 + 1
elif b < 0:
    b *= -1
    cnt += c // 2 + 1 + min(max(c - 2, 0) // 2, b - 1)
    cnt += (c - 1) // 2 + min((c - 1) // 2 + 1, b + 1)
print(cnt)
