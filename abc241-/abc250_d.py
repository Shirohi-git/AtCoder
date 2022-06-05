from bisect import bisect


class Eratosthenes():
    def __init__(self, N):
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]


def main():
    prime = Eratosthenes(INF).prime
    
    ans = 0
    for q in prime:
        ans += bisect(prime, min(N//q**3, q-1))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    INF = min(10**6, N)

    main()
    