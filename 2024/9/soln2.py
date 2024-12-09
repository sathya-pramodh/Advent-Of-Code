import sys
sys.setrecursionlimit(int(1e9))

with open("input.txt") as file:
    line = file.read().strip()
    idx = 0
    nums = []
    dots = []
    idd = 0
    for id, c in enumerate(line):
        if id % 2 == 0:
            n = ord(c) - ord('0')
            nums.append((idd, n, idx))
            idd += n
            idx += 1
        else:
            n = ord(c) - ord('0')
            dots.append((idd, n))
            idd += n

    sum_ = 0
    for i, (num_start, num_length, num) in enumerate(nums[::-1]):
        for j, (dot_start, dot_length) in enumerate(dots):
            dot_start, dot_length = dots[j]
            if dot_start > num_start or dot_length < num_length:
                continue

            dots[j] = (dot_start + num_length, dot_length - num_length)
            nums[len(nums) - 1 - i] = (dot_start, num_length, num)
            break

    for num_start, num_length, num in nums:
        for i in range(num_start, num_start + num_length):
            sum_ += i*num

    print(sum_)
