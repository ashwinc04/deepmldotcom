Calculate Eigenvalues of a Matrix

Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sorted from highest to lowest.

Example:  
Input:  
```python
matrix = [[2, 1], [1, 2]]
```
Output:  
```python
[3.0, 1.0]
```

The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, which for a 2x2 matrix is:

λ² - trace(A) * λ + det(A) = 0

trace(A) = a + d
det(A) = ad - bc