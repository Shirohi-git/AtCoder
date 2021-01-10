n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = sum(ai * bi for ai, bi in zip(a, b))
print('Yes' if ans == 0 else 'No')
