def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    rows = len(matrix)
    if rows == 0:
        cols = 0
    else:
        cols = len(matrix[0])
    if mode == 'column':
        for j in range(cols):
            temp = 0
            for i in range(rows):
                temp += matrix [i][j]
            temp = temp/rows
            means.append(temp)
    if mode == 'row':
        for i in range(rows):
            means.append(sum(matrix[i])/cols)
    return means

#################
'''
FOLLOWING CODE WAS VIBE CODED FOR TESTING THE ABOVE MANUAL WRITTEN CODE
'''
#################

# Test cases for the function
matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 20], [30, 40], [50, 60]],
    [[5, 5, 5], [10, 10, 10]],
    []
]
modes = ['row', 'column']

for matrix in matrices:
    for mode in modes:
        print(f"Matrix: {matrix}, Mode: {mode}, Result: {calculate_matrix_mean(matrix, mode)}")

