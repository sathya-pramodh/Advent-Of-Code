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
            for i in range(n):
                nums.append((idd, idx))
                idd += 1
            idx += 1
        else:
            n = ord(c) - ord('0')
            dots.append((idd, n))
            idd += n

    sum_ = 0
    for start, length in dots:
        for i in range(start, start + length):
            idd, last = nums[-1]
            if idd < start:
                break
            nums.pop()
            sum_ += last*i

    for idd, idx in nums:
        sum_ += idd*idx

    print(sum_)
