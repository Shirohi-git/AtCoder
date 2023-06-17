def main():
    def solve(i):
        for j in range(N-i):
            if S[j] == S[j+i]:
                return print(j)
        return print(N-i)

    for i in range(1, N):
        solve(i)

    return


if __name__ == '__main__':
    N = int(input())
    S = input()

    main()
