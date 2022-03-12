def main():
    ans = sum(ai == bi for ai, bi in zip(A, B))
    print(ans)

    ans = len(set(A) & set(B)) - ans
    print(ans)
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
