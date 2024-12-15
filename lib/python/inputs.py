def grid(file):
    with open(file) as f:
        lines = f.readlines()
        grid = []
        for i, line in enumerate(lines):
            grid.append([])
            for c in line.strip():
                grid[i].append(c)
        return grid


def blocks(file):
    r = ""
    with open(file) as f:
        r = f.read().strip()

    return r.split("\n\n")


def nums(file):
    lines = []
    with open(file) as f:
        lines = list(
            map(lambda line: list(map(int, line.strip().split())), f.readlines()))
    return lines


def string(file):
    return open(file).read().strip()


def lines(file):
    return open(file).readlines()
