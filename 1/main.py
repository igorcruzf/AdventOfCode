sum_greather_than_previous_number = lambda lines: sum(1 for previous, actual in zip(lines, lines[1:]) if actual > previous)


def one_line_part_one(): print(sum_greather_than_previous_number([int(line) for line in open("1/input.txt").readlines()]))


def one_line_part_two(lines=[int(line) for line in open("1/input.txt").readlines()]): print(sum_greather_than_previous_number([first + second + third for first, second, third in zip(lines, lines[1:], lines[2:])]))


if __name__ == '__main__':
    one_line_part_one()
    one_line_part_two()
