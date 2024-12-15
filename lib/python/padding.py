def padj4():
    return [[-1, 0], [0, 1], [1, 0], [0, -1]]


def padj8():
    return padj4() + [[1, 1], [1, -1], [-1, 1], [-1, -1]]


def not_in_bounds(graph, r, c):
    return r < 0 or r >= len(graph) or c < 0 or c >= len(graph[0])
