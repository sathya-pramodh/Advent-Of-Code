import sys
try:
    sys.path.append("../../")
except ImportError:
    exit(1)

import lib.python.inputs as I

N = I.nums("input.txt")
ans = 0
for nums in N:
    sign = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if not sign:
            if diff > 0:
                sign = 1
            elif diff < 0:
                sign = -1
            else:
                break
            if abs(diff) > 3:
                break
        else:
            if sign*diff <= 0 or abs(diff) > 3:
                break
    else:
        ans += 1
print(ans)
