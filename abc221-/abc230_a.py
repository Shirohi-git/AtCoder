def main():
    res = str(N+(N > 41)).zfill(3)
    return print("AGC" + res)


if __name__ == '__main__':
    N = int(input())

    main()
