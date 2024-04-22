import copy
import random


def main():
    board = generate_empty_board()
    options = generate_options()
    board = create_solved_board(board, options, (0, 0))

    print_board(board)
    print("\n\n")
    gaps_count = get_difficulty()
    board = create_gaps(board, gaps_count)
    print_board(board)
    return


def create_gaps(board, gaps_count):
    gaps_created = 0
    while gaps_created < gaps_count:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != " ":
            board[row][col] = " "
            gaps_created += 1

    return board


def get_difficulty():
    prompt = "Select difficulty:\n\t1. Easy\n\t2. Medium\n\t3. Hard\n> "
    selection = int(input(prompt))
    if selection == 1:
        return 30
    if selection == 2:
        return 45
    if selection == 3:
        return 60

    print("Invalid selection, defaulting to medium")
    return 45


def print_board(board):
    print("-" * 21)
    for row in board:
        print("|", end=" ")
        for num in row:
            print(num, end=" ")
        print("|")

    print("-" * 21)
    return


def create_solved_board(board, options, cell):
    if board_is_full(board):
        return board

    for num in options[cell]:
        if is_option_valid(board, cell, num):
            new_board = copy.deepcopy(board)

            new_board[cell[0]][cell[1]] = num
            new_options = update_options(copy.deepcopy(options), cell, num)

            next_cell = get_next_cell(cell)
            new_board = create_solved_board(new_board, new_options, next_cell)
            if new_board:
                return new_board

    return False


def get_next_cell(cell):
    if cell[1] == 8:
        return cell[0] + 1, 0

    return cell[0], cell[1] + 1


def update_options(options, cell, num):
    row, col = cell[0], cell[1]

    # Update row options
    for c in range(9):
        if num in options[(row, c)]:
            options[(row, c)].remove(num)

    # Update column options
    for r in range(9):
        if num in options[(r, col)]:
            options[(r, col)].remove(num)

    # Update square options
    center_cell = get_square_center_cell(get_cell_square(cell))
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if num in options[(center_cell[0] + i), center_cell[1] + j]:
                options[(center_cell[0] + i), center_cell[1] + j].remove(num)

    return options


def is_option_valid(board, cell, option):
    if option in board[cell[0]]:  # Rows
        return False

    if option in [board[i][cell[1]] for i in range(9)]:  # Columns
        return False

    if option in get_cell_square_nums(board, cell):  # Square
        return False

    return True


def get_cell_square_nums(board, cell):
    square = get_cell_square(cell)
    center_cell = get_square_center_cell(square)

    square_nums = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            square_nums.append(board[center_cell[0] + i][center_cell[1] + j])

    return square_nums


def get_square_center_cell(square):
    count = 0
    for i in (1, 4, 7):
        for j in (1, 4, 7):
            if square == count:
                return i, j
            else:
                count += 1


def get_cell_square(cell):
    row, col = cell[0], cell[1]

    if row in (0, 1, 2):
        return col // 3
    if row in (3, 4, 5):
        return 3 + (col // 3)

    return 6 + (col // 3)


def board_is_full(board):
    return board[-1][-1] != " "


def generate_options():
    base_row = [i for i in range(1, 10)]
    options = {}
    for i in range(9):
        for j in range(9):
            random.shuffle(base_row)
            options[(i, j)] = copy.copy(base_row)

    return options


def generate_empty_board():
    board = []
    row = [" " for _ in range(9)]

    for _ in range(9):
        board.append(copy.copy(row))

    return board


if __name__ == "__main__":
    main()
    # Time to complete: 40 minutes
