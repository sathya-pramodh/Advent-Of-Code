import sys
sys.setrecursionlimit(int(1e9))
count = 1


def solve(graph, n, p, dirs, j):
    global count
    dirn = dirs[j]
    r = p[0] + dirn[0]
    c = p[1] + dirn[1]

    if r < 0 or r >= n or c < 0 or c >= n:
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


dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
graph[p[0]][p[1]] = 'X'
solve(graph, n, p, dirs, 0)
for row in graph:
    for c in row:
        print(c, end="")
    print()
print(count)
