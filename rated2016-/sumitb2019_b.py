def main():
    for x in range(MAX):
        if int(x * 1.08) == N:
            return print(x)
    return print(':(')


if __name__ == '__main__':
    N = int(input())
    MAX = 50000

    main()
