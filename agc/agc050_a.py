def main():
    for i in range(N):
        print((2*i) % N + 1, (2*i+1) % N + 1)
    return


if __name__ == '__main__':
    N = int(input())

    main()
