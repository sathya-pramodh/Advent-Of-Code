import os
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


def solve(robot, t):
    px, py = robot["p"]
    vx, vy = robot["v"]

    fx, fy = px + t*vx, py + t*vy
    tx, ty = translate_coords(fx, fy)
    return tx, ty


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

    t = 1
    seen = []
    while True:
        os.system("clear")
        graph = [['.']*n for _ in range(m)]
        for robot in robots:
            tx, ty = solve(robot, t)
            graph[tx][ty] = '#'

        if graph in seen:
            break

        seen.append(graph)
        print(t)
        for row in graph:
            r = ""
            for c in row:
                r += c
            if "#"*10 in r:
                break
        else:
            t += 1
            continue
        print(t)
        for row in graph:
            for c in row:
                print(c, end=" ")
            print()

        break
