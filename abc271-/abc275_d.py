def main():
    res = {0: 1}
    stack = [N]
    while stack:
        q = stack[-1]
        if q in res:
            stack.pop()
            continue
        if q//2 not in res:
            stack.append(q//2)
        if q//3 not in res:
            stack.append(q//3)
        if q//2 in res and q//3 in res:
            res[q] = res[q//2] + res[q//3]
    return print(res[N])


if __name__ == '__main__':
    N = int(input())

    main()
