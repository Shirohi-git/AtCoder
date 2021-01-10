def nearlist(N):
	NEAR = [[] for _ in range(N)]
	for a, b in ab:
		a, b = a - 1, b - 1
		if c[a] == c[b]:
			NEAR[a].append(b)
			NEAR[b].append(a)
	return NEAR


def dfs(s):
	stack = [(i, s) for i in near[s]]
	flag[s] = 0
	while stack:
		q, p = stack.pop()
		if not ans[p * n + q]:
			ans[p * n + q], ans[q * n + p] = '->', '<-'
		if flag[q]:
			stack += [(r, q) for r in near[q]]
			flag[q] = 0


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]
c = list(map(int, input().split()))

flag, ans = [1] * n, [''] * n ** 2
near = nearlist(n)
for i in range(n):
	if flag[i]:
		dfs(i)
for a, b in ab:
	a, b = a - 1, b - 1
	if c[a] != c[b]:
		ans[a * n + b] = '->' if c[a] > c[b] else '<-'
	print(ans[a * n + b])
