n = int(input())
d = sorted(list(map(int, input().split())) + [0])

# 解説AC 貪欲法
ans, cnt = [], 1
for num in d:
    ans.append(((num - 12) * cnt + 12) % 24)
    cnt *= -1

ans = sorted(ans + [i + 24 for i in ans])
s = min(ans[i] - ans[i - 1] for i in range(1, len(ans)))
print(s)
