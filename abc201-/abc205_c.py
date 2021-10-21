def main():
    if C % 2 == 0:
        a, b = map(abs, [A, B])
        return print(Res[(a >= b) + (a > b)])
    return print(Res[(A >= B) + (A > B)])


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    Res = ['<', '=', '>']
    main()
