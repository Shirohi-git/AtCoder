n = int(input())
s = [set(input()) for _ in range(n)]

ans = []
for i in range(n // 2):
    for strin in s[i]:
        if strin in s[n - i - 1]:
            ans.append(strin)
            break
    else:
        print(-1)
        exit()

rev_ans = ans[::-1]
if n % 2 == 1:
    l = list(s[n // 2])
    ans += l[0]
ans += rev_ans
print(*ans, sep='')
