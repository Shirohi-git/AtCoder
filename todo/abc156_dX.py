from math import factorial as fra

n, a, b = map(int, input().split())
fn = fra(n)
ans = 2**n - (fn//fra(a)//fra(n - a)) - (fn//fra(b)//fra(n - b)) - 1
print(ans % (10**9+7))