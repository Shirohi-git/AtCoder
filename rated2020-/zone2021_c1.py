n = int(input())
stt = [list(map(int, input().split())) for _ in range(n)]

# 別解ver. O(n**2)
ans = 0
maxlst = [max(si[i] for si in stt) for i in range(5)]
for i, si in enumerate(stt):
    for sj in stt[i:]:
        tmp = [max(si[k], sj[k]) for k in range(5)]
        idx = tmp.index(min(tmp))
        tmp[idx] = maxlst[idx]
        ans = max(ans, min(tmp))
print(ans)
