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
count = 1


def solve(graph, n, p, dirs, j):
    global count
    dirn = dirs[j]
    r = p[0] + dirn[0]
    c = p[1] + dirn[1]

    if PD.not_in_bounds(graph, r, c):
        return

    if graph[r][c] == '#':
        j = (j + 1) % 4
        solve(graph, n, p, dirs, j)
        return

    if graph[r][c] != 'X':
        count += 1

    graph[r][c] = 'X'
    p = [r, c]
    solve(graph, n, p, dirs, j)


graph = I.grid("input.txt")
p = [0, 0]
for i, row in enumerate(graph):
    for j, c in enumerate(row):
        if c == '^':
            p[0] = i
            p[1] = j
            break

n = len(graph)

dirs = PD.padj4()
graph[p[0]][p[1]] = 'X'
solve(graph, n, p, dirs, 0)
for row in graph:
    for c in row:
        print(c, end="")
    print()
print(count)
