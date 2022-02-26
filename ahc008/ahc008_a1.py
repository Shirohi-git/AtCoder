#!/usr/bin/python3

from collections import Counter


DIR = {'U': (-1, 0, 'u'), 'D': (1, 0, 'd'),
       'L': (0, -1, 'l'), 'R': (0, 1, 'r')}
H, W, T = 30, 30, 300


class Room:
    def __init__(self, h):
        self.size = (Large if h > 7 else Small)
        self.make_map(h)
        self.make_route(h)

    def make_map(self, h):
        self.make_block(h)
        self.make_id(h)
        return

    def make_block(self, h):
        self.room = [['.'] * W for _ in range(H)]
        for b, x in zip(self.size.BLOCK_X, self.size.LINE_X):
            for j in x:
                for i in range(H):
                    self.room[i][j] = b[i]
        for b, y in zip(self.size.BLOCK_Y, self.size.LINE_Y):
            for i in y:
                self.room[i] = b[:]
        for i, (x, y) in enumerate(self.size.POSITION[:-1]):
            self.room[x][y] = str(i)
            if i >= h:
                self.room[x][y] = '#'
        return

    def make_id(self, h):
        self.id = list(self.size.ROOMID[::-1])
        for x, y in self.size.POSITION[:h]:
            for dx, dy, _ in DIR.values():
                self.bfs(x+dx, y+dy)
        return

    def bfs(self, sx, sy):
        if self.room[sx][sy] != '.':
            return
        id = self.room[sx][sy] = self.id.pop()

        que = [(sx, sy)]
        for qx, qy in que:
            for dx, dy, _ in DIR.values():
                px, py = qx+dx, qy+dy
                if (0 <= px < H) and (0 <= py < W):
                    if self.room[px][py] != '.':
                        continue
                    self.room[px][py] = id
                    que.append((px, py))
        return

    def make_route(self, h):
        self.route = []
        for i, (x, y) in enumerate(self.size.POSITION[:h]):
            if i == 4:
                self.route.append([(x, y), self.size.CENTER, (x, 0), (x, 29)])
            elif i in [1, 2, 3]:
                self.route.append([(x, y), (0, y), (29, y)])
            else:
                self.route.append([(x, y), (x, 0), (x, 29)])
        return


class Small:
    ROOMID = "ABCDEFGHIJKL"
    WEIGHT = [0, 0, 1, -1, -1, 0, 1, 0, 0, 1, 1, 0]

    BLOCK_X = [list('#########.#........#.#########'),
               list('........#.##########.#........')]
    BLOCK_Y = [list('......#.#######.#.....#.######'),
               list('#######.#.....#.#######.#.....')]
    LINE_X, LINE_Y = [(6, 16, 22), (8, 14, 24)], [(8, 21), (10, 19)]
    POSITION = [(i, j) for i in [9, 20] for j in [7, 15, 23]]
    POSITION += [POSITION.pop(4)] * 2
    CENTER = POSITION[-1]


class Large:
    ROOMID = "ABCDEFGHIJKLMNOP"
    WEIGHT = [0, 0, 1, -1, -1, 0, 1, 0, -1, 0, 0, -1, 1, 0, 0, 1]

    BLOCK_X = [list('#######.#.....#.#######.#.....'),
               list('......#.#######.#.....#.######')]
    BLOCK_Y = [list('......#.#######.#.....#.######'),
               list('#######.#.....#.#######.#.....')]
    LINE_X, LINE_Y = [(6, 16, 22), (8, 14, 24)], [(6, 16, 22), (8, 14, 24)]
    POSITION = [(i, j) for i in [7, 15, 23] for j in [7, 15, 23]]
    pos4 = POSITION.pop(4)
    POSITION += [pos4] * 2
    CENTER = POSITION[-1]


