# Reshape the Matrix
# Platform: LeetCode
# Difficulty: Easy
# Topics: Array, Matrix, Simulation

"""
This solution first checks if the total number of elements in the original matrix (`m * n`) matches the requested shape (`r * c`), returning the original matrix immediately if they are incompatible. If valid, it flattens the 2D matrix into a 1D list using a list comprehension and then slices this flat list into `r` chunks of size `c` to form the new 2D matrix. Both the time and space complexities are $O(m \times n)$ because every element in the matrix is visited and stored twice (once during flattening and once in the final result).
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
            
        flat = [num for row in mat for num in row]
        return [flat[i * c:(i + 1) * c] for i in range(r)]