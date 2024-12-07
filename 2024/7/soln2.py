import sys
sys.setrecursionlimit(int(1e9))


def get_all_combinations(nums, target):
    if len(nums) <= 1:
        return nums

    head = nums[len(nums) - 1]
    combs = get_all_combinations(nums[:-1], target)
    new_combs = []
    for comb in combs:
        if head + comb <= target:
            new_combs.append(head + comb)

        if head * comb <= target:
            new_combs.append(head * comb)

        if int(str(comb) + str(head)) <= target:
            new_combs.append(int(str(comb) + str(head)))

    return new_combs


ans = 0
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        res, nums = line.split(":")
        numsS = nums.strip().split()
        nums = list(map(lambda x: int(x), numsS))
        res = int(res)

        combinations = get_all_combinations(nums, res)
        for comb in combinations:
            if comb == res:
                ans += res
                break

print(ans)
