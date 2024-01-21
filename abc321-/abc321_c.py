def main():
    bfo = num = [*range(1, 10)]
    while bfo:
        nxt = []
        for bi in bfo:
            for j in range(bi % 10):
                nxt.append(bi*10+j)
        num += nxt
        bfo = nxt
    print(num[K-1])


if __name__ == '__main__':
    K = int(input())
    main()
