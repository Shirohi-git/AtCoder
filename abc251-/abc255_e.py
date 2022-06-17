from collections import Counter


def main():
    a = [0]
    for si in S:
        a.append(si - a[-1])

    cnt = Counter()
    for i, ai in enumerate(a, 1):
        for xj in X:
            num = pow(-1, i) * (xj-ai)
            cnt[num] += 1
    return print(max(cnt.values()))


if __name__ == '__main__':
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    X = list(map(int, input().split()))

    main()
