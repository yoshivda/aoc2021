import numpy as np

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def parse(data):
    return [int(x) for x in data[0].split(',')], \
           [np.array([[int(x) for x in row.split()] for row in grid.splitlines()]) for grid in data[1:]]


def part_one(data):
    nums, cards = parse(data)
    for num in nums:
        for i, card in enumerate(cards):
            card[card == num] = -1
            if any(x == -5 for axis in range(2) for x in card.sum(axis)):
                card[card == -1] = 0
                return card.sum(0).sum() * num


def part_two(data):
    nums, cards = parse(data)
    finished = set()
    for num in nums:
        for i, card in enumerate(cards):
            if i in finished:
                continue
            card[card == num] = -1
            if any(x == -5 for axis in range(2) for x in card.sum(axis)):
                if len(cards) - len(finished) > 1:
                    finished.add(i)
                else:
                    card[card == -1] = 0
                    return card.sum(0).sum() * num


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
