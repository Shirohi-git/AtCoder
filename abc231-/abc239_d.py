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
    res = 0
    for i in range(A, B+1):
        res |= all((i+j not in Prime) for j in range(C, D+1))
    return print('Aoki' if 1-res else 'Takahashi')


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    Prime = set(Eratosthenes(200).prime)

    main()
