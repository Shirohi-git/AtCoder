l = int(input())

fact = [1, 1]
for i in range(2, l):
    fact.append(fact[-1] * i)
ans = fact[l - 1] // fact[l - 12] // fact[11]
print(ans)
