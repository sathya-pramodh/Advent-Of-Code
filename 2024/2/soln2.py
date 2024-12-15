import sys
try:
    sys.path.append("../../")
except ImportError:
    exit(1)

import lib.python.inputs as I


def is_valid(nums):
    sign = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if not sign:
            if diff > 0:
                sign = 1
            elif diff < 0:
                sign = -1
            else:
                return False
            if abs(diff) > 3:
                return False
        else:
            if sign*diff <= 0 or abs(diff) > 3:
                return False
    return True


N = I.nums("input.txt")
ans = 0
for nums in N:
    for i in range(len(nums)):
        if is_valid(nums[:i] + nums[i + 1:]):
            ans += 1
            break
print(ans)
