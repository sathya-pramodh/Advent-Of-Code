import sys
sys.setrecursionlimit(int(1e9))

m = 101
n = 103


def translate_coords(x, y):
    rem_x = abs(x) % m
    rem_y = abs(y) % n
    translated_x, translated_y = 0, 0
    if x < 0:
        translated_x = (m - rem_x) % m
    else:
        translated_x = rem_x

    if y < 0:
        translated_y = (n - rem_y) % n
    else:
        translated_y = rem_y

    return translated_x, translated_y


def solve(robot, quads, quad_cnt):
    px, py = robot["p"]
    vx, vy = robot["v"]

    fx, fy = px + 100*vx, py + 100*vy
    tx, ty = translate_coords(fx, fy)
    for i, quad in enumerate(quads):
        (x1, y1), (x2, y2) = quad
        if x1 <= tx and tx < x2 and y1 <= ty and ty < y2:
            quad_cnt[i] += 1
            return


with open("input.txt") as file:
    lines = file.readlines()
    robots = []
    for line in lines:
        ps, vs = line.strip().split()
        _, pxys = ps.split("=")
        _, vxys = vs.split("=")
        px, py = list(map(int, pxys.split(",")))
        vx, vy = list(map(int, vxys.split(",")))
        robots.append({
            "p": [px, py],
            "v": [vx, vy],
        })

    quads = [
        [(0, 0), (m//2, n//2)],
        [(m//2 + 1, 0), (m, n//2)],
        [(0, n//2 + 1), (m//2, n)],
        [(m//2 + 1, n//2 + 1), (m, n)]
    ]
    quad_cnt = [
        0,
        0,
        0,
        0
    ]
    for robot in robots:
        solve(robot, quads, quad_cnt)

    ans = 1
    for cnt in quad_cnt:
        ans *= cnt

    print(ans)
