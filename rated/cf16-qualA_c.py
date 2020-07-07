s, k = input(), int(input())

ans = []
a = ord('z') + 1
for i in s:
    if a - ord(i) <= k and i != 'a':
        k -= a - ord(i)
        ans.append(ord('a'))
    else:
        ans.append(ord(i))
ans[-1] += k % 26
if ans[-1] >= a:
    ans[-1] -= 26
print(*map(chr, ans), sep='')
