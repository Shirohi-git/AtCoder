def main():
    for s, t in ST:
        print(A[s-1][t-1])
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    ST = [list(map(int, input().split())) for _ in range(Q)]

    main()
