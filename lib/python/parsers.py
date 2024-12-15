def parse_to_grid(inp):
    lines = inp.split("\n")
    grid = []
    for i, line in enumerate(lines):
        grid.append([])
        for c in line:
            grid[i].append(c)
    return grid
