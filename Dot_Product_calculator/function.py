import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	"""
	return vec1 @ vec2

k = calculate_dot_product(np.array([1, 2, 3]),np.array([4, 5, 6]))
print(k)