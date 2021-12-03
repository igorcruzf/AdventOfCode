from functools import reduce
from itertools import accumulate


def one_line_part_one(): print(sum([[1 for i in range(len(lines)-1) if lines[i+1] > lines[i]] for lines in [list(map(int, open("input.txt").readlines()))]][0]))


def one_line_part_one_with_reduce_and_accumulate(): print(reduce(lambda x, y: [x[0], x[1] + y[1]], list(accumulate([[int(line), 0] for line in open("input.txt").readlines()], lambda x, y: [y[0], 1] if x[0] < y[0] else y)))[1])


def one_line_part_two(): print(sum([[1 for i in range(len(lines)-3) if lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]] for lines in [list(map(int, open("input.txt").readlines()))]][0]))


if __name__ == '__main__':
    one_line_part_one_with_reduce_and_accumulate()
    one_line_part_one()
    one_line_part_two()
