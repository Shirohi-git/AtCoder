s, k = input(), int(input())

for i in range(k):
    if s[i] != '1' or i + 1 >= k:
        exit(print(s[i]))
