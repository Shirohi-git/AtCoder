from itertools import product

n = int(input())

if n % 2:
    exit(print())
for bit in product([0, 1], repeat=n):
    a, b = 0, 0
    ans = []
    for bi in bit:
        a, b = a + (1-bi), b + bi
        ans.append(")" if bi else "(")
        if a < b or a > n//2:
            break
    if a == b:
        print(*ans, sep='')
