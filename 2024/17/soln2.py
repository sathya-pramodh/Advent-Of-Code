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


R, PP = I.blocks("input.txt")
registers = {
    "A": 0,
    "B": 0,
    "C": 0,
}
for i, line in enumerate(R.strip().split("\n")):
    val = int(line.split(":")[1])
    reg = chr(ord("A") + i)
    registers[reg] = val


@FC.cache
def run(val_a):
    registers = {
        "A": val_a,
        "B": 0,
        "C": 0,
    }
    instrs = list(map(int, PP.strip().split(":")[1].strip().split(",")))
    output = ""
    ip = 0
    while ip < len(instrs):
        instr = instrs[ip]
        if instr == 0:
            # adv
            combo = instrs[ip + 1]
            val = combo2val(combo, registers)
            ip += 2
            registers["A"] //= 2**val
        elif instr == 1:
            # bxl
            literal = instrs[ip + 1]
            ip += 2
            registers["B"] = registers["B"] ^ literal
        elif instr == 2:
            # bst
            combo = instrs[ip + 1]
            val = combo2val(combo, registers)
            ip += 2
            registers["B"] = val % 8
        elif instr == 3:
            # jnz
            literal = instrs[ip + 1]
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
            ip += 2
            val = combo2val(combo, registers)
            output += f"{val % 8}"
        elif instr == 6:
            # bdv
            combo = instrs[ip + 1]
            val = combo2val(combo, registers)
            ip += 2
            registers["B"] = registers["A"]//(2**val)
        elif instr == 7:
            # cdv
            combo = instrs[ip + 1]
            val = combo2val(combo, registers)
            ip += 2
            registers["C"] = registers["A"]//(2**val)

    return ",".join(output)


def count_matching(out, actual):
    if len(out) != len(actual):
        return len(actual.replace(",", "")) - 1
    actual = actual[::-1]
    out = out[::-1]
    for idx in range(len(out)):
        if actual[idx] != out[idx]:
            return idx + 1

    return len(out.replace(",", ""))


instrs = list(map(int, PP.strip().split(":")[1].strip().split(",")))
actual = ",".join(map(str, instrs))
# low = 236196491952128
low = 1
while True:
    out = run(low)
    print(low, out, actual)
    if out == actual:
        print(low)
        break
    cnt = count_matching(out, actual)
    if cnt == len(instrs) - 1:
        low += 8**(cnt)
    else:
        low += 8**(len(instrs) - 1 - cnt)
