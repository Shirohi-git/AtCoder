def main():
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            diff = B[i][j] - A[i][j]
            if diff == 0:
                continue
            ans += abs(diff)
            for x, y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                A[i+x][j+y] += diff
    return print(*(['Yes', ans] if A==B else ['No']), sep='\n')


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    main()
