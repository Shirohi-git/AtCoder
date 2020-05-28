s = str(input())

num = [int(s[-1])]
for i in range(1, len(s)):
    tmp = num[-1] + pow(10, i, 2019) * int(s[-i - 1])
    num.append(tmp % 2019)

mod = [1] + [0] * 2018
ans = 0
for i in num:
    ans += mod[i]
    mod[i] += 1
print(ans)
