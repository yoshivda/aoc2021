import itertools
import re
from math import ceil

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    res = data[0]
    for i in range(1, len(data)):
        res = f'[{res},{data[i]}]'
        while new_res := reduce(res):
            res = new_res
    return magnitude(res)


def reduce(number):
    return explode(number) or split(number)


def explode(number):
    level = 0
    prev_num_index = -1
    for i, c in enumerate(number):
        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
        elif c.isdigit():
            prev_num_index = i
        if level == 5:  # Pair nested in 4 other pairs
            pair_str = re.match(r'\[\d+,\d+]', number[i:]).group()
            fst, snd = list(map(int, re.findall(r'\d+', pair_str)))  # Pair numbers
            next_num_index = -1
            for j in range(i + len(pair_str), len(number)):  # Locate next number to the right (if exists)
                if number[j].isdigit():
                    next_num_index = j
                    break
            if next_num_index >= i:  # If next number: replace with num+snd
                next_num_str = re.match(r'\d+', number[next_num_index:]).group()
                new_next_num = int(next_num_str) + snd
                number = number[:next_num_index] + str(new_next_num) + number[next_num_index + len(next_num_str):]
            if prev_num_index >= 0:  # If prev number: replace with num+fst
                prev_num_str = re.findall(r'\d+', number[:prev_num_index + 1])[-1]
                new_prev_num = int(prev_num_str) + fst
                number = number[:prev_num_index - len(prev_num_str) + 1] + str(new_prev_num) + number[prev_num_index + 1:]
                i += len(str(new_prev_num)) - len(prev_num_str)
            number = number[:i] + '0' + number[i + len(pair_str):]  # Replace pair with 0
            return number
    return None


def split(number):
    match = re.search(r'\d\d+', number)
    if not match:
        return None
    num = int(match.group())
    return re.sub(str(num), f'[{num // 2},{ceil(num / 2)}]', number, 1)


def magnitude(number):
    if isinstance(number, str):
        number = eval(number)  # Turn string into python list of ints for easy processing
    if isinstance(number, list):
        return 3 * magnitude(number[0]) + 2 * magnitude(number[1])
    return number  # Must be an int


def part_two(data):
    return max(part_one([a, b]) for a, b in itertools.permutations(data, 2))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
