from functools import reduce


def part_one():
    lines = open("input.txt").readlines()
    horizontal_position = depth = 0
    for line in lines:
        action, units = line.split()
        if action == "forward":
            horizontal_position += int(units)
        elif action == "up":
            depth -= int(units)
        else:
            depth += int(units)
    print(horizontal_position*depth)


def one_line_part_one(): print(reduce(lambda horizontal_position, depth: horizontal_position*depth, reduce(lambda x, y: [x[0]+y[0], x[1]+y[1]], ([int(units) if action == "forward" else 0, int(units) if action == "down" else -int(units) if action == 'up' else 0] for action, units in [line.split() for line in open("input.txt").readlines()]))))


def part_two():
    lines = open("input.txt").readlines()
    horizontal_position = depth = aim = 0
    for line in lines:
        action, units = line.split()
        if action == "forward":
            horizontal_position += int(units)
            depth += aim * int(units)
        elif action == "up":
            aim -= int(units)
        else:
            aim += int(units)
    print(horizontal_position*depth)


def one_line_part_two(): print(reduce(lambda horizontal_position, depth: horizontal_position * depth, [reduce(lambda x, y: [x[0] + y[0], x[1] + y[1], x[2] + (y[0]*x[1])], ([int(units) if action == "forward" else 0, int(units) if action == "down" else -int(units) if action == 'up' else 0, 0] for action, units in [line.split() for line in open("input.txt").readlines()]))[i] for i in [0, 2]]))


if __name__ == '__main__':
    part_one()
    one_line_part_one()
    part_two()
    one_line_part_two()

