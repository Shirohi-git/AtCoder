def main():
    ans = [0, 0, 0]
    for si, si1 in zip(S, S[1:]):
        ans.append(ans[-3] + si1 - si)
    for i in range(3):
        mn = min(ans[i::3])
        ans[i::3] = [ai - mn for ai in ans[i::3]]
    diff = S[0] - sum(ans[:3])
    if diff < 0:
        return print("No")
    print("Yes")
    ans[::3] = [ai + diff for ai in ans[::3]]
    return print(*ans)


if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))

    main()