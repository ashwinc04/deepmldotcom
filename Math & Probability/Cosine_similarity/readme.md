# Calculate Cosine Similarity Between Vectors

Task: Implement Cosine Similarity
In this task, you need to implement a function cosine_similarity(v1, v2) that calculates the cosine similarity between two vectors. Cosine similarity measures the cosine of the angle between two vectors, indicating their directional similarity.

Input:
v1 and v2: Numpy arrays representing the input vectors.
Output:
A float representing the cosine similarity, rounded to three decimal places.
Constraints:
Both input vectors must have the same shape.
Input vectors cannot be empty or have zero magnitude.
Example:
Input:
```
import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))
```
Output:
```
1.0
```
Reasoning:
The cosine similarity between v1 and v2 is 1.0, indicating perfect similarity.

## Cosine Similarity

Cosine similarity measures the cosine of the angle between two vectors. It doesn't consider the magnitude of the vectors but focuses on the angle between them.

### Cosine Similarity Formula

cos(θ) = (Σ AᵢBᵢ) / (√(Σ Aᵢ²) * √(Σ Bᵢ²))


Where:
- \( A \) and \( B \) are the two vectors.
- \( p \) is the number of dimensions.

### Implementation Steps for Cosine Similarity

1. **Handle Input**  
   Ensure input vectors have the same dimensions and handle edge cases (e.g., zero vectors).

2. **Dot Product**  
   Compute the dot product:  
   \[
   \sum_{i=1}^{p} A_i B_i
   \]

3. **Magnitudes**  
   Compute the L2 norms:  
   \[
   \sqrt{\sum_{i=1}^{p} A_i^2}, \quad \sqrt{\sum_{i=1}^{p} B_i^2}
   \]

4. **Final Result**  
   Divide the dot product by the product of the magnitudes.

### Use Cases

- Text and image similarity
- Recommendation systems
- Query matching

### Pitfalls

#### 1. Magnitude Blindness

Even vectors with vastly different magnitudes can have cosine similarity = 1.

**Example:**

```text
vector1 = (1, 1)  
vector2 = (1000, 1000)
cosine_similarity = 1
```
#### 2. Sparse Data Issues
In high-dimensional spaces, where data is often sparse, cosine similarity may become less reliable.

#### 3. Non-Negative Data Limitation
If all values are positive, cosine similarity cannot capture negative relationships or inverse trends.