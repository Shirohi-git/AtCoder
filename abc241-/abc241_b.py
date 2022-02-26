from collections import Counter

def main():
    for bi in B:
        A[bi] -= 1
    res = all(ai >= 0 for ai in A.values())
    return print('Yes' if res else 'No')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = Counter(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
