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


def check_180(prev, now):
    return prev[0]*now[0] < 0 or prev[1]*now[1] < 0


G = I.grid("input.txt")
start = (0, 0)
end = (0, 0)
for i, row in enumerate(G):
    for j, c in enumerate(row):
        if c == "S":
            start = (i, j)
        elif c == "E":
            end = (i, j)


def dijkstra(start, end, init_dir=[0, 1]):
    INF = int(1e20)
    m = len(G)
    n = len(G[0])
    dist = [[[INF, None] for _ in range(n)] for _ in range(m)]
    dist[start[0]][start[1]] = [0, init_dir]

    pq = []
    heapq.heappush(pq, ([0, init_dir], start, init_dir))

    while pq:
        w, u, dirn = heapq.heappop(pq)

        for ii, jj in PD.padj4():
            r = u[0] + ii
            c = u[1] + jj

            if PD.not_in_bounds(G, r, c):
                continue

            if G[r][c] == "#":
                continue

            ww = 1001 if check_90(dirn, (ii, jj)) else (
                1 if not check_180(dirn, (ii, jj)) else 2001)
            if ww + dist[u[0]][u[1]][0] < dist[r][c][0]:
                dist[r][c] = [ww + dist[u[0]][u[1]][0], (ii, jj)]
                heapq.heappush(pq, (dist[r][c], (r, c), (ii, jj)))

    return dist


def print_g(G):
    import os
    import time
    os.system("clear")
    for row in G:
        for c in row:
            print(c, end="")
        print()
    time.sleep(1/60)


cnt = 0
from_start = dijkstra(start, end)
visited = []
for i, row in enumerate(G):
    for j, c in enumerate(row):
        dirn = from_start[i][j][1]
        if dirn is None:
            continue
        to_end = dijkstra((i, j), end, init_dir=dirn)
        if (i, j) in visited:
            continue
        if from_start[i][j][0] + to_end[end[0]][end[1]][0] == from_start[end[0]][end[1]][0]:
            G[i][j] = "O"
            print_g(G)
            visited.append((i, j))
            cnt += 1

for row in G:
    for c in row:
        print(c, end="")
    print()

print(cnt)
