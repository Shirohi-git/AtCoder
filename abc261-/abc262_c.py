def main():
    ans, eql = 0,0
    for i, ai in enumerate(A, 1):
        if i == ai:
            eql += 1
        elif A[ai-1] == i and i < ai:
            ans += 1
    ans += eql * (eql-1) // 2
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
