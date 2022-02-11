def main():
    a, b = map(int, A[::-1]), map(int, B[::-1])
    res = any(ai + bi > 9 for ai, bi in zip(a, b))
    return print('Hard' if res else 'Easy')


if __name__ == '__main__':
    A, B = input().split()

    main()
