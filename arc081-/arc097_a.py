s = input()
k = int(input())

ssort = sorted(set(s))
cnt, ans = 0, set()
while len(ans) < k:
    for i, si in enumerate(s):
        if si == ssort[cnt]:
            ans |= {s[i:i + j + 1] for j in range(k)}
    cnt += 1
print(sorted(ans)[k - 1])
