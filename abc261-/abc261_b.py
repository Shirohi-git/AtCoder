def main():
    ans = "correct"
    for i in range(N):
        for j in range(i):
            if [A[i][j], A[j][i]].count('D') == 1:
                ans = "incorrect"
            elif A[i][j] == A[j][i] != 'D':
                ans = "incorrect"
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [list(input()) for _ in range(N)]

    main()
