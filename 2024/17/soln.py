# 513437217
import sys

try:
    sys.path.index("../../")
except ValueError:
    sys.path.append("../../")

try:
    sys.setrecursionlimit(int(1e9))
except Exception as e:
    raise e

import lib.python.inputs as I
import lib.python.padding as PD
import lib.python.parsers as P
import collections as C
from copy import deepcopy
import functools as FC
import re


def combo2val(combo, registers):
    if combo >= 4:
        reg = chr(ord("A") + combo - 4)
        return registers[reg]
    return combo


R, P = I.blocks("input.txt")
registers = {
    "A": 0,
    "B": 0,
    "C": 0,
}
for i, line in enumerate(R.strip().split("\n")):
    val = int(line.split(":")[1])
    reg = chr(ord("A") + i)
    registers[reg] = val

output = ""
instrs = list(map(int, P.strip().split(":")[1].strip().split(",")))
ip = 0
while ip < len(instrs):
    instr = instrs[ip]
    print("Reg: ", registers)
    print("IP: ", ip)
    print("Instr: ", instr)
    if instr == 0:
        # adv
        combo = instrs[ip + 1]
        print("Combo: ", combo)
        val = combo2val(combo, registers)
        print("Val: ", val)
        ip += 2
        registers["A"] //= 2**val
    elif instr == 1:
        # bxl
        literal = instrs[ip + 1]
        print("Literal: ", literal)
        ip += 2
        registers["B"] = registers["B"] ^ literal
    elif instr == 2:
        # bst
        combo = instrs[ip + 1]
        print("Combo: ", combo)
        val = combo2val(combo, registers)
        print("Val: ", val)
        ip += 2
        registers["B"] = val % 8
    elif instr == 3:
        # jnz
        literal = instrs[ip + 1]
        print("Literal: ", literal)
        ip += 2
        if registers["A"] == 0:
            continue
        ip = literal
    elif instr == 4:
        # bxc
        _ = instrs[ip + 1]
        ip += 2
        registers["B"] = registers["B"] ^ registers["C"]
    elif instr == 5:
        # out
        combo = instrs[ip + 1]
        print("Combo: ", combo)
        ip += 2
        val = combo2val(combo, registers)
        print("Val: ", val)
        output += f"{val % 8}"
        print("Out: ", output)
    elif instr == 6:
        # bdv
        combo = instrs[ip + 1]
        print("Combo: ", combo)
        val = combo2val(combo, registers)
        print("Val: ", val)
        ip += 2
        registers["B"] = registers["A"]//(2**val)
    elif instr == 7:
        # cdv
        combo = instrs[ip + 1]
        print("Combo: ", combo)
        val = combo2val(combo, registers)
        print("Val: ", val)
        ip += 2
        registers["C"] = registers["A"]//(2**val)

    while True:
        c = input()
        if c == "":
            break

print(",".join(output))
