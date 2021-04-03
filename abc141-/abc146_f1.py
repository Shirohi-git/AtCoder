n, m = map(int, input().split())
s = input()

#解説AC O(n) 公式解説ver.
now, ans = n, []
while now:
    for q in range(max(0, now - m), now):
        if s[q] == '0':
            ans.append(now - q)
            now = q
            break
    else:
        now, ans = 0, [-1]
print(*ans[::-1])
