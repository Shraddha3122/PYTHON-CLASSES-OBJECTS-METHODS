

# Design a class Matrix with methods for addition, subtraction, and multiplication of matrices. 
# Ensure proper error handling for dimension mismatches.


class Matrix:
    def __init__(self, data):
        if not self._is_valid_matrix(data):
            raise ValueError("Invalid matrix data.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def _is_valid_matrix(self, data):
        """Check if the provided data is a valid matrix (2D list)."""
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            return False
        row_length = len(data[0])
        return all(len(row) == row_length for row in data)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = [
            [
                self.data[i][j] + other.data[i][j] for j in range(self.cols)
            ] for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")
        
        result = [
            [
                self.data[i][j] - other.data[i][j] for j in range(self.cols)
            ] for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)
            ] for i in range(self.rows)
        ]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

# Example usage:
if __name__ == "__main__":
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    # Addition
    result_add = matrix1 + matrix2
    print("\nAddition Result:")
    print(result_add)

    # Subtraction
    result_sub = matrix1 - matrix2
    print("\nSubtraction Result:")
    print(result_sub)

    # Multiplication
    matrix3 = Matrix([[1, 2], [3, 4], [5, 6]])
    result_mul = matrix1 * matrix3
    print("\nMultiplication Result:")
    print(result_mul)