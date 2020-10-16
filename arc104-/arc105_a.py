from itertools import product

cookie = list(map(int, input().split()))

sumc, ans = sum(cookie), 0
for bit in product([0, 1], repeat=4):
    tmp = sum(bi * ci for bi, ci in zip(bit, cookie))
    ans += (2 * tmp == sumc)
print('Yes' if ans > 0 else 'No')
