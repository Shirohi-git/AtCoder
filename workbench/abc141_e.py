def Z_algo(S):
    bfo, N = 0, len(S)
    z = [0] * N
    for i in range(1, N):
        l = i - bfo
        if i + z[l] < bfo + z[bfo]:
            z[i] = z[l]
        elif i + z[l] >= bfo + z[bfo]:
            j = max(0, bfo + z[bfo] - i)
            while i + j < N and S[j] == S[i + j]:
                j += 1
            z[i], bfo = j, i
    return z


n, s = int(input()), input()

ans = 0
for stg in range(n):
    lst = Z_algo(s[stg:])
    res = max(ri for i, ri in enumerate(lst, 1) if ri < i)
    ans = max(ans, res)
print(ans)
