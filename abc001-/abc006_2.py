n = int(input())
mod = 10007

tri = [0] * 10 ** 6
tri[2] = 1
for i in range(3, n):
    tri[i] = (tri[i - 1] + tri[i - 2] + tri[i - 3]) % mod
print(tri[n - 1])
