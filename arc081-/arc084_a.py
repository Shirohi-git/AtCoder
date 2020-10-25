n = int(input())
a = sorted(map(int, input().split())) + [10 ** 11]
b = sorted(map(int, input().split())) + [10 ** 10]
c = sorted(map(int, input().split()))

cnta, comb = 0, 0
cntb, comc = 0, 0
for ci in c:
    while b[cntb] < ci:
        while a[cnta] < b[cntb]:
            cnta += 1
        comb += cnta
        cntb += 1
    comc += comb
print(comc)
