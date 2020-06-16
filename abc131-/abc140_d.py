n, k = map(int, input().split())
s = input()

cnt = n - 1 - s.count('LR') - s.count('RL')
ans = min(n - 1, 2 * k + cnt)
print(ans)
