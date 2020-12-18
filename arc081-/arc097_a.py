s, k = input(), int(input())

ans = set()
for alp in sorted(set(s)):
    for i, si in enumerate(s):
        if si == alp:
            ans |= {s[i:i + j + 1] for j in range(k)}
    if len(ans) >= k:
        exit(print(sorted(ans)[k - 1]))
