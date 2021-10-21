def main():
    def kto10(num):
        res = 0
        for ni in num:
            res = res * K + int(ni)
        return res
    return print(kto10(A) * kto10(B))


if __name__ == '__main__':
    K = int(input())
    A, B = input().split()

    main()
