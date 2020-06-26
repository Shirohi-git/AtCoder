n, k = map(int, input().split())

ans = 1
ans += (n - k) * (k - 1) * 6
ans += (n - 1) * 3
print(ans / pow(n, 3))
