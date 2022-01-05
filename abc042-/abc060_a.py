def main():
    res = (A[-1] == B[0])
    res &= (B[-1] == C[0])
    return print('YES' if res else 'NO')


if __name__ == '__main__':
    A, B, C = input().split()

    main()
