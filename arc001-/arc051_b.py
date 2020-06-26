def fibonacci(n, FIBO):
    if FIBO[n - 1] > 0:
        return FIBO[n-1]
    elif n <= 2:
        FIBO[n - 1] = 1
        return FIBO[n - 1]
    else:
        FIBO[n - 1] = fibonacci(n - 1, FIBO) + fibonacci(n - 2, FIBO)
        return FIBO[n - 1]

k = int(input())

fibo = [0] * (k + 2)
fibonacci(k + 2, fibo)
print(fibo[k + 1], fibo[k])
