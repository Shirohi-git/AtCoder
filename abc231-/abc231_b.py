def main():
    from collections import Counter

    cnt = Counter(S)
    ans = max(cnt, key=lambda x: cnt[x])
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()
