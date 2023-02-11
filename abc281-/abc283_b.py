def main():
    a = A[:]
    for k, *q in Query:
        if k == 1:
            a[q[0]-1] = q[1]
        if k == 2:
            print(a[q[0]-1])
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    Query = [list(map(int, input().split())) for _ in range(Q)]

    main()
