def main():
    set_a = set(A[:-1])
    b = [i for i in range(N, 0, -1) if i not in set_a]

    ans = []
    for ai in A[:-1]:
        ans.append(ai)
        if ai > b[-1]:
            ans.append(b.pop())
    ans += b[::]
    return print(*ans)


if __name__ == '__main__':
    N, K= map(int, input().split())
    A = list(map(int, input().split()))

    main()