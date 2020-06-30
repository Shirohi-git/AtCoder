n = int(input())
alp = [chr(i + 97) for i in range(26)]

ans = [[] for _ in range(n)]
ans[0] = ['a']
for i in range(1, n):
    for j in ans[i - 1]:
        for k in range(len(set(j)) + 1):
            ans[i].append(j + alp[k])
print(*ans[n - 1], sep='\n')
