import sys
sys.setrecursionlimit(int(1e9))
ans = 0
cache = {}


def zero(x):
    if x == 0:
        return True, 1
    return False, -1


def even_digits(x):
    if len(str(x)) % 2 != 0:
        return False, None

    s = str(x)
    n1 = int(s[:len(s)//2])
    n2 = int(s[len(s)//2:])

    return True, [n1, n2]


def mul_2024(x):
    return True, x*2024


def calculate(num, c):
    if c == 0:
        return 1

    if (num, c) in cache:
        return cache[(num, c)]

    rules = [
        zero,
        even_digits,
        mul_2024
    ]

    ans = 0
    for rule in rules:
        success, new_num = rule(num)
        if success:
            if isinstance(new_num, list):
                an = calculate(new_num[0], c-1) + calculate(new_num[1], c-1)
                cache[(num, c)] = an
                ans += an
            else:
                an = calculate(new_num, c-1)
                cache[(num, c)] = an
                ans += an
            break

    return ans


with open("input.txt") as file:
    line = file.read().strip()
    nums = list(map(int, line.split()))

    cs = [num for num in nums]
    for comp in cs:
        an = calculate(comp, 75)
        ans += an

    print(ans)
