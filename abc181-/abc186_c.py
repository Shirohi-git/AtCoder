n = int(input())

ans = n
for i in range(1, n + 1):
    ans -= ('7' in str(i)) or ('7' in oct(i))
print(ans)
