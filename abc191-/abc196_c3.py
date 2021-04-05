n = input()
n, l = int(n), len(n)

half = 10 ** (l // 2)
print(half - 1 if l % 2 else n // half - (n // half > n % half))
