def main():
    if sorted(A) != sorted(B):
        return print("No")
    if len(A) != len(set(A)):
        return print("Yes")

    for i in range(N-2):
        if A[i] == B[i]:
            continue
        idx = A[i:].index(B[i]) + i
        if (idx - i) % 2 == 1:
            if idx + 1 >= N:
                A[idx-2:] = [A[idx]] + A[idx-2:idx]
                idx -= 2
            A[idx-1:idx+2] = [A[idx+1]] + A[idx-1:idx+1]
            idx += 1
        A[i:idx+1] = [A[idx]] + A[i:idx]
    return print('Yes' if A == B else 'No')


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
