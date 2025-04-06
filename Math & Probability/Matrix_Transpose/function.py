def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    cols = len(a)
    if cols == 0:
        rows = 0
    else:
        rows = len(a[0])
    b = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            b[i][j] = a[j][i]
    return b

# k = transpose_matrix([[1,2,3],[4,5,6]])
# print(k)