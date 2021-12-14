from collections import Counter, defaultdict

from lib import load_input


def solve(data):
    template, rest = data.split('\n\n')
    # return part_one(template, {line.split(' -> ')[0]: line.split(' -> ')[1] for line in rest.splitlines()})
    return part_two(template, {line.split(' -> ')[0]: line.split(' -> ')[1] for line in rest.splitlines()})


def part_one(template, rules):
    for _ in range(10):
        new_template = []
        for i in range(len(template) - 1):
            new_template.append(template[i])
            new_template.append(rules[template[i:i+2]])
        new_template.append(template[-1])
        template = ''.join(new_template)
    counter = Counter(template)
    return max(counter.values()) - min(counter.values())


def part_two(template, rules):
    round = Counter(template[i:i+2] for i in range(len(template) - 1))
    freqs = Counter(template)

    for _ in range(40):
        new_round = defaultdict(int)
        for pair, count in round.items():
            p1, p2 = pair[0] + rules[pair], rules[pair] + pair[1]
            new_round[p1] += count
            new_round[p2] += count
            freqs[rules[pair]] += count
        round = new_round

    return max(freqs.values()) - min(freqs.values())


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
