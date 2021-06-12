def main():
    cost = [A[i] - A[i+1] for i in range(N-1)]
    ans = sum(abs(ci) for ci in cost)
    for l, r, v in LRV:
        if 0 <= l-2:
            ans += abs(cost[l-2] - v) - abs(cost[l-2])
            cost[l-2] -= v
        if r-1 < N-1:
            ans += abs(cost[r-1] + v) - abs(cost[r-1])
            cost[r-1] += v
        print(ans)
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    LRV = [list(map(int, input().split())) for _ in range(Q)]

    main()
