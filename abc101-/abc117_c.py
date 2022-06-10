n, m = map(int, input().split())
x = sorted(map(int, input().split()))

cnt = sorted([x[i] - x[i - 1] for i in range(1, m)])
print(sum(cnt[:m-n]) if m > n else 0)
