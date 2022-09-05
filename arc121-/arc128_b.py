def main():

    def solve(rgb):
        ans = sum(rgb)
        mod3 = list(map(lambda x: x % 3, rgb))
        if len(set(mod3)) == 3:
            ans = -1
        for i in range(3):
            if mod3[i] == mod3[i-1]:
                cnt = max(rgb[i], rgb[i-1])
                ans = min(ans, cnt)
        return print(ans)

    for rgbi in RGB:
        solve(rgbi)
    return


if __name__ == '__main__':
    T = int(input())
    RGB = [list(map(int, input().split())) for _ in range(T)]

    main()
