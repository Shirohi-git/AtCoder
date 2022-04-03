def main():
    d = (A**2 + B**2)**0.5
    return print(A/d, B/d)


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
