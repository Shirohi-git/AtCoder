def main():
    ans = (N > 4 or N == 1)
    return print("Yes" if ans else "No")


if __name__ == '__main__':
    N = int(input())

    main()