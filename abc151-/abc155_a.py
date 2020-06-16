a, b, c = map(int, input().split())

if (a == b) & (a == c):
    print('No')
elif (a == b) | (a == c) | (c == b):
    print('Yes')
else:
    print('No')
