n, k = map(int, input().split())

num = n
for i in range(k):
    small = sorted(str(num))
    large = small[::-1]
    num = int(''.join(large)) - int(''.join(small))
print(num)
