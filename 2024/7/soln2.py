import sys
sys.setrecursionlimit(int(1e9))


def evaluate(comb):
    cur_symb = ""
    st_num = []
    print(comb)

    for c in comb:
        if c == '*' or c == '+' or c == '||':
            if cur_symb == '+' or cur_symb == '*' or cur_symb == '||':
                n1 = st_num.pop()
                n2 = st_num.pop()
                if cur_symb == '+':
                    st_num.append(n1 + n2)
                elif cur_symb == '*':
                    st_num.append(n1 * n2)
                else:
                    st_num.append(int(str(n2) + str(n1)))
            cur_symb = c
        else:
            st_num.append(c)

    if cur_symb == '+' or cur_symb == '*' or cur_symb == "||":
        n1 = st_num.pop()
        n2 = st_num.pop()
        if cur_symb == '+':
            return n1 + n2
        elif cur_symb == "*":
            return n1 * n2
        else:
            return int(str(n2) + str(n1))
    return st_num.pop()


def get_all_combinations(nums):
    combs = [[nums[0]]]

    for i in range(1, len(nums)):
        ll = len(combs)
        for j in range(ll):
            comb = combs[j]
            comb1 = comb + ['+', nums[i]]
            comb2 = comb + ['*', nums[i]]
            comb3 = comb + ['||', nums[i]]
            combs.append(comb1)
            combs.append(comb2)
            combs.append(comb3)

    return combs


ans = 0
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        res, nums = line.split(":")
        numsS = nums.strip().split()
        nums = list(map(lambda x: int(x), numsS))
        res = int(res)

        combinations = get_all_combinations(nums)
        for comb in combinations:
            if len(comb) == 2*len(nums) - 1 and evaluate(comb) == res:
                ans += res
                break

print(ans)
