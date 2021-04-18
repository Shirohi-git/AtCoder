a, b = map(int, input().split())

a1, b1 = a - (a < b), b - (b < a)
alst = [i + 1 for i in range(a1)]
blst = [-i - 1 for i in range(b1)]
if a < b:
    alst.append(-sum(blst[a1:]))
if b < a:
    blst.append(-sum(alst[b1:]))
print(*(alst + blst))
