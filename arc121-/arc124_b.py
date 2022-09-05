def main():
    ans, x = set(), [A[0] ^ bi for bi in B]
    for xj in x:
        ax = sorted([ai ^ xj for ai in A])
        if ax == B:
            ans.add(xj)
    return print(*([len(ans)] + sorted(ans)), sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split()))

    main()
