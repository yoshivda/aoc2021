import numpy as np

from lib import load_input


def solve(data):
    bin_string = ''.join(str(bin(int(c, 16)))[2:].zfill(4) for c in data.strip())
    # return part_one(bin_string)[0]
    return part_two(bin_string)[0]


def part_one(packet, start=0):
    packet = packet[start:]
    version = packet[:3]
    typeid = packet[3:6]
    res = int(version, 2)
    if typeid == '100':
        i = 6
        while i < len(packet):
            i += 5
            if packet[i-5] == '0':
                break
        return res, i
    else:
        ltid = int(packet[6])
        if ltid == 0:
            length = int(packet[7:22], 2)
            index = 22
            while index < length + 22:
                total, taken_pos = part_one(packet, index)
                index += taken_pos
                res += total
        else:
            num_packets = int(packet[7:18], 2)
            index = 18
            for _ in range(num_packets):
                total, taken_pos = part_one(packet, index)
                index += taken_pos
                res += total
    return res, index


def part_two(packet, start=0):
    packet = packet[start:]
    typeid = int(packet[3:6], 2)
    if typeid == 4:
        value = []
        i = 6
        while i < len(packet):
            value.append(packet[i + 1:i + 5])
            i += 5
            if packet[i - 5] == '0':
                break
        value = int(''.join(value), 2)
        return value, i
    values = []
    ltid = int(packet[6])
    if ltid == 0:
        length = int(packet[7:22], 2)
        index = 22
        while index < length + 22:
            value, taken_pos = part_two(packet, index)
            index += taken_pos
            values.append(value)
    else:
        num_packets = int(packet[7:18], 2)
        index = 18
        for _ in range(num_packets):
            value, taken_pos = part_two(packet, index)
            index += taken_pos
            values.append(value)

    if typeid == 0:
        return sum(values), index
    if typeid == 1:
        return np.prod(values), index
    if typeid == 2:
        return min(values), index
    if typeid == 3:
        return max(values), index
    if typeid == 5:
        return int(values[0] > values[1]), index
    if typeid == 6:
        return int(values[0] < values[1]), index
    if typeid == 7:
        return int(values[0] == values[1]), index


if __name__ == '__main__':
    # print(solve(load_input('literal')))
    # print(solve(load_input('operator')))
    # for input in load_input('multiple_pt1').splitlines():
    #     print(solve(input))
    for input in load_input('multiple_pt2').splitlines():
        print(solve(input))
    print(solve(load_input()))
