def main():
    from itertools import permutations

    ans = sorted(set(permutations(S)))[K-1]
    return print(*ans, sep='')


if __name__ == '__main__':
    S, K = input().split()
    K = int(K)

    main()
