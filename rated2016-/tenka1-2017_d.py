n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

# 解説AC
ans = sum(b for a, b in ab if (k | a) == k)
for i in range(k.bit_length()):
    if (k >> i) & 1:
        num = (k - (1 << i)) | ((1 << i) - 1)
        tmp = sum(b for a, b in ab if (num | a) == num)
        ans = max(ans, tmp)
print(ans)
