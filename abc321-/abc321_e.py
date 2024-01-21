def child_count(x, k):
    ans = 0
    if k <= 100 and (x << k) <= N:
        c = x << k
        ans += min(N - c + 1, 1 << k)
    return ans


def main():
    ans = child_count(X, K)

    # parent
    if K > 0:
        ans += ((X >> K) > 0)

    # child
    x, k = X, K
    while x > 1 and k > 1:
        ans += child_count(x ^ 1, k - 2)
        x >>= 1
        k -= 1
    return print(ans)


if __name__ == '__main__':
    T = int(input())
    NXK = [list(map(int, input().split())) for _ in range(T)]
    for t in range(T):
        N, X, K = NXK[t]
        main()
