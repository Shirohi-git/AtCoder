n, m = map(int, input().split())

cnt = min(n, m // 2)
print(cnt + (m - cnt * 2) // 4)
