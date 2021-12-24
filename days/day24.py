import re
from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    chars = [''] * 14
    for i, (j, target) in compute(data).items():
        if target > 0:
            chars[i], chars[j] = 9, 9 - target
        else:
            chars[i], chars[j] = 9 + target, 9
    return ''.join(map(str, chars))


def part_two(data):
    chars = [''] * 14
    for i, (j, target) in compute(data).items():
        if target > 0:
            chars[i], chars[j] = 1 + target, 1
        else:
            chars[i], chars[j] = 1, 1 - target
    return ''.join(map(str, chars))


def compute(lines):
    nums = [[int(re.search(r'-?\d+', lines[x * 18 + y]).group()) for y in (4, 5, 15)] for x in range(14)]
    x = []
    matches = dict()
    for inst_index, (num1, num2, num3) in enumerate(nums):
        if num1 == 1:  # push
            x.append((inst_index, num3))  # push index with number for matching
        elif num1 == 26:  # pop
            pushed_index, num4 = x.pop()  # matching push instruction
            matches[inst_index] = (pushed_index, num4 + num2)  # num4 + num2 = char[i] - char[j]
    return matches


if __name__ == '__main__':
    print(solve(load_input()))
