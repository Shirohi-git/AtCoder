s = str(input())

if s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
elif len(s) == 26:
    tmp = ord(s[-1])
    for i in range(len(s))[::-1]:
        if ord(s[i]) < tmp:
            ans = sorted(s[i:])
            for j in ans:
                if ord(j) > ord(s[i]):
                    print(s[:i] + j)
                    exit()
        tmp = ord(s[i])
else:
    alpha = [chr(i) for i in range(97, 97 + 26)]
    for i in alpha:
        if i not in s:
            print(s + i)
            break
