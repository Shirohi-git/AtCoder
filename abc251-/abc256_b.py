def main():
    grid = [0, 0, 0, 0, 0]
    for ai in A:
        grid[0] += 1
        for j in range(4)[::-1]:
            grid[min(4, j+ai)] += grid[j]
            grid[j] = 0
    return print(grid[-1])


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
