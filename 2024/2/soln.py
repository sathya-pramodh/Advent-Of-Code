with open("input.txt", "r") as file:
    lines = file.readlines()
    ans = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
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
