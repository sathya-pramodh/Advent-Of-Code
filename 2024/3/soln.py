import re
with open("input.txt", "r") as file:
    txt = file.read()
    oc = re.findall("mul\([0-9]+,[0-9]+\)", txt)
    ans = 0
    for o in oc:
        o = o.replace("mul", "")
        o = o.replace("(", "")
        o = o.replace(")", "")
        nums = list(map(int, o.split(",")))
        ans += nums[0]*nums[1]
    print(ans)
