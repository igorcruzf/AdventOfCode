from functools import reduce


def part_one():
    f = open('input.txt')
    lines = [line.strip() for line in f.readlines()]
    most_common_bits = [[0, 0] for _ in range(len(lines[0]))]
    for line in lines:
        for i in range(len(line)):
            most_common_bits[i][int(line[i])] += 1
    gamma = epsilon = ''
    for bits in most_common_bits:
        if bits[0] > bits[1]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    power_consumption = int(gamma, 2)*int(epsilon, 2)
    print(power_consumption)


def one_line_part_one(): print(reduce(lambda gamma, epsilon: int(gamma, 2) * int(epsilon, 2), reduce(lambda x, y: [x[0]+y[0], x[1]+y[1]], [['0', '1'] if bits[0] > bits[1] else ['1', '0'] for bits in reduce(lambda x, y: [[x[i][0]+y[i][0], x[i][1]+y[i][1]] for i in range(len(x))], [[[0, 1] if int(bit) == 1 else [1, 0] for bit in line] for line in [line.strip() for line in open('input.txt').readlines()]])])))


def get_rating(flow):
    f = open('input.txt')
    lines = [line.strip() for line in f.readlines()]
    rating = lines.copy()
    bit_index = 0
    while len(rating) > 1:
        sum_bits = [0, 0]
        for line in rating:
            sum_bits[int(line[bit_index])] += 1
        most_common_bit = 0 if sum_bits[0] > sum_bits[1] else 1
        new_rating = []
        for line in rating:
            if flow == 'oxygen' and int(line[bit_index]) == most_common_bit:
                new_rating.append(line)
            elif flow == 'co2' and int(line[bit_index]) != most_common_bit:
                new_rating.append(line)
        rating = new_rating.copy()
        bit_index += 1
    return int(rating[0], 2)


def part_two():
    life_support = get_rating("oxygen")*get_rating("co2")
    print(life_support)


def one_line_part_two():
    life_support = 1
    for flow in ['oxygen', 'co2']:
        rating = [line.strip() for line in open('input.txt').readlines()]
        for bit_index in range(len(rating[0])):
            rating = list(filter(lambda line: (flow == 'oxygen' and int(line[bit_index]) == [0 if bit[0] > bit[1] else 1 for bit in [reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], [[1, 0] if int(line[bit_index]) == 0 else [0, 1] for line in rating])]][0]) or (flow == 'co2' and int(line[bit_index]) != [0 if bit[0] > bit[1] else 1 for bit in [reduce(lambda x, y: [x[0] + y[0], x[1] + y[1]], [[1, 0] if int(line[bit_index]) == 0 else [0, 1] for line in rating])]][0]), rating)) if len(rating) > 1 else rating
        life_support *= int(rating[0], 2)
    print(life_support)


if __name__ == '__main__':
    part_one()
    one_line_part_one()
    part_two()
    one_line_part_two()
