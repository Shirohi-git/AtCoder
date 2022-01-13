def main():
    plus = max([min(A), max(A)], key=lambda x: abs(x))
    idx = A.index(plus) + 1

    ans = [(idx, i+1) for i in range(N)]
    if plus > 0:
        ans += [(i+1, i+2) for i in range(N-1)]
    else:
        ans += [(N-i, N-i-1) for i in range(N-1)]

    print(len(ans))
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
