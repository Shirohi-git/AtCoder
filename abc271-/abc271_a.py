def main():
    ans = hex(N)[2:]
    return print(ans.upper().zfill(2))


if __name__ == '__main__':
    N = int(input())

    main()
