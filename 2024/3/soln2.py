import sys

try:
    sys.path.index("../../")
except ValueError:
    sys.path.append("../../")

import lib.python.inputs as I
import lib.python.parsers as P
import collections as C
import re

txt = I.string("input.txt")


def sum_nums(txt):
    oc = re.findall(r"mul\([0-9]+,[0-9]+\)", txt)
    ans = 0
    for o in oc:
        o = o.replace("mul", "")
        o = o.replace("(", "")
        o = o.replace(")", "")
        nums = list(map(int, o.split(",")))
        ans += nums[0]*nums[1]
    return ans


with open("input.txt", "r") as file:
    txt = file.read()
    ans = 0
    enabled = True
    while txt:
        print(txt)
        idx_do = txt.find("do()")
        idx_dont = txt.find("don't()")
        if idx_dont == -1:
            if enabled:
                ans += sum_nums(txt)
            txt = ""
            continue
        if idx_do == -1:
            if idx_dont == -1:
                if enabled:
                    ans += sum_nums(txt)
            else:
                if enabled:
                    ans += sum_nums(txt[:idx_dont])
            txt = ""
            continue

        if idx_dont < idx_do:
            if enabled:
                ans += sum_nums(txt[:idx_dont])
            enabled = True
            txt = txt[idx_do+4:]

        else:
            if enabled:
                ans += sum_nums(txt[:idx_do])
            ans += sum_nums(txt[idx_do:idx_dont])
            enabled = False
            txt = txt[idx_dont+7:]
    print(ans)
