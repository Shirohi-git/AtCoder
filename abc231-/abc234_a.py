def main():
    def f(x):
        return x**2 + 2*x + 3
    ans = f(f(f(t)+t)+f(f(t)))
    return print(ans)


if __name__ == '__main__':
    t = int(input())

    main()
