def main():
    ans = (X > 0 and X % 100 == 0)
    return print("Yes" if ans else "No")


if __name__ == '__main__':
    X = int(input())

    main()