from collections import Counter


def main():
    bc = [B[ci-1] for ci in C]
    cnt_a, cnt_bc = Counter(A), Counter(bc)
    ans = sum(cnt_a[ai] * cnt_bc[ai]for ai in cnt_a)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    main()
