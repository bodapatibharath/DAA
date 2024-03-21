def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication not possible. Number of columns in A must be equal to the number of rows in B.")
        return None

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter {cols} space-separated elements for row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

try:
    rows_A, cols_A = map(int, input("Enter dimensions of matrix A (rows cols): ").split())
    A = input_matrix(rows_A, cols_A)

    rows_B, cols_B = map(int, input("Enter dimensions of matrix B (rows cols): ").split())
    B = input_matrix(rows_B, cols_B)

    result = matrix_multiply(A, B)
    if result:
        print("Matrix product (A * B):")
        for row in result:
            print(row)
except ValueError:
    print("Invalid input. Please enter valid dimensions and elements for matrices.")
