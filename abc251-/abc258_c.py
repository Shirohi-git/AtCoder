def main():
    idx = 0
    for t, x in Query:
        if t == 1:
            idx = (idx - x) % N
        if t == 2:
            print(S[(idx+x-1) % N])
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    S = input()
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
