from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


match = {'(': ')', '[': ']', '{': '}', '<': '>'}


def part_one(data):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    res = 0
    for line in data:
        stack = []
        for char in line:
            if char in '[{(<':
                stack.append(match[char])
            else:
                if stack.pop() != char:
                    res += scores[char]
                    break
    return res


def part_two(data):
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    res = []
    for line in data:
        stack = []
        for char in line:
            if char in '[{(<':
                stack.append(match[char])
            else:
                if stack.pop() != char:
                    break
        else:
            score = 0
            for char in stack[::-1]:
                score = score * 5 + scores[char]
            res.append(score)
    return sorted(res)[len(res) // 2]


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
