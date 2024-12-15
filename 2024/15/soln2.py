import sys
import time
import os
sys.setrecursionlimit(int(1e9))


def not_in_bounds(i, j, m, n):
    return i < 0 or i >= m or j < 0 or j >= n


def try_move(graph, r, c, m, n, dir, coords):
    if not_in_bounds(r, c, m, n):
        return False, None

    if graph[r][c] == '.':
        if (r, c) not in coords:
            coords.append((r, c))
        return True, (r, c)

    if graph[r][c] == '#':
        return False, None

    if (r, c) not in coords:
        coords.append((r, c))
    if dir == [0, -1] or dir == [0, 1]:
        ii = dir[0]
        jj = dir[1]
        rr = r + ii
        cc = c + jj
        movable, coord = try_move(graph, rr, cc, m, n, dir, coords)
        return movable, coord

    next = (0, 0)
    if graph[r][c] == "]":
        next = (r, c - 1)
    elif graph[r][c] == "[":
        next = (r, c + 1)
    else:
        return False, None
    ii = dir[0]
    jj = dir[1]
    rr = r + ii
    cc = c + jj
    rrr = next[0] + ii
    ccc = next[1] + jj
    if next not in coords:
        coords.append(next)
    movable1, coords1 = try_move(
        graph, rr, cc, m, n, dir, coords)
    movable2, coords2 = try_move(
        graph, rrr, ccc, m, n, dir, coords)
    if movable1 and movable2:
        coordd = []
        if isinstance(coords1, list):
            for coord in coords1:
                if coord not in coordd:
                    coordd.append(coord)
        else:
            if coords1 not in coordd:
                coordd.append(coords1)
        if isinstance(coords2, list):
            for coord in coords2:
                if coord not in coordd:
                    coordd.append(coord)
        else:
            if coords2 not in coordd:
                coordd.append(coords2)

        return True, coordd

    return False, None


def move(graph, i, j, r, c):
    print(i, j, " -> ", r, c)
    graph[i][j], graph[r][c] = graph[r][c], graph[i][j]
    return (r, c)


def move_all(graph, i, j, dir, coordd):
    ii, jj = (-1*dir[0], -1*dir[1])
    prev = (i, j)
    if graph[i][j] != ".":
        return
    while True:
        r = prev[0] + ii
        c = prev[1] + jj
        if (r, c) not in coordd:
            break

        move(graph, prev[0], prev[1], r, c)
        prev = (r, c)


def solve(graph, start, m, n, dir):
    i = start[0]
    j = start[1]
    ii = dir[0]
    jj = dir[1]
    r = i + ii
    c = j + jj
    if not_in_bounds(r, c, m, n):
        return start

    if graph[r][c] == '.':
        return move(graph, i, j, r, c)

    coordb = []
    coordb.append((i, j))
    movable, coordd = try_move(graph, r, c, m, n, dir, coordb)
    if movable:
        if isinstance(coordd, list):
            # Sort by '.'s that area farthest (manhattan distance metric)
            coordd = sorted(coordd, key=lambda c: abs(
                i - c[0] + j - c[1]), reverse=True)
            for coord in coordd:
                move_all(graph, coord[0], coord[1], dir, coordb)
        elif isinstance(coordd, tuple):
            move_all(graph, coordd[0], coordd[1], dir, coordb)
        return (r, c)
    return start


with open("input.txt") as file:
    s = file.read().strip()
    s1, s2 = s.split("\n\n")
    s1 = s1.replace("O", "[]")
    s1 = s1.replace("#", "##")
    s1 = s1.replace(".", "..")
    s1 = s1.replace("@", "@.")
    lines = s1.split("\n")

    graph = []
    start = (0, 0)
    for i, line in enumerate(lines):
        graph.append([])
        for j, c in enumerate(line):
            graph[i].append(c)
            if c == "@":
                start = (i, j)
    moves = []
    for c in s2:
        if c == '^':
            moves.append([-1, 0])
        elif c == 'v':
            moves.append([1, 0])
        elif c == '<':
            moves.append([0, -1])
        elif c == '>':
            moves.append([0, 1])

    m = len(graph)
    n = len(graph[0])
    for mov in moves:
        os.system("clear")
        for row in graph:
            for c in row:
                print(c, end="")
            print()
        print()
        start = solve(graph, start, m, n, mov)
        # time.sleep(1/144)

    for row in graph:
        for c in row:
            print(c, end="")
        print()
    print()
    ans = 0
    for i, row in enumerate(graph):
        for j, c in enumerate(row):
            if c == "[":
                ans += 100*i + j

    print(ans)
