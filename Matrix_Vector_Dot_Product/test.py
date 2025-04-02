'''
    vibe coded this test.py using AI to test edge cases in my code.
'''
from function import matrix_dot_vector

def test_matrix_dot_vector_valid_input():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [1, 0, -1]
    expected = [-2, -2, -2]
    result = matrix_dot_vector(a, b)
    print("Test valid input:", "Pass" if result == expected else f"Fail (Got {result})")

def test_matrix_dot_vector_invalid_dimensions():
    a = [[1, 2], [3, 4]]
    b = [1, 2, 3]
    expected = -1
    result = matrix_dot_vector(a, b)
    print("Test invalid dimensions:", "Pass" if result == expected else f"Fail (Got {result})")

def test_matrix_dot_vector_empty_matrix():
    a = []
    b = [1, 2, 3]
    expected = -1
    result = matrix_dot_vector(a, b)
    print("Test empty matrix:", "Pass" if result == expected else f"Fail (Got {result})")

def test_matrix_dot_vector_empty_vector():
    a = [[1, 2, 3], [4, 5, 6]]
    b = []
    expected = -1
    result = matrix_dot_vector(a, b)
    print("Test empty vector:", "Pass" if result == expected else f"Fail (Got {result})")

def test_matrix_dot_vector_single_row():
    a = [[1, 2, 3]]
    b = [1, 0, -1]
    expected = [-2]
    result = matrix_dot_vector(a, b)
    print("Test single row:", "Pass" if result == expected else f"Fail (Got {result})")

def test_matrix_dot_vector_single_column():
    a = [[1], [2], [3]]
    b = [4]
    expected = [4, 8, 12]
    result = matrix_dot_vector(a, b)
    print("Test single column:", "Pass" if result == expected else f"Fail (Got {result})")

# Run all tests
if __name__ == "__main__":
    test_matrix_dot_vector_valid_input()
    test_matrix_dot_vector_invalid_dimensions()
    test_matrix_dot_vector_empty_matrix()
    test_matrix_dot_vector_empty_vector()
    test_matrix_dot_vector_single_row()
    test_matrix_dot_vector_single_column()