from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    gamma = ''
    epsilon = ''
    for i in range(len(data[0])):
        most, least = find_most_least(data, i)
        gamma += most[0][i]
        epsilon += least[0][i]
    return int(gamma, 2) * int(epsilon, 2)


def find_most_least(data, i):
    ones = [x for x in data if x[i] == '1']
    zeros = [x for x in data if x[i] == '0']
    return (zeros, ones) if len(zeros) > len(ones) else (ones, zeros)


def part_two(data):
    oxy = data[::]
    co2 = data[::]

    i = 0
    while len(oxy) > 1:
        oxy, _ = find_most_least(oxy, i)
        i += 1

    i = 0
    while len(co2) > 1:
        _, co2 = find_most_least(co2, i)
        i += 1

    return int(oxy[0], 2) * int(co2[0], 2)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
