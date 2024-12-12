import sys
sys.setrecursionlimit(int(1e9))

graph = []

def visit_all_neighbors(graph, i, j, m, n, visited, col):
    if graph[i][j] != col:
        return []
    
    visited[i][j] = 1
    
    ans = []
    dr = [[1,0], [0,1], [-1, 0], [0, -1]]
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
    sd = 0
    dr = [[1,0], [0,1], [-1, 0], [0, -1]]
    rr = []
    for idx, (ii, jj) in enumerate(dr):
        r = i + ii
        c = j + jj
        if r < 0 or r >= m or c < 0 or c >= n:
            rr.append((r, c, idx))
            continue
        if visited[r][c]:
            rr.append((r, c, idx))
    if len(rr) == 2:
        _, _, d1 = rr[0]
        _, _, d2 = rr[1]
        if d1 != 0 and d2 != 2 or d1 != 1 or d2 != 3:
            sd = 2
    elif len(rr) == 1:
        sd = 1
    elif len(rr) == 0:
        sd = 4
    return sd

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
                area, sides = len(neighs), 0
                for row, col in neighs:
                    sd = check_neigh(graph, row, col, m, n, visited)
                    sides += sd
                print(c, area, sides)

                char_ans += area*sides

    ans += char_ans

print(ans)
