def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    eigenvalues = []
    trace = matrix[0][0] + matrix[1][1]
    det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    root1 = (trace + (trace**2 - 4*det)**0.5)/2
    root2 = (trace - (trace**2 - 4*det)**0.5)/2
    eigenvalues.append(root1)
    eigenvalues.append(root2)
    return sorted(eigenvalues, reverse=True)

print(calculate_eigenvalues([[2, 1], [1, 2]]))