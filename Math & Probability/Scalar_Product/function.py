def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    rows = len(matrix)
    if rows == 0:
        cols = 0
    else:
        cols = len(matrix[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] * scalar
    return result

k = scalar_multiply([[1, 2], [3, 4]], 2)

print(k)