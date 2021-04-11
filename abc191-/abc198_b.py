n = input()
res = (n == n[::-1])
for i in range(10):
    n = '0' + n
    res |= (n == n[::-1])
print('Yes' if res else 'No')
