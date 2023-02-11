def main():
    flag = set()
    stack = [[]]
    for si in S:
        if si == '(':
            stack.append([])
        elif si == ')':
            for ti in stack.pop():
                flag.remove(ti)
        elif si in flag:
            return print("No")
        else:
            stack[-1].append(si)
            flag.add(si)
    return print('Yes')


if __name__ == '__main__':
    S = input()

    main()
