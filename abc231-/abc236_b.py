def main():
    from collections import Counter

    cnt = Counter(A)
    for k, v in cnt.items():
        if v < 4:
            ans = k
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
