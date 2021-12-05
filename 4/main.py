def part_one():
    f = open('input.txt')
    bingo_input = [int(number) for number in f.readline().strip().split(',')]
    boards = []
    lines = f.readlines()
    index = 0
    board = []
    columns = [[] for _ in range(5)]
    for line in lines:
        if line.strip() != '':
            row = [int(number) for number in line.split()]
            for i in range(len(row)):
                columns[i].append(row[i])
            board.append(row)
            index += 1
            if index == 5:
                index = 0
                [board.append(column) for column in columns]
                boards.append(board)
                board = []
                columns = [[] for _ in range(5)]

    for number in bingo_input:
        for board in boards:
            for entry in board:
                if number in entry:
                    entry.remove(number)
            if has_won(board):
                return final_score(board, number)


def final_score(board, number):
    total = 0
    for entry in board:
        total += sum(entry)
    return int(total/2) * number


def has_won(board):
    if len(board) != 0:
        for entry in board:
            if len(entry) == 0:
                return True
    return False


def one_line_part_one(): [[[[entry.remove(number) or (print(int(sum([sum(entry) for entry in board])/2) * number) or boards.clear() if sum([1 for entry in board if len(entry) > 0]) != len(board) else None) if number in entry else None for entry in board] for board in boards] for number in bingo_input] for bingo_input, boards in [[[[int(number) for number in f.readline().strip().split(',')], [[item for sublist in [board, [[int(line[i]) for line in board] for i in range(len(board))]] for item in sublist] for board in [[[int(number) for number in line.split()] for line in board] for board in [list(entry[1:]) for entry in zip(*[iter(f.readlines())] * 6)]]]] for f in [open('input.txt')]]][0]]


def part_two():
    f = open('input.txt')
    bingo_input = [int(number) for number in f.readline().strip().split(',')]
    boards = []
    lines = f.readlines()
    index = 0
    board = []
    columns = [[] for _ in range(5)]
    for line in lines:
        if line.strip() != '':
            row = [int(number) for number in line.split()]
            for i in range(len(row)):
                columns[i].append(row[i])
            board.append(row)
            index += 1
            if index == 5:
                index = 0
                [board.append(column) for column in columns]
                boards.append(board)
                board = []
                columns = [[] for _ in range(5)]

    for number in bingo_input:
        for board in boards:
            for entry in board:
                if number in entry:
                    entry.remove(number)
            if has_won(board):
                if last_board(boards):
                    return final_score(board, number)
                else:
                    board.clear()


def last_board(boards):
    return sum([1 for board in boards if len(board) > 0]) == 1


def one_line_part_two(): [[[[entry.remove(number) or ((print(int(sum([sum(entry) for entry in board])/2) * number) or board.clear() if sum([1 for _board in boards if len(_board) > 0]) == 1 else board.clear()) if sum([1 for entry in board if len(entry) > 0]) != len(board) else None) if number in entry else None for entry in board] for board in boards] for number in bingo_input] for bingo_input, boards in [[[[int(number) for number in f.readline().strip().split(',')], [[item for sublist in [board, [[int(line[i]) for line in board] for i in range(len(board))]] for item in sublist] for board in [[[int(number) for number in line.split()] for line in board] for board in [list(entry[1:]) for entry in zip(*[iter(f.readlines())] * 6)]]]] for f in [open('input.txt')]]][0]]


if __name__ == '__main__':
    print(part_one())
    one_line_part_one()
    print(part_two())
    one_line_part_two()
