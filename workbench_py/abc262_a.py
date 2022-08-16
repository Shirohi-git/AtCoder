def main():
    mod = (2 - Y % 4) % 4
    return print(Y + mod)


if __name__ == '__main__':
    Y = int(input())

    main()
