def main():
    pos = [(i, j) for i in range(9) for j in range(9)]
    ans = 0
    for ax, ay in pos:
        for bx, by in pos:
            if ax > bx or ay >= by:
                continue
            x, y = ax-bx, ay-by
            cx, cy, dx, dy = bx+y, by-x, ax+y, ay-x
            if any(z not in range(9) for z in [cx, cy, dx, dy]):
                continue
            if '.' in [S[ax][ay], S[bx][by], S[cx][cy], S[dx][dy]]:
                continue
            ans += 1
    return print(ans)


if __name__ == '__main__':
    S = [input() for _ in range(9)]

    main()
