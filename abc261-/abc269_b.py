def main():
    ans = [-1, -1, -1, -1]
    for i, si in enumerate(S):
        if ans[0] < 0 and '#' in si:
            ans[0] = i+1
            ans[2] = si.index('#') + 1
            ans[3] = si[ans[2]:].index('.') + ans[2]
        elif ans[0] * ans[1] < 0 and '#' not in si:
            ans[1] = i
    return print(*ans[:2]), print(*ans[2:])


if __name__ == '__main__':
    S = [input()+'.' for _ in range(10)] + ['.']

    main()
