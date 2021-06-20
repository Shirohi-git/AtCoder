from collections import Counter


def main():
    Acnt = Counter(ai % D for ai in A)
    Bcnt = Counter(bi % D for bi in B)
    Ccnt = Counter(ci % D for ci in C)

    ans = 0
    for i in range(D):
        for j in range(D):
            k = (D-i-j) % D
            ans += Acnt[i] * Bcnt[j] * Ccnt[k]
    return print(ans)


if __name__ == '__main__':
    N, D = int(input()), 46
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    main()
