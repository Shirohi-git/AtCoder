def main():
    s0, s1 = zip(*S)
    res = (N == len(set(S)))
    res &= all(s in 'HDCS' for s in s0)
    res &= all(s in 'A23456789TJQK' for s in s1)
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N = int(input())
    S = [input() for _ in range(N)]

    main()
