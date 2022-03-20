def main():
    flag = [0] * (2*N+2)
    flag[0] = 1
    nxt = 0
    for _ in range(N+1):
        while flag[nxt] > 0:
            nxt += 1
        print(nxt)
        flag[nxt] = 1
        flag[int(input())] = 1
    return


if __name__ == '__main__':
    N = int(input())

    main()
