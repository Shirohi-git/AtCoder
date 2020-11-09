from itertools import product

x, y, z, k = map(int, input().split())
a = sorted(map(int, input().split()))[::-1]
b = sorted(map(int, input().split()))[::-1]
c = sorted(map(int, input().split()))[::-1]

ab = [ai + bi for ai, bi in product(a, b)]
ab = sorted(ab)[:-k-1:-1]

abc = [abi + ci for abi, ci in product(ab, c)]
abc = sorted(abc)[:-k-1:-1]
print(*abc, sep='\n')
