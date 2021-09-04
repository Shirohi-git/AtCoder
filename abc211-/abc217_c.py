def main():
    Q = [-1] * N
    for i, pi in enumerate(P):
        Q[pi-1] = i+1
    return print(*Q)


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    main()
