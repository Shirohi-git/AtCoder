def main():
    ans = sum([[i, i*100, i*10000] for i in range(1, 100)], [])
    print(len(ans))
    return print(*ans)


if __name__ == '__main__':
    W = int(input())

    main()
