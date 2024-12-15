import sys

try:
    sys.path.index("../../")
except ValueError:
    sys.path.append("../../")

try:
    sys.setrecursionlimit(int(1e9))
except Exception as e:
    raise e

import lib.python.inputs as I
import lib.python.padding as PD
import lib.python.parsers as P
import collections as C
from copy import deepcopy
import re
count = 0


def solve(graph, n, p, dirs, j, iter):
    global count
    dirn = dirs[j]
    r = p[0] + dirn[0]
    c = p[1] + dirn[1]

    if PD.not_in_bounds(graph, r, c):
        return True

    if iter > n*n:
        return False

    if graph[r][c] == '#':
        j = (j + 1) % 4
        return solve(graph, n, p, dirs, j, iter + 1)

    if graph[r][c] == '.':
        graph[r][c] = 'X'
    p = [r, c]
    return solve(graph, n, p, dirs, j, iter + 1)


graph = I.grid("input.txt")
n = 0
p = [0, 0]
for i, line in enumerate(graph):
    for j, c in enumerate(line):
        if c == '^':
            p[0] = i
            p[1] = j
            break

n = len(graph)

fg = deepcopy(graph)
dirs = PD.padj4()
graph[p[0]][p[1]] = 'X'
solve(graph, n, p, dirs, 0, 0)
graph[p[0]][p[1]] = '^'
for i, row in enumerate(graph):
    for j, c in enumerate(row):
        if c == 'X':
            graph_cpy = deepcopy(fg)
            graph_cpy[i][j] = '#'
            res = solve(graph_cpy, n, p, dirs, 0, 0)
            if not res:
                count += 1
        print(c, end="")
    print()
print(count)
