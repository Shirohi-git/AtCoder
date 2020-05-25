k, a, b = map(int, input().split())

if b > a + 1:
    ans = (k - a + 1) // 2 * (b - a) + a
    print(ans if (k - a + 1) % 2 == 0 else ans + 1)
if b <= a + 1:
    print(k + 1)
