def main():
    p_k = sorted(P)[-K]
    for pi in P:
        print("Yes" if pi+300 >= p_k else "No")
    return


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = [sum(map(int, input().split())) for _ in range(N)]

    main()
