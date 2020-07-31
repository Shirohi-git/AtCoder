k, t = map(int, input().split())
a = sorted(list(map(int, input().split())))
print(2 * a[-1] - k - 1 if a[-1] > k // 2 else 0)
