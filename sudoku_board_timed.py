import random
import copy


def main() -> None:
    board = generate_empty_board()
    options = generate_options()

    board = create_solved_board(board, options, (0, 0))
    gaps_count = get_user_difficulty_selection()
    board = create_board_gaps(board, gaps_count)
    print_board(board)

    return


def print_board(board: list[list]):
    print("-" * 21)
    for row in board:
        print("| ", end="")
        print(*(str(num) for num in row), end="")
        print(" |")
    print("-" * 21)

    return


def create_board_gaps(board: list[list], gaps: int) -> list[list]:
    gaps_created = 0
    while gaps_created < gaps:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != " ":
            board[row][col] = " "
            gaps_created += 1

    return board


def get_user_difficulty_selection() -> int:
    prompt = "Please select a difficult:\n\t1. Easy\n\t2. Medium\n\t3. Hard\n> "
    selection = int(input(prompt))
    if selection == 1:
        return 30
    if selection == 2:
        return 45
    if selection == 3:
        return 60

    print("Invalid selection: Defaulting to Medium\n")
    return 45


def create_solved_board(board: list[list], options: dict[tuple[int, int], list], cell: tuple[int, int]):
    if is_board_full(board):
        return board

    for option in options[cell]:
        if is_option_valid(board, option, cell):
            new_board = copy.deepcopy(board)
            new_board[cell[0]][cell[1]] = option
            new_options = copy.deepcopy(options)
            update_new_options(new_options, option, cell)

            next_cell = get_next_cell(cell)
            new_board = create_solved_board(new_board, new_options, next_cell)
            if new_board:
                return new_board

    return False


def get_next_cell(cell: tuple[int, int]) -> tuple[int, int]:
    if cell[1] == 8:
        return cell[0] + 1, 0

    return cell[0], cell[1] + 1


def update_new_options(options, option: int, cell: tuple[int, int]) -> dict[tuple[int, int], list]:
    options = update_row_options(options, option, cell)
    options = update_column_options(options, option, cell)
    options = update_square_options(options, option, cell)
    return options


def update_square_options(options, option, cell):
    cell_square_center = get_cell_square_center(get_cell_square(cell))
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if option in options[(cell_square_center[0] - i, cell_square_center[1] - j)]:
                options[(cell_square_center[0] - i, cell_square_center[1] - j)].remove(option)

    return option


def update_column_options(options, option, cell):
    for r in range(9):
        if option in options[(r, cell[1])]:
            options[(r, cell[1])].remove(option)

    return options


def update_row_options(options, option, cell):
    for c in range(0, 9):
        if option in options[(cell[0], c)]:
            options[(cell[0], c)].remove(option)

    return options


def is_option_valid(board: list[list], option: int, cell: tuple[int, int]) -> bool:
    for num in board[cell[0]]:
        if num == option:
            return False

    for r in range(9):
        if board[r][cell[1]] == option:
            return False

    for num in get_square(board, cell):
        if num == option:
            return False

    return True


def get_square(board: list[list], cell: tuple[int, int]) -> list[int]:
    square = []
    center_cell = get_cell_square_center(get_cell_square(cell))
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            square.append(board[center_cell[0] + i][center_cell[1] + j])

    return square


def get_cell_square_center(square: int) -> tuple[int, int]:
    square_num = 0
    for i in (1, 4, 7):
        for j in (1, 4, 7):
            if square_num == square:
                return i, j
            square_num += 1


def get_cell_square(cell: tuple[int, int]) -> int:
    row, col = cell[0], cell[1]
    if row in (0, 1, 2):
        return col // 3
    if row in (3, 4, 5):
        return 3 + (col // 3)

    return 6 + (col // 3)


def is_board_full(board: list[list]) -> bool:
    return board[8][8] != " "


def generate_options() -> dict[tuple[int, int], list]:
    choices = [k for k in range(1, 10)]
    cell_options = {}
    for i in range(9):
        for j in range(9):
            random.shuffle(choices)
            cell_options[(i, j)] = copy.copy(choices)

    return cell_options


def generate_empty_board() -> list[list]:
    board = []
    for _ in range(9):
        board.append([" " for _ in range(9)])

    return board


if __name__ == "__main__":
    main()
    # Time to write: 55 minutes
