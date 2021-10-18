def main():
    ans  = []
    for ti in T:
        ans.append(S[int(ti)-1])
    return print(*ans, sep='')


if __name__ == '__main__':
    S = [input() for _ in range(3)]
    T = input()

    main()
