def main():
    def grid_bfs(s0):
        que = [s0]
        near = [(0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1)]
        for qx, qy in que:
            for dx, dy in near:
                p = qx+dx, qy+dy
                if p in XY and p not in flag:
                    flag.add(p)
                    que.append(p)
        return

    ans = 0
    flag = set()
    for xy in XY:
        if xy not in flag:
            grid_bfs(xy)
            ans += 1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = set(tuple(map(int, input().split())) for _ in range(N))

    main()
