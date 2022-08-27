def main():
    X = [3.5]
    for _ in range(N-1):
        nxt = sum(max(X[-1], ni) for ni in NUM)
        X += [nxt/6]
    return print(X[-1])


if __name__ == '__main__':
    N = int(input())
    NUM = [1, 2, 3, 4, 5, 6]

    main()
