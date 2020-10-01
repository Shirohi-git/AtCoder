n, z, w = map(int, input().split())
a = list(map(int, input().split()))

# 解説AC
a = [w] + a
print(max(abs(a[-2] - a[-1]), abs(a[-1] - w)))
