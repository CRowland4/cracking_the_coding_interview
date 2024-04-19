#  Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
import copy
import random


def zero_matrix(matrix: [list[list]]) -> list[list]:
    zeroed_rows = []
    zeroed_cols = []

    for r, row in enumerate(matrix):
        for c, num in enumerate(row):
            if num == 0:
                if r not in zeroed_rows:
                    zeroed_rows.append(r)
                if c not in zeroed_cols:
                    zeroed_cols.append(c)

    for row in zeroed_rows:
        for i in range(len(matrix[0])):
            matrix[row][i] = 0

    for col in zeroed_cols:
        for i in range(len(matrix)):
            if i not in zeroed_rows:
                matrix[i][col] = 0

    return matrix


def create_test_matrix():
    base_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    test = []
    for i in range(10):
        random.shuffle(base_row)
        new_row = copy.copy(base_row)
        for j in range(3):
            new_row.remove(new_row[random.randint(0, 5)])
        test.append(new_row)

    for row in test:
        print(row)

    print("\n\n\n")
    for row in zero_matrix(test):
        print(row)


if __name__ == "__main__":
    create_test_matrix()