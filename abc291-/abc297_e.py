from heapq import heappush, heappop


def main():
    ans = -1
    res = [0]
    for _ in range(K+1):
        while ans == res[0]:
            heappop(res)
        ans = heappop(res)
        for ai in A:
            heappush(res, ans + ai)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))

    main()
