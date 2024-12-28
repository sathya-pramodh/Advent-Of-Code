import sys
import heapq

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
import functools as FC
import re


def check_90(prev, now):
    return prev[0]*now[0] + prev[1]*now[1] == 0


G = I.grid("input.txt")
start = (0, 0)
end = (0, 0)
for i, row in enumerate(G):
    for j, c in enumerate(row):
        if c == "S":
            start = (i, j)
        elif c == "E":
            end = (i, j)

INF = int(1e20)
m = len(G)
n = len(G[0])
dist = [[INF for _ in range(n)] for _ in range(m)]
dist[start[0]][start[1]] = 0

pq = []
heapq.heappush(pq, (0, start, [0, 1]))

while pq:
    w, u, dirn = heapq.heappop(pq)

    for ii, jj in PD.padj4():
        r = u[0] + ii
        c = u[1] + jj

        if PD.not_in_bounds(G, r, c):
            continue

        if G[r][c] == "#":
            continue

        ww = 1001 if check_90(dirn, (ii, jj)) else 1
        if ww + dist[u[0]][u[1]] < dist[r][c]:
            dist[r][c] = ww + dist[u[0]][u[1]]
            heapq.heappush(pq, (dist[r][c], (r, c), (ii, jj)))


print(dist[end[0]][end[1]])
