def one_line_part_one(lines=[int(line) for line in open("1/input.txt").readlines()]): print(sum(1 for i in range(len(lines)-1) if lines[i+1] > lines[i]))


def one_line_part_two(lines=[int(line) for line in open("1/input.txt").readlines()]): print(sum(1 for i in range(len(lines)-3) if lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]))


if __name__ == '__main__':
    one_line_part_one()
    one_line_part_two()
