import sys
from copy import deepcopy
sys.setrecursionlimit(int(1e9))
count = 0


def solve(graph, n, p, dirs, j, iter):
    global count
    dirn = dirs[j]
    r = p[0] + dirn[0]
    c = p[1] + dirn[1]

    if r < 0 or r >= n or c < 0 or c >= n:
        return True

    if iter > 130*130:
        return False

    if graph[r][c] == '#':
        j = (j + 1) % 4
        return solve(graph, n, p, dirs, j, iter + 1)

    if graph[r][c] == '.':
        graph[r][c] = 'X'
    p = [r, c]
    return solve(graph, n, p, dirs, j, iter + 1)


graph = []
n = 0
p = [0, 0]
with open("input.txt") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        graph.append([])
        j = 0
        for c in line.strip():
            graph[i].append(c)
            if c == '^':
                p[0] = i
                p[1] = j
            j += 1
        i += 1
    n = i


fg = deepcopy(graph)
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
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
