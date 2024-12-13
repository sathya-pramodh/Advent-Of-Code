import sys
sys.setrecursionlimit(int(1e9))
MAX = 10000000000000

blocks = []
i = 0
with open("input.txt") as file:
    lines = file.read()
    inc = {
        "A": [0, 0],
        "B": [0, 0],
    }
    tgt = [0, 0]
    for blk in lines.split("\n\n"):
        for line in blk.strip().split("\n"):
            if "Prize" not in line:
                block_id, contents = line.split(":")
                block_id = block_id.replace("Button ", "")
                x, y = contents.strip().split(",")
                x = int(x.replace("X+", ""))
                y = int(y.replace("Y+", ""))
                inc[block_id] = [x, y]
            else:
                _, contents = line.split(":")
                x, y = contents.strip().split(",")
                x = int(x.replace("X=", ""))
                y = int(y.replace("Y=", ""))
                tgt = [MAX + x, MAX + y]
                blocks.append((inc, tgt))
                i += 1
                inc = {
                    "A": [0, 0],
                    "B": [0, 0],
                }
                tgt = [0, 0]

    ans = 0
    for inc, tgt in blocks:
        x, y = tgt
        (x1, y1), (x2, y2) = inc["A"], inc["B"]
        numer = x*y1 - x1*y
        denom = x2*y1 - x1*y2
        if numer%denom != 0:
            continue
        b = numer//denom
        numer = x - b*x2
        denom = x1
        if numer%denom != 0:
            continue
        a = numer//denom
        ans += 3*a + b

    print(ans)

