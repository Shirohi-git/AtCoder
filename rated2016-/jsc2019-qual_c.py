def main():
    ans, cnt, lr = (S[0] == 'B'), 1, 1
    for s1, s2 in zip(S, S[1:]):
        if s1 == s2:
            lr ^= 1
        if not lr:
            ans = ans * cnt % MOD1
            cnt -= 1
        else: # elif lr:
            cnt += 1
    if cnt != 0:
        return print(0)
    
    for i in range(N):
        ans = ans * (i+1) % MOD1
    return print(ans)


if __name__ == '__main__':
    N, S = int(input()), input()
    MOD1 = 10**9 + 7

    main()