def row_sums(matrix):
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


def column_sums(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    sums = []
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        sums.append(col_sum)
    return sums


def diagonal_pattern(size):
    matrix = [[0] * size for _ in range(size)]
    for row in range(size):
        for col in range(size):
            if row < col:
                matrix[row][col] = 1
            elif row > col:
                matrix[row][col] = 2
    return matrix


def transform(matrix):
    if not matrix:
        return []
    new_matrix = [row.copy() for row in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if new_matrix[i][j] < 0:
                new_matrix[i][j] = 0
    return new_matrix
