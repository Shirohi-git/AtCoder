from collections import Counter


def main():
    cnt = Counter(C[:K])
    ans = now = len(cnt)
    for ci, cj in zip(C, C[K:]):
        cnt[ci] -= 1
        now += (cnt[cj] == 0) - (cnt[ci] == 0)
        cnt[cj] += 1
        ans = max(ans, now)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    main()
