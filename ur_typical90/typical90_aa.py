def main():
    dic = set()
    for i in range(N):
        if not A[i] in dic:
            dic.add(A[i])
            print(i+1)
    return


if __name__ == '__main__':
    N = int(input())
    A = [input() for _ in range(N)]

    main()
