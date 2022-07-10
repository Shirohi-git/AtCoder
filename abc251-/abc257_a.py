def main():
    alp = []
    for i in range(26):
        alp += [chr(ord('A')+i)] * N
    return print(alp[X-1])


if __name__ == '__main__':
    N, X = map(int, input().split())

    main()
