class AVLTree:
    class Node:
        def __init__(self, key, val):
            self.key, self.val = key, val
            self.l_node = self.r_node = None
            self.bias, self.size = 0, 1

    def __init__(self):
        self.root = None

    def __rotate_left(self, v):
        u = v.r_node
        u.size = v.size
        v.size -= 1 + (u.r_node.size if u.r_node is not None else 0)
        v.r_node, u.l_node = u.l_node, v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias, v.bias = 1, -1
        return u

    def __rotate_right(self, v):
        u = v.l_node
        u.size = v.size
        v.size -= 1 + (u.l_node.size if u.l_node is not None else 0)
        v.l_node, u.r_node = u.r_node, v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias, v.bias = -1, 1
        return u

    def __update_bias_double(self, v):
        if v.bias == 1:
            v.r_node.bias = -1
            v.l_node.bias = 0
        elif v.bias == -1:
            v.r_node.bias = 0
            v.l_node.bias = 1
        else:
            v.r_node.bias = 0
            v.l_node.bias = 0
        v.bias = 0
        return None

    def __rotate_LR(self, v):
        u, t = v.l_node, v.l_node.r_node
        t.size = v.size
        v.size -= u.size - (t.r_node.size if t.r_node is not None else 0)
        u.size -= 1 + (t.r_node.size if t.r_node is not None else 0)
        u.r_node, t.l_node = t.l_node, u
        v.l_node, t.r_node = t.r_node, v
        self.__update_bias_double(t)
        return t

    def __rotate_RL(self, v):
        u, t = v.r_node, v.r_node.l_node
        t.size = v.size
        v.size -= u.size - (t.l_node.size if t.l_node is not None else 0)
        u.size -= t.l_node.size + 1 if t.l_node is not None else 1
        u.l_node, t.r_node = t.r_node, u
        v.r_node, t.l_node = t.l_node, v
        self.__update_bias_double(t)
        return t

    def __rotate(self, v):
        if v.bias == 2:
            if v.l_node.bias == -1:
                new_v = self.__rotate_LR(v)
            else:
                new_v = self.__rotate_right(v)

        elif v.bias == -2:
            if v.r_node.bias == 1:
                new_v = self.__rotate_RL(v)
            else:
                new_v = self.__rotate_left(v)
        return new_v

    def __set_child(self, v, vdir, c):
        if vdir == 1:
            v.l_node = c
        else:  # vdir == -1:
            v.r_node = c
        return

    def __get_node(self, key):
        v = self.root
        self.history = []
        while v is not None:
            if key == v.key:
                return v
            elif key < v.key:
                self.history.append((v, 1))
                v = v.l_node
            elif v.key < key:
                self.history.append((v, -1))
                v = v.r_node
        return None

    def insert(self, key, val=0):
        if self.root is None:
            self.root = self.Node(key, val)
            return

        v = self.__get_node(key)
        if v is not None:
            v.val = val
            return

        history = self.history
        p, pdir = history[-1]
        self.__set_child(p, pdir, self.Node(key, val))

        while history:
            v, direction = history.pop()
            v.bias += direction
            v.size += 1

            new_v = None
            if v.bias in [2, -2]:
                new_v = self.__rotate(v)
            elif v.bias == 0:
                break

            if new_v is not None:
                if len(history) == 0:
                    self.root = new_v
                    return
                p, pdir = history.pop()
                p.size += 1
                self.__set_child(p, pdir, new_v)
                break

        while history:
            p, pdir = history.pop()
            p.size += 1
        return

    def delete(self, key):
        v = self.__get_node(key)
        if v is None:
            return False

        history = self.history
        if v.l_node is not None:
            history.append((v, 1))
            lmax = v.l_node
            while lmax.r_node is not None:
                history.append((lmax, -1))
                lmax = lmax.r_node
            v.key, v.val = lmax.key, lmax.val
            v = lmax

        c = v.l_node if v.l_node is not None else v.r_node
        if history:
            p, pdir = history[-1]
            self.__set_child(p, pdir, c)
        else:
            self.root = c
            return True

        while history:
            p, pdir = history.pop()
            p.bias -= pdir
            p.size -= 1

            new_p = None
            if p.bias in [2, -2]:
                new_p = self.__rotate(p)
            elif p.bias != 0:
                break

            if new_p is not None:
                if len(history) == 0:
                    self.root = new_p
                    return True
                gp, gpdir = history[-1]
                self.__set_child(gp, gpdir, new_p)
                if new_p.bias != 0:
                    break

        while history:
            p, pdir = history.pop()
            p.size -= 1
        return True

    def get(self, key):
        v = self.root
        while v is not None:
            if key == v.key:
                return v.val
            elif key < v.key:
                v = v.l_node
            elif v.key < key:
                v = v.r_node
        return None

    def lower_bound(self, key):
        res = None
        v = self.root
        while v is not None:
            if v.key >= key:
                if res is None or res > v.key:
                    res = v.key
                v = v.l_node
            else:
                v = v.r_node
        return res


def main():
    avl = AVLTree()
    ans = [-1] * N
    for i, pi in enumerate(P):
        key, val = avl.lower_bound(pi), []
        if key is not None:
            val = avl.get(key)
            avl.delete(key)
        val.append(pi)
        if len(val) == K:
            for v in val + [pi]:
                ans[v-1] = i+1
            continue
        avl.insert(pi, val)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    main()
