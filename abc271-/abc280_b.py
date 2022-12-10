def main():
    a = []
    for si, sj in zip(S, S[1:]):
        a.append(sj-si)
    return print(*a)


if __name__ == '__main__':
    N = int(input())
    S = [0] + list(map(int, input().split()))

    main()
