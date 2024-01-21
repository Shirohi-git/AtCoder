def main():
    ans, ng_idx = 0, M
    b_acc = [0]
    for bi in B:
        b_acc.append(b_acc[-1]+bi)
    for aj in A:
        for i in range(ng_idx)[::-1]:
            if aj+B[i] <= P:
                ng_idx = i+1
                break
        else:
            ng_idx = 0
        ans += aj*ng_idx + b_acc[ng_idx] + P*(M-ng_idx)
    return print(ans)


if __name__ == '__main__':
    N, M, P = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    main()
