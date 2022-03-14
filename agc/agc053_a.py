def main():
    ans = min(abs(ai - aj) for ai, aj in zip(A, A[1:]))
    print(ans)
    if ans == 0:
        return

    basic = [ai // ans for ai in A]
    a_mod = [ai % ans for ai in A]
    for _ in range(ans):
        res = basic[:]
        for i in range(N+1):
            if a_mod[i] > 0:
                a_mod[i] -= 1
                res[i] += 1
        print(*res)
    return


if __name__ == '__main__':
    N, S = int(input()), input()
    A = list(map(int, input().split()))

    main()
