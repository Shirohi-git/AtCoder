def main():
    ans = int(A+B+C) + int(B+C+A) + int(C+A+B)
    return print(ans)


if __name__ == '__main__':
    A, B, C = input()

    main()
