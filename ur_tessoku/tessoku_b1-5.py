# B04
print(int(input(), 2))

# B03
N = int(input())
A = list(map(int, input().split()))
res = 0
for i, ai in enumerate(A):
    for j, aj in enumerate(A[:i]):
        res |= any(ai+aj+ak == 1000 for ak in A[:j])
print('Yes' if res else 'No')

# B02
A, B = map(int, input().split())
res = any(100 % i == 0 for i in range(A, B+1))
print('Yes' if res else 'No')

# B01
print(sum(map(int, input().split())))
