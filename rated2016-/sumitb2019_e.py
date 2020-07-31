n = int(input())
a = list(map(int, input().split()))
mod = 1000000007


ans, cnt = 1, [0, 0, 0]
for i in a:
    ans = ans * cnt.count(i) % mod
    for j in range(3):
        if cnt[j] == i:
            cnt[j] += 1
            break
print(ans)
