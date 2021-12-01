from lib import load_input


def solve(data):
    # return part_one(list(map(int, list(data.splitlines()))))
    return part_two(list(map(int, list(data.splitlines()))))


def part_one(data):
    return sum(data[i] < data[i + 1] for i in range(len(data) - 1))


def part_two(data):
    return sum(data[i] < data[i+3] for i in range(len(data) - 3))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
