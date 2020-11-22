n, s = int(input()), input()

ans, bfo = n, [0]
for i in range(n):
    if s[i] == 'f':
        bfo.append(1)
    elif s[i] == 'o' and bfo[-1] == 1:
        bfo[-1] += 1
    elif s[i] == 'x' and bfo[-1] == 2:
        ans -= bfo.pop() + 1
    else:
        bfo = [0]
print(ans)
