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


with open("input.txt", "r") as file:
    lines = file.readlines()
    ans = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
        for i in range(len(nums)):
            if is_valid(nums[:i] + nums[i + 1:]):
                ans += 1
                break
    print(ans)
