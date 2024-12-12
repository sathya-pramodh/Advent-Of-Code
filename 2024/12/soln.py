import sys
sys.setrecursionlimit(int(1e9))

graph = []


def visit_all_neighbors(graph, i, j, m, n, visited, col):
    if graph[i][j] != col:
        return []

    visited[i][j] = 1

    ans = []
    dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ans.append((i, j))
    for ii, jj in dr:
        r = i + ii
        c = j + jj
        if r < 0 or r >= m or c < 0 or c >= n:
            continue
        if not visited[r][c]:
            ans = ans + visit_all_neighbors(graph, r, c, m, n, visited, col)

    return ans


def check_neigh(graph, i, j, m, n, visited):
    ar = 1
    pe = 4
    dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for ii, jj in dr:
        r = i + ii
        c = j + jj
        if r < 0 or r >= m or c < 0 or c >= n:
            continue
        if visited[r][c]:
            pe -= 1

    return ar, pe


unq = set()
with open("input.txt") as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        if len(graph) < i + 1:
            graph.append([])
        for c in line.strip():
            graph[i].append(c)
            unq.add(c)
        i += 1

    m = len(graph)
    n = len(graph[0])

ans = 0
for c in unq:
    visited = [[0]*n for _ in range(m)]
    char_ans = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                neighs = visit_all_neighbors(graph, i, j, m, n, visited, c)
                area, perim = 0, 0
                for row, col in neighs:
                    ar, pe = check_neigh(graph, row, col, m, n, visited)
                    area += ar
                    perim += pe

                char_ans += area*perim

    ans += char_ans

print(ans)
