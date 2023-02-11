def main():
    flag = [0] * (X+2)
    flag[0] = 1
    for i in range(X):
        if (not flag[i]) or (i in B):
            continue
        for ai in A:
            flag[min(X+1, i+ai)] = 1
    return print('Yes' if flag[X] else 'No')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = set(map(int, input().split()))
    X = int(input())

    main()
