k = int(input())

fibo = [0] * (k + 2)
fibo[0], fibo[1] = 1, 1
for i in range(2, k + 2):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[k + 1], fibo[k])
