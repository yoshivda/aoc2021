import itertools
from functools import cache

from lib import load_input


def solve(data):
    starting_positions = (int(line.split()[-1]) for line in data.splitlines())
    # return part_one(*starting_positions)
    return part_two(*starting_positions)


def part_one(a_pos, b_pos):
    a_score = 0
    b_score = 0
    die = 0
    a_turn = True
    while a_score < 1000 and b_score < 1000:
        die += 3
        mov_pos = 3 * die - 3
        if a_turn:
            a_pos = (a_pos + mov_pos - 1) % 10 + 1
            a_score += a_pos
        else:
            b_pos = (b_pos + mov_pos - 1) % 10 + 1
            b_score += b_pos
        a_turn = not a_turn
    return (a_score if a_score < b_score else b_score) * die


throws = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]


def part_two(a_pos, b_pos):
    return max(quantum_game(a_pos, 0, b_pos, 0, True))


@cache
def quantum_game(a_pos, a_score, b_pos, b_score, a_turn):
    if a_score >= 21:
        return 1, 0
    if b_score >= 21:
        return 0, 1
    pos = a_pos if a_turn else b_pos
    new_positions = [(pos + throw - 1) % 10 + 1 for throw in throws]
    if a_turn:
        subgames = (quantum_game(new_p, a_score + new_p, b_pos, b_score, False) for new_p in new_positions)
    else:
        subgames = (quantum_game(a_pos, a_score, new_p, b_score + new_p, True) for new_p in new_positions)
    return sum(a for a, _ in subgames), sum(b for _, b in subgames)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
