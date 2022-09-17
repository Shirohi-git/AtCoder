def main():
    res = 0
    b = min(-1, B)
    if A < 0 and (b-A+1) % 2:
        res = 2
    if A <= 0 <= B:
        res = 1
    return print(["Positive", "Zero", "Negative"][res])


if __name__ == '__main__':
    A, B = map(int, input().split())

    main()
