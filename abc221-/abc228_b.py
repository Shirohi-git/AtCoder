def main():
    cnt = set()
    nxt = X
    while nxt not in cnt:
        cnt.add(nxt)
        nxt = A[nxt-1]
    return print(len(cnt))


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    main()
