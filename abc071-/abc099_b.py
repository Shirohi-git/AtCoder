def main():
    idx = B - A
    b = idx * (idx+1) // 2
    return print(b - B)


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