class human_pet:
    def __init__(self, r, h, h_lst, p, p_lst):
        self.h_cnt = h
        self.h_place = [(x-1, y-1) for x, y in h_lst]
        self.h_complete = [0] * h
        self.h_route = [ri[:] for ri in r.route]

        self.p_cnt = p
        self.p_place = [(x-1, y-1) for x, y, _ in p_lst]

        self.cant_move = [['.'] * W for _ in range(H)]
        self.room = r.room
        self.room_id = r.size.ROOMID
        self.room_weight = r.size.WEIGHT
        self.center = r.size.CENTER
        self.update(0)

    def is_grid(self, x, y):
        res = (0 <= x < H) and (0 <= y < W)
        if res:
            res = (self.cant_move[x][y] != '#')
        return res

    def human_move(self, h, x, y, d):
        self.h_place[h] = (x, y)
        self.cant_block.add((x, y))
        return d

    def humans_decision(self):
        res = []
        canmake_block = all(ci >= 1 for ci in self.h_complete)
        maked_block = all(ci >= 4 for ci in self.h_complete)
        for h, (x, y) in enumerate(self.h_place):
            mv = '.'
            if maked_block:
                mv = self.human_canclose(h, x, y)
            elif canmake_block and self.h_complete[h] < 4:
                shouldmake_block, mv = self.human_needblock(h, x, y)
                if not shouldmake_block:
                    mv = self.human_destination(h, x, y)
            elif self.h_complete[h] == 0:
                mv = self.human_destination(h, x, y)
            res.append(mv)
        return print(*res, sep='')

    def human_destination(self, h, x, y):
        mv = '.'
        if not self.h_route[h]:
            self.h_complete[h] = 4
            return mv
        tx, ty = self.h_route[h][-1]
        if (x, y) == (tx, ty):
            self.h_complete[h] += 1
            self.h_route[h].pop()
            return mv

        for dir, (dx, dy, _) in DIR.items():
            nx, ny = x+dx, y+dy
            if not self.is_grid(nx, ny):
                continue
            if abs(tx-nx) < abs(tx-x):
                mv = self.human_move(h, nx, ny, dir)
                return mv
            elif abs(ty-ny) < abs(ty-y):
                mv = self.human_move(h, nx, ny, dir)
                return mv
        return print("#destination_ERROR")

    def human_needblock(self, h, x, y):
        sb, mv = False, '.'
        for _, (dx, dy, block) in DIR.items():
            nx, ny = x+dx, y+dy
            if not self.is_grid(nx, ny):
                continue
            if (nx, ny) == self.center:
                if self.h_complete[h] < 3:
                    continue
            if self.room[nx][ny] == '#':
                sb = True
                mv = self.make_block(nx, ny, block)
                return sb, mv
        return sb, mv

    def human_canclose(self, h, x, y):
        mv = '.'
        closed = 0
        for dx, dy, block in DIR.values():
            nx, ny = x+dx, y+dy
            if not self.is_grid(nx, ny):
                closed += 1
        if closed >= 3:
            return mv

        for dx, dy, block in DIR.values():
            nx, ny = x+dx, y+dy
            if not self.is_grid(nx, ny):
                continue
            if self.room_cnt[self.room[nx][ny]] > self.close_count[h]:
                mv = self.make_block(nx, ny, block)
                return mv
        return mv

    def count_connectpets(self):
        self.bfs_petplace = set(self.p_place)
        self.bfs_flag = [[0] * W for _ in range(H)]
        self.h_connect_pets = [-1] * self.h_cnt
        self.close_count = [-1] * self.h_cnt
        for h in range(self.h_cnt):
            if self.h_connect_pets[h] < 0:
                self.bfs(*self.h_place[h])
        return

    def bfs(self, sx, sy):
        human, room, pet = set(), set(), 0
        que = [(sx, sy)]
        for qx, qy in que:
            for dx, dy, _ in DIR.values():
                px, py = qx+dx, qy+dy
                if not self.is_grid(px, py):
                    continue
                if self.bfs_flag[px][py]:
                    continue
                self.bfs_flag[px][py] = 1
                for xy in self.p_place:
                    if xy == (px, py):
                        pet += 1
                for h, xy in enumerate(self.h_place):
                    if xy == (px, py):
                        human.add(h)
                if self.room[px][py] in self.room_id:
                    room.add(self.room[px][py])
                que.append((px, py))
        for h in human:
            self.h_connect_pets[h] = pet
            self.close_count[h] = 2
            if pet * 1 <= len(room):
                self.close_count[h] = 1
        return

    def shouldclose_room(self, t):
        self.pets_count()
        for x, y in self.h_place:
            for dx, dy, _ in DIR.values():
                nx, ny = x+dx, y+dy
                if not self.is_grid(nx, ny):
                    continue
                if (nx, ny) in self.cant_block:
                    self.room_cnt[self.room[nx][ny]] = 0
        self.lastclose_room(t)
        return

    def lastclose_room(self, t):
        self.last_turn = T - 10
        self.late_turn = T - 30

        if self.late_turn > t:
            for id, w in zip(self.room_id, self.room_weight):
                if self.room_cnt[id]:
                    self.room_cnt[id] += w
        if t > self.last_turn:
            for ri in self.room_cnt:
                self.room_cnt[ri] *= 3
        return

    def make_block(self, x, y, b):
        if (x, y) not in self.cant_block:
            self.cant_move[x][y] = '#'
            return b
        b = '.'
        return b

    def pets_count(self):
        self.room_cnt = Counter()
        for x, y in self.p_place:
            self.room_cnt[self.room[x][y]] += 1
        return

    def pets_move(self, p_mv):
        for p, mv, (x, y) in zip(range(self.p_cnt), p_mv, self.p_place):
            nx, ny = x, y
            for dx, dy, _ in map(lambda mi: DIR[mi], mv):
                nx, ny = nx+dx, ny+dy
            self.p_place[p] = (nx, ny)
        return

    def pets_predmv(self):
        res = []
        for x, y in self.p_place:
            res += [(x+dx, y+dy) for dx, dy, _ in DIR.values()]
        return res

    def update_cant_block(self):
        self.cant_block = set(self.h_place + self.p_place + self.pets_predmv())
        return

    def update(self, t):
        self.update_cant_block()
        self.count_connectpets()
        self.shouldclose_room(t)
        return


def main():
    hp = human_pet(Room(M), M, HM, N, PET)

    for turn in range(T):
        hp.update(turn)
        hp.humans_decision()
        hp.pets_move(input().split())
    return


if __name__ == '__main__':
    N = int(input())
    PET = [tuple(map(int, input().split())) for _ in range(N)]
    M = int(input())
    HM = [tuple(map(int, input().split())) for _ in range(M)]

    main()
