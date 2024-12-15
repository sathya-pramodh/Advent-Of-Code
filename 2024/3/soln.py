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
oc = re.findall(r"mul\([0-9]+,[0-9]+\)", txt)
ans = 0
for o in oc:
    o = o.replace("mul", "")
    o = o.replace("(", "")
    o = o.replace(")", "")
    nums = list(map(int, o.split(",")))
    ans += nums[0]*nums[1]
print(ans)
