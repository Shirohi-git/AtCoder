def main():
    bfo = [1]
    for i in range(1, N):
        print(*bfo)
        nxt = []
        for j in range(i+1):
            tmp = (1 if (j in [0, i]) else bfo[j-1] + bfo[j])
            nxt.append(tmp)
        bfo = nxt[:]
    return print(*bfo)


if __name__ == '__main__':
    N = int(input())

    main()
