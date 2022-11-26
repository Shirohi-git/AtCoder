def main():
    s = [si for si in zip(*S)]
    t = [ti for ti in zip(*T)]
    res = (sorted(s) == sorted(t))
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]

    main()
