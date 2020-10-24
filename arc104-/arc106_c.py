n, m = map(int, input().split())

if m < 0 or m >= n - 1 >= 1:
    print(-1)
elif n - 1 > m >= 0 or n == 1:
    if n > 1:
        print(1, 2 * (m + 2))
    for i in range(1, n + 1):
        if i != m + 2:
            print(2 * i, 2 * i + 1)
