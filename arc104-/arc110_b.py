from re import fullmatch

n, t = int(input()), input()

t = '11' * (t[:2] == '01') + '1' * (t[:2] == '10') + t
t += '10' * (t[-2:] == '01') + '0' * (t[-2:] == '11')

res = fullmatch('(110)*', t) or (len(t) == 1)
ans = 10 ** 10 - len(t) // 3 + (len(t) > 1)
print(ans + ans * (t == '1') if res else 0)
