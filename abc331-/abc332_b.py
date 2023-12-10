def main():
    g, m = 0, 0
    for _ in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        else:
            g, m = min(G, m), max(0, m-G+g)
    return print(g, m)


if __name__ == '__main__':
    K, G, M = map(int, input().split())

    main()
