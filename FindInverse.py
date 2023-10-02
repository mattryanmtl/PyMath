def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

def matrix_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for col in range(len(matrix)):
        determinant += ((-1) ** col) * matrix[0][col] * matrix_determinant(matrix_minor(matrix, 0, col))
    return determinant

def matrix_inverse(matrix):
    determinant = matrix_determinant(matrix)
    if determinant == 0:
        raise ValueError("The matrix is singular and does not have an inverse.")
    
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -matrix[0][1] / determinant],
                [-matrix[1][0] / determinant, matrix[0][0] / determinant]]

    cofactors = []
    for row in range(len(matrix)):
        cofactor_row = []
        for col in range(len(matrix)):
            minor = matrix_minor(matrix, row, col)
            cofactor = ((-1) ** (row + col)) * matrix_determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    adjugate = transpose(cofactors)
    inverse = [[adjugate[i][j] / determinant for j in range(len(adjugate))] for i in range(len(adjugate))]
    
    return inverse

# Define your square matrix
matrix = [[2, 1, 1],
          [1, 3, 2],
          [1, 0, 0]]

# Calculate the matrix inverse
try:
    inverse_matrix = matrix_inverse(matrix)
    print("Original Matrix:")
    for row in matrix:
        print(row)
    print("\nInverse Matrix:")
    for row in inverse_matrix:
        print(row)
except ValueError as e:
    print(e)
