def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	a, b = matrix[0]
	c, d = matrix[1]
	det = a*d - b*c
	if det == 0:
		return None
	else:
		return [
			[d/det, -b/det],
			[-c/det, a/det]
        ]
print(inverse_2x2([[4, 7], [2, 6]]))
