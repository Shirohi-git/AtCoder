n, x = map(int, input().split())

print('Yes' if 1 < x < (2 * n - 1) else 'No')
if 1 < x < (2 * n - 1):
    cnt = [i for i in range(2, 2 * n - 1) if i != x]
    ans = cnt[n - 2:] + [1, x, 2 * n - 1] + cnt[:n - 2]
    print(*ans, sep='\n')
