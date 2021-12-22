def main():
    ans = [['.'] * (S-R+1) for _ in range(Q-P+1)]
    for k in range(max(P-A, R-B), min(Q-A, S-B)+1):
        ans[A+k-P][B+k-R] = '#'
    for k in range(max(P-A, B-S), min(Q-A, B-R)+1):
        ans[A+k-P][B-k-R] = '#'
    for ai in ans:
        print(*ai, sep='')
    return


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())

    main()
