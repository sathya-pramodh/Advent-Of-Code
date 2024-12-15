import sys
import time
import os
sys.setrecursionlimit(int(1e9))


def not_in_bounds(i, j, m, n):
    return i < 0 or i >= m or j < 0 or j >= n


def try_move(graph, r, c, m, n, dir, coords=[]):
    if not_in_bounds(r, c, m, n):
        return False, coords

    if graph[r][c] == '.':
        coords.append((r, c))
        return True, coords

    if graph[r][c] == '#':
        return False, coords

    coords.append((r, c))
    ii = dir[0]
    jj = dir[1]
    rr = r + ii
    cc = c + jj
    movable, coords = try_move(graph, rr, cc, m, n, dir, coords)
    return movable, coords


def move(graph, i, j, r, c):
    graph[i][j], graph[r][c] = graph[r][c], graph[i][j]
    return (r, c)


def solve(graph, start, m, n, dir):
    i = start[0]
    j = start[1]
    ii = dir[0]
    jj = dir[1]
    r = i + ii
    c = j + jj
    if not_in_bounds(r, c, m, n) or graph[r][c] == '#':
        return start

    if graph[r][c] == '.':
        return move(graph, i, j, r, c)

    coords = [(i, j)]
    movable, coords = try_move(graph, r, c, m, n, dir, coords)
    if movable:
        prev = None
        for coord in coords[::-1]:
            if prev is None:
                prev = coord
                continue
            move(graph, prev[0], prev[1], coord[0], coord[1])
            prev = coord
        return (r, c)
    return start


with open("input.txt") as file:
    s = file.read().strip()
    s1, s2 = s.split("\n\n")
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

    ans = 0
    for i, row in enumerate(graph):
        for j, c in enumerate(row):
            if c == "O":
                ans += 100*i + j

    print(ans)
