from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(len(part) in (2, 3, 4, 7) for line in data for part in line.split(' | ')[1].split())


easy = {2: 1, 3: 7, 4: 4, 7: 8}


def part_two(data):
    res = 0
    for line in data:
        digits, to_decode = line.split('|')
        decode = {easy[len(digit)]: digit for digit in digits.split() if len(digit) in easy}
        res += sum(to_num(number, decode) * 10 ** i for i, number in enumerate(reversed(to_decode.split())))
    return res


def to_num(string, decode):
    if len(string) in easy:
        return easy[len(string)]
    elif len(string) == 5:
        if all(x in string for x in decode[7]):
            return 3
        elif sum(x in string for x in decode[4]) == 3:
            return 5
        return 2
    elif len(string) == 6:
        if any(x not in string for x in decode[1]):
            return 6
        elif any(x not in string for x in decode[4]):
            return 0
        return 9


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('medium')))
    print(solve(load_input()))
