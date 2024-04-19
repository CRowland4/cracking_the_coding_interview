import random
import copy

#  square_center_cells[i] is the center cell of the ith
SQUARE_CENTER_CELLS = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
# ITERATION_COUNT = 0


def main():
    board = generate_empty_board()
    options = generate_board_options()
    board = create_solved_board(board, options, (0, 0))
    gaps = get_difficulty_gaps()
    print_board(board)

    board = make_gaps(gaps, board)
    print("\n\n\n\n\n")
    print_board(board)
    return


def get_difficulty_gaps() -> int:
    prompt = "Choose a difficulty:\n\t1. Easy\n\t2. Medium\n\t3. Hard\n> "
    choice = int(input(prompt))

    if choice == 1:
        return 30
    if choice == 2:
        return 45

    return 60


def make_gaps(gaps_to_make: int, board: list[list]) -> list[list]:
    gaps_made = 0
    while gaps_made < gaps_to_make:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if isinstance(board[row][col], int):
            board[row][col] = " "
            gaps_made += 1

    return board


def print_board(board: list[list]) -> None:
    print("_" * 21)
    for row in board:
        print("|", " ".join(str(num) for num in row), "|")

    print("_" * 21)
    return


def create_solved_board(board: list[list], options: [list[list[list]]], current_cell: tuple[int, int]) -> list[list] | bool:
    # global ITERATION_COUNT
    if is_board_full(board):
        return board

    # ITERATION_COUNT += 1
    for choice in options[current_cell[0]][current_cell[1]]:
        # print(ITERATION_COUNT)
        if is_option_valid(board, current_cell, choice):
            board_copy = copy.deepcopy(board)
            options_copy = copy.deepcopy(options)

            board_copy[current_cell[0]][current_cell[1]] = choice
            next_cell = get_next_cell(current_cell)
            options_copy = update_options(options_copy, current_cell, choice)
            new_board = create_solved_board(board_copy, options_copy, next_cell)
            if new_board:
                return new_board

    return False


def update_options(options: list[list[list]], cell: tuple[int, int], choice: int) -> list[list[list]]:
    row, col = cell[0], cell[1]

    for i in range(9):
        if choice in options[row][i]:
            options[row][i].remove(choice)
        if choice in options[i][col]:
            options[i][col].remove(choice)

    cell_square_center = SQUARE_CENTER_CELLS[get_cell_square(cell)]
    crow, ccol = cell_square_center[0], cell_square_center[1]
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if choice in options[crow + i][ccol + j]:
                options[crow + i][ccol + j].remove(choice)

    return options



def is_option_valid(board: list[list], cell: tuple[int, int], option: int) -> bool:
    if option in board[cell[0]]:
        return False
    if option in get_columns(board)[cell[1]]:
        return False

    square = get_cell_square(cell)
    if option in get_squares(board)[square]:
        return False

    return True


def get_cell_square(cell: tuple[int, int]) -> int:
    row, col = cell[0], cell[1]

    if row in (0, 1, 2):
        return col // 3
    if row in (3, 4, 5):
        return 3 + col // 3

    return 6 + col // 3


def get_next_cell(cell: tuple[int, int]) -> tuple[int, int]:
    if cell[1] == 8:
        return cell[0] + 1, 0

    return cell[0], cell[1] + 1


def is_board_full(board: list[list]) -> bool:
    for row in board:
        for item in row:
            if not isinstance(item, int):
                return False

    return True


def get_columns(board: list[list]) -> list[list]:
    """Returns the columns of the board"""
    columns = []
    for c in range(9):
        column = []
        for r in range(9):
            column.append(board[r][c])
        columns.append(column)

    return columns


def get_squares(board: list[list]) -> list[list]:
    """Returns the 9 squares of a sudoku board, left-right, top-down."""
    squares = []
    for i in range(9):
        square = []
        center = SQUARE_CENTER_CELLS[i]
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                square.append(board[center[0] + j][center[1] + k])

        squares.append(square)

    return squares


def generate_empty_board() -> list[list]:
    """Generates and returns an empty 9x9 sudoku board"""
    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(" ")

    return board


def generate_board_options() -> list[list[list]]:
    base_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    options = []
    for i in range(9):
        options.append([])
        for _ in range(9):
            random.shuffle(base_row)
            options[i].append(copy.copy(base_row))

    return options


if __name__ == "__main__":
    main()