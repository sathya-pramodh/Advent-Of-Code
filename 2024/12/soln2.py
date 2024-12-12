import sys
sys.setrecursionlimit(int(1e9))

graph = []


def out_of_bounds(r, c, m, n):
    return r < 0 or r >= m or c < 0 or c >= n


def visit_all_neighbors(graph, i, j, m, n, visited, col, group_no):
    if graph[i][j] != col:
        return []

    visited[i][j] = group_no

    ans = []
    dr = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ans.append((i, j))
    for ii, jj in dr:
        r = i + ii
        c = j + jj
        if out_of_bounds(r, c, m, n):
            continue
        if visited[r][c] != group_no:
            ans = ans + \
                visit_all_neighbors(graph, r, c, m, n, visited, col, group_no)

    return ans


def corners(graph, i, j, m, n, visited, group_no):
    cnt = 0
    dr1 = [[1, 0], [0, 1], [1, 1]]
    dr2 = [[0, 1], [-1, 0], [-1, 1]]
    dr3 = [[-1, 0], [0, -1], [-1, -1]]
    dr4 = [[0, -1], [1, 0], [1, -1]]

    for dr in [dr1, dr2, dr3, dr4]:
        ii, jj = dr[0]
        iii, jjj = dr[1]
        iiii, jjjj = dr[2]
        r1, c1 = i + ii, j + jj
        r2, c2 = i + iii, j + jjj
        r3, c3 = i + iiii, j + jjjj
        if out_of_bounds(r1, c1, m, n) and out_of_bounds(r2, c2, m, n):
            cnt += 1
        elif out_of_bounds(r1, c1, m, n):
            if visited[r2][c2] != group_no:
                cnt += 1
        elif out_of_bounds(r2, c2, m, n):
            if visited[r1][c1] != group_no:
                cnt += 1
        else:
            if visited[r1][c1] != group_no and visited[r2][c2] != group_no:
                cnt += 1
            elif visited[r1][c1] == group_no and visited[r2][c2] == group_no and visited[r3][c3] != group_no:
                cnt += 1

    return cnt


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
    group_no = 1
    for i in range(m):
        for j in range(n):
            if visited[i][j] == 0:
                neighs = visit_all_neighbors(
                    graph, i, j, m, n, visited, c, group_no)
                area = len(neighs)
                sides = 0
                for row, col in neighs:
                    sides += corners(graph, row, col, m, n, visited, group_no)
                group_no += 1
                char_ans += area*sides

    ans += char_ans

print(ans)
