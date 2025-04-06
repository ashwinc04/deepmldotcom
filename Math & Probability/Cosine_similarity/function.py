import numpy as np

def cosine_similarity(v1, v2):
	num = np.dot(v1, v2)
	v1l2 = np.sqrt(np.dot(v1, v1))
	v2l2 = np.sqrt(np.dot(v2, v2))
	final = num/(v1l2*v2l2)
	return final

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))