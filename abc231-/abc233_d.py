from itertools import accumulate
from collections import Counter


def main():
    ans = 0
    acc = list(accumulate([0]+A))
    cnt = Counter()
    for ai in acc:
        ans += cnt[ai - K]
        cnt[ai] += 1
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    main()
