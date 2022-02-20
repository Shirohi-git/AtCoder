def main():
    ans, tube = [0], []
    for ai in A:
        if (not tube) or (tube[-1][0] != ai):
            ans.append(ans[-1] + 1)
            tube.append([ai, 1])
        elif tube[-1][0] == ai:
            if tube[-1][1] == ai-1:
                ans.append(ans[-1] - tube[-1][1])
                tube.pop()
            else:
                ans.append(ans[-1]+1)
                tube[-1][1] += 1
    return print(*ans[1:], sep='\n')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
